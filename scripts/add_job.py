#!/usr/bin/env python3
"""
add_job.py — Claude's tool to add a job + application to the tracker.

Usage (run by Claude during chat sessions):
  python3 scripts/add_job.py

The script:
1. Reads job metadata passed as arguments or from a temp file
2. Inserts the job into Supabase `jobs` table
3. Creates an application row in `applications` table
4. Optionally uploads CV and cover letter PDFs to Supabase Storage
5. Prints the job ID for reference
"""

import os
import sys
import json
import argparse
from datetime import date
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client

# Load .env from Job_Hunting root
load_dotenv(Path(__file__).parent.parent / ".env")

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
BUCKET = "application-files"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_user_id(email: str) -> str:
    """Look up user ID by email using service role."""
    res = supabase.auth.admin.list_users()
    for user in res:
        if user.email == email:
            return user.id
    raise ValueError(f"No user found with email: {email}")


def insert_job(job: dict) -> str:
    """Insert job into jobs table, return job ID."""
    res = supabase.table("jobs").insert(job).execute()
    return res.data[0]["id"]


def insert_application(user_id: str, job_id: str) -> str:
    """Create application row with status applied and today's date, return application ID."""
    res = supabase.table("applications").upsert(
        {
            "user_id": user_id,
            "job_id": job_id,
            "status": "applied",
            "applied_date": date.today().isoformat(),
        },
        on_conflict="user_id,job_id"
    ).execute()
    return res.data[0]["id"]


def upload_file(user_id: str, app_id: str, file_type: str, file_path: str) -> str:
    """Upload a file to Supabase Storage, return storage path."""
    path = Path(file_path)
    ext = path.suffix
    storage_path = f"{user_id}/{app_id}/{file_type}{ext}"
    with open(file_path, "rb") as f:
        supabase.storage.from_(BUCKET).upload(
            storage_path, f.read(),
            file_options={"content-type": "application/pdf", "upsert": "true"}
        )
    return storage_path


def update_application_files(app_id: str, cv_path: str = None, cl_path: str = None):
    """Update application with file paths."""
    patch = {}
    if cv_path:
        patch["cv_file_path"] = cv_path
    if cl_path:
        patch["cover_letter_file_path"] = cl_path
    if patch:
        supabase.table("applications").update(patch).eq("id", app_id).execute()


def main():
    parser = argparse.ArgumentParser(description="Add a job to the tracker")
    parser.add_argument("--data", required=True, help="Path to JSON file with job data")
    parser.add_argument("--email", required=True, help="Your Supabase user email")
    parser.add_argument("--cv", help="Path to tailored CV PDF")
    parser.add_argument("--cover-letter", help="Path to tailored cover letter PDF")
    parser.add_argument("--job-id", help="Existing job ID — skip insert, just upload files")
    parser.add_argument("--app-id", help="Existing application ID — skip insert, just upload files")
    args = parser.parse_args()

    # Load job data
    with open(args.data) as f:
        job_data = json.load(f)

    print(f"Job: {job_data.get('title')} @ {job_data.get('company')}")

    # Get user ID
    user_id = get_user_id(args.email)
    print(f"User ID: {user_id}")

    # Use existing IDs or insert new
    if args.job_id and args.app_id:
        job_id = args.job_id
        app_id = args.app_id
        print(f"Using existing job: {job_id}")
        print(f"Using existing application: {app_id}")
    else:
        job_id = insert_job(job_data)
        print(f"Job inserted: {job_id}")
        app_id = insert_application(user_id, job_id)
        print(f"Application created: {app_id}")

    # Upload files if provided
    cv_storage_path = None
    cl_storage_path = None

    if args.cv and Path(args.cv).exists():
        cv_storage_path = upload_file(user_id, app_id, "cv", args.cv)
        print(f"CV uploaded: {cv_storage_path}")

    if args.cover_letter and Path(args.cover_letter).exists():
        cl_storage_path = upload_file(user_id, app_id, "cover_letter", args.cover_letter)
        print(f"Cover letter uploaded: {cl_storage_path}")

    if cv_storage_path or cl_storage_path:
        update_application_files(app_id, cv_storage_path, cl_storage_path)

    print(f"\nDone! View at: https://jobs.chunxuhan.com")
    print(f"Job ID: {job_id}")
    print(f"Application ID: {app_id}")


if __name__ == "__main__":
    main()
