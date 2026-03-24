# Job Hunting — Chunxu Han

**Status:** Actively searching | Available now | Based in Copenhagen, Denmark

---

## Strategy

### Target Role Types

I'm targeting all data/AI-relevant roles, not just bioinformatics. Three tiers:

| Tier | Role types | My angle |
|------|-----------|----------|
| **A — Bioinformatics / Computational Biology** | Bioinformatics Scientist, Computational Biologist, Research Scientist, Data Scientist (pharma/biotech) | 2 publications, scBatch package, Novo Nordisk thesis, IsoformSwitchAnalyzeR contributor |
| **B — Data Science / ML (any industry)** | Data Scientist, ML Engineer, Analytics Engineer, AI/LLM Engineer | Python/R/ML coursework, production package dev, cross-functional experience, AI agent projects |
| **C — PhD Programs** | Computational biology, single-cell, AI for biology, ML in medicine | Strong academic output for a master's student, DTU/Novo Nordisk network, 2 preprints |

**Note on Tier B:** Some roles will require reframing my profile or filling skill gaps. Strategy is to take targeted online courses or build small hobby projects to demonstrate relevant skills (e.g. SQL-heavy roles, cloud infrastructure, NLP).

### Where to Search

| Platform | Priority | Notes |
|----------|----------|-------|
| LinkedIn | Primary | Daily check, set job alerts |
| Jobindex.dk | Secondary | Good for Danish companies |
| Jobnet.dk | Secondary | Official Danish job portal |
| TheHUB | Secondary | Startup/tech-focused Denmark |
| Company list | Proactive outreach | Pre-filtered list at tracker.chunxuhan.com — contact one by one |
| EURAXESS | PhD only | EU academic positions |
| DTU Career Portal | Supplementary | DTU network and alumni postings |

### Target Companies (Proactive Outreach)

Pre-filtered and ranked company list lives at **tracker.chunxuhan.com**. Reach out systematically, one by one.

Key sectors to cover:
- **Pharma/Biotech:** Novo Nordisk, Novonesis, LEO Pharma, Genmab, Bavarian Nordic, Symphogen, Zealand Pharma
- **CROs/Consultancy:** Parexel, ICON, Syneos, Curida, Nordic Bioscience
- **Tech/Data:** Danish data-driven companies, AI startups, analytics agencies
- **Public sector:** SSI, DTU, hospitals with bioinformatics units

---

## Weekly Routine

### Daily (15–30 min)
- Scan LinkedIn, Jobindex, Jobnet, TheHUB for new postings
- Add any interesting roles to the tracker with status `to_apply`
- If 1–2 strong matches found: apply same day with Claude's help

### Application workflow (per job)
1. Paste the job ad to Claude in chat
2. Claude parses the job, analyzes fit vs. master profile, and inserts it directly into the tracker database (jobs.chunxuhan.com)
3. Claude tailors your CV and cover letter and saves them in `applications/YYYY-MM_Company_Role/`
4. Compile the PDFs locally (`xelatex cv_tailored.tex`)
5. Claude uploads the PDFs to Supabase Storage and attaches them to your application
6. Submit the application → go to jobs.chunxuhan.com and update status to `Applied`

### Proactive outreach (2–3x per week)
- Pick next company from tracker.chunxuhan.com
- Research the company and find the right contact
- Write a short, targeted cold email or LinkedIn message
- Update tracker status

### Weekly target
- **3–5 formal applications** (quality over quantity)
- **2–3 cold outreach messages** to target companies
- **1 skill-building action** (course module, small project, or blog post)

### Friday reflection (weekly)
Write a short reflection saved to the tracker:
- How many applications sent this week?
- Any responses, interviews, rejections?
- What worked? What didn't?
- What skill gap came up most?
- Plan for next week

---

## Application Materials Workflow

### Phase 1: Profile (done)
- [profile/master_profile.md](profile/master_profile.md) — full background, skills, experience
- [profile/writing_style.md](profile/writing_style.md) — tone and style notes

### Phase 2: Per-Application Pipeline (Claude-automated)
Each application lives in `applications/YYYY-MM_Company_Role/`:

```
applications/
└── YYYY-MM_Company_Role/
    ├── job_ad.md           # Raw job posting (copy-pasted by you)
    ├── alignment.md        # Claude's fit analysis: strengths + gaps
    ├── cv_tailored.tex     # Tailored CV (Claude writes this)
    └── cover_letter.tex    # Tailored cover letter (Claude writes this)
```

Claude also:
- Inserts the job into the Supabase `jobs` table automatically
- Creates your application row with status `to_apply`
- Uploads the compiled PDFs to Supabase Storage after you compile them

### Phase 3: Track & Reflect
All tracking lives at **jobs.chunxuhan.com** — you only go there to:
- Update status as you hear back (`Applied → Screening → Interview → Offer/Rejected`)
- Write your Friday weekly reflection
- Download any CV or cover letter you need to reference

---

## Automation (Claude + scripts/)

Claude handles all database and file operations automatically. You never need to fill in forms on the website.

### What Claude does for each job
1. Parses job ad → extracts all metadata
2. Scores fit against master profile (1–10) with reasons and gaps
3. Writes job JSON → runs `scripts/add_job.py` to insert into Supabase
4. Creates application row with status `to_apply`
5. Tailors CV and cover letter → saves `.tex` files in `applications/`
6. After you compile PDFs → uploads to Supabase Storage and links to the application

### What you do
- Paste job ads here in chat
- Compile the LaTeX PDFs (`xelatex cv_tailored.tex`)
- Go to jobs.chunxuhan.com to update status as you hear back
- Write your Friday reflection on the Weekly Log tab

### Scripts
```
scripts/
└── add_job.py    # Inserts job + application into Supabase, uploads files
```

Run by Claude — not manually. Requires `.env` in repo root (gitignored).

---

## Tracker System (jobs.chunxuhan.com)

The job tracker is a separate Next.js + Supabase + Vercel project at https://github.com/chunxubioinfor/job-tracker.

### Database Design (3 tables)

**Table 1: `jobs`** — job metadata (public, visible to all users)
- Job title, company, sector, location, URL
- Full job description
- Platform (LinkedIn / Jobindex / Jobnet / TheHUB / Referral / Other)
- Deadline, date added
- AI match score, match reasons, gaps (vs. master profile)
- Source type: `open_application` | `job_ad`

**Table 2: `applications`** — private per-user tracking (Row Level Security: each user sees only their own)
- Links to a job in `jobs`
- Status pipeline: `to_apply → applied → screening → interview → offer → rejected → withdrawn`
- Date applied
- CV version used (filename or text)
- Cover letter used (filename or text)
- Notes
- Timestamps

**Table 3: `weekly_logs`** — Friday reflections (private per-user)
- Week start date
- Applications sent (count)
- Responses received (count)
- Interviews (count)
- What worked
- What didn't
- Skill gap identified
- Plan for next week

### Access Model
- **Anyone** can sign up and use the tracker for their own job search
- **All users** can see the `jobs` table (shared job postings)
- **Each user** sees only their own `applications` and `weekly_logs` (Row Level Security)
- **Dashboard** shows: status pipeline bar, application counts by status, weekly trend chart

---

## Skill Development Plan

For Tier B roles that require skills not yet demonstrated:

| Skill gap | Action |
|-----------|--------|
| SQL / data engineering | Build a small project with dbt or BigQuery |
| Cloud (AWS/GCP) | Complete one cloud certification module |
| NLP / LLM applications | Extend DailyJobMatch AI agent project |
| Dashboard / BI tools | Already have Power BI; add a Streamlit or Looker project |

---

## Quick Reference

### Key files
- **Master profile:** [profile/master_profile.md](profile/master_profile.md)
- **Writing style:** [profile/writing_style.md](profile/writing_style.md)
- **Applications:** [applications/](applications/)
- **Company tracker:** tracker.chunxuhan.com

### Compile a CV (LaTeX)
```bash
cd applications/YYYY-MM_Company_Role
xelatex cv_tailored.tex
```
