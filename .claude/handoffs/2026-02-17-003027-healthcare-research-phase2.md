# Handoff: RBC Borealis — Healthcare Research Complete, Ready for Idea Selection & Proposal

## Session Metadata
- Created: 2026-02-17 00:30:27
- Project: /Users/aryanbhatia/Documents/0DevProjects/rbc-borealis
- Branch: main
- Session duration: ~2 hours (continuation session from context compaction)

### Recent Commits (for context)
  - c70b37b docs: add PDF versions of all research files
  - 98c924f feat: add program docs and project idea research for Let's SOLVE It Spring 2026

## Handoff Chain

- **Continues from**: [2026-02-16-235842-rbc-borealis-research.md](./2026-02-16-235842-rbc-borealis-research.md)
  - Previous title: RBC Borealis Let's SOLVE It — Program Research & Idea Generation
- **Supersedes**: None (builds on previous handoff)

## Current State Summary

Healthcare-focused research phase is **complete**. We created 10 markdown files in `research-healthcare/` covering 9 healthcare ML project ideas (ranked) plus a summary. The user is now evaluating which idea to pursue for their RBC Borealis "Let's SOLVE It" Spring 2026 proposal. Key discussion: the user asked about feasibility of the top-ranked ADR (Adverse Drug Reactions) idea for a team without medical background. Recommendation was to go with **Diabetes Risk (#2) or Pediatric Asthma (#3)** instead, as those have intuitive features that don't require domain expertise. The user has NOT yet made a final selection. One PDF was generated (ADR idea). No commits were made this session — all files were written in the previous session.

## Codebase Understanding

### Architecture Overview

This is a research/documentation repo for an RBC Borealis Let's SOLVE It Spring 2026 application. No code yet — just markdown research files, PDFs, and program documentation. The actual ML project code will be written after acceptance into the program.

### Critical Files

| File | Purpose | Relevance |
|------|---------|-----------|
| `research/00-selection-criteria.md` | Inferred scoring rubric from 23 past accepted projects | Basis for all idea scoring |
| `research/01-ideas-ranked.md` | 6 cross-domain ideas ranked (top: Indigenous Water Quality 4.8) | Original research phase |
| `research-healthcare/00-healthcare-ideas-ranked.md` | 9 healthcare ideas ranked with scores | Healthcare research summary |
| `research-healthcare/01-idea-adverse-drug-reactions.md` | #1 ranked (4.8) — ADR prediction from Canada Vigilance | Top pick but needs medical knowledge |
| `research-healthcare/02-idea-diabetes-risk.md` | #2 ranked (4.8) — Diabetes risk from CCHS survey | Recommended for non-medical team |
| `research-healthcare/03-idea-pediatric-asthma.md` | #3 ranked (4.8) — Asthma from air quality + weather | Recommended for non-medical team |
| `docs/proposal-guide.md` | Program proposal format: 500-1000 words, 4 sections | Template for writing proposal |
| `docs/example-proposal.md` | Example accepted proposal | Reference for tone/structure |
| `docs/application-guide.md` | Application checklist and deadlines | Logistics |
| `docs/past-projects-reference.md` | All 23 past projects across 3 cohorts | Context for differentiation |

### Key Patterns Discovered

- Healthcare is the most accepted category: 7/23 past projects (30%)
- Scoring rubric: Canadian/Community Focus (High weight), Clear ML Application (High), Data Availability (High), Quantifiable Impact (Medium), Feasibility in 2 months (Medium), Novelty (Medium), Equity/Diversity Angle (Medium)
- Past healthcare projects: ED wait times, radiology, stroke risk, anesthesia depth, liver transplant, glioblastoma, food bank — so avoid overlap
- Program runs March 13 - May 9, 2026 (2 months)
- Team: 2-3 undergrads paired with an RBC mentor
- GitHub: https://github.com/XboxAryan/rbc-borealis (public)

## Work Completed

### Tasks Finished

- [x] Created 10 healthcare research markdown files in `research-healthcare/`
- [x] Ranked all 9 healthcare ideas using consistent scoring rubric
- [x] Generated PDF for ADR idea (`01-idea-adverse-drug-reactions.pdf`)
- [x] Discussed tangible model outcomes for ADR idea (signal detection, seriousness prediction, risk dashboard)
- [x] Assessed feasibility of ADR for non-medical team — recommended Diabetes or Asthma instead

### Files Modified/Created This Session

| File | Changes | Rationale |
|------|---------|-----------|
| `research-healthcare/01-idea-adverse-drug-reactions.pdf` | Generated PDF | User requested PDF conversion |

Note: All 10 markdown files were written in the previous session (before context compaction). This session was primarily discussion and one PDF generation.

### Decisions Made

| Decision | Options Considered | Rationale |
|----------|-------------------|-----------|
| Ranked ADR, Diabetes, Asthma as top 3 (all 4.8) | All 9 healthcare ideas | Best combination of novelty, data availability, Canadian focus, feasibility |
| Excluded Mental Health Crisis as deep-dive | Could have written a 10th idea file | Overlaps with past cohort projects MindTech and Crisis Companion |
| Recommended Diabetes/Asthma over ADR for non-medical team | ADR was #1 ranked | ADR requires MedDRA coding, drug class knowledge, pharma terminology |
| Signal detection framed as headline ADR deliverable | Seriousness prediction, risk dashboard | Most compelling story: "model flags dangerous drugs before regulators" |

## Pending Work

## Immediate Next Steps

1. **Choose primary idea** — User needs to decide between Diabetes Risk and Pediatric Asthma (or another idea). Key factors: team background, data comfort, story appeal
2. **Choose secondary/backup idea** — Good to have in case the primary overlaps with another applicant
3. **Write 500-1000 word proposal** — Follow format in `docs/proposal-guide.md` with 4 sections: Problem → Why Important → Why ML → What Data
4. **Convert remaining healthcare research files to PDFs** — Only ADR has been converted so far
5. **Review PR #1 from Tanay** — `gh pr view 1` to see collaborator's contribution
6. **Complete application materials** — Per checklist in `docs/application-guide.md`

### Blockers/Open Questions

- [ ] User has not yet selected their primary idea
- [ ] Unknown: does the team have any data science experience with specific tools (Python, R)?
- [ ] Unknown: application deadline (not explicitly stated in scraped materials)
- [ ] PR #1 from Tanay has not been reviewed

### Deferred Items

- Converting all research-healthcare markdown files to PDFs (only ADR done)
- Creating the actual proposal document
- Committing new files to git (no commits made this session)

## Context for Resuming Agent

## Important Context

1. **The user's team has NO medical/healthcare background.** This is the single most important constraint for idea selection. Diabetes Risk and Pediatric Asthma were recommended because their features are intuitive (BMI, age, smoking, PM2.5, temperature).

2. **Two research folders exist:**
   - `research/` — 6 cross-domain ideas (Indigenous Water Quality scored highest at 4.8)
   - `research-healthcare/` — 9 healthcare-specific ideas (ADR, Diabetes, Asthma all 4.8)

3. **Healthcare is strategically the best category** — 30% of past acceptances. But the user should pick an idea they can actually execute well.

4. **The proposal is 500-1000 words** with 4 mandatory sections. See `docs/proposal-guide.md` and `docs/example-proposal.md` for format.

5. **Original research PDFs already exist** in `research/` (converted in a prior session). Healthcare PDFs have NOT been bulk-converted yet.

6. **The ~/md2pdf tool** is available for markdown-to-PDF conversion. Themes: default, dark, minimal.

### Assumptions Made

- Program starts March 13, 2026 — timeline is tight for application
- Team is 2-3 undergrads (including the user) without medical domain expertise
- The user has access to Python/scikit-learn/XGBoost for the actual project
- CCHS PUMF is accessible via Borealis (free for Canadian academics)
- NAPS air quality data is freely downloadable as CSV

### Potential Gotchas

- The CCHS PUMF (for Diabetes idea) may require university library access or Borealis registration — verify early
- Pediatric Asthma idea requires joining multiple datasets (NAPS + AQHI + weather + CCDSS) — more data engineering than Diabetes
- Don't confuse the two research folders (`research/` vs `research-healthcare/`)
- Past cohort overlap: ED wait times, mental health apps, radiology — avoid these
- The scoring rubric was *inferred* from past projects, not officially published by RBC Borealis

## Environment State

### Tools/Services Used

- `~/md2pdf` — Markdown to PDF converter (themes: default, dark, minimal)
- `gh` CLI — GitHub operations (repo: XboxAryan/rbc-borealis)
- Python 3 with `uv` for package management

### Active Processes

- None

### Environment Variables

- None required for this project

## Related Resources

- Previous handoff: `.claude/handoffs/2026-02-16-235842-rbc-borealis-research.md`
- Program website (scraped): `docs/program-overview.md`
- GitHub repo: https://github.com/XboxAryan/rbc-borealis
- RBC Borealis website: https://rbcborealis.com/lets-solve-it/

---

**Security Reminder**: Before finalizing, run `validate_handoff.py` to check for accidental secret exposure.
