# Handoff: RBC Borealis — Pivot to Homelessness/Shelter ML, Building on Re:Housed

## Session Metadata
- Created: 2026-02-17 02:06:44
- Project: /Users/aryanbhatia/Documents/0DevProjects/rbc-borealis
- Branch: main
- Session duration: ~2 hours

### Recent Commits (for context)
  - c70b37b docs: add PDF versions of all research files
  - 98c924f feat: add program docs and project idea research for Let's SOLVE It Spring 2026

## Handoff Chain

- **Continues from**: [2026-02-17-003027-healthcare-research-phase2.md](./2026-02-17-003027-healthcare-research-phase2.md)
  - Previous title: RBC Borealis — Healthcare Research Complete, Ready for Idea Selection & Proposal
- **Supersedes**: None (builds on previous, adds new direction)

## Current State Summary

The user pivoted away from healthcare ideas. After exploring a data center siting idea (inspired by Carney's AI infrastructure push) and finding it too GIS-heavy, the user discovered the **Re:Housed project** (AI4Good Lab 2025 Toronto Accelerator Award winner) — a Random Forest model that recommends optimal shelter placement locations in Toronto. The user asked how to build on it. Three options were presented, and **Option A was recommended: predicting WHO becomes chronically homeless** from shelter system flow data (binary classification). This complements Re:Housed (which answers WHERE) by answering WHO needs intervention. The user has NOT yet confirmed this direction. No new files were written this session — this was entirely strategic discussion.

## Codebase Understanding

### Architecture Overview

Research/documentation repo for RBC Borealis Let's SOLVE It Spring 2026 application. Two completed research folders exist (`research/` and `research-healthcare/`). No code yet. The shelter/homelessness direction has not been written up as a research file.

### Critical Files

| File | Purpose | Relevance |
|------|---------|-----------|
| `research/00-selection-criteria.md` | Scoring rubric inferred from 23 past projects | Still applies to any new idea |
| `research-healthcare/00-healthcare-ideas-ranked.md` | 9 healthcare ideas ranked | May be abandoned if user pivots to shelter idea |
| `docs/proposal-guide.md` | 500-1000 word proposal format (4 sections) | Template for writing the actual application |
| `docs/example-proposal.md` | Example accepted proposal | Reference for tone/structure |
| `docs/past-projects-reference.md` | All 23 past projects across 3 cohorts | CRITICAL: shelter bed demand forecasting in Toronto was done in a past cohort — must differentiate |
| `research-healthcare/01-idea-adverse-drug-reactions.pdf` | Only PDF generated this session | User requested this earlier |

### Key Patterns Discovered

- Past RBC Borealis cohort included a "Shelter Bed Demand Forecasting" project (Toronto) — any new shelter project MUST differentiate from this
- Re:Housed (AI4Good 2025) used Random Forest on Toronto encampment data for shelter PLACEMENT optimization — 7-week project, won award
- Re:Housed's stated limitations: occupancy unreliable as demand metric, no temporal component, Toronto-only, wants shelter intake call data
- Social services is the 2nd most accepted category after healthcare (17% of past projects)
- The user's team has NO medical/healthcare background — shelter/homelessness doesn't require domain expertise

## Work Completed

### Tasks Finished

- [x] Explored data center siting idea — concluded too GIS-heavy and weak ML task for 2-month project
- [x] Researched Re:Housed project (AI4Good 2025 award winner) — extracted methodology, data, limitations
- [x] Identified 3 options to build on Re:Housed: (A) chronic homelessness prediction, (B) demand spike forecasting, (C) multi-city expansion
- [x] Recommended Option A as strongest pick
- [x] Researched Carney's AI/data center policy for Canadian context
- [x] Generated PDF for ADR healthcare idea
- [x] Confirmed program timeline: Welcome Day March 6, Presentation Day May 11, ~8 weeks at 10 hrs/week

### Files Modified/Created This Session

| File | Changes | Rationale |
|------|---------|-----------|
| `research-healthcare/01-idea-adverse-drug-reactions.pdf` | Generated PDF | User requested |
| `.claude/handoffs/2026-02-17-003027-healthcare-research-phase2.md` | Created mid-session handoff | User requested handoff before pivot |

### Decisions Made

| Decision | Options Considered | Rationale |
|----------|-------------------|-----------|
| ADR not suitable for non-medical team | ADR vs Diabetes vs Asthma | ADR requires MedDRA coding, drug class knowledge; Diabetes/Asthma have intuitive features |
| Data center siting idea not feasible | Build vs don't build | No training labels, small N (~300 CDs), requires GIS skills team doesn't have |
| Recommended Option A (chronic homelessness) over B and C | A: WHO becomes chronic, B: demand spikes, C: multi-city expansion | A has no overlap with Re:Housed or past RBC project, single clean dataset, published baselines, clear binary classification |
| Shelter/homelessness direction explored | Healthcare vs social services | User explicitly said "ignore all previous ideas" when asking about Re:Housed |

## Pending Work

## Immediate Next Steps

1. **User must confirm direction** — Are they going with the chronic homelessness prediction idea, or still exploring?
2. **Deep-dive research on chronic homelessness prediction** — If confirmed, run comprehensive research (datasets, published ML results, Canadian statistics) similar to healthcare research
3. **Write research markdown file** — Create `research-shelter/` or similar folder with the idea writeup
4. **Write 500-1000 word proposal** — Follow `docs/proposal-guide.md` format
5. **Review PR #1 from Tanay** — Still pending from previous sessions

### Blockers/Open Questions

- [ ] User has NOT confirmed the shelter/homelessness direction — still in exploration mode
- [ ] Need to verify Toronto Shelter System Flow data has enough features for individual-level prediction (age, gender, shelter type, prior episodes)
- [ ] Need to check: does the published Canadian HMIS chronic homelessness paper use the same Toronto open data, or restricted HIFIS data?
- [ ] Past RBC Borealis shelter bed forecasting project — need to review exactly what they did to ensure differentiation
- [ ] Unknown: does the team have any personal connection to homelessness/housing issues? (strengthens proposal per guide)

### Deferred Items

- Healthcare idea PDFs (only ADR converted so far) — may not be needed if user pivots away from healthcare
- Committing new files to git — no commits this session
- Choosing between healthcare ideas (Diabetes vs Asthma) — may be moot if user goes with shelter idea

## Context for Resuming Agent

## Important Context

1. **The user is exploring a PIVOT from healthcare to homelessness/shelter ML.** They explicitly said "ignore all previous ideas" when asking about Re:Housed. However, they have NOT confirmed this direction yet.

2. **Three options were presented to build on Re:Housed:**
   - **Option A (recommended): Predict WHO becomes chronically homeless** — binary classification on Toronto Shelter System Flow data. Complements Re:Housed (WHERE) with WHO. No overlap with past RBC Borealis shelter project (which was demand forecasting).
   - **Option B: Predict demand spikes** — time series from daily occupancy + weather/economic factors. Risky because it overlaps with past RBC Borealis shelter bed forecasting project.
   - **Option C: Multi-city expansion** — replicate Re:Housed in Vancouver/Montreal/Calgary. High overlap with Re:Housed itself, fragmented data across cities.

3. **Key data sources identified for Option A:**
   - [Toronto Shelter System Flow Data](https://www.toronto.ca/city-government/data-research-maps/research-reports/housing-and-homelessness-research-and-reports/shelter-system-flow-data/) — monthly, free, tracks entries/exits/returns by demographics
   - [Daily Shelter & Overnight Service Usage](https://www.toronto.ca/city-government/data-research-maps/research-reports/housing-and-homelessness-research-and-reports/shelter-census/) — daily occupancy, free
   - [Toronto Shelter System Flow on Kaggle](https://www.kaggle.com/datasets/ericjdunn/toronto-shelter-system-flow)
   - [StatCan National Shelter Capacity](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410035301) — 2016-2024
   - Published ML paper: [Interpretable ML for chronic homelessness](https://www.sciencedirect.com/science/article/abs/pii/S0952197621000907) — uses Canadian HMIS data

4. **The data center idea was explored and rejected.** User asked about predicting feasible data center locations that minimize environmental harm, inspired by Carney's $925M sovereign AI cloud investment and 100MW+ data center call. Rejected because: no training labels, small N, requires GIS skills, weak ML task. A simplified version (predict environmental stress per census division) was discussed but user moved on to Re:Housed.

5. **Two completed research folders still exist:**
   - `research/` — 6 cross-domain ideas (top: Indigenous Water Quality 4.8/5)
   - `research-healthcare/` — 9 healthcare ideas (top 3: ADR, Diabetes, Asthma all 4.8/5)
   - These can serve as secondary proposal material even if user goes with the shelter idea

6. **Program constraints remain:** 3-5 undergrads, 2 months, 10 hrs/week, no ML experience required, presentation + code repo + one-page report as deliverables.

### Assumptions Made

- Toronto Shelter System Flow data contains enough individual-level features for classification (needs verification — may be aggregate only)
- The published Canadian HMIS chronic homelessness paper provides a reproducible methodology
- The user's team does not have GIS experience (based on data center discussion)
- Social services category (17% of past acceptances) is still a strong category for acceptance

### Potential Gotchas

- **Past RBC Borealis overlap:** A shelter bed demand forecasting project was done in a previous cohort. The chronic homelessness prediction angle is different (WHO vs HOW MANY) but the user should acknowledge and differentiate explicitly in the proposal
- **Toronto Shelter System Flow data may be aggregate** — the monthly data shows counts by demographic group, NOT individual-level records. Need to verify whether individual trajectories can be reconstructed, or if the Kaggle version has more granularity
- **Privacy sensitivity:** Homelessness data involving individuals requires careful framing around ethics, even with de-identified data. The proposal should address this.
- **Re:Housed is very recent (2025)** — citing it shows awareness of current work, but reviewers might wonder if you're just copying their approach. The differentiation (WHO vs WHERE) must be crystal clear.
- **The user explored and rejected 3 separate directions this session** (healthcare, data centers, then shelter). They may still be exploring. Don't assume the shelter idea is final.

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

- Previous handoffs: `.claude/handoffs/2026-02-16-235842-rbc-borealis-research.md`, `.claude/handoffs/2026-02-17-003027-healthcare-research-phase2.md`
- Re:Housed project page: https://www.ai4goodlab.com/news/project-reports/2025/10/31/rehoused-2025-toronto-accelerator-award-winner/
- AI4Good Lab 2025 projects: https://mila.quebec/en/news/ai4good-lab-2025-14-ai-projects-for-social-impact
- Toronto 2025-2030 Homelessness Strategic Plan: https://www.toronto.ca/city-government/data-research-maps/research-reports/housing-and-homelessness-research-and-reports/2025-2030-strategic-plan-to-address-homelessness/
- Carney AI/data center policy: https://www.cbc.ca/news/politics/federal-budget-quantum-ai-computing-9.6966549
- GitHub repo: https://github.com/XboxAryan/rbc-borealis

---

**Security Reminder**: Before finalizing, run `validate_handoff.py` to check for accidental secret exposure.
