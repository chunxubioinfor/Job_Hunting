# Side Project Learning Plan

**Goal:** Build two portfolio projects that close the biggest gaps identified from job applications, while learning the fundamentals well enough to talk about them in interviews.

---

## Priority Order

### Project 1: Databricks Job Market Analytics (do this first)
**Why first:** Databricks came up in both Laerdal and CPH applications. It's the most common gap and the fastest to close (1-2 days). Once done, you can immediately put it on your CV.

**Full plan:** See `side_project_databricks.md`

### Project 2: Job Tracker Data Engineer Pipeline (do this second)
**Why second:** This project closes multiple gaps at once (ETL pipelines, Prefect orchestration, dbt modelling, production SQL) and turns your existing job tracker into a real data engineering portfolio piece. Takes 2-3 weekends.

**Full plan:** See `side_project_data_engineer.md`

---

## Instructions for Claude Code (New Session)

When starting a new Claude Code session for either project, paste the following context:

---

### Context for Claude

I am Chunxu, a bioinformatics MSc graduate job hunting in Denmark. I am building portfolio projects to close skill gaps for data scientist and data engineer roles. **I want to learn by doing.** This means:

1. **Teach me as we go.** Before writing code, briefly explain the concept or tool we are about to use. Keep explanations short (2-3 sentences) but make sure I understand *why* we are doing something, not just *what*.

2. **Document everything in a learning log.** After each major step, add a short entry to `LEARNING_LOG.md` in the project root with:
   - What we did
   - What tool/concept was used
   - One sentence on why it matters
   - Any gotchas or things I should remember for interviews

3. **Flag interview-relevant topics.** If something we are doing is commonly asked about in data science or data engineering interviews, mark it with `[INTERVIEW]` in the learning log. For example: "Delta Lake uses ACID transactions [INTERVIEW: explain what ACID means and why it matters for data pipelines]."

4. **Let me try first.** When possible, describe what needs to be done and let me attempt it before writing the code for me. If I get stuck, then help.

5. **Keep a cheat sheet.** Maintain a `CHEAT_SHEET.md` with short command/syntax references for new tools I learn (PySpark, dbt, Prefect, Databricks CLI, etc.) so I can look things up quickly later.

### My existing projects for reference
- **Job_dk** (`/Users/hanchunxu/Desktop/Job_dk/`): Python scraping pipeline with LLM analysis layer. Data files in `data/output/`.
- **Job Tracker** (`/Users/hanchunxu/Desktop/job-tracker/`): Next.js + Supabase web app. PostgreSQL database with jobs, applications, weekly_logs tables.
- **Side project plans:** `/Users/hanchunxu/Desktop/Job_Hunting/side_project_databricks.md` and `/Users/hanchunxu/Desktop/Job_Hunting/side_project_data_engineer.md`

### What I already know
- Python (strong), R (strong), SQL (coursework + basic production), Git, Docker
- ML/DL coursework (logistic regression, random forest, neural networks)
- Jupyter notebooks, matplotlib, pandas, scikit-learn
- Next.js, Supabase, Vercel (from job tracker)

### What I need to learn
- **Project 1:** PySpark, Delta Lake, Databricks SQL, MLflow, Databricks Workflows, medallion architecture
- **Project 2:** Prefect (orchestration), dbt (data modelling), production SQL patterns, ETL best practices

---

## After Completing the Projects

### Update your CV
Add the new experience to the relevant experience bank at `/Users/hanchunxu/Desktop/Job_Hunting/source_materials/relevant_experience_bank.md`.

Suggested paragraphs to add:

**For Databricks:**
> **Cloud Analytics with Databricks.** Built an end-to-end analytics pipeline on Databricks using the medallion architecture (bronze/silver/gold Delta tables). Ingested and transformed 2,500+ job market records with PySpark, wrote SQL analytics for trend analysis, tracked ML experiments with MLflow, and orchestrated the pipeline with Databricks Workflows.

**For Data Engineer Pipeline:**
> **ETL Pipeline and Data Modelling.** Extended my job tracker web app with an automated ETL pipeline that ingests job listings from external sources, deduplicates and loads them into PostgreSQL, and orchestrates daily runs with Prefect. Modelled analytics-ready tables with dbt, including staging models, marts, and automated tests.

### Update your Skills line
> Python, R, Bash, SQL, PySpark, Databricks, Delta Lake, MLflow, dbt, Prefect, Power BI, Git, Docker

### Prepare for interviews
Review `LEARNING_LOG.md` from both projects, especially entries marked `[INTERVIEW]`. These are the concepts you are most likely to be asked about.

Key topics to be ready to explain:
- What is the medallion architecture and why use it?
- What is Delta Lake and how is it different from Parquet?
- What does MLflow track and why is experiment tracking important?
- What is dbt and how does it differ from writing raw SQL?
- What is Prefect and how does it compare to Airflow?
- What is an ETL pipeline vs ELT?
- What are ACID transactions?
- What is idempotency and why does it matter for pipelines?
