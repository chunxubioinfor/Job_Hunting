#!/usr/bin/env python3
from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(url, key)

# Find Novonesis jobs
response = supabase.table("jobs").select("*").eq("company", "Novonesis").execute()
print(f"Found {len(response.data)} Novonesis job(s):")
for job in response.data:
    print(f"  Job ID: {job['id']}")
    print(f"  Title: {job['title']}")
    print(f"  Created: {job['created_at']}")
    print()
