#!/usr/bin/env python3
from supabase import create_client
from dotenv import load_dotenv
import os
import sys

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(url, key)

job_id = sys.argv[1]

# Delete applications first
apps = supabase.table("applications").select("*").eq("job_id", job_id).execute()
for app in apps.data:
    supabase.table("applications").delete().eq("id", app["id"]).execute()
    print(f"Deleted application: {app['id']}")

# Delete job
supabase.table("jobs").delete().eq("id", job_id).execute()
print(f"Deleted job: {job_id}")
