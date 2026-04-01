# Relevant Experience Paragraph Bank

This file is a reusable library of Relevant Experience paragraphs for CV tailoring.
Each paragraph has tags, a title (bold-lead format), and the text.

Before writing a new paragraph from scratch, check here first.
If reusing, lightly adapt the opening sentence to match the role's language — don't copy verbatim.
After writing a good new paragraph for a real application, add it here.

---

## How to use

- Pick 2–3 paragraphs that best match the job
- Adapt the opening to reflect the role's specific framing
- Keep the bold title short and punchy

---

## Paragraphs

---

### [tags: batch-correction, single-cell, methodology, quantitative, thesis]

**Quantitative Research & Signal Development**

At Novo Nordisk, my thesis centres on developing a novel quantitative metric — the Batch Mixing Index (BMI) — to detect and measure systematic variation in large single-cell RNA-seq datasets. I designed the mathematical formulation, implemented it in Python, and validated it using permutation-based significance testing across multiple experimental conditions. This is fundamentally the same loop as any rigorous quantitative research: define a signal, build a pipeline to compute it, and test whether it holds up statistically.

---

### [tags: pipelines, hpc, software, r-package, large-scale, isoform]

**Large-Scale Data Pipelines & Research Software**

At DTU HealthTech, I built and maintained data infrastructure for isoform-level proteomics analysis, curating and re-quantifying more than 40,000 samples from a public database using HPC-based parallel processing pipelines. I also co-developed \href{https://github.com/kvittingseerup/IsoformSwitchAnalyzeR}{IsoformSwitchAnalyzeR} v2, an R package used by researchers worldwide, now published as a preprint on bioRxiv. For my thesis I am building \href{https://github.com/chunxubioinfor/scbatch_vari}{scBatch}, a Python package for structured batch variability assessment. Writing clean, testable research software that others can rely on is something I take seriously.

---

### [tags: adaptability, domain-transfer, ml, learning, cross-domain]

**Moving Between Theory and Implementation**

I adapt quickly across problem domains and enjoy the full cycle from mathematical formulation to working code. I transitioned from biotechnology to market consulting to bioinformatics, and in each case built the technical skills needed from scratch. I hold DTU's Machine Learning and Deep Learning courses, and have applied these methods practically in research settings. I am comfortable in environments where ideas are judged by evidence and the bar for implementation quality is high.

---

### [tags: bioinformatics, software, pipelines, r-package, github-issues]

**Bioinformatics Software & Pipelines Development**

During the past two years, I've been working on the development, maintenance and update of \href{https://github.com/kvittingseerup/IsoformSwitchAnalyzeR}{IsoformSwitchAnalyzeR}. I regularly checked and solved issues on GitHub, then planned and implemented the necessary updates. We've updated it to version 2.0 and applied it to both long-read (Alzheimer's) and single-cell (Glioblastoma) RNAseq data to decode disease mechanisms at the isoform level (preprint available).

---

### [tags: r-shiny, dashboard, visualization, integration, thesis]

**Development of R Shiny Dashboards**

In my master's thesis, I'm developing quantitative methods to assess batch-to-batch variability in single-cell RNAseq data. Because no single method covers everything, I'm designing and implementing interactive R Shiny dashboards that integrate and visualise results from multiple computational methods in one place — making complex analyses accessible to researchers without a bioinformatics background.

---

### [tags: collaboration, teamwork, phd-environment, support]

**Collaborative Mindset**

I've worked closely with PhD students, postdocs, and researchers at both DTU and Novo Nordisk. I often help biologists run analyses, troubleshoot pipelines, or discuss data interpretation, and I genuinely enjoy this kind of collaborative problem-solving. I'm used to working in fast-paced research environments where priorities shift and ad-hoc requests are part of the job.

---

### [tags: data-analysis, quantitative, r, python, benchmarking, statistics]

**Quantitative Data Analysis**

I study bioinformatics, a field combining biology and data science, and have two years of experience working at DTU HealthTech. I contributed to the development of an R package and introduced a new statistical framework for isoform-switch analysis. This work involved extensive quantitative modelling, benchmarking, and visualisation, and has resulted in a research paper. I work daily with R and Python and am comfortable designing and interpreting statistical analyses from scratch.

---

### [tags: data-management, data-collection, metadata, consulting, secondary-data]

**Data Collection and Management**

At DTU HealthTech, I collaborated with colleagues on data collection, quality control, metadata handling, and preprocessing for large-scale proteomics and transcriptomics datasets. During my consulting internship at Illuminera (IQVIA), I also worked with secondary data sources to track market trends in pharma, performed competitive landscape research, and collected social-media data for social listening analyses. I'm used to working with messy, heterogeneous data and turning it into something structured and usable.

---

### [tags: data-translation, communication, stakeholders, consulting, non-technical]

**Data Translation & Communication**

I have experience translating complex analyses into both academic outputs and actionable insights for pharmaceutical clients. At Illuminera, I used Power BI and PowerPoint to deliver strategic reports to clients, tailoring the framing to different audiences. In research settings, I regularly explain statistical results to biologists and clinicians who don't have a computational background. Getting that translation right — precise but accessible — is something I've put a lot of thought into.

---

### [tags: ai, llm, agent, nlp, hobby-project, practical-ai, n8n, openai, workflow-automation]

**Applied AI \& Agent Development**

Outside of my thesis, I've been building AI-powered tools to solve real problems.

\textbf{DailyJobMatch} is an automated job-matching workflow built on n8n and deployed with Docker. It uses Apify to scrape LinkedIn for new postings daily, retrieves my CV from Google Drive, then scores each job against my profile using the OpenAI API across six dimensions (background match, skills overlap, experience relevance, seniority, language, company fit). It deduplicates and filters out irrelevant listings, then sends a formatted HTML email digest with ranked matches, scoring breakdowns, and direct apply links. The key tech: n8n workflow automation, OpenAI API (structured JSON output), Apify LinkedIn scraper, Google Drive/Gmail integration, Docker deployment.

\textbf{Job\_dk} is a separate Python project: an end-to-end scraping and analysis pipeline for the Danish job market. It scrapes 2,500+ Jobindex listings using multi-strategy extraction (requests + trafilatura, BeautifulSoup fallback, Playwright headless browser for JS pages), then runs two LLM layers on top: Claude Haiku for structured field extraction (sector, seniority, skills) and GPT-4o for CV-to-job matching with scores and reasoning. Key tech: Python, Playwright, trafilatura, BeautifulSoup, rate limiting, URL caching, resume support, OpenAI API, Anthropic API.

These are two different projects and should not be confused. DailyJobMatch is a no-code n8n workflow; Job\_dk is a Python codebase.

---

### [tags: cancer, immunology, single-cell, translational, glioblastoma, hla]

**Computational Cancer Research**

My interest in cancer research developed through both coursework and project work. In my immunological bioinformatics course at DTU, I worked on epitope prediction and HLA-aware filtering for HIV-1 vaccination. More recently, I applied isoform-level analysis to single-cell glioblastoma data as part of the IsoformSwitchAnalyzeR project, where we observed isoform usage changes potentially linked to tumour invasion. I find the intersection of computational methods and cancer biology genuinely compelling.

---

### [tags: deep-learning, ehr, clinical-data, icu, transformer, mortality-prediction, health-data]

**Deep Learning Model Development for Electronic Health Records (EHR)**

During the Deep Learning course at DTU, we developed and adapted deep learning models for mortality risk prediction using large-scale ICU EHR time-series data. We re-designed an existing state-space-based architecture into a transformer-based model, implemented strategies to address severe class imbalance, and improved sensitivity to high-risk patients while critically evaluating trade-offs in AUROC, precision, and recall.

---

### [tags: sql, database, data-management, etl, fair, hpc, gpmdb]

**Database and Data Management (SQL)**

Enrolled in both DTU's database course and IBM's Databases and SQL for Data Science course, giving a solid foundation in SQL and ETL. At DTU HealthTech, developed and maintained data resources for isoform-level proteomics analysis: collected, curated, and QC'd 40k+ proteomics samples from GPMdb, built HPC pipeline to re-quantify all data, extracted and organised metadata adhering to FAIR principles, created automated update scripts, and initiated a mini-project to transform these resources into a true relational database.

---

### [tags: public-health, surveillance, sequencing, ssi-style, monitoring]

**Bioinformatics for Public Health & Surveillance**

My experience spans both research tool development and applied analysis, and I find the idea of bioinformatics supporting public health monitoring particularly meaningful. Having lived through the COVID-19 pandemic, I've thought a lot about how better computational infrastructure — for sequencing, tracking, and interpretation — could have made a real difference earlier. I bring both technical skills and genuine motivation to work where analysis has direct health impact.

---
