# MVP Scope and 8-Week Timeline

---

## Team Assumptions

- **Team size:** 4 undergraduate students
- **Weekly commitment:** 10 hours per person
- **Total budget:** 4 people x 10 hours/week x 8 weeks = **320 person-hours**
- **Skill level:** Intermediate Python, introductory machine learning, no specialized domain expertise required

All libraries and tools used in this project are pip-installable, well-documented, and supported by extensive tutorials. No proprietary software, paid APIs, or specialized hardware is required.

### Suggested Role Allocation

| Role | Team Members | Primary Responsibilities |
|---|---|---|
| Data Engineering Lead | 1 | Data acquisition, cleaning, pipeline scripts, API integration |
| ML Modeling Lead | 1 | Sub-model training, hyperparameter tuning, evaluation |
| Integration and Visualization Lead | 1 | Composite scoring, Monte Carlo, Folium map, dashboard |
| Research and Documentation Lead | 1 | Literature review, report writing, presentation, assumption documentation |

All team members contribute to all areas. The lead designation determines who owns the deliverable for each component and makes tie-breaking decisions on scope.

### Person-Hour Budget Breakdown

| Phase | Hours | Share |
|---|---|---|
| Data collection and EDA (Weeks 1-2) | 80 | 25% |
| Model development and training (Weeks 3-4) | 80 | 25% |
| Composite scoring and visualization (Weeks 5-6) | 80 | 25% |
| Integration, testing, report, and presentation (Weeks 7-8) | 80 | 25% |
| **Total** | **320** | **100%** |

The even distribution across phases is deliberate. Projects that front-load data work and compress the presentation phase produce weaker final deliverables.

---

## MVP Target Cities

The MVP covers 5-8 cities selected to span Canada's full range of grid carbon intensity, climate zones, and data center market maturity. This diversity is essential for demonstrating that the Societal Impact Score produces meaningfully different recommendations across regions.

| City | Province | Grid Type | Carbon Intensity (gCO2/kWh) | DC Presence | Selection Rationale |
|---|---|---|---|---|---|
| Toronto | ON | Nuclear + hydro + gas | ~38 | Highest (72 facilities) | Largest Canadian DC market, complex mixed grid |
| Montreal | QC | Hydro dominant | ~1.7 | High (54 facilities) | Near-zero carbon baseline, second-largest market |
| Calgary | AB | Gas dominant | ~490 | Fast-growing (~2 GW pipeline) | Highest-growth market, fossil-heavy grid |
| Vancouver | BC | Hydro dominant | ~15 | Medium (28 facilities) | Low-carbon hydro grid, water stress risk |
| Winnipeg | MB | Hydro dominant | ~1.4 | Low | Lowest carbon intensity in Canada |
| Halifax | NS | Coal + gas | ~700 | Low | High-carbon grid, Atlantic Canada representation |
| Saskatoon | SK | Coal + gas | ~670 | Low | Second-highest carbon intensity nationally |
| Moncton | NB | Mixed | ~350 | Low | Mixed generation, interprovincial trade |

The 200x variation in carbon intensity across these cities (1.4 to 700 gCO2/kWh) provides a natural experiment that no other country offers with comparable data quality.

---

## Week-by-Week Plan

| Week | Focus Area | Activities | Deliverable |
|---|---|---|---|
| 1 | Data Collection and Setup | Download all raw datasets (IESO, AESO, Hydro-Quebec, ECCC weather, WRI Aqueduct, Electricity Maps). Set up Python environment, GitHub repository, and project structure. Initial exploratory data analysis. | Raw datasets downloaded, exploratory Jupyter notebook, project README |
| 2 | Feature Engineering | Build cleaned feature matrices for each city. Engineer temporal, demand, supply, weather, and market features for grid stress model. Prepare climate features for PUE regression. Merge water stress indices. | Cleaned feature matrices per city, data pipeline scripts |
| 3 | Grid Stress and Carbon Models | Train XGBoost classifier for grid stress on Ontario and Alberta hourly data. Train Prophet baseline for carbon intensity forecasting. Validate against held-out test sets. | Working XGBoost and Prophet models for ON + AB with evaluation metrics |
| 4 | PUE and Water Models | Build semi-synthetic PUE regression from TMY weather data and published benchmarks. Construct water intensity estimation from WUE benchmarks and WRI Aqueduct stress indices. | All four sub-models operational and individually validated |
| 5 | Composite Scoring | Implement weighted linear combination for Societal Impact Score. Build Monte Carlo uncertainty propagation pipeline (10,000 draws). Run sensitivity analysis across weight scenarios. | SIS calculation pipeline end-to-end with confidence intervals |
| 6 | Visualization | Build interactive Folium map with city-level SIS scores, pop-up details showing sub-model breakdowns, and color-coded risk indicators. Generate static matplotlib/seaborn diagnostic plots. | Interactive map prototype, model diagnostic figures |
| 7 | Integration and Testing | End-to-end pipeline integration. Cross-validation of all sub-models. Sensitivity analysis across weight configurations. Edge case testing. Documentation of all assumptions. | Validated end-to-end pipeline, sensitivity analysis report |
| 8 | Presentation | Write final report with methodology, results, limitations, and policy recommendations. Prepare presentation slides. Clean and document GitHub repository. | Final report, presentation slides, polished repository |

---

## Key Simplifications for MVP

The following scope constraints keep the project feasible within 320 person-hours while preserving analytical rigor.

### Temporal Resolution

- **MVP:** Monthly and seasonal averages for most sub-models
- **Full version:** Hourly forecasting with real-time data feeds
- **Justification:** Monthly granularity captures the dominant source of variation (inter-provincial differences), which is 10-100x larger than intra-day variation within a single province

### PUE Estimation

- **MVP:** Semi-synthetic PUE model using TMY (Typical Meteorological Year) weather data crossed with published industry benchmarks by climate zone
- **Full version:** Real sensor telemetry from operating facilities
- **Justification:** The physics of data center cooling is well-understood. Dry-bulb and wet-bulb temperature are the highest-influence parameters (Lei et al. 2024, Sobol sensitivity analysis). TMY data captures climate variation accurately.

### Water Stress

- **MVP:** Static WRI Aqueduct water stress indices per watershed
- **Full version:** Dynamic seasonal water modeling with municipal capacity constraints
- **Justification:** WRI Aqueduct provides globally consistent, peer-reviewed baseline stress indices at sub-basin resolution. Dynamic modeling requires hydrological expertise beyond the team's scope.

### Grid Stress Coverage

- **MVP:** Full hourly modeling for Ontario (IESO) and Alberta (AESO). Other provinces use annual capacity and demand ratios scaled from Statistics Canada Table 25-10-0015-01.
- **Full version:** Hourly modeling for all provinces with ISO-level data
- **Justification:** Ontario and Alberta have the best open data and represent the two most critical DC markets. The annual scaling approach introduces uncertainty but captures the primary inter-provincial variation.

### Carbon Intensity

- **MVP:** Published ECCC provincial emission factors, validated against Electricity Maps historical data where available
- **Full version:** Marginal emission factors computed from hourly fuel-mix dispatch data
- **Justification:** Provincial annual factors capture 90%+ of inter-regional variation. Marginal factors add precision but require hourly dispatch modeling that is a project in itself.

### Composite Weights

- **MVP:** Equal weights across all four sub-models, with sensitivity analysis showing how results change under alternative weight configurations
- **Full version:** Full Analytic Hierarchy Process (AHP) elicitation with domain expert stakeholders
- **Justification:** Equal weights are transparent and defensible. Sensitivity analysis demonstrates robustness across plausible weight ranges.

---

## Libraries and Tools

All tools are open-source, pip-installable, and well-documented with extensive tutorials.

| Tool | Purpose | Learning Curve | Notes |
|---|---|---|---|
| scikit-learn | Preprocessing, metrics, Random Forest baseline | Low | Standard ML toolkit |
| xgboost | Gradient boosting for grid stress classification | Low | Drop-in scikit-learn API |
| Prophet | Carbon intensity baseline forecasting | Low | 10-line setup, automatic seasonality |
| pandas / numpy | Data wrangling and numerical computation | Low | Team prerequisite |
| Folium | Interactive map visualization with Leaflet.js | Low-Medium | GeoJSON support, custom pop-ups |
| matplotlib / seaborn | Static plots and model diagnostics | Low | Standard visualization |
| SHAP | Model interpretability and feature importance | Low-Medium | Tree-based SHAP is fast |
| gridstatus | IESO and AESO data access | Low | Wraps ISO APIs cleanly |
| Streamlit (stretch) | Interactive dashboard with weight sliders | Medium | Only if time permits |

### Environment Setup

```
python -m venv .venv
source .venv/bin/activate
pip install pandas numpy scikit-learn xgboost prophet folium matplotlib seaborn shap gridstatus
```

No GPU required. All models train on CPU in minutes on standard laptop hardware.

---

## Stretch Goals

If the team completes the core MVP ahead of schedule, the following extensions are prioritized by impact-to-effort ratio.

| Priority | Stretch Goal | Estimated Effort | Value Added |
|---|---|---|---|
| 1 | Hourly carbon intensity forecasting for Ontario and Alberta | 15-20 hours | Enables time-of-day siting recommendations |
| 2 | Streamlit interactive dashboard with weight sliders | 10-15 hours | Dramatically improves presentation and stakeholder engagement |
| 3 | Scenario modeling: Alberta grid decarbonization 2025-2035 | 10-15 hours | Shows how siting decisions "age" over time |
| 4 | Full AHP stakeholder elicitation for weights | 8-12 hours | Replaces equal weights with expert-informed preferences |
| 5 | Integration with CarbonCast open-source framework | 15-20 hours | Connects to established carbon forecasting infrastructure |

---

## Deliverables

The project produces five concrete deliverables.

| # | Deliverable | Format | Description |
|---|---|---|---|
| 1 | GitHub repository | Code + docs | All source code, data processing scripts, and documentation under MIT license |
| 2 | Exploratory notebooks | Jupyter (.ipynb) | EDA for each dataset, model training and evaluation, sensitivity analysis |
| 3 | Interactive map | Folium HTML | City-level SIS scores with pop-up sub-model breakdowns, color-coded risk |
| 4 | Written report | PDF/Markdown | Methodology, results, limitations, policy recommendations (15-20 pages) |
| 5 | Presentation slides | PDF/PPTX | Final demo presentation (15-20 minutes) |

### Deliverable 3: Interactive Map Detail

The Folium map is the primary demonstration artifact. Each city marker includes a pop-up with:

- Overall SIS score (with 90% confidence interval)
- Sub-model breakdown: grid stress index, carbon intensity, estimated PUE, water risk score
- Color coding: green (low impact), yellow (moderate), red (high impact)
- Province-level context: generation mix pie chart, installed DC capacity

The map is exported as a self-contained HTML file that opens in any browser without a server. This ensures the deliverable is immediately shareable with reviewers and stakeholders.

---

## Risk to Timeline

The highest-risk weeks are Week 3 (model training) and Week 5 (composite scoring with Monte Carlo). If either falls behind, the buffer strategy is:

- **Week 3 delay:** Simplify grid stress to a lookup table by province rather than a trained classifier. This sacrifices granularity but unblocks the composite scoring pipeline.
- **Week 5 delay:** Drop Monte Carlo uncertainty and report point estimates with manual sensitivity analysis. Confidence intervals are valuable but not essential for a proof-of-concept.

The Week 8 deliverables (report and presentation) are non-negotiable and should not be compressed.

---

## Key References

- Lei et al. 2024, "Data Center PUE with Economizer Types across Climate Zones," MDPI Buildings
- Jang et al. 2024, "Comparative Analysis of Deep Learning for Load Forecasting," International Journal of Energy Research
- LBNL 2024, "United States Data Center Energy Usage Report"
- `gridstatus` Python library: https://github.com/kmax12/gridstatus
- WRI Aqueduct: https://www.wri.org/aqueduct
