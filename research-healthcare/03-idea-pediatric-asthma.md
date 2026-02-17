# Idea #3: Predicting Pediatric Asthma Exacerbations from Environmental Factors

**Acceptance Likelihood: 4.8/5 — Top Healthcare Pick**

---

## The Problem

Asthma affects approximately **10% of Canadian children**, with emergency visits and hospitalizations concentrated in low-income and Indigenous communities. Environmental factors — air quality, temperature, allergens — are key triggers that follow predictable patterns.

### Key Statistics
- **10% of Canadian children** diagnosed with asthma; higher in boys (18%) vs. girls (13%)
- **20% of children** with asthma visited the ER 2-5 times/year (Asthma Canada 2024)
- Hospitalization rates **1.5x higher** in lowest-income vs. highest-income neighbourhoods
- **First Nations 2x more likely** to be hospitalized for asthma regardless of urban/rural residence
- Alberta: highest-acuity asthma presentations increased by **>300%** between 2010 and 2022
- Montreal study: temperatures of 15.8-19.3°C associated with **37% increase** in pediatric asthma ED visits
- A **1-unit increase in AQHI** linked to **2.1% increase** in same-day asthma hospitalization

### Why It Matters
Climate change is extending allergy seasons and increasing air pollution episodes. Predicting asthma exacerbation risk from environmental data enables proactive public health warnings and resource allocation at hospitals.

---

## Why Machine Learning Can Help

Asthma exacerbations result from complex interactions between air pollutants (PM2.5, O3, NO2), weather (temperature, humidity), allergens, and socioeconomic factors. ML captures these non-linear relationships better than traditional epidemiological models.

### ML Task
**Regression:** Predict aggregate weekly/monthly asthma hospitalization counts for a Canadian city from environmental and socioeconomic features.

### Proven Approaches
- **Random Forest with environmental factors:** AUC **0.856** for hospitalization prediction
- **XGBoost on EHR data:** AUC **0.964** for individual exacerbation prediction
- **CHILD Cohort ML (McMaster):** AUC **>0.90** at age 3 for asthma diagnosis prediction
- **Key features:** prior exacerbation, PM2.5, O3, temperature, socioeconomic indicators

---

## Datasets

### 1. NAPS — National Air Pollution Surveillance (Primary)
- **Source:** Environment and Climate Change Canada
- **URL:** https://open.canada.ca/data/en/dataset/1b36a356-defd-4813-acea-47bc3abd859b
- **Contains:** PM2.5, PM10, O3, NO2, SO2, CO from ~260 stations in 150 communities; data since 1969
- **Format:** CSV
- **Access:** Open Government Licence

### 2. AQHI Observations
- **URL:** https://open.canada.ca/data/dataset/28936e1b-681f-4c73-b04a-e86d4b3917c6
- **Contains:** Air Quality Health Index (1-10+ scale) by location, daily
- **Format:** JSON, CSV
- **Access:** Open

### 3. ECCC Historical Weather Data
- **URL:** https://climate.weather.gc.ca/historical_data/search_historic_data_e.html
- **Contains:** Hourly/daily temperature, humidity, wind, precipitation for all Canadian stations
- **Format:** CSV
- **Access:** Open

### 4. CCDSS Asthma Surveillance
- **URL:** https://health-infobase.canada.ca/ccdss/data-tool/
- **Contains:** Asthma incidence, prevalence, mortality by age/sex/province/year
- **Access:** Open (Excel export from web tool)

### 5. Census 2021 Socioeconomic Data
- **URL:** https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E
- **Contains:** Income, education, housing by census tract
- **Access:** Open; programmable via `cancensus` R package

---

## Proposed ML Pipeline

```
1. Data acquisition (focus on one city: Toronto, Montreal, or Edmonton)
   - Download NAPS PM2.5/O3/NO2 for target city stations
   - Download AQHI daily observations
   - Download ECCC daily weather (temperature, humidity)
   - Export CCDSS asthma data for target province

2. Feature engineering
   - Lag features: 1-day, 3-day, 7-day rolling averages of pollutants
   - Seasonal indicators, day-of-week effects
   - Pollutant interaction terms (PM2.5 x temperature)
   - Census income quintiles by neighbourhood

3. Model training
   - Linear Regression (baseline)
   - Random Forest, XGBoost
   - Optional: Prophet or simple LSTM for time-series component
   - Cross-validation: time-based splits (no future leakage)

4. Evaluation
   - MAE, RMSE, R² for regression
   - SHAP for feature importance
   - Stratify predictions by income quintile (equity analysis)

5. Deliverable
   - Prediction model for weekly asthma ED burden
   - Feature importance showing which environmental factors matter most
   - Equity analysis: do low-income areas face higher predicted risk?
```

---

## Strengths

- **Entirely open data pipeline** — NAPS + AQHI + ECCC + CCDSS = zero access barriers
- **Strong Canadian precedent** — Montreal, Edmonton, Ottawa studies all use this data
- **Climate change framing** is timely and compelling for presentation
- **Equity lens** — 1.5x income disparity and 2x Indigenous disparity are directly addressable
- **Novel for Let's SOLVE It** — no past project combines environmental ML with health outcomes
- **Scalable output** — model can be applied to any Canadian city with NAPS coverage

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Aggregate-only health data (no individual patient records) | Frame as population-level prediction — useful for public health planning |
| Geographic mismatch between air stations and health regions | Focus on city with high NAPS density (Edmonton, Toronto) |
| Pollen data not freely available | Omit pollen; use seasonal dummies as proxy |
| Class imbalance if framed as binary | Use regression (hospitalization count) instead of classification |

---

## References

- Montreal Temperatures & Pediatric Asthma ED Visits (2024): https://link.springer.com/article/10.1007/s11869-024-01610-6
- Edmonton Air Pollution & Asthma ED Visits: https://ehjournal.biomedcentral.com/articles/10.1186/1476-069X-6-40
- CHILD Cohort ML Prediction (2024): https://www.nature.com/articles/s41390-023-02988-2
- CIHI Socio-economic Inequalities in Asthma: https://www.cihi.ca/en/socio-economic-inequalities-affect-asthma-hospitalization-rates-for-kids
- Asthma Canada 2024 National Survey: https://asthma.ca/wp-content/uploads/2024/11/2024-National-Asthma-Survey-Findings-_-Asthma-Canada.pdf
- NAPS Open Data: https://open.canada.ca/data/en/dataset/1b36a356-defd-4813-acea-47bc3abd859b
