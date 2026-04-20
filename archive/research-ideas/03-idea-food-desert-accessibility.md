# Idea #2: Mapping and Predicting Food Deserts in Canadian Cities

**Acceptance Likelihood: 4.7/5 — Strong Pick**

---

## The Problem

Food deserts are areas where residents have poor geographic access to grocery stores and fresh food. In Canada, this disproportionately affects low-income, elderly, immigrant, and disabled populations.

### Key Statistics
- **62%** of families in subsidized housing are food insecure (StatCan)
- **48%** of female lone-parent families are food insecure
- **48%** of Indigenous families are food insecure
- **60%** of families where major income earner is unemployed are food insecure
- Urban food deserts defined as residences **>1 km** from a food store
- Rural food deserts defined as residences **>16 km** from a food store
- Food insecurity rates have risen significantly post-COVID with grocery inflation

### Why It Matters
People in food deserts rely on convenience stores with limited, expensive, and unhealthy options. This directly contributes to diet-related diseases (diabetes, heart disease, obesity) and deepens poverty cycles. Identifying and predicting food deserts enables cities to make informed decisions about zoning, transit, and food program placement.

---

## Why Machine Learning Can Help

Food desert formation is driven by observable socioeconomic and geographic patterns:

- **Income levels** (strongest predictor per CHAID analysis)
- **Population density and demographics** (age, immigration status)
- **Retail store density and type**
- **Transit accessibility scores**
- **Housing type and tenure** (owned vs. rented)
- **Neighborhood deprivation indices**

ML can identify at-risk neighborhoods before they become full food deserts, and classify existing areas by severity.

### ML Tasks
1. **Clustering:** K-medians to identify food environment typologies across 56,589 Canadian dissemination areas
2. **Classification:** Decision tree / Random Forest to predict food desert status from socioeconomic features
3. **Spatial analysis:** Map predictions to identify intervention priorities

### Published Approaches
- **CHAID decision trees:** Successfully identified income as key predictor of food desert status
- **K-medians clustering:** Can-FED dataset used this to create categorical food environment variables
- **Logistic regression:** Used in Mississauga study to identify socioeconomic indicators of food deserts

---

## Datasets

### 1. StatCan Food Desert Indices (Primary)
- **Source:** Statistics Canada via Open Canada Portal
- **URL:** https://open.canada.ca/data/en/dataset/c69d8357-061a-4122-b8b9-51bcbc786aa7
- **Contains:** Geographic food desert indices, accessibility scores to food shops (grocery stores, supermarkets, public markets)
- **Coverage:** Quebec-focused but methodology applicable nationally
- **Format:** GeoJSON, downloadable

### 2. Can-FED Pan-Canadian Food Environment Dataset
- **Source:** Statistics Canada Business Register
- **URL:** https://www150.statcan.gc.ca/n1/pub/82-003-x/2022002/article/00001-eng.htm
- **Contains:** Retail food environment measures for 56,589 dissemination areas across all of Canada
- **Features:** Network buffer distances to food retailers, food environment typology classifications
- **Format:** Academic dataset — may need to request access

### 3. StatCan Food Insecurity Survey Data
- **Source:** Canadian Income Survey / Household Food Security Survey Module
- **URL:** https://www150.statcan.gc.ca/n1/pub/75-006-x/2023001/article/00013-eng.htm
- **Contains:** Food insecurity rates by demographic group, province, income level
- **Use:** Ground truth for validation and impact framing

---

## Proposed ML Pipeline

```
1. Data collection & integration
   - Download food desert indices from Open Canada
   - Obtain or reconstruct Can-FED measures
   - Merge with Census demographic data (income, age, immigration status)

2. Exploratory analysis
   - Spatial visualization of food deserts across Canadian cities
   - Correlation between deprivation indices and food access
   - Comparison across provinces/CMAs

3. Model training
   - K-medians clustering to identify food environment typologies
   - Random Forest classifier to predict food desert status
   - CHAID decision tree for interpretable policy recommendations
   - Feature importance analysis

4. Evaluation
   - Classification accuracy, precision, recall
   - Spatial validation (does the model identify known food deserts?)
   - Cross-city generalization testing

5. Deliverable
   - Interactive map of Canadian food deserts with risk scores
   - Feature importance dashboard (what drives food deserts?)
   - Policy recommendation report for city planners
```

---

## Strengths

- **Purpose-built government dataset:** StatCan created this data specifically for food desert analysis
- **Pan-Canadian scope:** Can-FED covers all 56,589 dissemination areas in Canada
- **Novel for Let's SOLVE It:** Food deserts never explored in past cohorts (food bank forecasting is different)
- **Strong equity angle:** Disproportionately affects low-income, Indigenous, immigrant, elderly populations
- **Actionable output:** Maps and risk scores directly useful for city planning and food program placement
- **Clear ML task:** Clustering + classification with clean tabular data — very feasible for undergrads

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Can-FED may require academic access | Use Open Canada food desert indices as primary. Supplement with Census data. |
| More analysis than prediction | Frame as predicting emerging food deserts — which neighborhoods are one store closure away? |
| Quebec-focused primary dataset | Acknowledge limitation. Propose national extension as future work. |
| Data is point-in-time | Use multiple Census years to create temporal dimension for prediction |

---

## References

- Open Canada Portal: "Indices of food desert and accessibility to food shops" — https://open.canada.ca/data/en/dataset/c69d8357-061a-4122-b8b9-51bcbc786aa7
- StatCan (2022): "A pan-Canadian dataset of neighbourhood retail food environment measures" — https://www150.statcan.gc.ca/n1/pub/82-003-x/2022002/article/00001-eng.htm
- MDPI (2025): "Identifying Food Deserts in Mississauga" — https://www.mdpi.com/2413-8851/9/7/265
- StatCan (2023): "Food insecurity among Canadian families" — https://www150.statcan.gc.ca/n1/pub/75-006-x/2023001/article/00013-eng.htm
