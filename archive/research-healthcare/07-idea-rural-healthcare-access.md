# Idea #7: Predicting Healthcare Access Gaps in Rural and Remote Canada

**Acceptance Likelihood: 4.5/5 — Strong Pick**

---

## The Problem

Canada faces a healthcare access crisis that disproportionately impacts rural and remote communities. **6.5 million Canadians** lack a family doctor, and the gap between urban and rural healthcare access is widening despite universal healthcare coverage.

### Key Statistics
- **22,823 family physician shortage** (2025 Health Canada report)
- **6.5 million Canadians** (~16%) lack a family doctor
- Only **8-10% of physicians** practice in rural areas (home to 18-22% of population)
- Rural Canadians travel **>35 km to see a doctor** and **30 km to nearest hospital**
- **22.5% of Canadians** live >1 hour from a Level I/II trauma centre
- Manitoba rural EDs closed for **80,000 hours in 2023**
- **2024 was the worst year** for Ontario ER closures — 38 hospitals affected
- First Nations life expectancy: **8.9 years shorter (males)**, **9.6 years shorter (females)**
- First Nations adults: **>2x the risk** of dying from avoidable causes
- Canada has **2.8 physicians per 1,000** vs. OECD average of **3.7**

### Why It Matters
Identifying which communities face the greatest access gaps enables targeted resource deployment, telehealth expansion, and facility planning. A predictive model can inform policy before gaps become crises.

---

## Why Machine Learning Can Help

Healthcare access is determined by complex interactions between geography, demographics, facility distribution, workforce availability, and socioeconomic factors. ML can synthesize these into an interpretable access risk score per community.

### ML Task
**Classification/regression:** Predict healthcare access gap score per census subdivision (binary: underserved vs. adequate, or continuous access index).

### Proven Approaches
- **Rural hospital distress prediction:** AUC **0.87** on US data
- **Gradient Boosting for healthcare access prediction:** Highest accuracy in published studies
- **2SFCA (Two-Step Floating Catchment Area):** Standard method for spatial accessibility, enhanced with ML
- **Canadian COVID-19 study using GBT:** AUC **0.796**

---

## Datasets

### 1. Open Database of Healthcare Facilities (ODHF) — Primary
- **Source:** Statistics Canada
- **URL:** https://open.canada.ca/data/en/dataset/543fe07a-fd79-40e9-a829-ccd697526765
- **Size:** 7,033 facilities with names, addresses, lat/long, facility type
- **Format:** CSV (zipped)
- **Access:** Open Government Licence

### 2. Index of Remoteness (2021)
- **URL:** https://open.canada.ca/data/en/dataset/428c61da-5609-4766-9768-a3667c180db2
- **Contains:** Remoteness scores (0-1) for all populated census subdivisions
- **Format:** CSV
- **Access:** Open Government Licence

### 3. Census 2021 Profile
- **URL:** https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/details/download-telecharger.cfm?Lang=E
- **Contains:** Population, income, education, Indigenous identity, age distribution by CSD
- **Format:** CSV
- **Access:** Open

### 4. CIHI Physician Supply Data Tables
- **URL:** https://www.cihi.ca/en/access-data-and-reports/data-tables
- **Contains:** Physician counts by province/territory, specialty, physician-to-population ratios
- **Access:** Free download (ZIP)

### 5. Health Region Boundary Files (GIS)
- **URL:** https://open.canada.ca/data/en/dataset/af595f3f-9f8c-4f69-bbb5-f740f0299c06
- **Contains:** GIS shapefiles for health regions
- **Access:** Open

---

## Proposed ML Pipeline

```
1. Data acquisition & merging (Weeks 1-2)
   - Download ODHF, Remoteness Index, Census Profile, CIHI physician data
   - Merge on census subdivision (CSD) codes
   - Compute haversine distances between CSDs and nearest facilities

2. Feature engineering (Week 3)
   - Distance to nearest hospital, clinic, nursing facility
   - Physician-to-population ratio by health region
   - Remoteness index, population density
   - Demographics: % elderly, % Indigenous, median income, education
   - Number of facilities within 25km, 50km, 100km radius

3. Target variable construction
   - Composite access gap index from: remoteness + physician ratio
     + facility density + avoidable mortality (StatCan)
   - Validate against known underserved areas (ER closure data, news reports)

4. Model training (Weeks 4-6)
   - Random Forest, XGBoost, Gradient Boosting
   - SHAP for feature importance
   - Cross-validation with geographic stratification

5. Deliverable (Weeks 7-8)
   - Interactive heatmap of predicted access gaps across Canada
   - Feature importance showing what drives gaps
   - Policy recommendations for targeted intervention
```

---

## Strengths

- **All data freely downloadable CSV** — zero access barriers, no ethics approval
- **Manageable data size** — ~7,000 facilities, ~5,000 CSDs — fits on a laptop
- **Novel for Canadian ML** — first model fusing ODHF + Remoteness Index + Census
- **Compelling visual output** — geographic heatmap is presentation-ready
- **Strong equity angle** — Indigenous and rural disparities are central
- **Published precedent** — US/international studies show AUC 0.78-0.87 for similar tasks

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| No direct "healthcare access gap" label exists | Construct composite target from remoteness + physician ratio + facility density |
| CIHI physician data may be province-level, not CSD | Use ODHF facility density + CCHS health region data as proxy |
| Small number of "very remote" CSDs | Use remoteness as continuous variable, not binary |
| Geospatial feature engineering complexity | Use `geopandas` + `geopy`; 2SFCA has Python implementations |

---

## References

- CIHI: State of the Health Workforce in Canada, 2024: https://www.cihi.ca/en/the-state-of-the-health-workforce-in-canada-2024
- StatCan: Does Geography Matter in Mortality?: https://www150.statcan.gc.ca/n1/pub/82-003-x/2019005/article/00001-eng.htm
- ODHF Dataset: https://open.canada.ca/data/en/dataset/543fe07a-fd79-40e9-a829-ccd697526765
- Index of Remoteness: https://open.canada.ca/data/en/dataset/428c61da-5609-4766-9768-a3667c180db2
- CBC: Manitoba ER Closures 80,000 Hours: https://cbc.ca/amp/1.7172529
- 2SFCA Method — Montreal: https://pmc.ncbi.nlm.nih.gov/articles/PMC3142205/
- Rural Hospital Distress Prediction (AUC 0.87): https://pubmed.ncbi.nlm.nih.gov/27500663/
