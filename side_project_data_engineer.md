# Side Project: Job Tracker Data Pipeline
**Goal:** Extend the job-tracker into a real data engineering portfolio piece to position as a Data Engineer

---

## Why This Works as a Portfolio Project

The job tracker already has a PostgreSQL database (Supabase) and a React frontend.
The missing piece is a real **data pipeline** that automatically ingests, transforms, and loads data.
Adding that layer transforms the project from "nice app" to "data engineering portfolio."

---

## Phase 1: ETL Pipeline — Auto-ingest job listings

**What:** Build a Python ETL pipeline that pulls job listings from a public source and loads them into your Supabase jobs table automatically.

**Options for data source:**
- Jobindex RSS feed (simplest, no auth needed)
- LinkedIn unofficial API (more impressive but more work)
- The Hub API (relevant for Danish tech roles)

**Steps:**
1. Write a Python script that fetches job listings from the source
2. Parse and clean the data (title, company, location, description, deadline)
3. Deduplicate against existing records in Supabase
4. Load new records into the `jobs` table
5. Log each run (rows fetched, inserted, skipped)

**Skills demonstrated:** Python, ETL/ELT design, API integration, SQL upserts, deduplication logic

---

## Phase 2: Orchestration with Prefect or Airflow

**What:** Schedule the pipeline to run automatically (e.g. every morning at 8am).

**Recommendation:** Start with **Prefect** — easier setup than Airflow, modern, and well-regarded.

**Steps:**
1. Wrap the ETL script as a Prefect flow with tasks
2. Add retry logic and error handling
3. Schedule it to run daily
4. Add logging and alerting (email or Slack on failure)

**Skills demonstrated:** Workflow orchestration (Prefect), scheduling, monitoring, alerting

---

## Phase 3: Data Modeling with dbt

**What:** Add a dbt layer on top of your Supabase PostgreSQL to model analytics-ready tables.

**Example models to build:**
- `jobs_enriched` — jobs with sector classification, match score bands
- `applications_summary` — weekly application stats per user
- `response_rate` — applications sent vs. responses received over time

**Steps:**
1. Set up dbt with Supabase PostgreSQL connection
2. Write 2-3 staging models (clean raw tables)
3. Write 2-3 mart models (analytics-ready aggregations)
4. Add tests (not_null, unique, relationships)

**Skills demonstrated:** dbt, data modeling, SQL, testing best practices

---

## Phase 4: Dashboard (optional but impressive)

**What:** Add a simple analytics page to the job tracker frontend showing pipeline stats.

**Ideas:**
- Jobs ingested per day (bar chart)
- Application funnel (to_apply → applied → response → interview)
- Match score distribution of jobs in the market

**Skills demonstrated:** Full-stack data application, end-to-end ownership

---

## Stack Summary (what to put on your CV)

| Tool | Purpose |
|------|---------|
| Python | ETL scripting |
| PostgreSQL (Supabase) | Data warehouse |
| Prefect | Orchestration & scheduling |
| dbt | Data modeling & transformation |
| Power BI | Business intelligence dashboard |
| GCP or Railway | Pipeline hosting (if you deploy it) |
| Git | Version control |

---

## CV Positioning After This Project

**Relevant Experience paragraph:**

> **Full-stack data pipeline for job market analytics.** Built an automated ETL pipeline in Python that ingests daily job listings from external sources, deduplicates and loads them into PostgreSQL, and orchestrates runs with Prefect. Modeled analytics-ready tables with dbt and surfaced insights through a Next.js dashboard. Deployed on [GCP/Railway].

---

## Phase 5: Power BI Dashboard (local)

**What:** Install Power BI Desktop (free) and connect it to your Supabase PostgreSQL database. Build a proper BI dashboard alongside your existing Next.js frontend.

**Why both:** The Next.js dashboard shows you can build custom web apps. The Power BI dashboard shows you can use the industry-standard tool that employers ask for. Different skills, both valuable.

**Dashboard pages to build:**
- **Application Overview** — funnel chart (applied → screening → interview → offer), KPI cards (total apps, response rate, avg match score)
- **Trends** — applications per week bar chart, cumulative applications line chart
- **Job Market** — match score distribution, sector breakdown, platform breakdown
- **Pipeline Health** — if you built Phase 1-3, show ETL run stats (rows ingested per day, success/failure rate)

**Steps:**
1. Install Power BI Desktop (free, runs on Mac via Parallels/VM, or use a Windows machine)
2. Connect to Supabase PostgreSQL using the connection string from your `.env`
3. Import tables: jobs, applications, weekly_logs
4. Build relationships between tables in the data model
5. Create the dashboard pages above
6. Export as PDF for portfolio, optionally publish to Power BI Service

**Note:** Power BI Desktop is Windows-only. On Mac you can use Parallels, a Windows VM, or the free Power BI web version at app.powerbi.com (limited but works for basic dashboards).

**Skills demonstrated:** Power BI, data modelling in BI tools, PostgreSQL connectivity, business reporting

---

## Suggested Order

1. Phase 1 first — get data flowing, this alone is already impressive
2. Phase 2 — add Prefect, turns it from a script into a pipeline
3. Phase 3 — add dbt, this is the most valued skill in data engineering right now
4. Phase 4 — Next.js analytics page, only if you enjoy it and have time
5. Phase 5 — Power BI dashboard, connect to your real database

**Estimated time:** Phase 1-3 = ~2-3 weekends of focused work. Phase 5 = ~1 day.
