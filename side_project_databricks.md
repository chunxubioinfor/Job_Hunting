# Side Project: Databricks Job Market Analytics

**Goal:** Build a real Databricks project using your existing Job_dk data to demonstrate hands-on experience with the Databricks ecosystem. This project should be completable in 1-2 days and cover the main technologies that employers ask for.

---

## Context for Claude

Chunxu is a bioinformatics MSc graduate job hunting in Denmark. He has an existing project called **Job_dk** (`/Users/hanchunxu/Desktop/Job_dk/`) that scraped 2,500+ job listings from the Danish job market, enriched them with full descriptions, and ran LLM-based analysis (sector classification, skills extraction, CV matching). The output files are:

- `data/output/jobs_enriched.jsonl` — raw scraped data with descriptions
- `data/output/jobs_analyzed.jsonl` — LLM-extracted fields (sector, seniority, skills, etc.)
- `data/output/jobs_llm_scored.jsonl` — CV match scores per job
- `analysis/figures/` — existing matplotlib charts from a Jupyter notebook analysis

He also has a **job-tracker** web app (`/Users/hanchunxu/Desktop/job-tracker/`) with a Supabase PostgreSQL database tracking his applications.

The purpose of this project is to redo the Job_dk analysis on Databricks, using Databricks-native tools, so he can put "Databricks" on his CV with real experience behind it.

---

## Databricks Key Technologies to Cover

| Technology | What it does | How this project uses it |
|---|---|---|
| **PySpark** | Distributed data processing | Load and transform the job listings data |
| **Delta Lake** | ACID-compliant storage layer | Store cleaned job data as Delta tables |
| **Databricks SQL** | SQL analytics on Delta tables | Write analytical queries (top employers, skill trends, sector breakdown) |
| **Notebooks** | Interactive development | All work done in Databricks notebooks |
| **MLflow** | ML experiment tracking | Track and log the job matching model (even a simple classifier) |
| **Workflows/Jobs** | Pipeline orchestration | Schedule a daily/weekly pipeline run |
| **Dashboard** | Built-in visualisation | Build a simple dashboard with key charts |

---

## Project Plan

### Phase 1: Data Ingestion (Day 1, morning)

1. Sign up for Databricks Community Edition (free)
2. Upload `jobs_analyzed.jsonl` to Databricks (DBFS or Unity Catalog volume)
3. Create a notebook that reads the JSONL into a Spark DataFrame
4. Clean and transform: parse dates, normalize sectors, explode skills arrays
5. Write the cleaned data as a **Delta table**: `jobs_bronze` (raw) and `jobs_silver` (cleaned)

**Key skills demonstrated:** PySpark, Delta Lake, medallion architecture (bronze/silver/gold)

### Phase 2: SQL Analytics (Day 1, afternoon)

1. Create a SQL notebook
2. Write queries against the Delta tables:
   - Jobs per sector per year (temporal trends)
   - Top 20 most requested skills
   - Top employers by posting volume
   - Seniority distribution by sector
   - Remote vs onsite trends over time
3. Save aggregated results as a `jobs_gold` Delta table

**Key skills demonstrated:** Databricks SQL, Delta Lake queries, gold layer

### Phase 3: ML with MLflow (Day 2, morning)

1. Build a simple model: predict sector from job title + description (text classification)
   - Use TF-IDF + logistic regression or a simple sklearn pipeline
   - Or: build a match score predictor using the LLM scores as labels
2. Log the experiment with **MLflow**:
   - Log parameters, metrics (accuracy, F1)
   - Log the trained model as an artifact
   - Compare runs in the MLflow UI
3. Register the best model in the MLflow Model Registry

**Key skills demonstrated:** MLflow experiment tracking, model registry, sklearn on Spark

### Phase 4: Dashboard and Workflow (Day 2, afternoon)

1. Build a **Databricks Dashboard** with 4-5 charts:
   - Jobs posted over time (bar chart)
   - Sector donut chart
   - Top skills bar chart
   - Match score distribution
2. Create a **Workflow** that runs the full pipeline:
   - Task 1: Ingest and clean data → Delta bronze/silver
   - Task 2: SQL aggregations → Delta gold
   - Task 3: ML training → MLflow
   - Schedule it (even if just a demo schedule)

**Key skills demonstrated:** Databricks Dashboards, Workflows/Jobs, end-to-end pipeline

---

## What to Put on Your CV After This

**Relevant Experience paragraph:**

> **Cloud Analytics with Databricks.** Built an end-to-end analytics pipeline on Databricks using the medallion architecture (bronze/silver/gold Delta tables). Ingested and transformed 2,500+ job market records with PySpark, wrote SQL analytics for trend analysis, tracked ML experiments with MLflow, and orchestrated the pipeline with Databricks Workflows.

**Skills line update:**

> Python, R, Bash, SQL, PySpark, Databricks, Delta Lake, MLflow, Power BI, Git, Docker

---

## What to Put on GitHub

Create a repo called `databricks-job-analytics` with:
- `README.md` — project description, screenshots of dashboard
- `notebooks/` — exported Databricks notebooks (.py or .ipynb)
- `data/sample/` — a small sample of the input data (not the full dataset)
- Screenshots of: Delta tables, MLflow experiment, Dashboard, Workflow

---

## Estimated Time

| Phase | Time |
|---|---|
| Phase 1: Data Ingestion | 2-3 hours |
| Phase 2: SQL Analytics | 2-3 hours |
| Phase 3: ML with MLflow | 2-3 hours |
| Phase 4: Dashboard + Workflow | 2-3 hours |
| **Total** | **1-2 days** |

---

## After This: Job Tracker Data Engineer Side Project

The next project after Databricks is documented in `/Users/hanchunxu/Desktop/Job_Hunting/side_project_data_engineer.md`. That project extends the job-tracker web app with:
- ETL pipeline (auto-ingest job listings from APIs)
- Prefect orchestration
- dbt data modelling
- Analytics dashboard

Together, the Databricks project + job tracker pipeline project cover all the major gaps identified in Chunxu's job applications (Databricks, cloud analytics, CI/CD, production SQL, ETL pipelines).
