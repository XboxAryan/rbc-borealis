# Handoff: RBC Borealis Let's SOLVE It — Program Research & Idea Generation

## Session Metadata
- Created: 2026-02-16 23:58:42
- Project: /Users/aryanbhatia/Documents/0DevProjects/rbc-borealis
- Branch: main
- Session duration: ~1 hour

### Recent Commits (for context)
  - c70b37b docs: add PDF versions of all research files
  - 98c924f feat: add program docs and project idea research for Let's SOLVE It Spring 2026

## Handoff Chain

- **Continues from**: None (fresh start)
- **Supersedes**: None

> This is the first handoff for this task.

## Current State Summary

We scraped the entire RBC Borealis "Let's SOLVE It" Spring 2026 mentorship program website and extracted all program information into structured markdown files. Then we researched and documented 6 ranked project ideas for the proposal, each with problem statistics, ML approaches, specific open datasets with URLs, and acceptance likelihood analysis based on patterns from 23 past accepted projects. All files also have PDF versions. The repo is public on GitHub at https://github.com/XboxAryan/rbc-borealis. The next phase is to choose a project idea and write the actual 500-1000 word proposal.

## Codebase Understanding

### Architecture Overview

This is a documentation/research repo — no application code. Two main directories:
- `docs/` — Program info scraped from rbcborealis.com (what the program is, how to apply, deadlines)
- `research/` — Our strategic analysis of which project ideas to propose (ranked by acceptance likelihood)

### Critical Files

| File | Purpose | Relevance |
|------|---------|-----------|
| `docs/program-overview.md` | Full program description, eligibility, benefits, deliverables | Reference when writing proposal |
| `docs/application-guide.md` | Every form field, attestations, pre-submission checklist | Use when filling out the actual application |
| `docs/timeline-and-deadlines.md` | Key dates: Welcome Day Mar 6, Program Mar 13–May 15, Presentation Day May 11 | Deadline tracking |
| `docs/proposal-guide.md` | Proposal requirements (500-1000 words), tips from past winners, project categories | Template for writing the proposal |
| `docs/example-proposal.md` | Official example proposal (food bank forecasting) with analysis of what makes it work | Model to follow for proposal structure and tone |
| `docs/past-projects-reference.md` | All 23 past projects across 3 cohorts with problems, solutions, ML techniques | Ensure our idea is novel and understand what gets accepted |
| `research/00-selection-criteria.md` | Inferred scoring rubric, patterns, topics to avoid | Strategic guide for idea selection |
| `research/01-ideas-ranked.md` | All 6 ideas ranked with composite scores and recommendation | Decision document for choosing primary + secondary proposal |
| `research/02-idea-indigenous-water-quality.md` | #1 ranked idea: Predicting DWAs on First Nations reserves (score 4.8/5) | Top pick — strongest equity angle + best data |
| `research/03-idea-food-desert-accessibility.md` | #2 ranked idea: Mapping Canadian food deserts (score 4.7/5) | Strong pick — purpose-built government dataset |
| `research/04-idea-opioid-overdose-prediction.md` | #3 ranked idea: Community-level overdose risk (score 4.3/5) | Urgent crisis with proven ML approaches |
| `research/05-idea-wildfire-smoke-health.md` | #4 ranked idea: Wildfire smoke PM2.5 health impact (score 4.3/5) | Best secondary proposal — different from past wildfire projects |
| `research/06-idea-housing-affordability.md` | #5 ranked idea: Neighborhood affordability risk (score 4.0/5) | Universal relevance but weaker equity angle |
| `research/07-idea-transit-accessibility-seniors.md` | #6 ranked idea: Senior transit gaps (score 3.7/5) | Novel but hardest to scope |
| `docs/LSI_Project_Proposal_Example.pdf` | Original official example proposal PDF from RBC Borealis | Reference document |

### Key Patterns Discovered

- **Past accepted projects** universally have: Canadian focus, specific statistics, actionable ML output, identified datasets
- **Overdone topics to avoid:** shelter bed forecasting (done 2x), wildfire fire detection (done 2x), generic mental health chatbot
- **Strong equity/diversity angle** aligns with RBC Borealis + CIFAR mission and likely boosts acceptance
- **Simple ML is fine:** Random Forest, logistic regression, basic neural nets all accepted. No need for cutting-edge architecture.
- **The official example proposal** is ~550 words, uses 4 clear sections, and is honest about data limitations

## Work Completed

### Tasks Finished

- [x] Scraped rbcborealis.com/lets-solve-it/ (main program page)
- [x] Scraped application form page with all fields and attestations
- [x] Downloaded and converted official example proposal PDF to markdown
- [x] Scraped 3 past presentation day articles (Spring 2024, Fall 2023, Spring 2023)
- [x] Scraped diversity/inclusion article for CIFAR partnership context
- [x] Created 7 structured docs/ files from scraped content
- [x] Analyzed 23 past projects to identify acceptance patterns
- [x] Web-searched 10+ social cause areas for ML feasibility and dataset availability
- [x] Researched specific datasets on Open Canada, StatCan, Kaggle for each idea
- [x] Created 8 research/ files with ranked ideas and deep dives
- [x] Converted all research files to PDFs
- [x] Initialized git repo, committed, created public GitHub repo, pushed all files
- [x] PR #1 exists from collaborator "tanay" with title "thoughts - tanay" (not yet reviewed)

### Files Modified

| File | Changes | Rationale |
|------|---------|-----------|
| All 15 .md files + 1 PDF + 8 research PDFs | Created from scratch | Full project setup |

### Decisions Made

| Decision | Options Considered | Rationale |
|----------|-------------------|-----------|
| Ranked Indigenous Water Quality as #1 idea | All 6 ideas compared | Highest composite score: novel, strong equity angle, government dataset on Open Canada, published XGBoost study (86% accuracy), uniquely Canadian |
| Recommended Wildfire Smoke Health as secondary proposal | Ideas #3-#6 | Different domain from primary, excellent NAPS data (260 stations since 1969), timely post-2023, differentiates from past fire detection projects |
| Used Open Canada / StatCan as primary data sources | Kaggle, academic, proprietary | Government open data has no access barriers — critical for a 2-month undergrad program |
| Kept each research file under 200 lines | Longer deep dives vs. concise | User requested 200-250 line max. Concise files are more useful for Claude context. |

## Pending Work

## Immediate Next Steps

1. **Choose primary + secondary project ideas** — Review `research/01-ideas-ranked.md` and decide which 1-2 ideas to propose
2. **Review PR #1** from collaborator Tanay — `gh pr view 1` or use VS Code GitHub PR extension to see their thoughts
3. **Write the 500-1000 word proposal** — Follow structure in `docs/proposal-guide.md` and model after `docs/example-proposal.md`
4. **Write optional secondary proposal** — Same format, different idea
5. **Prepare application materials** — Use checklist in `docs/application-guide.md` to gather all per-member info before starting the form (form cannot be saved mid-progress)

### Blockers/Open Questions

- [ ] Which idea(s) does the team want to pursue? Need team consensus.
- [ ] Does any team member have personal connection to the chosen cause? (Strengthens proposal per analysis)
- [ ] PR #1 from Tanay — may contain additional ideas or feedback to incorporate
- [ ] Need to confirm all team members' availability for Welcome Day (Mar 6) and Presentation Day (May 11)

### Deferred Items

- Writing the actual proposal document (waiting on idea selection)
- Filling out the application form (waiting on proposal + team member info)
- Detailed dataset exploration / downloading actual data files (do after acceptance)

## Context for Resuming Agent

## Important Context

- **Application deadline is approaching** — applications are currently open, program starts March 13, 2026
- **The application form CANNOT be saved** — all materials must be ready before starting it
- **PR #1 exists** from collaborator "tanay" at https://github.com/XboxAryan/rbc-borealis/pull/1 — review before finalizing idea choice
- **Proposal structure** should follow the 4-section format from the official example: "What is the problem?" → "Why is it important to me?" → "Why Machine Learning Can Help?" → "What Data to Use?"
- **Two proposals allowed** — primary (evaluated first) + optional secondary (mentor picks between them if selected)
- **GitHub repo is public** at https://github.com/XboxAryan/rbc-borealis under account XboxAryan

### Assumptions Made

- Team size and members are not yet finalized (research was done independently of team composition)
- No specific personal connection to any cause was assumed — team should pick based on genuine interest
- All datasets identified are publicly accessible (verified via Open Canada / StatCan / Kaggle URLs)
- The program will accept the Spring 2026 cohort as described on the current website

### Potential Gotchas

- **Don't repeat past topics:** Shelter forecasting and fire detection have been done 2x each — reviewers may prefer fresh ideas
- **Indigenous data sensitivity:** If choosing water quality idea, proposal must respectfully frame it as supporting communities, not extracting from them. Acknowledge data sovereignty.
- **Opioid data access:** Individual-level health data (BCOOAF) requires StatCan Research Data Centre access — may need to scope to aggregated/public data
- **Quebec food desert data:** Primary StatCan food desert dataset is Quebec-focused — proposal should acknowledge and propose national extension
- **Form is one-shot:** Cannot save the application mid-progress. Have everything ready first.

## Environment State

### Tools/Services Used

- GitHub CLI (`gh`) — authenticated as XboxAryan
- `pdftotext` (homebrew) — used for PDF text extraction
- `md2pdf` (~/md2pdf) — custom tool for markdown-to-PDF conversion
- Git over SSH to github.com

### Active Processes

- None — no servers or background processes running

### Environment Variables

- None required for this project

## Related Resources

- Program main page: https://rbcborealis.com/lets-solve-it/
- Application form: https://rbcborealis.com/program-applications/lets-solve-it-spring-2026/
- GitHub repo: https://github.com/XboxAryan/rbc-borealis
- PR #1: https://github.com/XboxAryan/rbc-borealis/pull/1
- Open Canada Portal: https://open.canada.ca/data/en/dataset
- ISC Water Advisory Data: https://open.canada.ca/data/en/dataset/57b86ac5-e127-41bc-94b8-14b2d89aed0b
- StatCan Food Desert Indices: https://open.canada.ca/data/en/dataset/c69d8357-061a-4122-b8b9-51bcbc786aa7
- NAPS Air Quality Data: https://open.canada.ca/data/en/dataset/1b36a356-defd-4813-acea-47bc3abd859b

---

**Security Reminder**: Before finalizing, run `validate_handoff.py` to check for accidental secret exposure.
