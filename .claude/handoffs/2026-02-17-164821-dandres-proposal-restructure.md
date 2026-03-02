# Handoff: Dandres et al. (2016) Integration into DC Siting Proposal

## Session Metadata
- Created: 2026-02-17 16:48:21
- Project: /Users/aryanbhatia/Documents/0DevProjects/rbc-borealis
- Branch: main
- Session duration: ~1.5 hours

### Recent Commits (for context)
  - 633c605 feat: integrate Dandres et al. (2016) marginal electricity analysis into proposal
  - e551617 Merge pull request #2 from TanayJyot:tanay
  - 0ee27bd Data Centre Idea
  - 6e3533a changes to quotes
  - 59b8877 thoughts

## Handoff Chain

- **Continues from**: [2026-02-17-020644-shelter-homelessness-pivot.md](./2026-02-17-020644-shelter-homelessness-pivot.md)
  - Previous title: RBC Borealis — Pivot to Homelessness/Shelter ML, Building on Re:Housed
- **Supersedes**: None

## Current State Summary

Deep-dived into Dandres et al. (2016), "Consequences of Future Data Center Deployment in Canada on Electricity Generation and Environmental Impacts" (Journal of Industrial Ecology, Yale). The paper's core finding — that marginal electricity serving new DC loads in Canada is 5-6x higher carbon than the grid average, and 60-70% comes from reduced US exports — was integrated into the proposal and all supporting research docs. The proposal is now restructured with a stronger problem framing ("the siting problem is harder than it looks"), the carbon intensity sub-model targets marginal intensity as its primary metric, and Dandres is positioned as the closest prior work that our SIS tool extends. DOCX and PDF regenerated and pushed to `main`.

## Codebase Understanding

### Architecture Overview

This is a research/proposal repo (not a software project yet). Structure:
- `proposal/` — The actual RBC Borealis submission (`draft-v1.md` is the source of truth, `generate-docx.py` renders it to branded DOCX, pandoc converts to PDF)
- `research-datacenter/` — Deep research organized by: problem domain, datasets, methodology (4 sub-models + composite scoring), feasibility, literature, and proposal alignment
- `research-healthcare/` — Alternative healthcare project ideas (ranked, not pursued)
- `research/` — Early-stage brainstorming

### Critical Files

| File | Purpose | Relevance |
|------|---------|-----------|
| `proposal/draft-v1.md` | The actual proposal submission text | Source of truth for DOCX/PDF |
| `proposal/generate-docx.py` | Python script generating branded DOCX | Must be updated when draft-v1.md changes |
| `research-datacenter/03-methodology/02-carbon-intensity-model.md` | Carbon intensity sub-model design | Now features marginal vs average as core design decision |
| `research-datacenter/03-methodology/05-composite-scoring.md` | Composite SIS formula and Monte Carlo | S_carbon now uses marginal intensity; MC includes marginal multiplier |
| `research-datacenter/05-literature/01-key-papers.md` | Annotated bibliography (15 papers) | Dandres is now paper #1 |
| `research-datacenter/06-proposal-alignment.md` | Rubric scoring and gap analysis | Dandres in novelty table; 4 novel contributions |
| `J of Industrial Ecology - 2016 - Dandres - ....pdf` | The Dandres paper itself | Key reference; figures verified against Table 1 and Table 2 |

### Key Patterns Discovered

- **DOCX generation is code-driven**: `generate-docx.py` hardcodes all proposal text with python-docx. When `draft-v1.md` changes, the script must be manually updated to match. They are NOT auto-synced.
- **PDF is generated via pandoc**: `pandoc proposal-v1.docx -o proposal-v1.pdf --pdf-engine=xelatex -V mainfont="Helvetica Neue"` — must use Helvetica Neue for Unicode subscript support (CO₂).
- **python-docx is installed under system Python 3.9** (`/Library/Developer/CommandLineTools/usr/bin/python3`), not the user's uv-managed Python 3.12.
- **Word count**: 970 words in draft-v1.md (963 body text in DOCX). No stated word limit found, but the document fits on 3 pages.

## Work Completed

### Tasks Finished

- [x] Read and analyzed full Dandres et al. (2016) paper (11 pages, Tables 1-2, Figures 2-5)
- [x] Rewritten problem statement in `draft-v1.md` with marginal intensity framing
- [x] Updated carbon intensity sub-model description in `draft-v1.md`
- [x] Added Dandres reference to data sources in `draft-v1.md`
- [x] Updated carbon intensity methodology doc (marginal as core design decision, Electricity Maps marginal data, multiplier fallback)
- [x] Updated composite scoring doc (S_carbon uses marginal, cross-border flag, MC uncertainty source)
- [x] Added Dandres as paper #1 in literature review with full citation and gap analysis
- [x] Updated proposal alignment doc (novelty table, quantifiable impact, 4 contributions)
- [x] Updated `generate-docx.py` to match new draft-v1.md text
- [x] Regenerated proposal-v1.docx and proposal-v1.pdf
- [x] Verified all Dandres figures against the PDF (Table 1: 0.85-0.93 kg CO2-eq/kWh; in-text: 0.89-1.01; natural gas 47-53%; coal 38-48%; 60-70% from US export reduction)
- [x] Committed and pushed to main (633c605)

### Files Modified

| File | Changes | Rationale |
|------|---------|-----------|
| `proposal/draft-v1.md` | Problem statement rewritten, carbon sub-model updated, Dandres data source added | Core proposal restructuring |
| `proposal/generate-docx.py` | Matching text updates to 3 sections | Keep DOCX in sync with markdown |
| `proposal/proposal-v1.docx` | Regenerated | Output artifact |
| `proposal/proposal-v1.pdf` | Regenerated | Output artifact |
| `research-datacenter/03-methodology/02-carbon-intensity-model.md` | Marginal vs average promoted to core design, new training targets, multiplier fallback | Methodology now reflects Dandres insights |
| `research-datacenter/03-methodology/05-composite-scoring.md` | S_carbon definition, MC uncertainty table, cross-border flag, references | Scoring uses marginal intensity |
| `research-datacenter/05-literature/01-key-papers.md` | Dandres added as paper #1 with full annotation | Most directly relevant prior work |
| `research-datacenter/06-proposal-alignment.md` | Gap table, quantifiable impact, novelty section | Positioning against Dandres |

### Decisions Made

| Decision | Options Considered | Rationale |
|----------|-------------------|-----------|
| Use "0.85-1.01 kg CO2-eq/kWh" as cited range | Table 1 only (0.85-0.93), in-text only (0.89-1.01), combined (0.85-1.01) | Combined range spans both the table and in-text references; conservative and accurate |
| Frame as additive, not contradictory to 286x hook | Replace 286x with marginal figures, keep 286x, layer both | "286x AND hidden marginal costs" is stronger than either alone |
| Scope out full CLCA / cross-border trade modeling | Build a trade model, use Dandres as calibration, flag only | Flag + future work framing stays within 320 person-hour budget |
| Use marginal intensity as default SIS input | Average only, marginal only, both with toggle | Marginal is methodologically correct for new loads; average available for comparison |
| Marginal multiplier fallback for data-scarce provinces | Skip provinces, use average, apply multiplier from Dandres | Uniform(2x-5x) for mixed grids, Uniform(1x-1.5x) for fossil grids — grounded in Dandres Table 1 |

## Pending Work

## Immediate Next Steps

1. **Team review of restructured proposal**: Share the updated `draft-v1.md` with team (Tanay et al.) for feedback on the Dandres integration — especially whether the marginal intensity framing resonates or feels overly academic
2. **Finalize proposal word count / format**: Check if RBC Borealis has a word limit or page limit; current draft is 970 words / 3 pages. May need trimming or expansion
3. **Data validation**: Confirm Electricity Maps provides marginal intensity data for CA-ON and CA-AB zones (claimed in methodology docs but not empirically verified)
4. **Consider adding Dandres to the "Strongest Pitch" paragraph** in `06-proposal-alignment.md` (lines 188-190) — currently still uses the old framing

### Blockers/Open Questions

- [ ] Does Electricity Maps actually expose marginal vs average intensity via their API/downloads? Need to verify before submission.
- [ ] The Dandres paper is from 2016 — should we acknowledge the Canadian grid has changed since then (Alberta coal phase-out, Pickering retirement)? Currently handled with "cite for methodology, not data" but team may want explicit caveat in proposal.
- [ ] Word count / format constraints for RBC Borealis submission are not documented anywhere in the repo.

### Deferred Items

- Full AHP stakeholder elicitation for weights (stretch goal, 8-12 hrs)
- CarbonCast integration (stretch goal, 15-20 hrs)
- Hourly carbon forecasting for ON/AB (stretch goal, 15-20 hrs)
- Streamlit dashboard (stretch goal, 10-15 hrs)

## Context for Resuming Agent

## Important Context

1. **The proposal is for RBC Borealis "Let's SOLVE It"** — an undergraduate ML for social good program. 4 students, 8 weeks, 320 person-hours. The proposal needs to be technically ambitious but feasible.

2. **The Dandres integration was a framing/literature change, not a methodology overhaul.** The 4 sub-models are unchanged architecturally. The key changes are: (a) problem statement is now stronger, (b) carbon model targets marginal intensity, (c) Monte Carlo includes marginal multiplier uncertainty, (d) Dandres is positioned as the closest prior work we extend.

3. **Total additional effort from Dandres integration: ~14-23 person-hours (4-7% of budget).** This was explicitly scoped to be low-risk.

4. **The `generate-docx.py` script and `draft-v1.md` must stay in sync manually.** If you edit one, edit the other. The DOCX has RBC Borealis branding (Calibri, navy header, page numbers). The PDF is a plain pandoc render — the DOCX is the presentation-ready version.

5. **Key Dandres figures (verified against PDF):**
   - Marginal GHG intensity: 0.85-1.01 kg CO2-eq/kWh (Table 1 + in-text p.1316)
   - Canadian average: 0.16 kg CO2-eq/kWh
   - Natural gas share of marginal: 47-53%
   - Coal share: 38-48%
   - US export displacement: 60-70% of marginal electricity
   - Paper DOI: 10.1111/jiec.12515

6. **Self-assessed rubric score: 4.7/5.** Strongest on data availability (30+ datasets), ML fit (4 sub-models), timeliness (Bill 40), and novelty (no cohort overlap). Weakest on equity (4/5, indirect community impact) and feasibility (4/5, integration complexity).

### Assumptions Made

- Electricity Maps provides marginal intensity data for Canadian zones (not yet empirically verified)
- The RBC Borealis proposal format accepts ~1000 words / 3 pages (no explicit limit found)
- The Dandres paper's qualitative insights (marginal >> average, cross-border effects) still hold despite the 2016 publication date
- Team members have not made conflicting changes to these files

### Potential Gotchas

- **python-docx runs on system Python 3.9**, not the user's uv-managed Python 3.12. Use `/Library/Developer/CommandLineTools/usr/bin/python3` to run `generate-docx.py`.
- **The Word temp file `~$oposal-v1.docx`** may appear if the DOCX was open during generation. It's in `.gitignore` territory but not formally gitignored.
- **pandoc PDF conversion** needs `--pdf-engine=xelatex -V mainfont="Helvetica Neue"` for Unicode subscript support. Default LaTeX engine chokes on CO₂.
- **The proposal references "Dandres et al. 2016" three times** — if you need to update the citation, change it in all three locations in `draft-v1.md` AND the matching locations in `generate-docx.py`.

## Environment State

### Tools/Services Used

- python-docx (installed via pip3 to system Python 3.9)
- pandoc (Homebrew, /opt/homebrew/bin/pandoc)
- xelatex (TeX Live 2025)
- git (pushing to github.com:XboxAryan/rbc-borealis.git)

### Active Processes

- None running

### Environment Variables

- None required for this work

## Related Resources

- Plan file: `/Users/aryanbhatia/.claude/plans/hidden-jingling-crown.md` — full analysis of Dandres paper implications
- Dandres PDF: `J of Industrial Ecology - 2016 - Dandres - Consequences of Future Data Center Deployment in Canada on Electricity.pdf` (repo root)
- Previous handoffs in `.claude/handoffs/`

---

**Security Reminder**: Before finalizing, run `validate_handoff.py` to check for accidental secret exposure.
