# ML Methodology & Technical Feasibility: Societal Impact Score for AI Data Center Siting in Canada

Research compiled for RBC Borealis Let's SOLVE It Spring 2026 proposal.

---

## 1. ML Approaches for Each Sub-Model

### 1a. Grid Stress Prediction

**Problem framing:** Binary classification — given hourly grid features, predict whether the grid is in a "high-stress" state (demand/capacity ratio above threshold, low reserve margin, price spike, or emergency alert).

**Best-performing model families (from literature):**

| Model | MAPE / Accuracy | Source |
|---|---|---|
| Hybrid LSTM-CNN | 0.231% error on load forecasting | Jang et al. 2024, *Wiley Int. Trans. Electrical Energy Systems* |
| Hybrid LSTM-XGBoost | MAPE 1.18%, R² = 0.994 | Load forecasting for energy communities, *Energy Informatics* 2022 |
| Optimized TPE-XGBoost | MAPE 2.61% (14% improvement over vanilla) | *Scientific Reports* 2022 |
| LightGBM | MAPE 0.18%, R² = 0.86 | *Int. Journal of Ambient Energy* 2025 |
| Transformer-based (univariate) | Best among deep learning for short-term | Survey: *arXiv* 2408.16202 |

**Recommended for this project: XGBoost or LightGBM.** Rationale:
- Tabular features (demand, reserve margin, temperature, time-of-day, day-of-week) are the bread and butter of gradient boosting
- No sequential architecture needed if framing as point-in-time classification
- Can achieve MAPE under 3% with minimal hyperparameter tuning
- scikit-learn-compatible API, fast training, interpretable via SHAP

**Feature engineering approaches:**
- **Temporal:** Hour-of-day, day-of-week, month, holiday flags, lag features (demand at t-1, t-24, t-168)
- **Weather:** Temperature, humidity, heating/cooling degree-days, wind speed
- **Grid state:** Rolling mean/max of demand-to-capacity ratio, reserve margin trend, generation mix percentages
- **Calendar:** Season, school breaks, major events

**Open-source implementations:**
- IESO publishes hourly demand, generation mix, and reserve data: [IESO Data Directory](https://www.ieso.ca/power-data/data-directory)
- AESO provides Alberta grid data: [AESO Grid Data](https://www.aeso.ca/grid/)
- [Gridwatch Ontario](https://gridwatch.ca/) provides real-time fuel-type breakdowns
- [Canadian Centre for Energy Information](https://energy-information.canada.ca/en/resources/high-frequency-electricity-data) hosts a high-frequency electricity data visualization tool
- GitHub: [AlbertaEnergySources](https://github.com/garrettj403/AlbertaEnergySources) for AESO data fetching

**Published benchmarks for grid stress classification specifically:**
Direct "grid stress" classification papers are less common than load forecasting, but the task reduces to: (1) forecast load, (2) threshold against capacity. The load forecasting benchmarks above apply directly. For the binary classification step, F1 scores of 0.85-0.92 are achievable with balanced classes and proper threshold tuning.

---

### 1b. Carbon Intensity Forecasting

**Problem framing:** Time-series regression — predict gCO2/kWh for a given grid region at hourly resolution.

**Best-performing model families:**

| Model | Performance | Context | Source |
|---|---|---|---|
| CarbonCast (CNN-LSTM hierarchical) | MAPE 4.80-13.93% across 6 regions | 96-hour forecast horizon | Maji et al. 2022, *ACM BuildSys* |
| Ensemble (XGBoost 51% + LSTM 28% + SARIMA 21%) | R² = 0.96 | Power plant emissions | Jones 2025, *Medium* |
| LSTM-GAT (Graph Attention) | 89.5% accuracy | Carbon emission prediction | Wu et al. 2024, *Journal of Computational Methods* |
| Temporal Fusion Transformer | State-of-the-art for interpretable forecasting | CO2 short-term forecasting | *Applied Soft Computing* 2024 |
| Prophet | Good baseline for seasonal patterns | Additive decomposition | Facebook/Meta |

**Recommended for this project: Prophet as baseline, XGBoost as primary model.**

Prophet rationale:
- Built-in handling of seasonality (daily, weekly, yearly), holiday effects, and trend changes
- Requires minimal feature engineering — just timestamps and target values
- Produces uncertainty intervals out of the box
- 10 lines of code to get a working model

XGBoost rationale for improvement:
- Can incorporate exogenous features (weather, generation mix, imports/exports)
- Literature shows ensemble approaches (XGBoost + LSTM) consistently beat single models

**CarbonCast (key reference):**
- First open-sourced multi-day carbon intensity forecasting tool
- Two-tier architecture: Tier 1 forecasts production by source, Tier 2 combines forecasts with weather for carbon intensity
- Code: [github.com/carbonfirst/CarbonCast](https://github.com/carbonfirst/CarbonCast)
- Robust to noisy/missing inputs — important for Canadian data gaps
- Covers 6 regions; architecture is adaptable to Canadian provinces

**ElectricityMap methodology:**
- Uses raw production data from official government/TSO sources
- Runs flow-tracing algorithm for consumption-based accounting
- Life-cycle carbon intensity factors (construction + fuel + operations + decommissioning)
- Open-source parsers: [github.com/electricitymaps/electricitymaps-contrib](https://github.com/electricitymaps/electricitymaps-contrib)
- Free tier API available for academic use
- Already covers Ontario (IESO) and Alberta (AESO)

**Forecasting horizon relevance:**
- **Hourly:** Most relevant for operational scheduling (when to run compute workloads)
- **Daily/Weekly:** Relevant for siting decisions — captures seasonal patterns
- **Seasonal:** Most relevant for this project — captures the fundamental differences between provinces
- For a siting tool, **monthly/seasonal averages with uncertainty bands** are the right granularity

**Canadian provincial carbon intensity (massive variation — the core insight):**

| Province | Approx. gCO2/kWh | Primary Sources |
|---|---|---|
| Quebec | ~1-3 | 95%+ hydro |
| British Columbia | ~10-15 | 90%+ hydro |
| Manitoba | ~3-5 | 97%+ hydro |
| Ontario | ~40-75 | Nuclear + hydro + gas |
| New Brunswick | ~290-340 | Mix: nuclear, hydro, gas, oil |
| Alberta | ~470 | Natural gas dominant |
| Saskatchewan | ~580-650 | Coal + gas |
| Nova Scotia | ~690 | Coal + gas dominant |

Source: [CER Provincial Energy Profiles](https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/provincial-territorial-energy-profiles/provincial-territorial-energy-profiles-canada.html); [Canada.ca emission factors](https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/output-based-pricing-system/federal-greenhouse-gas-offset-system/emission-factors-reference-values.html)

This 200x variation across provinces is what makes Canada uniquely interesting for this project.

---

### 1c. PUE / Cooling Regression

**Problem framing:** Regression — predict Power Usage Effectiveness (PUE) from climate and design variables.

**Key findings from literature:**

**Google DeepMind benchmark (the gold standard):**
- Neural network ensemble trained on sensor data from Google data centers
- Achieved 40% reduction in cooling energy, 15% reduction in overall PUE
- 5 hidden layers, 50 nodes each, trained on 2 years of monitoring data
- Features: temperatures, power, pump speeds, setpoints from thousands of sensors
- Source: [DeepMind blog](https://deepmind.google/discover/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/)

**Academic PUE prediction studies:**
- Lei et al. evaluated PUE with three economizer types (DASE, WSE, seawater) across climate zones
- Sobol sensitivity analysis identified outdoor dry-bulb temperature and wet-bulb temperature as the highest-influence parameters
- Parameter ranges studied: dry-bulb -40 to 40 C, relative humidity 0-100%
- Source: [MDPI Buildings 2024](https://www.mdpi.com/2075-5309/14/1/299)

**ASHRAE free cooling analysis:**
- Psychrometric bin analysis using TMY3 weather data
- 5,500+ free cooling hours (60% of year) available across most of Canada
- Alternative cooling strategies applicable in all climate zones
- Average cooling energy savings of ~80% where economizers are feasible
- Source: [NREL / DOE](https://www1.eere.energy.gov/buildings/publications/pdfs/rsf/psychrometric_bin_analysis_alternative_cooling_strategies_data_centers.pdf)

**Key features for PUE regression:**
1. **Outdoor dry-bulb temperature** (highest influence per Sobol analysis)
2. **Outdoor wet-bulb temperature** (determines evaporative cooling potential)
3. **Relative humidity** (affects cooling tower performance)
4. **Cooling system type** (air-cooled, evaporative, hybrid, liquid)
5. **IT load factor** (partial load = higher PUE)
6. **Design PUE baseline** (varies by facility age/design)

**Published PUE ranges by archetype:**

| Configuration | Typical PUE Range |
|---|---|
| State-of-the-art hyperscale (cold climate) | 1.05 - 1.15 |
| Modern hyperscale (moderate climate) | 1.10 - 1.25 |
| Enterprise (cold climate, economizer) | 1.20 - 1.40 |
| Enterprise (hot climate, chiller) | 1.40 - 1.80 |
| Legacy facility (no economizer) | 1.80 - 2.50 |
| Industry average (2024) | ~1.55 - 1.60 |

**Recommended for this project: Linear regression or Random Forest regression.**

Rationale:
- PUE is largely driven by a handful of well-understood physical variables
- The relationship between temperature and cooling energy is approximately linear in the free-cooling regime and piecewise-linear with a breakpoint at the economizer switchover temperature
- A Random Forest with 5-8 features can capture the nonlinearity at switchover points
- Training data can be semi-synthetic: use published PUE benchmarks + TMY3 weather data for Canadian cities to build a lookup + regression model
- No need for deep learning; interpretability matters for a policy tool

**Practical approach for MVP:**
Rather than training from scratch, use a physics-informed regression:
1. Download TMY3 or CWEC (Canadian Weather for Energy Calculations) data for target cities
2. Compute free-cooling hours per city using ASHRAE bins
3. Estimate PUE = 1.0 + (cooling_overhead / IT_load) where cooling overhead is modeled as a function of dry-bulb temperature relative to supply temperature setpoint
4. Validate against published PUE ranges

---

### 1d. Water Intensity Estimation

**Problem framing:** Estimate liters of water consumed per kWh of IT energy for a given location and cooling type.

**WUE benchmarks from industry:**

| Cooling Type | WUE (L/kWh) | Notes |
|---|---|---|
| Air-cooled only | ~0 | No water, but higher energy use |
| Best-in-class evaporative (e.g., AWS) | 0.19 | AWS global average |
| Typical evaporative | 1.8 | Industry average per Equinix |
| Inefficient evaporative (hot/humid) | 2.5 - 9.0 | Upper bound depends on climate |
| Hybrid (air + evaporative) | 0.5 - 1.5 | Partial water use |
| Microsoft zero-water design (2024+) | ~0 | Chip-level liquid cooling, no evaporation |

Sources: [EESI](https://www.eesi.org/articles/view/data-centers-and-water-consumption); [Equinix blog](https://blog.equinix.com/blog/2024/11/13/what-is-water-usage-effectiveness-wue-in-data-centers/); [Dgtl Infra](https://dgtlinfra.com/data-center-water-usage/); [Microsoft Cloud blog](https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/)

**Modeling approach:**

The water intensity model does not need ML in the traditional sense. A physics-based estimation works well:

```
Water_consumption (L/kWh) = f(cooling_type, dry_bulb_temp, wet_bulb_temp, humidity)
```

For evaporative cooling, water consumption scales with:
- The enthalpy difference between outdoor and supply air
- The number of hours requiring evaporative cooling (vs free cooling)
- The cooling tower efficiency (cycles of concentration)

**Practical formula for MVP:**
```
WUE_estimated = base_WUE(cooling_type) * climate_adjustment(wet_bulb_temp)
Water_harm = WUE_estimated * Total_energy * water_stress_multiplier(region)
```

**Water stress data:**
- [WRI Aqueduct 4.0](https://www.wri.org/data/aqueduct-water-risk-atlas) provides provincial/sub-provincial water stress indices
- 13 indicators including groundwater availability, water depletion, baseline water stress
- Monthly snapshots available
- Downloadable and available via Google Earth Engine
- Canadian provincial rankings included

**Regional water stress context for Canada:**
- Prairie provinces (Alberta, Saskatchewan) have higher water stress
- BC interior has seasonal water stress (summer drought)
- Ontario Great Lakes region has abundant water supply
- Quebec has very low water stress
- This creates a meaningful differentiator when combined with carbon intensity

---

## 2. Composite Scoring (Societal Impact Score)

### MCDA Framework

**Recommended approach: Weighted Linear Combination (WLC) with sensitivity analysis.**

The Societal Impact Score combines four sub-scores:

```
SIS = w_carbon * S_carbon + w_water * S_water + w_grid * S_grid + w_uncertainty * S_uncertainty
```

Where each S is normalized to [0, 1] and lower is better.

**Normalization:** Min-max scaling across all candidate regions:
```
S_i = (value_i - min_all) / (max_all - min_all)
```

### Weighting Strategies

| Strategy | Description | Pros | Cons | Recommended? |
|---|---|---|---|---|
| Equal weights | w = 0.25 each | Simple, transparent, no bias | Ignores relative importance | Good baseline |
| AHP (Analytic Hierarchy Process) | Pairwise comparison matrix from experts | Principled, widely used in MCDA literature | Requires expert elicitation | Good for report |
| Stakeholder-defined | Survey-based weights | Democratic, contextual | Needs actual stakeholders | Stretch goal |
| Entropy-based | Data-driven from variance | Objective, reproducible | May not reflect policy priorities | Alternative |

Sources: [ScienceDirect MCDA overview](https://www.sciencedirect.com/topics/social-sciences/multiple-criteria-decision-analysis); [Wieckowski et al. 2023, *Knowledge-Based Systems*](https://journals.sagepub.com/doi/10.3233/KES-230487)

**Recommended for MVP:** Equal weights as default, with an interactive slider in the dashboard allowing users to adjust weights. This is both technically simple and powerful for demonstration.

**For the report/presentation:** Run AHP with 2-3 weight scenarios:
1. Climate-first (carbon = 0.4, water = 0.3, grid = 0.2, uncertainty = 0.1)
2. Grid-reliability-first (grid = 0.4, carbon = 0.3, water = 0.2, uncertainty = 0.1)
3. Equal weights (0.25 each)

Show how rankings change under different weight assumptions -- this is a strong analytical contribution.

### Uncertainty Quantification

**Monte Carlo simulation (recommended for this project):**

1. For each sub-model, characterize prediction uncertainty as a distribution
   - Prophet gives uncertainty intervals natively
   - XGBoost: use quantile regression or bootstrap the training set
   - PUE regression: propagate weather data uncertainty
2. Sample N=1000 draws from each sub-model's uncertainty distribution
3. Compute SIS for each draw
4. Report the 5th and 95th percentile as a 90% confidence interval

```python
import numpy as np

def monte_carlo_sis(carbon_dist, water_dist, grid_dist, weights, n=1000):
    carbon_samples = np.random.normal(carbon_dist['mean'], carbon_dist['std'], n)
    water_samples = np.random.normal(water_dist['mean'], water_dist['std'], n)
    grid_samples = np.random.normal(grid_dist['mean'], grid_dist['std'], n)

    sis_samples = (weights['carbon'] * carbon_samples +
                   weights['water'] * water_samples +
                   weights['grid'] * grid_samples)

    return {
        'mean': np.mean(sis_samples),
        'ci_low': np.percentile(sis_samples, 5),
        'ci_high': np.percentile(sis_samples, 95)
    }
```

This is straightforward to implement and provides genuine uncertainty quantification -- a strong differentiator for an undergraduate project.

Sources: [Winrock Monte Carlo guidance](https://winrock.org/wp-content/uploads/2018/02/UncertaintyReport-12.26.17.pdf); [PMC Monte Carlo consistency](https://pmc.ncbi.nlm.nih.gov/articles/PMC8201410/)

---

## 3. Feasibility Assessment

### Can undergrads build this in 2 months?

**Yes, with appropriate scoping.** Here is the breakdown:

#### Week-by-week plan (8 weeks, 4 people, 10 hrs/week each = 320 person-hours total):

| Week | Activity | Deliverable |
|---|---|---|
| 1 | Data collection, exploration, environment setup | Raw datasets downloaded, EDA notebook |
| 2 | Feature engineering for all sub-models | Cleaned feature matrices |
| 3 | Train grid stress + carbon intensity models | Working XGBoost/Prophet models |
| 4 | Train PUE regression + water estimation | All four sub-models operational |
| 5 | Composite scoring + Monte Carlo uncertainty | SIS calculation pipeline |
| 6 | Folium map visualization + dashboard | Interactive map prototype |
| 7 | Integration, testing, sensitivity analysis | End-to-end pipeline |
| 8 | Presentation prep, report writing | Final deliverables |

#### Realistic MVP scope (what to build):

1. **Scope to 5-8 Canadian cities/regions** across provinces with different grid profiles:
   - Toronto (ON) -- nuclear + hydro + gas
   - Montreal (QC) -- hydro dominant
   - Calgary (AB) -- gas dominant
   - Vancouver (BC) -- hydro dominant
   - Winnipeg (MB) -- hydro dominant
   - Halifax (NS) -- coal + gas
   - Saskatoon (SK) -- coal + gas
   - Moncton (NB) -- mixed

2. **Use monthly/seasonal averages** rather than hourly forecasting for the MVP. Hourly forecasting is a stretch goal.

3. **Semi-synthetic PUE model** based on TMY weather data + published benchmarks rather than training on real data center telemetry (which is proprietary).

4. **Static water stress indices** from WRI Aqueduct rather than dynamic water modeling.

5. **Folium choropleth map** showing SIS by province/city with pop-up details.

#### What simplifications are appropriate:

- **PUE model:** Use regression on weather data + published benchmarks rather than real sensor data. The physics is well-understood; ML adds marginal value here for an MVP.
- **Water model:** Use lookup table (cooling type x climate zone) rather than trained ML model. WUE values are well-documented.
- **Grid stress:** Focus on Ontario and Alberta (where hourly data is readily available), extrapolate for other provinces using annual averages.
- **Carbon intensity:** Use ElectricityMap historical data or published provincial emission factors rather than building a forecaster from scratch.
- **Composite score:** Equal weights with sensitivity analysis rather than full AHP elicitation.

#### Libraries and tools:

| Tool | Purpose | Learning Curve |
|---|---|---|
| **scikit-learn** | XGBoost, Random Forest, preprocessing, metrics | Low (undergrad ML course) |
| **Prophet** | Carbon intensity baseline forecasting | Low (10-line setup) |
| **pandas / numpy** | Data wrangling | Low |
| **Folium** | Interactive map visualization | Low-Medium |
| **matplotlib / seaborn** | Static plots, model diagnostics | Low |
| **SHAP** | Model interpretability | Low-Medium |
| **xgboost** | Gradient boosting (if needed beyond sklearn) | Low |
| **Streamlit** (stretch) | Interactive dashboard | Medium |

All of these are pip-installable, well-documented, and have extensive tutorials. A team with one ML course and basic Python should be productive within a week.

---

## 4. Differentiation from Existing Work

### What already exists:

1. **Cornell/Nature Sustainability roadmap (Xiao & You, Nov 2025):**
   - US-focused (Midwest, windbelt states)
   - Macro-level projections (24-44 MtCO2/year by 2030)
   - Proposes smart siting conceptually but does not provide a tool
   - Source: [Cornell Chronicle](https://news.cornell.edu/stories/2025/11/roadmap-shows-environmental-impact-ai-data-center-boom)

2. **ElectricityMap:**
   - Real-time carbon intensity visualization
   - Does not do siting optimization or composite scoring
   - Does not include water or grid stress

3. **Google DeepMind cooling optimization:**
   - Operational optimization for existing facilities
   - Does not address siting decisions
   - Proprietary, not reproducible

4. **Commercial tools (e.g., Schneider, Vertiv):**
   - Focus on facility design and operational efficiency
   - Not open-source, not policy-oriented
   - Do not include societal/environmental composite scoring

### What makes this project novel:

1. **Canada-specific focus:** No existing tool addresses Canadian provincial grid diversity for data center siting. The 200x variation in carbon intensity across provinces (Quebec ~2 gCO2/kWh vs Saskatchewan ~600 gCO2/kWh) creates a uniquely stark decision landscape.

2. **Multi-dimensional composite scoring:** Existing tools address carbon OR water OR efficiency in isolation. Combining all four dimensions (carbon, water, grid stress, PUE/cooling) into a single uncertainty-aware score is genuinely novel.

3. **Uncertainty quantification:** The Monte Carlo confidence intervals on the composite score add a layer of rigor that is absent from existing commercial tools and most academic work.

4. **Open-source, transparent, policy-oriented:** Designed to inform public policy and community advocacy, not commercial facility planning.

5. **Provincial grid diversity as a natural experiment:** Canada's federated electricity system -- where each province controls its own generation mix -- creates a natural experiment. Quebec's hydro grid vs Alberta's gas grid vs Ontario's nuclear grid produce dramatically different environmental impacts for identical data center workloads. No other country has this level of variation within a single national boundary with comparable data quality.

### Policy relevance:

- **Canada's Net-Zero by 2050 target:** Data center siting decisions made today lock in 20-30 years of emissions. A tool that quantifies the carbon implications of siting choices directly supports national climate policy.
- **Provincial electricity planning:** Alberta's grid is rapidly decarbonizing (coal phase-out complete, growing wind/solar). A forecasting component could show how siting decisions age over time.
- **Water policy:** BC and Alberta face increasing summer drought risk. A tool incorporating water stress helps avoid exacerbating regional water crises.
- **Indigenous consultation:** Many proposed data center sites are near Indigenous communities. Grid stress modeling can quantify whether new load jeopardizes electricity reliability for existing communities.
- **RBC Borealis alignment:** Fits the program's mission of using ML for societal benefit. Combines environmental sustainability with community impact. Novel for the program -- no past cohort has done this.

---

## 5. Key References

### Grid Stress / Load Forecasting
- Jang et al. 2024: [Comparative Analysis of Deep Learning for Load Forecasting](https://onlinelibrary.wiley.com/doi/full/10.1155/2024/5587728)
- [Frontiers: Evaluation of Electrical Load Demand Forecasting](https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2024.1408119/full)
- [MDPI: Enhancing Electricity Load Forecasting](https://www.mdpi.com/2227-7080/13/2/59)
- [Scientific Reports: Optimised XGBoost for Short-term Load Forecasting](https://www.nature.com/articles/s41598-022-22024-3)

### Carbon Intensity Forecasting
- Maji et al. 2022: [CarbonCast](https://dl.acm.org/doi/abs/10.1145/3563357.3564079) | [GitHub](https://github.com/carbonfirst/CarbonCast)
- [ElectricityMap open-source parsers](https://github.com/electricitymaps/electricitymaps-contrib)
- [ElectricityMap API docs](https://app.electricitymaps.com/docs)
- [CER Provincial Energy Profiles](https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/provincial-territorial-energy-profiles/provincial-territorial-energy-profiles-canada.html)

### PUE / Cooling
- [DeepMind Data Centre Cooling](https://deepmind.google/discover/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40/)
- [MDPI: Data Center PUE with Economizer Types across Climate Zones](https://www.mdpi.com/2075-5309/14/1/299)
- [DOE: Psychrometric Bin Analysis for Data Centers](https://www1.eere.energy.gov/buildings/publications/pdfs/rsf/psychrometric_bin_analysis_alternative_cooling_strategies_data_centers.pdf)
- [MDPI: Prediction of Overall Energy Consumption of Data Centers](https://www.mdpi.com/1424-8220/22/10/3704)

### Water
- [EESI: Data Centers and Water Consumption](https://www.eesi.org/articles/view/data-centers-and-water-consumption)
- [DOE: Cooling Water Efficiency for Federal Data Centers](https://www.energy.gov/femp/cooling-water-efficiency-opportunities-federal-data-centers)
- [WRI Aqueduct 4.0](https://www.wri.org/data/aqueduct-water-risk-atlas)
- [Dgtl Infra: Data Center Water Usage Guide](https://dgtlinfra.com/data-center-water-usage/)
- [Equinix: WUE in Data Centers](https://blog.equinix.com/blog/2024/11/13/what-is-water-usage-effectiveness-wue-in-data-centers/)
- [Microsoft: Zero-Water Datacenter Design](https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/)

### Composite Scoring / MCDA
- [ScienceDirect: MCDA for Sustainability Assessment](https://www.sciencedirect.com/science/article/pii/S1470160X14002647)
- [Wieckowski et al. 2023: Recent Advances in MCDA](https://journals.sagepub.com/doi/10.3233/KES-230487)
- [Wikipedia: MCDA](https://en.wikipedia.org/wiki/Multiple-criteria_decision_analysis)

### Data Center Environmental Impact (2024-2025)
- Xiao & You 2025: [Nature Sustainability - Environmental Impact of AI Data Centers](https://news.cornell.edu/stories/2025/11/roadmap-shows-environmental-impact-ai-data-center-boom)
- [Frontiers: Forecasting US Data Center CO2 Emissions](https://www.frontiersin.org/journals/sustainability/articles/10.3389/frsus.2024.1507030/full)
- [Patterns: Carbon and Water Footprints of Data Centers](https://www.cell.com/patterns/fulltext/S2666-3899(25)00278-8)

### Canadian Data Sources
- [IESO Data Directory](https://www.ieso.ca/power-data/data-directory)
- [AESO Grid Data](https://www.aeso.ca/grid/)
- [Canada.ca Emission Factors](https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/output-based-pricing-system/federal-greenhouse-gas-offset-system/emission-factors-reference-values.html)
- [ElectricityMap Free Tier API](https://www.electricitymaps.com/free-tier-api)
- [Gridwatch Ontario](https://gridwatch.ca/)

---

## 6. Summary Recommendation

**This project is feasible for a team of 4 undergrads in 2 months.** The key to success is disciplined scoping:

**Build:** XGBoost for grid stress (ON + AB only), Prophet + published factors for carbon intensity, physics-based regression for PUE, lookup table for water intensity, weighted linear combination with Monte Carlo uncertainty, Folium map.

**Skip (for MVP):** Hourly forecasting for all provinces, deep learning, real-time dashboard, full AHP stakeholder elicitation.

**The strongest pitch for the proposal:** This is the only open-source tool that combines carbon, water, grid stress, and cooling efficiency into a single uncertainty-aware siting score for Canadian provinces. The 200x variation in provincial carbon intensity makes Canada the most interesting country in the world for this analysis. The tool is policy-relevant, timely (AI data center boom), and uses proven ML techniques on publicly available data.
