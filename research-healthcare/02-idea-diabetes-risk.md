# Idea #2: Predicting Type 2 Diabetes Risk in Canadian Communities

**Acceptance Likelihood: 4.8/5 — Top Healthcare Pick**

---

## The Problem

Type 2 diabetes affects **3.7 million Canadians** (9.4% of population) and costs the healthcare system an estimated **$27 billion annually**, projected to exceed **$39 billion by 2028**.

### Key Statistics
- First Nations on-reserve prevalence: **17.2%** (3.4x higher than general population)
- Lifetime diabetes risk for First Nations: **80%** vs. 50% non-First Nations
- Prevalence is **2.1x higher** in lowest income group vs. highest
- **7x more** lower limb amputations in Indigenous populations
- **22.5% of adults** meeting diagnostic criteria are unaware they have diabetes
- Prediabetes affects **6.3%** of Canadian adults aged 20-79

### Why It Matters
Early identification of high-risk individuals enables preventive intervention before irreversible complications. Existing screening tools (CANRISK) use simple questionnaires — ML can incorporate richer social determinant data for better prediction.

---

## Why Machine Learning Can Help

Diabetes risk follows patterns across demographics, lifestyle, and socioeconomic factors that ML excels at detecting — particularly non-linear interactions between income, ethnicity, geography, and health behaviors.

### ML Task
**Binary classification:** Predict diabetes status (yes/no) from behavioral, demographic, and socioeconomic features.

### Proven Approaches (Canadian Studies)
- **XGBoost on CPCSSN data (8,602 records):** AUC **0.92** — top features: HbA1c, LDL, hypertension meds, HDL, BMI
- **SVM on Toronto neighbourhood data (CCHS + Census):** AUC **0.96** (test), **0.95** (external validation)
- **DNN for prediabetes prediction:** AUC **0.71** — best recall (60%)
- **DPoRT model on CCHS (85,706 respondents):** C-statistic **0.77** for diabetes inequities by income/education

---

## Datasets

### 1. Canadian Community Health Survey (CCHS) PUMF — Primary
- **Source:** Statistics Canada
- **URL:** https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/ZVCGBK
- **Size:** ~130,000 respondents per 2-year cycle; 1M+ across harmonized cycles
- **Contains:** Diabetes status, BMI, physical activity, smoking, alcohol, blood pressure, income, education, ethnicity, food security, chronic conditions
- **Format:** CSV, SAS, SPSS
- **Access:** Statistics Canada Open License via Borealis
- **Tool:** `cchsflow` R package harmonizes 160+ variables across cycles

### 2. Open Canada — Diabetes Aggregate Data
- **URL:** https://open.canada.ca/data/en/dataset/c55e9690-bfa6-47c7-b742-6775bd988fb8
- **Contains:** Prevalence by province, age group, sex; time series
- **Access:** Free download (CSV/XML)

### 3. CDC BRFSS Diabetes Health Indicators (Fallback)
- **URL:** https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset
- **Size:** 253,680 records, 21 features
- **Access:** Free download
- **Use:** Guaranteed-access alternative if CCHS PUMF takes time

---

## Proposed ML Pipeline

```
1. Data acquisition
   - Download CCHS PUMF via Borealis (or use cchsflow R package)
   - If CCHS delayed: start with BRFSS Kaggle dataset, apply to CCHS in parallel

2. Feature engineering
   - BMI categories, income quintiles, age groups
   - Social determinants: food security, education, housing
   - Interaction features: income x ethnicity, geography x age

3. Model training
   - Logistic Regression (baseline, compare against CANRISK)
   - Random Forest, XGBoost, SVM
   - Handle class imbalance: SMOTE, stratified sampling
   - Cross-validation: 5-fold stratified

4. Evaluation
   - AUC-ROC, precision, recall, F1
   - SHAP feature importance
   - Subgroup analysis: by income quintile, province, Indigenous status

5. Deliverable
   - Risk prediction model with SHAP explainability
   - Comparison against CANRISK baseline
   - Provincial/regional disparity analysis
```

---

## Strengths

- **Canadian-specific ML gap** — most studies use US or international data; CCHS angle is novel
- **Strong equity angle** — income and Indigenous disparities directly measurable
- **Government dataset** via Open License — no ethics approval barriers
- **Published Canadian ML precedent** — XGBoost AUC 0.92, SVM AUC 0.96 validate feasibility
- **CANRISK comparison** — built-in baseline from PHAC's validated Canadian risk tool
- **1M+ respondents** via cchsflow — substantial sample size for robust models

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| CCHS PUMF access may take weeks | Start with BRFSS Kaggle dataset; apply for PUMF immediately |
| CCHS lacks clinical biomarkers (no HbA1c) | Frame as population-level screening using behavioral/demographic factors |
| Class imbalance (~8-10% prevalence) | SMOTE, stratified sampling, AUC/F1 metrics instead of accuracy |
| Indigenous data sensitivity | Focus on income/geography disparities; follow OCAP principles |

---

## References

- Snapshot of Diabetes in Canada, 2023 (PHAC): https://www.canada.ca/en/public-health/services/publications/diseases-conditions/snapshot-diabetes-canada-2023.html
- Predicting Diabetes in Canadian Adults (medRxiv 2024): https://www.medrxiv.org/content/10.1101/2024.02.03.24302302v1.full
- Neighbourhood-Level Diabetes Drivers, Toronto (medRxiv 2025): https://www.medrxiv.org/content/10.1101/2025.02.28.25323125v1.full
- CCHS PUMF via Borealis: https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/ZVCGBK
- cchsflow R Package: https://github.com/Big-Life-Lab/cchsflow
- CANRISK Tool: https://www.healthycanadians.gc.ca/en/canrisk
