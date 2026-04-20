# Handoff: AI Data Center Siting — Research + Proposal Draft Complete

**Date:** 2026-02-17
**Branch:** `main`
**Status:** Research complete, proposal v1 drafted (DOCX + PDF)

---

## What Was Done

### 1. Research Folder (`research-datacenter/`)

19 files, ~4,000 lines — comprehensive knowledge base for the proposal.

```
research-datacenter/
├── 00-overview.md                          (150 lines)
├── 01-problem/
│   ├── 01-datacenter-growth-global.md      (165)
│   ├── 02-datacenter-growth-canada.md      (178)
│   └── 03-environmental-impact.md          (220)
├── 02-datasets/
│   ├── 01-grid-electricity.md              (287)
│   ├── 02-carbon-intensity.md              (219)
│   ├── 03-water-and-climate.md             (183)
│   ├── 04-datacenter-locations.md          (187)
│   └── 05-benchmarks.md                    (264)
├── 03-methodology/
│   ├── 01-grid-stress-model.md             (216)
│   ├── 02-carbon-intensity-model.md        (215)
│   ├── 03-pue-cooling-model.md             (225)
│   ├── 04-water-intensity-model.md         (169)
│   └── 05-composite-scoring.md             (250)
├── 04-feasibility/
│   ├── 01-mvp-scope-timeline.md            (199)
│   └── 02-risks-mitigations.md             (197)
├── 05-literature/
│   ├── 01-key-papers.md                    (214)
│   └── 02-frameworks-standards.md          (225)
└── 06-proposal-alignment.md                (225)
```

### 2. Proposal (`proposal/`)

```
proposal/
├── draft-v1.md          — Markdown draft for editing (802 words)
├── generate-docx.py     — Python script to generate formatted DOCX
├── proposal-v1.docx     — Formatted DOCX matching RBC Borealis sample style
└── proposal-v1.pdf      — PDF exported via Microsoft Word
```

**Proposal formatting** matches the official sample PDF (`docs/LSI_Project_Proposal_Example.pdf`):
- "RBC BOREALIS" header in navy blue with letter-spacing
- Large Calibri Light title (28pt, left-aligned)
- Section headings in 16pt Calibri Light, dark gray
- Body text 11pt Calibri, 1.3 line spacing
- Footer with "RBC Borealis" + page numbers
- ~794 words (limit: 500–1,000)

**To regenerate DOCX after edits:** `.venv/bin/python proposal/generate-docx.py`
**To re-export PDF:** Open DOCX in Word, or use the AppleScript method from the session.

### 3. Environment

- Python venv at `.venv/` with `python-docx` installed
- Activate: `source .venv/bin/activate`

---

## Selected Project Idea

**Societal Impact Score (SIS)** for AI data center siting across Canadian provinces. Four ML sub-models:

1. **Grid Stress** — XGBoost binary classifier (IESO/AESO hourly data)
2. **Carbon Intensity** — Prophet + XGBoost forecasting (200x provincial variation: QC ~2 vs SK ~670 gCO₂/kWh)
3. **PUE/Cooling** — Random Forest regression on climate variables (semi-synthetic from TMY weather data)
4. **Water Intensity** — Physics-based lookup table (WRI Aqueduct stress indices)

Combined via Weighted Linear Combination + Monte Carlo uncertainty quantification (N=1000).

## Key Context

- **Program:** RBC Borealis Let's SOLVE It Spring 2026
- **Team:** ~4 undergrads, 2-month timeline, 10 hrs/week each
- **Selection decision:** This is the final selected idea. Previous ranked ideas in `research/01-ideas-ranked.md` are superseded.
- **Tanay's original doc:** `tanay/rbc-borealis-data-centers-idea.md`
- **Policy hook:** Ontario Bill 40 (Dec 2025) — Minister of Energy approval required for DC grid connections
- **Target cities (MVP):** Toronto, Montreal, Calgary, Vancouver, Winnipeg, Halifax, Saskatoon, Moncton
- **Score:** 4.7/5 on the same rubric used for other ideas (see `06-proposal-alignment.md`)
- **Proposal is purely extracurricular** — no coursework requirement
- **Personal angle:** Team cares about environmental cost of AI tools they use daily + sustainability interest

## Proposal Datasets (with links)

1. **ECCC Provincial Emission Factors** — https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/output-based-pricing-system/federal-greenhouse-gas-offset-system/emission-factors-reference-values.html
2. **IESO Ontario Hourly Generation** — https://www.ieso.ca/power-data/data-directory
3. **WRI Aqueduct 4.0** — https://www.wri.org/applications/aqueduct/water-risk-atlas/

## Unplanned Artifact

`research/08-idea-data-center-siting-ml-research.md` — raw research dump from an agent. Content properly organized into `research-datacenter/`. Can be deleted.

## Next Steps

1. **Review and iterate on proposal text** — edit `proposal/draft-v1.md`, update `generate-docx.py`, regenerate
2. **Decide on team roles** for the 8-week timeline (see `04-feasibility/01-mvp-scope-timeline.md`)
3. **Validate key datasets** — download samples from IESO and Electricity Maps to confirm API access
4. **Prepare application materials** — resumes, proof of enrollment, technical skills summaries (see `docs/application-guide.md`)
5. **Optional: write secondary proposal** — mentor picks between primary and secondary if team is selected
