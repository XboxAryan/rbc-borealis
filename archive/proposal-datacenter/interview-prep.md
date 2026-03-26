# RBC Borealis Interview Prep — Team Handout

**Project:** Societal Impact Modeling for AI Data Center Siting in Canada
**Round:** 2nd Round — Informal Mentor Chat
**Team:** Aryan, Anandita, Shreeya, Aaina, Tanayjyot

---

## 1. Proposal Overview — Know Every Detail

### 30-Second Elevator Pitch

> Canada's data center capacity is about to double, but there's no public tool to evaluate where these facilities should go. The carbon difference between provinces is 286x, and research shows the real marginal emissions are 5x higher than what standard accounting reports. We're building the first open-source Societal Impact Score — a composite metric covering carbon, water, grid stress, and cooling efficiency — with uncertainty quantification so policymakers can make honest, evidence-based siting decisions.

### 2-Minute Walk-Through

**The problem:** AI data centers are expanding fast in Canada — 10.3 GW installed, 9 GW in the pipeline. Where you build one matters enormously: a 100 MW facility in Alberta emits ~430,000 tonnes CO2/year vs ~1,500 in Quebec (286x difference). But even that understates it — Dandres et al. (2016) found that the *marginal* electricity serving new loads is 5-6x dirtier than the grid average because Canada reduces hydro exports and the US fires up coal and gas plants. Ontario's Bill 40 now requires ministerial approval for data center grid connections, but there's no public tool to inform those decisions. Siting choices lock in 20-30 years of consequences.

**Our solution:** An open-source Societal Impact Score (SIS) built from four ML sub-models — grid stress prediction, carbon intensity forecasting, cooling efficiency regression, and water intensity estimation — combined into a single composite metric with Monte Carlo uncertainty quantification. Input a proposed city, facility size, and cooling type; get back a score with a confidence interval.

**Why ML:** The environmental impact depends on nonlinear interactions between grid conditions, climate, water availability, and facility design. ML captures these relationships better than lookup tables, and lets us produce uncertainty-aware predictions instead of misleading point estimates.

**Data:** Three primary open datasets — ECCC provincial emission factors, IESO hourly generation data, and WRI Aqueduct water stress atlas — plus supplementary sources from Electricity Maps, AESO, and Hydro-Quebec.

### Section-by-Section: What We Wrote and Why

| Proposal Section | Core Message | Why We Framed It This Way |
|---|---|---|
| **What is the problem?** | Canada's DC capacity is doubling; carbon impact varies 286x by province; marginal emissions are 5x higher than reported; no public tool exists; Bill 40 signals policy demand | Opens with scale (10.3 GW), then the "hidden complexity" hook (marginal > average), then urgency (Bill 40) |
| **Why does this matter to our team?** | We use AI daily and asked "what does this cost?"; Quebec looks clean but marginal electricity is 6x dirtier; we bring CS/econ/finance backgrounds suited to a decision-making problem | Personal connection (we're AI users) + intellectual honesty (we found something surprising) + team fit (multidisciplinary) |
| **Why can ML help?** | Four sub-models addressing distinct prediction tasks; composite score with Monte Carlo | Shows ML is a natural fit, not forced; each sub-model solves a real prediction problem |
| **What data?** | Three primary datasets with links; Dandres as methodological reference | Concrete, verifiable, all free/open |
| **Coursework?** | Purely extracurricular | Required disclosure; clean answer |
| **Willingness to pivot** | Fully open to mentor guidance | Shows flexibility and program alignment |

### Every Claim → Its Source

| Claim in Proposal | Source |
|---|---|
| 10.3 GW installed capacity | CER Market Snapshot, October 2024 |
| 9 GW in development pipeline | Industry press aggregates (CBRE, JLL, Cushman & Wakefield 2024-2025) |
| 100 MW in Alberta → ~430,000 tonnes CO2/year | Calculation: 100 MW × 8,760 hrs × 490 gCO2/kWh (ECCC) × PUE 1.0 = ~429,240 t |
| Same in Quebec → ~1,500 tonnes | Calculation: 100 MW × 8,760 hrs × 1.7 gCO2/kWh (ECCC) × PUE 1.0 = ~1,489 t |
| 286-fold difference | 430,000 / 1,500 ≈ 286 |
| Marginal GHG intensity 0.85-1.01 kg CO2-eq/kWh | Dandres et al. (2016), Table 1 + in-text p.1316 |
| ~5x higher than Canadian average | 0.85-1.01 vs 0.16 kg CO2-eq/kWh Canadian avg (Dandres Table 1) |
| 60-70% from reduced US exports | Dandres et al. (2016), Results section |
| 47-53% natural gas, 38-48% coal in marginal mix | Dandres et al. (2016), Table 2 |
| Bill 40, December 2025 | Ontario Legislature, Royal Assent Dec 11, 2025 |
| 20-30 year lock-in | Standard infrastructure lifespan for data centers |
| "No publicly available tool exists" | Literature review of 15 papers; no operational open-source DC siting tool found |

---

## 2. Technical Approach & Modeling

### Sub-Model 1: Grid Stress Prediction

**What it predicts:** Whether adding a data center's load would push a provincial grid toward reliability limits (binary: high-stress hour or not).

**ML technique:** XGBoost binary classifier.

**Why XGBoost:** Handles tabular data with mixed feature types (temporal, numerical, categorical). Literature benchmarks show XGBoost achieves F1 0.85-0.92 for grid stress classification and MAPE 2.61% for load forecasting. It's interpretable via SHAP, fast to train, and doesn't require GPU resources.

> **If asked "Why not a neural net?"** — Neural nets (LSTM, Transformer) shine with sequential/image data. For tabular grid data with engineered features, tree-based models consistently match or beat deep learning at a fraction of the complexity. A hybrid LSTM-XGBoost approach could be a stretch goal, but XGBoost alone gives us a strong baseline.

**Key features:** Hour of day (cyclically encoded), demand current/lag/rolling averages, reserve margin, fuel-type generation shares, temperature, price volatility.

**Training data:** IESO (Ontario) hourly generation data, 2010-present, free CSV downloads via `gridstatus` Python library. AESO (Alberta) as second province.

**Performance benchmark:** XGBoost load forecasting: MAPE 2.61%, R² 0.987 (Scientific Reports 2022). Binary stress classification F1: 0.85-0.92 (literature aggregate).

**Fallback:** If model training doesn't converge in time, use annual capacity-to-demand ratios from Statistics Canada as a deterministic stress indicator — simpler but still useful.

### Sub-Model 2: Carbon Intensity Forecasting

**What it predicts:** Carbon intensity (gCO2/kWh) of electricity at a proposed site, using *marginal* intensity as the primary metric.

**ML technique:** Facebook Prophet (baseline) → XGBoost with exogenous features (primary).

**Why Prophet first:** Built-in seasonality handling, automatic uncertainty intervals, 10-line proof-of-concept. Gets us a working model in hours, not weeks.

**Why marginal, not average:** Average intensity is what standard accounting uses, but it's fundamentally wrong for evaluating *new* loads. When you add a data center, the grid dispatches the next available generator — usually natural gas or coal. Dandres et al. showed this marginal electricity is 0.85-1.01 kg CO2-eq/kWh vs the 0.16 average. Using average would massively understate the real carbon cost.

> **If asked "How do you get marginal intensity data?"** — Electricity Maps provides both average and marginal intensity for Canadian zones (CA-ON, CA-AB, etc.) from 2021-present. For provinces without direct marginal data, we apply a multiplier from Dandres: Uniform(2x-5x) for mixed-source grids, Uniform(1x-1.5x) for fossil-dominant grids.

**Training data:** Electricity Maps historical (2021-2024) for 11 Canadian zones, supplemented by IESO/AESO hourly generation data. Calibrated against ECCC annual emission factors.

**Performance benchmark:** CarbonCast (Maji et al. 2022): MAPE 4.80-13.93% for 96-hour forecasts. Ensemble methods: R² 0.96.

**Fallback:** Use published ECCC provincial emission factors (static annual averages) with the Dandres marginal multiplier applied. No ML required — still provides meaningful comparative analysis.

### Sub-Model 3: Cooling Efficiency (PUE) Regression

**What it predicts:** Power Usage Effectiveness (PUE) — total facility energy divided by IT equipment energy. PUE 1.0 is theoretical minimum; industry average is ~1.56.

**ML technique:** Random Forest regression.

**Why Random Forest:** The relationship between outdoor temperature and cooling energy is approximately piecewise-linear with a threshold at ~18-22°C (free-cooling cutoff). 5-8 well-understood physical variables. Full interpretability. Random Forest captures this structure with high accuracy — deep learning is overkill for this feature space.

> **If asked about Google DeepMind's 40% cooling reduction:** — DeepMind uses thousands of proprietary real-time sensor features to optimize *operational control* (real-time setpoints). Our use case is *pre-construction siting prediction* from public climate data. Completely different problem. Their approach requires access to facility telemetry we won't have.

**Key features:** Dry-bulb temperature (highest importance), wet-bulb temperature, relative humidity, cooling system type, IT load factor.

**Training data:** Semi-synthetic approach. Use TMY (Typical Meteorological Year) weather data for target Canadian cities. Apply ASHRAE psychrometric bin analysis to estimate free-cooling hours and annual PUE. Validate against Uptime Institute survey benchmarks.

**Canadian cities and estimated PUE:**

| City | Free-Cooling Hours/Year | Estimated PUE |
|---|---|---|
| Vancouver | ~6,500 (74%) | 1.10-1.18 |
| Winnipeg | ~6,200 (71%) | 1.12-1.18 |
| Calgary | ~6,000 (68%) | 1.12-1.20 |
| Montreal | ~5,800 (66%) | 1.14-1.22 |
| Halifax | ~5,600 (64%) | 1.14-1.22 |
| Toronto | ~5,400 (62%) | 1.16-1.25 |

**Fallback:** Linear regression with explicit breakpoints at economizer threshold. Even simpler, equally valid for this feature space.

### Sub-Model 4: Water Intensity Estimation

**What it predicts:** Water consumption from cooling systems, weighted by local water stress.

**ML technique:** Physics-based lookup + WRI Aqueduct stress multiplier (not ML — deterministic calculation).

**Why not ML here:** Water consumption is dominated by cooling technology choice (air-cooled = 0 L/kWh, evaporative = 0.5-9.0 L/kWh). This is a design parameter, not a prediction target. The physics is well-understood. ML would be overkill.

**Key formula:**
```
Water harm = WUE (L/kWh) × Total energy × Water stress index (0-5)
```

**Data:** WRI Aqueduct 4.0 Water Risk Atlas — sub-basin level water stress indices for all of Canada, CC BY 4.0 licensed. Free download as GeoJSON or Shapefile.

**Key insight:** Alberta has high carbon (~490 gCO2/kWh) AND moderate-high water stress = double penalty. Quebec has near-zero carbon AND very low water stress = both dimensions favor siting.

**Fallback:** Already the simplest approach — no fallback needed.

### Composite Score: Societal Impact Score (SIS)

**Formula:**
```
SIS = w_carbon × S_carbon + w_water × S_water + w_grid × S_grid + w_uncertainty × S_uncertainty
```

- Each S component normalized to [0, 1] via min-max scaling across candidate cities
- Default weights: equal (0.25 each) with interactive sliders
- **Lower SIS = more responsible siting choice**
- S_uncertainty penalizes data-scarce regions to prevent false confidence

**Three scenarios we'd present:**

| Scenario | Carbon | Water | Grid | Uncertainty | Use Case |
|---|---|---|---|---|---|
| Climate-first | 0.40 | 0.30 | 0.20 | 0.10 | Net-Zero 2050 alignment |
| Grid-reliability | 0.20 | 0.20 | 0.40 | 0.20 | Bill 40 context |
| Equal baseline | 0.25 | 0.25 | 0.25 | 0.25 | Neutral starting point |

If Quebec ranks first under all three, the recommendation is robust. If rankings shift, the analysis reveals the trade-offs at stake.

### Monte Carlo Uncertainty Quantification

**In plain language:** Instead of saying "Toronto scores 0.35 and Montreal scores 0.28," we run 10,000 simulations where each sub-model's prediction varies within its uncertainty range. We report "Toronto 0.35 [0.22-0.51] and Montreal 0.28 [0.19-0.40]" — those ranges overlap, so we can't confidently say one is better. But "Quebec 0.12 [0.08-0.18] vs Alberta 0.71 [0.62-0.80]" — no overlap, robust conclusion.

> **If asked "Why not just point estimates?"** — Two cities scoring 0.42 and 0.45 look different, but if their 90% confidence intervals overlap, there's no meaningful distinction. Monte Carlo gives honest answers. It's also an academic differentiator — genuine uncertainty quantification is rare in the DC sustainability literature.

### Anticipated Technical Deep-Dives

**Q: "What's the simplest version that still works?"**
A: Published ECCC emission factors for carbon + TMY weather data for PUE + WRI Aqueduct for water stress, combined with equal weights. No ML training required. Just a lookup table with a weighted sum. We'd get a meaningful comparative ranking across cities in a weekend. ML makes it better (temporal dynamics, uncertainty intervals, marginal vs average), but the core insight holds even with the simple version.

**Q: "How do you validate a composite score with no ground truth?"**
A: We validate each sub-model independently against published benchmarks. For the composite: (1) sanity checks — Quebec should always score better than Alberta on carbon; (2) sensitivity analysis — if small weight changes wildly change rankings, the score isn't robust; (3) we present three weighting scenarios and check if conclusions are stable.

**Q: "What if Prophet doesn't forecast well?"**
A: That's why we have a fallback hierarchy. Prophet → XGBoost with exogenous features → published ECCC annual factors with Dandres multiplier. Each step down loses temporal resolution but remains scientifically grounded.

---

## 3. Data — Sources, Access, Limitations

### Primary Datasets (In the Proposal)

| Dataset | What It Contains | Format | Coverage | Access | Limitations |
|---|---|---|---|---|---|
| **ECCC Provincial Emission Factors** | Official gCO2e/kWh for every province/territory | Web table | All of Canada, annual (2023-2026) | Free, no auth | Annual averages only; no hourly/seasonal; no marginal vs average distinction |
| **IESO Ontario Hourly Generation** | Hourly generation by fuel type, demand, price | CSV/XML | Ontario, 2010-present | Free, `gridstatus` library | Ontario only; other provinces need separate sources |
| **WRI Aqueduct 4.0** | Sub-basin water stress indices (13 indicators) | GeoJSON/Shapefile | Global including Canada | Free, CC BY 4.0 | Static indices (no real-time seasonal updates); spatial resolution at sub-basin level |

### Supplementary Sources

| Source | What It Adds | Access |
|---|---|---|
| **Electricity Maps** | Hourly average + marginal carbon intensity for 11 Canadian zones (2021-2024) | Free tier: 5 CSV downloads + live endpoint (rate-limited) |
| **AESO (Alberta)** | Hourly generation, pool price, Alberta Internal Load (2001-present) | Free standard datasets; `gridstatus` library |
| **Hydro-Quebec** | Hourly generation by source (May 2021-present) | Free REST API, no authentication |
| **CCEI (NRCan)** | Unified multi-provincial demand, generation, pricing | Free JSON API |
| **ECCC Weather** | Climate normals 1991-2020 + historical hourly for 8,756 stations | Free |
| **Statistics Canada 25-10-0015-01** | Monthly electric power generation by type, all provinces | Free CSV |

### Anticipated Data Questions

**Q: "Have you actually downloaded and looked at this data?"**
A: We've verified the IESO CSV structure through `gridstatus` documentation and the Electricity Maps free tier download format. ECCC emission factors are published on a government web page we've read. WRI Aqueduct has a public data explorer we've used to check Canadian coverage. We haven't done a full exploratory data analysis yet — that's Week 1 of the project.

**Q: "What if the data quality is poor or has gaps?"**
A: IESO and AESO are operational grid data — they're the most reliable datasets in the country because grid operators depend on them. The main risk is coverage gaps for smaller provinces (Saskatchewan, territories). Our fallback: use CCEI as a unified backbone and validate against primary ISO sources for the three main markets (Toronto, Montreal, Calgary).

**Q: "Is the Electricity Maps free tier sufficient?"**
A: For MVP, yes — 5 CSV downloads covers our target cities. If we need more, they offer academic/research access. The open-source parsers on GitHub also allow local replication of their methodology.

**Q: "How do you handle provinces with limited data?"**
A: That's what the S_uncertainty component in the SIS is for. Provinces with sparse data get higher uncertainty penalties so the tool doesn't falsely favor them just because we haven't seen enough data to identify risks. For carbon intensity, we fall back to ECCC annual factors with the Dandres marginal multiplier.

---

## 4. Problem Statistics — Quick Reference

### The Numbers You Must Know

| Statistic | Value | Source | Context |
|---|---|---|---|
| **Canada DC installed capacity** | 10.3 GW | CER Market Snapshot 2024 | Scale of existing infrastructure |
| **Development pipeline** | ~9 GW | Industry press 2024-2025 | Nearly doubling |
| **Carbon: Alberta vs Quebec** | 286x difference | ECCC factors: 490 vs 1.7 gCO2/kWh | Why siting matters |
| **Alberta 100 MW emissions** | ~430,000 t CO2/year | Calculated from ECCC factor | Scale of a single facility |
| **Quebec 100 MW emissions** | ~1,500 t CO2/year | Calculated from ECCC factor | The contrast |
| **Marginal intensity (Canada)** | 0.85-1.01 kg CO2-eq/kWh | Dandres et al. (2016), Table 1 + p.1316 | Real cost of new loads |
| **Canadian average intensity** | 0.16 kg CO2-eq/kWh | Dandres et al. (2016) | What standard accounting reports |
| **Marginal / average ratio** | ~5-6x | Dandres et al. (2016) | The hidden gap |
| **US export displacement** | 60-70% of marginal electricity | Dandres et al. (2016) | Cross-border effect |
| **Marginal fuel mix** | 47-53% gas, 38-48% coal | Dandres et al. (2016), Table 2 | What's actually generating |
| **Bill 40 (Ontario)** | Royal Assent Dec 11, 2025 | Ontario Legislature | Policy urgency signal |
| **Siting lock-in** | 20-30 years | Standard DC infrastructure lifespan | Why getting it right matters now |
| **Global DC electricity (2024)** | ~415 TWh (1.5% of global) | IEA Electricity 2025 | Global context |
| **Projected 2030** | ~945 TWh (3.4% of global) | IEA Electricity 2025 | Trajectory |
| **Microsoft Vaughan water** | 730 million L/year | CBC / municipal planning | Comparable to 12-15K residents |
| **Toronto DC count** | 72 facilities, 42 operators | DataCenterMap.com | Largest Canadian market |
| **Calgary pipeline share** | >25% of Canadian pipeline | Industry press | Fastest-growing market |
| **Global avg PUE** | 1.56 | Uptime Institute 2024 | Industry efficiency baseline |
| **Canada free-cooling hours** | 5,500+/year (~60% of hours) | TMY weather analysis | Canadian climate advantage |

### Anticipated Statistics Questions

**Q: "Where did you get the 286x number?"**
A: Direct calculation from ECCC provincial emission factors. Alberta is 490 gCO2/kWh, Quebec is 1.7. For a 100 MW facility running 8,760 hours/year at PUE 1.0: Alberta = 100,000 kW × 8,760 h × 0.490 kg = ~429,240 tonnes. Quebec = 100,000 × 8,760 × 0.0017 = ~1,489 tonnes. Ratio: 429,240 / 1,489 ≈ 288, rounded to 286 in the proposal (varies slightly with PUE assumptions).

**Q: "The Dandres paper is from 2016 — is it still relevant?"**
A: The specific numbers may have shifted (Alberta has phased out coal since then, Ontario's Pickering nuclear plant is retiring), but the core methodological insight is timeless: marginal electricity is fundamentally different from average, and cross-border export effects are real. We cite Dandres for the methodology, not as current data. Our tool uses 2021-2024 data from Electricity Maps for current values. The fact that Canadian grids are changing is a feature, not a bug — it means our tool can show how SIS scores evolve as grids decarbonize.

**Q: "What's actually changed since Bill 40 passed?"**
A: Bill 40 gave Ontario's Minister of Energy the authority to prioritize data center grid connections based on economic benefits, strategic considerations, community impact, and grid reliability. It's the first Canadian law that explicitly treats data centers as infrastructure-scale consumers needing special regulatory treatment. It does not apply to projects with connection requests before June 3, 2025. The law creates demand for exactly the kind of analytical framework we're building.

---

## 5. Why Mentorship Matters

### Frame: Three Specific Acceleration Points

**1. Model selection and validation strategy**
We've identified the ML techniques for each sub-model from literature, but we've never built production-grade ML pipelines end-to-end. A mentor with ML engineering experience can help us avoid common pitfalls: data leakage from shuffled cross-validation on time-series data, class imbalance handling for grid stress (high-stress hours are ~5-15% of data), and hyperparameter tuning priorities. This could save us 2-3 weeks of trial and error.

**2. Data pipeline architecture**
We're integrating 5+ heterogeneous data sources — REST APIs, CSV downloads, geospatial shapefiles, static lookup tables — across different temporal resolutions (5-minute to annual) and spatial scales (sub-basin to provincial). A mentor who's built data pipelines can help us design a clean architecture from the start instead of accumulating technical debt we'd have to refactor in week 5.

**3. Scoping and prioritization**
We have 4 sub-models, a composite scoring system, Monte Carlo simulation, and visualization — that's ambitious for 320 person-hours. The hardest decision isn't what to build, it's what to defer. A mentor can help us identify which sub-model to focus on first, when to use a fallback instead of training a model, and when our results are "good enough" to move to the next component.

### What We Bring vs What We Need

| What We Already Have | What Mentorship Adds |
|---|---|
| Strong problem framing and literature review | Guidance on translating research into working code |
| Identified datasets with access paths | Experience with data quality issues and preprocessing |
| Clear ML technique choices with fallbacks | Knowledge of when to pivot from primary to fallback |
| Monte Carlo methodology designed on paper | Practical implementation experience (when to simplify) |
| Multidisciplinary team (CS, econ, finance) | ML engineering patterns and best practices |

### Anticipated Mentorship Questions

**Q: "What specific ML concepts are you least confident about?"**
A: Time-series cross-validation (avoiding data leakage), handling class imbalance for rare events (grid stress), and calibrating uncertainty intervals so they're actually well-calibrated (90% CI should contain 90% of actuals). We understand the theory from coursework but haven't applied it to real, messy data.

**Q: "Have any of you built an ML model before?"**
A: Aryan has built ML models in his finance coursework (RSM338) and applied them professionally — a RAG platform with hybrid search and embedding pipelines at BMO, plus a constraint-aware portfolio optimizer with walk-forward backtesting. The rest of the team has coursework exposure but not full project experience. That's exactly why the program is valuable — we want to learn by doing with mentorship support.

**Q: "What would you do if your mentor suggested a completely different approach?"**
A: We'd be open to it. The proposal says we're "fully open to pivoting," and we mean it. The problem is what matters to us, not the specific architecture. If a mentor sees a better path — maybe a simpler approach we hadn't considered, or a different ML technique that fits the data better — we'd rather build the right thing than stubbornly follow our original plan.

---

## 6. Best Outcome

### Three Tiers of Success

**Minimum Viable (8-week floor):**
A working composite Societal Impact Score for 5-8 Canadian cities using published ECCC emission factors, TMY weather data for PUE estimation, and WRI Aqueduct water stress indices. Visualized on an interactive Folium map where each city marker shows its SIS score and sub-component breakdown. Demonstrates quantitatively that siting location matters and that trade-offs exist between carbon, water, grid stress, and efficiency.

**Target Outcome (what we're aiming for):**
All 4 sub-models trained and producing predictions with uncertainty intervals. Carbon intensity model uses marginal intensity as primary metric. Monte Carlo simulation propagates uncertainty through the composite score. Folium map with pop-ups showing SIS with 90% confidence intervals per city. Three weighting scenarios (climate-first, grid-reliability-first, equal) demonstrating sensitivity. Clear written report with methodology, results, and policy implications.

**Stretch Goal:**
A Streamlit dashboard where a user can input a proposed city, facility size (MW), and cooling type, and get back an SIS score with confidence interval in real time. Interactive weight sliders to explore trade-offs. This would be a genuinely usable tool, not just a research output.

### Anticipated Outcome Questions

**Q: "What does the final deliverable actually look like?"**
A: A GitHub repository (MIT licensed) containing:
1. Jupyter notebooks with exploratory data analysis and model training
2. A self-contained interactive Folium map (HTML file) showing SIS scores across Canada
3. A 15-minute presentation with live demo
4. A one-page written summary
5. (Stretch) A Streamlit web app

**Q: "Who would use this tool?"**
A: Three audiences: (1) Provincial policymakers evaluating data center applications under frameworks like Bill 40; (2) sustainability teams at companies deciding where to build; (3) researchers studying the environmental impact of digital infrastructure. The tool is open-source specifically so anyone can audit and extend it.

**Q: "What happens to this project after the program ends?"**
A: The code repository stays public. We'd write a blog post documenting the methodology and results. If the tool proves useful, we'd continue maintaining it — updating emission factors annually, adding provinces as data becomes available. The modular architecture (4 independent sub-models + configurable weights) means any component can be improved independently.

---

## 7. Individual Talking Points

### How to Introduce Yourself
Each person: name, program, year, one relevant thing, one sentence on your role, one sentence on why you care. Keep it to 30 seconds.

### Aryan Bhatia
- **Intro:** "I'm Aryan, third-year Bachelor of Commerce at Rotman, specializing in management. I've taken Machine Learning in Finance and I'm currently building a RAG platform at BMO Global Asset Management."
- **Role:** Technical lead — ML model development, data pipeline architecture, codebase management.
- **Why I care:** "I work with AI infrastructure every day in my internship. I've seen firsthand how much compute these systems consume, and I realized I've never questioned where that compute comes from or what it costs the grid and climate."

### Anandita
- **Intro:** [Name, program, year, one relevant skill or experience]
- **Role:** [To be filled based on team discussion — e.g., data collection and preprocessing, research, visualization]
- **Why I care:** [Personal connection to the problem — sustainability interest, policy interest, etc.]

### Shreeya
- **Intro:** [Name, program, year, one relevant skill or experience]
- **Role:** [To be filled — e.g., carbon intensity sub-model, literature review, report writing]
- **Why I care:** [Personal connection]

### Aaina
- **Intro:** [Name, program, year, one relevant skill or experience]
- **Role:** [To be filled — e.g., water/cooling sub-models, data visualization, presentation design]
- **Why I care:** [Personal connection]

### Tanayjyot
- **Intro:** [Name, program, year, one relevant skill or experience]
- **Role:** [To be filled — e.g., grid stress sub-model, Monte Carlo simulation, data engineering]
- **Why I care:** [Personal connection]

> **Note for the team:** Fill in your sections before the interview. Each person should practice their intro out loud. The mentor will likely ask each of you to introduce yourself individually. Keep it conversational — this is an informal chat, not a job interview.

---

## 8. Quick-Fire Q&A — Other Likely Questions

**Q: "Can you commit 10 hours/week for 8 weeks?"**
A: Yes, all five of us have confirmed availability. We can all attend Welcome Day (March 6) and Presentation Day (May 11).

**Q: "Have you checked if a similar project was done in a previous cohort?"**
A: Yes. A shelter bed demand forecasting project in Toronto was done in a previous cohort, which is a different domain. No data center / energy infrastructure project has been done before in the program. Our project is novel for the cohort.

**Q: "Is this too ambitious for 8 weeks?"**
A: We've explicitly designed fallbacks for each sub-model. The minimum viable version (lookup tables + weighted sum + map) is achievable in 2-3 weeks. ML models add value on top of that. We'd rather aim high with clear fallbacks than propose something too easy.

**Q: "Why not just use an existing tool?"**
A: There isn't one. Commercial tools like Schneider Electric's EcoStruxure focus on operational optimization within existing facilities, not siting decisions. Academic tools like CarbonCast focus on carbon forecasting only, not multi-dimensional impact. No open-source tool combines carbon, water, grid stress, and cooling efficiency into a single composite metric with uncertainty quantification for Canadian locations.

**Q: "How does this help a real community?"**
A: Data center siting decisions affect communities through grid reliability (blackout risk), water availability (competing with residential/agricultural use), carbon emissions (climate impact), and local economic development. Our tool makes these trade-offs visible and quantifiable. A community facing a proposed 100 MW facility can use the SIS to understand what that means for their grid, water, and emissions — and compare it to alternative sites.
