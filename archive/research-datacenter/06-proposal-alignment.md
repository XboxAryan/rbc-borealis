# Alignment with RBC Borealis Selection Criteria

---

## Overview

This document maps the Societal Impact Score project against the inferred evaluation rubric for RBC Borealis Let's SOLVE It proposals. The rubric is derived from analysis of all 23 accepted projects across three cohorts (Spring 2023, Fall 2023, Spring 2024). Each criterion is scored on a 1-5 scale with detailed justification.

---

## Scoring Summary

| Factor | Weight (Inferred) | Score | Justification |
|---|---|---|---|
| Canadian/Community Focus | High | 5 | Provincial grid diversity is uniquely Canadian. 200x variation in carbon intensity. Ontario Bill 40. Three major DC hubs (Toronto, Montreal, Calgary) account for 93% of IT load. |
| Clear ML Application | High | 5 | Four natural ML tasks: XGBoost classification (grid stress), Prophet forecasting (carbon intensity), regression (PUE), Monte Carlo simulation (uncertainty). Not forced. |
| Data Availability | High | 5 | 30+ free, public datasets identified with programmatic APIs (IESO, AESO, Hydro-Quebec, CCEI, ECCC, WRI Aqueduct, Electricity Maps, Statistics Canada). |
| Quantifiable Impact | Medium | 5 | A 100 MW DC in Alberta emits approximately 430,000 tCO2/yr vs approximately 1,500 t in Quebec -- a 286x difference. Tool quantifies this tradeoff for every province. |
| Feasibility in 2 Months | Medium | 4 | Scoped to 5-8 cities, monthly averages, semi-synthetic PUE, equal weights. Standard Python libraries only. One point deducted for data integration complexity across 4 sub-models. |
| Novelty | Medium | 5 | No open-source Canadian DC siting tool exists. No past RBC Borealis cohort has addressed data center environmental impact. No prior environmental project covered infrastructure siting. |
| Equity/Diversity Angle | Medium | 4 | Grid reliability for rural and Indigenous communities, water stress in drought-prone regions, distributional impact analysis. Less directly equity-centered than Indigenous water or food desert projects. |
| **Weighted Score** | | **4.7 / 5** | |

---

## Detailed Criterion Analysis

### Canadian/Community Focus: 5/5

This project is fundamentally Canadian in a way that cannot be replicated for another country with equal analytical value.

**Why Canada is uniquely suited:**

- **200x carbon intensity variation:** Quebec (~2 gCO2/kWh) to Saskatchewan (~670 gCO2/kWh) within a single national data ecosystem. No other country offers this range with comparable data quality.
- **Provincial control over generation mix:** Canada's federated electricity system creates distinct regulatory and emissions profiles that are independently modeled.
- **Active policy moment:** Ontario Bill 40 (Royal Assent December 11, 2025) is the first Canadian law requiring ministerial approval for data center grid connections. Our tool directly supports the kind of analysis Bill 40 was designed to enable.
- **Concentrated geography:** 93% of IT load in three metropolitan hubs makes the siting problem tractable.
- **High-quality open data:** Statistics Canada, CER, ECCC, and provincial ISOs all publish granular, machine-readable data under open licenses.

**Comparison to other jurisdictions:**

| Country | Carbon Variation | Data Quality | Policy Window | Suitability |
|---|---|---|---|---|
| Canada | 200x (provincial) | High (open ISOs) | Active (Bill 40) | Ideal |
| United States | ~50x (state-level) | Fragmented (30+ ISOs) | Limited | Good but harder |
| EU | ~20x (national) | Inconsistent | EU-wide targets | Moderate |
| Nordics | ~3x | High | Mature | Too little variation |

---

### Clear ML Application: 5/5

The project involves four distinct, well-defined ML tasks that are natural fits for the problem. None are forced or artificial.

| Sub-Model | ML Task | Algorithm | What It Predicts | Evaluation Metric |
|---|---|---|---|---|
| Grid Stress | Binary classification | XGBoost | High-stress grid state probability | F1, AUC-ROC |
| Carbon Intensity | Time-series forecasting | Prophet | Provincial gCO2/kWh | MAPE, R-squared |
| PUE / Cooling | Regression | XGBoost / Linear | Annualized PUE from climate variables | RMSE, R-squared |
| Water Intensity | Estimation + indexing | Regression + lookup | L/kWh + watershed risk score | Calibration against benchmarks |
| Composite SIS | Uncertainty quantification | Monte Carlo | Composite score with confidence intervals | Sensitivity analysis |

Each sub-model has published academic benchmarks (see `05-literature/01-key-papers.md`) demonstrating that the chosen algorithms achieve strong performance on comparable tasks.

---

### Data Availability: 5/5

This project has the strongest data availability profile of any candidate idea analyzed. Over 30 free, public datasets have been identified, most with programmatic API access.

| Category | Sources | Access Method | Cost |
|---|---|---|---|
| Grid electricity | IESO, AESO, Hydro-Quebec, CCEI, BC Hydro, SaskPower | API, CSV, JSON | Free |
| Carbon intensity | ECCC emission factors, Electricity Maps, CER | API, CSV | Free |
| Weather/climate | ECCC historical stations, TMY data | CSV, API | Free |
| Water stress | WRI Aqueduct, ECCC hydrological data | GeoJSON, CSV | Free |
| DC locations | DataCenters.com, DC Byte, Baxtel | Web, CSV | Free tier |
| Grid projections | CER Energy Futures, IESO APO | CSV, PDF | Free |

No dataset requires paid access, institutional credentials, or data use agreements. All are available under open government licenses or Creative Commons terms.

---

### Quantifiable Impact: 5/5

The impact is concrete, numerical, and dramatic.

**Core statistic:** A 100 MW data center in Alberta produces approximately 430,000 tonnes of CO2 per year under standard grid-average accounting. The same facility in Quebec produces approximately 1,500 tonnes. That is a **286x difference** determined entirely by siting decision.

**Deeper insight (Dandres et al. 2016):** Using marginal intensity -- the carbon cost of the generation that actually responds to new load -- even "clean" provinces carry marginal carbon costs of 0.85-1.01 kg CO2-eq/kWh, roughly 5x higher than the Canadian average. This makes the siting optimization problem more nuanced than average grid intensity alone suggests, and strengthens the case for a multi-dimensional scoring tool.

**Additional quantifiable impacts:**

| Metric | Value | Context |
|---|---|---|
| Canada DC pipeline | ~9 GW | Near-doubling of installed base in 3-5 years |
| Emission lock-in period | 20-30 years | Facility lifespan locks in siting decision consequences |
| Free-cooling hours (Canada) | 5,500+/year | 80% cooling energy savings vs. warm-climate siting |
| Water consumption (100 MW) | ~50-150 million L/year | Varies by cooling technology and climate |
| Grid stress (Ontario) | Pickering retirement creating capacity gap | Bill 40 motivated by concern over uncontrolled DC connections |

The tool produces specific numerical outputs (SIS scores with confidence intervals) for each candidate city, enabling direct comparison.

---

### Feasibility in 2 Months: 4/5

The project is scoped for 320 person-hours (4 students, 10 hrs/week, 8 weeks) with explicit simplifications.

**What makes it feasible:**

- Monthly/seasonal averages instead of hourly forecasting
- Semi-synthetic PUE model instead of real sensor data
- Equal weights instead of full AHP elicitation
- Standard Python libraries with extensive documentation
- No GPU or cloud compute required
- Well-defined fallbacks for every risk (see `04-feasibility/02-risks-mitigations.md`)

**What costs one point:**

- Four sub-models require four data integration pipelines
- Cross-provincial data formats are heterogeneous (some APIs, some Excel, some web-only)
- Monte Carlo uncertainty propagation adds implementation complexity
- End-to-end testing requires all sub-models to be functional

The week-by-week plan (see `04-feasibility/01-mvp-scope-timeline.md`) includes explicit buffer strategies for weeks that fall behind.

---

### Novelty: 5/5

**No existing tool covers this space:**

| Existing Tool/Study | What It Does | What It Lacks |
|---|---|---|
| **Dandres et al. 2016 (J. Industrial Ecology)** | **Consequential LCA of Canadian DC deployment; identified marginal generation and cross-border export displacement effects** | **No uncertainty quantification, limited to 5 scenarios, no spatial resolution below province, no water model, no operational tool** |
| Electricity Maps | Real-time carbon intensity visualization for global grids | No siting optimization, no water, no grid stress, no composite score |
| Xiao & You 2025 (Nature Sustainability) | US-focused roadmap for DC environmental impact | US-only, conceptual framework, no operational tool |
| Google DeepMind cooling | Operational cooling optimization for existing Google facilities | Not siting-related, proprietary, not reproducible |
| Commercial tools (Schneider, Vertiv) | Facility design and operational efficiency software | Not open-source, not policy-oriented, no societal scoring |
| CarbonCast | Open-source carbon intensity forecasting (6 US regions) | Single dimension only, not Canadian, no composite scoring |

**Four novel contributions:**

1. **Extends Dandres et al. (2016).** The closest prior work -- a consequential LCA of Canadian DC deployment published in *J. Industrial Ecology* -- identified marginal generation and cross-border effects but could not build a tool, run Monte Carlo, model water, or achieve sub-provincial resolution. Our SIS addresses every limitation they identified.
2. **Multi-dimensional composite scoring.** First tool combining carbon + water + grid stress + PUE into a single uncertainty-aware score.
3. **Canada-specific.** Provincial grid diversity creates a natural experiment with 200x variation. No other country offers this combination of extreme variation and high data quality.
4. **Open-source and policy-oriented.** Designed to inform public policy and community advocacy, not commercial facility planning. All code, data, and methodology publicly available.

**No past RBC Borealis cohort overlap:**

- No prior cohort addressed data center siting or infrastructure environmental impact
- No prior cohort used grid electricity data as a primary input
- The closest domain (environment) was represented by wildfire and earthquake projects, which address different problems entirely

---

### Equity/Diversity Angle: 4/5

The equity dimension is genuine but less central than in projects that directly serve marginalized populations.

**How equity is addressed:**

| Dimension | Equity Concern | How the Tool Addresses It |
|---|---|---|
| Grid reliability | New DC load can jeopardize electricity service for rural communities | Grid stress model explicitly quantifies whether proposed load exceeds safe capacity thresholds |
| Water justice | Evaporative cooling competes with residential and agricultural water use | Water intensity model flags watershed stress and competing demands |
| Indigenous consultation | DC sites may be on traditional territories | Tool designed to support community advocacy and informed consent |
| Environmental justice | Pollution burdens should not fall disproportionately on vulnerable communities | Multi-dimensional scoring captures distributional impacts that single-metric tools miss |
| Economic transparency | Tax incentives may reduce net community benefit | Framework allows cost-benefit comparison across dimensions |

**Why not 5/5:** The project is infrastructure-oriented rather than directly community-serving. Projects like Indigenous water quality monitoring or food desert analysis serve marginalized communities as the primary stakeholder. Our tool serves policymakers and planners, with indirect benefits to communities through better-informed siting decisions.

---

## Policy Relevance

The project aligns with five active Canadian policy contexts.

| Policy Context | Connection to This Project |
|---|---|
| Canada Net-Zero 2050 | DC siting decisions made today lock in 20-30 years of emissions. High-carbon siting is directly counterproductive to national climate commitments. |
| Ontario Bill 40 | First Canadian legislation requiring ministerial approval for DC grid connections. Our tool supports the analytical framework Bill 40 envisions. |
| Provincial electricity planning | Shows how siting decisions interact with grid decarbonization trajectories (e.g., Alberta coal phase-out). |
| Water policy | BC and Alberta face increasing summer drought risk. Tool flags water stress at the watershed level. |
| Indigenous consultation | Grid stress modeling quantifies whether new load jeopardizes reliability for existing communities, including First Nations. |

---

## Strongest Pitch

The following paragraph is designed for the proposal abstract. It leads with the Canadian context, states the specific ML task, identifies the data, and frames the impact.

> Canada's federated electricity system -- where each province controls its own generation mix -- creates the world's most dramatic variation in data center environmental impact within a single country. A 100 MW data center in Alberta produces 286 times the carbon emissions of the same facility in Quebec, yet no public tool exists to evaluate these tradeoffs. We propose building the first open-source, uncertainty-aware Societal Impact Score for AI data center siting in Canada, combining four ML sub-models (grid stress, carbon intensity, PUE/cooling, water intensity) into a single composite metric. Using 30+ publicly available Canadian datasets, our tool will help policymakers, planners, and communities make evidence-based decisions about where data centers should -- and should not -- be built.

---

## Comparison to Other Candidate Ideas

Based on the scoring rubric applied consistently across all candidate ideas:

| Idea | Score | Strongest Dimension | Weakest Dimension |
|---|---|---|---|
| **DC Siting (this project)** | **4.7** | Data availability (30+ datasets) | Feasibility (4 sub-models) |
| Indigenous Water Quality | 4.8 | Equity (directly serving First Nations) | Data availability (sensor gaps) |
| Food Deserts in Low-Income Areas | 4.7 | Equity + ML fit | Novelty (related work exists) |
| Wildfire Health Impact | 4.5 | Timeliness (post-2023 fires) | Novelty (wildfire done in 2 cohorts) |

**Relative strengths of this project:**

- Strongest data availability of any candidate (30+ datasets with APIs, all free)
- Strongest ML fit (4 distinct sub-models, each with clear tasks and published benchmarks)
- Most timely (DC boom happening now; Bill 40 passed December 2025)
- No overlap with any past cohort project

**Relative weakness:**

- Slightly less direct equity impact than Indigenous water or food desert projects
- Higher integration complexity than single-model projects

---

## Key References

- **Dandres, T. et al. 2016,** "Consequences of Future Data Center Deployment in Canada on Electricity Generation and Environmental Impacts," *J. Industrial Ecology* 20(5), 1312-1322. -- Most directly relevant prior work; establishes marginal intensity and cross-border effects.
- RBC Borealis Let's SOLVE It: Past cohort analysis (Spring 2023, Fall 2023, Spring 2024)
- Ontario Bill 40: Protect Ontario by Securing Affordable Energy for Generations Act, 2025
- Xiao & You 2025, Nature Sustainability
- DC Byte, Canada Data Center Market, Q2 2025
- CER, "Market Snapshot: Data Centres in Canada," October 2024
