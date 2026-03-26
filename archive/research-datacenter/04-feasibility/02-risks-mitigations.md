# Risks and Mitigations

---

## Overview

This document catalogs the primary risks to project success, assesses their severity and likelihood, and defines specific mitigation strategies and fallback plans. Risks are organized from highest to lowest combined severity-likelihood impact.

---

## Risk Register

| # | Risk | Severity | Likelihood | Category |
|---|---|---|---|---|
| R1 | No DC-specific water consumption data in Canada | High | Certain | Data |
| R2 | No real data center sensor telemetry for PUE modeling | High | Certain | Data |
| R3 | Scope creep beyond 8-week timeline | Medium | High | Project Management |
| R4 | Model validation without ground truth SIS | Medium | High | Methodology |
| R5 | CCEI unified data has quality gaps | Medium | Medium | Data |
| R6 | Reviewers perceive project as "too-broad climate change" | Medium | Medium | Framing |
| R7 | Electricity Maps free tier rate limits | Low | Medium | Data Access |
| R8 | Alberta grid rapidly decarbonizing (coal phase-out) | Low | Certain | External |

---

## Detailed Mitigation Plans

### R1: No DC-Specific Water Data in Canada

**Severity:** High | **Likelihood:** Certain

Canadian data centers do not publicly report facility-level water consumption. No federal or provincial database tracks data center WUE. This is a known gap across the entire Canadian data center industry.

**Mitigation:**
- Use published industry WUE benchmarks from hyperscaler sustainability reports (Google: 1.1 L/kWh, Microsoft: 1.2 L/kWh, Equinix: 1.8 L/kWh)
- Apply LBNL water consumption estimation methodology: WUE as a function of cooling technology type and local wet-bulb temperature
- Cross-reference with WRI Aqueduct basin-level water stress indices for local watershed health
- Proxy estimation: combine TMY climate data with published WUE-by-climate-zone tables from AWS and Google sustainability reports
- Clearly document that water estimates are modeled, not measured, with stated uncertainty ranges

**Fallback:** If proxy estimation proves too uncertain, reduce water dimension to a binary classification (high-stress watershed vs. low-stress watershed) using WRI Aqueduct alone.

---

### R2: No Real DC Sensor Telemetry for PUE

**Severity:** High | **Likelihood:** Certain

No Canadian data center operator publishes real-time or historical PUE sensor data. Hyperscaler PUE figures are reported as annual averages without site-level granularity.

**Mitigation:**
- Build semi-synthetic PUE model from first principles: PUE is primarily a function of outdoor dry-bulb temperature, wet-bulb temperature, humidity, and cooling technology choice
- Use TMY (Typical Meteorological Year) weather data from ECCC for each target city
- Calibrate against published PUE ranges by climate zone (LBNL 2024, Uptime Institute Annual Survey)
- Validate by comparing model predictions against known hyperscaler PUE reports for facilities in comparable climates
- Sobol sensitivity analysis (Lei et al. 2024) confirms dry-bulb and wet-bulb temperature as highest-influence parameters, supporting a climate-driven model

**Fallback:** Replace regression model with a lookup table mapping ASHRAE climate zones to PUE ranges from published benchmarks. Less granular but still defensible.

---

### R3: Scope Creep Beyond 8-Week Timeline

**Severity:** Medium | **Likelihood:** High

Undergraduate teams commonly underestimate integration complexity and overcommit to features. The multi-dimensional nature of this project (four sub-models plus composite scoring) creates natural scope expansion pressure.

**Mitigation:**
- Define and freeze MVP scope in Week 1: 5-8 cities, monthly granularity, equal weights, semi-synthetic PUE
- Maintain a strict "stretch goals" boundary -- features beyond MVP are documented but not started until core pipeline is end-to-end functional
- Weekly check-ins with explicit go/no-go decisions for each sub-model
- If any sub-model falls behind by more than 3 days, invoke the simplified fallback (lookup table or published averages)
- Protect Week 8 for report writing and presentation preparation -- no new feature work in the final week

**Fallback:** Reduce city coverage to the three primary DC hubs (Toronto, Montreal, Calgary). This still demonstrates the tool's value across the three most important markets while cutting data integration work roughly in half.

---

### R4: Model Validation Without Ground Truth SIS

**Severity:** Medium | **Likelihood:** High

The Societal Impact Score is a novel composite metric. No ground truth exists to validate the composite output directly. This is an inherent limitation of any new scoring framework.

**Mitigation:**
- Validate each sub-model independently against established benchmarks:
  - Carbon intensity predictions against ECCC published provincial emission factors
  - Grid stress classifier against historical ISO emergency alerts and price spike events
  - PUE estimates against Uptime Institute survey data by climate zone
  - Water stress indices against WRI Aqueduct peer-reviewed assessments
- For the composite score, demonstrate validity through:
  - Sensitivity analysis across 100+ weight configurations
  - Sanity checks: Quebec should consistently score better than Alberta on carbon; Halifax should score worse than Montreal
  - Monte Carlo confidence intervals that appropriately widen for cities with less data
  - Comparison with qualitative expert assessments of known DC markets

**Fallback:** If sub-model validation reveals unacceptable error rates, present the tool as an exploratory framework with clearly stated uncertainty bounds rather than a prescriptive scoring system.

---

### R5: CCEI Unified Data Has Quality Gaps

**Severity:** Medium | **Likelihood:** Medium

The Canadian Centre for Energy Information (CCEI) aggregates provincial data via web scraping, which can introduce gaps, duplicates, and lag relative to primary ISO sources.

**Mitigation:**
- Use CCEI as a convenience layer for cross-provincial comparison and discovery
- Validate all CCEI data against primary ISO sources (IESO, AESO, Hydro-Quebec) for the three major markets
- For provinces without primary ISO APIs (Saskatchewan, Nova Scotia, New Brunswick), cross-check CCEI against Statistics Canada Table 25-10-0015-01 monthly figures
- Document all identified data quality issues and their impact on model outputs

**Fallback:** Fall back to Statistics Canada monthly tables plus Electricity Maps historical CSVs. Coarser temporal resolution but more reliable provenance.

---

### R6: Reviewers Perceive Project as "Too-Broad Climate Change"

**Severity:** Medium | **Likelihood:** Medium

Past RBC Borealis cohort analysis indicates that vaguely framed "climate change" proposals are flagged as unfocused. The multi-dimensional nature of this project could trigger this perception.

**Mitigation:**
- Lead every description with the specific ML task, not the policy question
- Frame as: "XGBoost classification for grid stress prediction + Prophet forecasting for carbon intensity + regression for PUE estimation" -- not "combating climate change"
- Emphasize specific datasets, specific evaluation metrics (F1, MAPE, R-squared), and specific deliverables
- Use the 286x carbon intensity variation as the hook -- concrete, quantifiable, surprising
- Position the composite score as a machine learning integration challenge, not an environmental advocacy statement

**Fallback:** If framing concerns persist, narrow the pitch to focus on the two strongest sub-models (grid stress + carbon intensity) and present PUE and water as extensions.

---

### R7: Electricity Maps Free Tier Rate Limits

**Severity:** Low | **Likelihood:** Medium

Electricity Maps provides 5 free historical CSV downloads and rate-limited API access. Heavy use during development could exhaust the free tier.

**Mitigation:**
- Download the 5 free historical CSVs early (Week 1) and cache locally
- Use Electricity Maps open-source parsers to scrape real-time data directly from ISO websites
- Use CCEI JSON API as the primary cross-provincial source, with Electricity Maps as validation only
- If API access is needed beyond free tier, the academic plan provides expanded access at no cost

**Fallback:** Rely entirely on CCEI and primary ISO sources. Electricity Maps data is useful for validation but not essential for core modeling.

---

### R8: Alberta Grid Rapidly Decarbonizing

**Severity:** Low | **Likelihood:** Certain

Alberta's coal-fired generation is being phased out under federal regulations. By 2030, the province's grid carbon intensity will be materially lower than current levels. This could make current siting scores "stale" for facilities with 20-30 year lifespans.

**Mitigation:**
- This is a feature, not a bug. The temporal dimension strengthens the project's analytical contribution.
- Include scenario modeling: "How does Alberta's siting score change under planned decarbonization trajectories?"
- Use CER Energy Futures projections for forward-looking grid composition estimates
- Show that siting decisions must account for grid evolution, not just current snapshot values

---

## Ethical Considerations

| Dimension | Consideration | Project Response |
|---|---|---|
| Indigenous consultation | Tool could be used to site DCs without meaningful community engagement | Frame tool as supporting community advocacy and informed consent, not replacing consultation |
| Grid reliability | New DC load could jeopardize service for existing communities | Grid stress model explicitly quantifies whether proposed load exceeds safe thresholds |
| Transparency | Scoring methodology must be auditable | All code open-source, all assumptions documented, all weights configurable |
| Data sovereignty | Must respect data governance norms | Use only publicly available government data under open licenses |
| Environmental justice | Pollution and resource burdens should not fall disproportionately on marginalized communities | Water stress and grid reliability dimensions capture distributional impacts |

---

## Failure Mode Summary

| If This Fails | Fallback To |
|---|---|
| CCEI API is unreliable | Statistics Canada monthly tables + Electricity Maps CSVs |
| PUE regression is too simplistic | Lookup table by ASHRAE climate zone |
| 8 cities is too ambitious | Focus on Toronto, Montreal, Calgary (the 3 DC hubs) |
| Folium map is insufficient for presentation | Plotly interactive charts or static matplotlib figures |
| Monte Carlo is too slow or complex | Point estimates with manual 3-scenario sensitivity analysis |
| Prophet carbon forecasting underperforms | Fall back to SARIMA or simple seasonal decomposition |
| XGBoost grid stress classifier underperforms | Threshold-based rules on reserve margin and price z-score |

---

## Key References

- WRI Aqueduct: https://www.wri.org/aqueduct
- LBNL 2024, "United States Data Center Energy Usage Report"
- Lei et al. 2024, "Data Center PUE with Economizer Types across Climate Zones," MDPI Buildings
- Uptime Institute, Annual Data Center Survey, 2024
- CCEI, High-Frequency Electricity Data: https://energy-information.canada.ca/
- CER, Canada's Energy Future Projections, 2024
