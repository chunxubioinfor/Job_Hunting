---
name: Chunxu Han — Writing Style
description: Notes on Chunxu's tone, structure, and style for CV bullet points and cover letters
type: user
---

# Writing Style Notes

## Cover Letter Style

**Tone:** Personal, genuine, reflective — not corporate or stiff. Chunxu writes like a thoughtful person talking to another person, not a template-filler.

**Structure pattern:**
1. Hook paragraph — a personal or story-driven opener that explains *why* this specific role/company caught attention (not just "I am applying for...")
2. Technical paragraph — concrete evidence of relevant skills/experience, naming specific tools, packages, outcomes
3. Connecting paragraph — bridges consulting/soft skills or explains trajectory (e.g. why moving from academic to industry, or why this role fits a long-term motivation)
4. Closing — brief, warm, invites further conversation

**Key stylistic traits:**
- Uses "I" naturally and frequently — doesn't hedge into passive voice
- Includes specific named projects and tools (IsoformSwitchAnalyzeR, scBatch, DailyJobMatch)
- References personal growth honestly: "I grew from X to Y", "I realised..."
- Shows genuine curiosity and self-awareness, not just competence claims
- Mentions personal connections when they exist (e.g. "a friend shared your website")
- Doesn't oversell — measured confidence, not hype
- Ends simply ("Thank you for considering my application") — no excessive flattery

**Length:** ~4 short paragraphs, concise. No bullet points in cover letters.

---

## CV Style

**Format:** RenderCV-style LaTeX with custom environments (`twocolentry`, `onecolentry`, `highlights`)
- Primary color: RGB(0, 79, 144) — professional blue
- ATS-parsable (glyph-to-unicode enabled)

**Bullet point style:**
- Bold lead phrase (e.g. `\textbf{Development and Maintenance of Tools:}`) followed by prose description
- Personal and reflective tone even in bullets: "This experience sharpened my...", "I pushed myself to..."
- Concrete numbers/scale when available (40,000+ samples, 2 years, v2)
- Links to GitHub/preprints included inline

**Sections used (varies by role):**
- Header (always)
- Motivation / Relevant Experience (for targeted roles — replaces or supplements standard sections)
- Education
- Work Experience
- Publications (when relevant)
- Skills and Hobbies (always)

**Key observation:** Chunxu swaps in a "Relevant Experience" or "Motivation" section at the top that is completely rewritten per application — this is the main customization zone. The Education, Work Experience, and Skills sections stay mostly stable.

---

## Adaptation patterns observed across versions

| Role type | Top section focus |
|-----------|------------------|
| Bioinformatics / Software | Software dev, pipelines, scBatch, IsoformSwitchAnalyzeR |
| Data Scientist (industry) | Data engineering, SQL, Power BI, GMP compliance |
| PhD / Academic | AI curiosity, single-cell methods, research software |
| Consulting | Consulting internship, stakeholder engagement, data storytelling |
| Retail (part-time) | Likely minimal technical content |
