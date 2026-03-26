# Idea #5: Predicting 30-Day Hospital Readmissions

**Acceptance Likelihood: 4.3/5 — Strong Pick**

---

## The Problem

Unplanned hospital readmissions cost Canada's healthcare system **$1.8-2.9 billion annually** and represent a significant quality-of-care indicator. Nearly **10% of hospitalized Canadians** are readmitted within 30 days.

### Key Statistics
- **~200,000** Canadians experience unplanned readmissions annually
- National 30-day readmission rate: **~9.1%** across all patient groups
- **Heart failure and COPD:** ~20% readmission rate (top 2 causes)
- **25% of readmissions** are estimated to be preventable
- **23,746 patients died on waitlists** in the most recent fiscal year — readmissions compound this burden
- Provincial variation: BC 9.7%, Ontario 9.2%, Nova Scotia 8.5%
- COVID backlog: **937,000 fewer surgeries** in first 31 pandemic months

### Why It Matters
Predicting which patients will be readmitted enables targeted discharge planning, follow-up care, and resource allocation — preventing avoidable suffering and freeing hospital capacity.

---

## Why Machine Learning Can Help

Readmission risk depends on complex interactions between clinical factors (diagnosis, comorbidities, lab values), medication patterns, and socioeconomic determinants. ML outperforms traditional scoring systems like LACE.

### ML Task
**Binary classification:** Predict whether a patient will be readmitted within 30 days of discharge.

### Proven Approaches
- **Alberta population-level GBM (428K patients):** AUC **0.83** (vs. LACE AUC 0.655)
- **RF on UCI Diabetes dataset:** AUC **0.94**
- **XGBoost for HF readmission with SHAP:** AUC **0.763**
- **Scoping review (43 studies):** Median AUC **0.68** (IQR 0.64-0.76)

---

## Datasets

### 1. UCI Diabetes 130-Hospitals Dataset (Primary — Immediate Access)
- **URL:** https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008
- **Size:** 101,766 encounters, 50+ features
- **Contains:** Demographics, lab results, medications (23 drug features), diagnoses, prior utilization, readmission outcome
- **Access:** Fully open, free download
- **Also on:** https://www.kaggle.com/datasets/vanpatangan/readmission-dataset

### 2. MIMIC-III/IV (Secondary — Application Required)
- **URL:** https://mimic.physionet.org/
- **Size:** ~40,000 ICU patients (MIMIC-III); expanded in MIMIC-IV
- **Contains:** Demographics, vital signs, lab results, medications, clinical notes
- **Access:** Free but requires PhysioNet application + CITI training (1-2 weeks)

### 3. CIHI DAD (Canadian — Restricted)
- **URL:** https://www.cihi.ca/en/discharge-abstract-database-dad-metadata
- **Contains:** National hospital discharge data with ICD-10 coding
- **Access:** Restricted; requires formal CIHI data request. Not feasible for 2-month project.
- **Use:** Reference for Canadian context and statistics only

---

## Proposed ML Pipeline

```
1. Data acquisition & cleaning (Weeks 1-2)
   - Download UCI Diabetes dataset (101K records)
   - Handle missing values (substantial missingness in some features)
   - Encode categorical variables (medications, diagnoses)
   - Address class imbalance (~11% readmission rate)

2. Feature engineering (Week 3)
   - Number of lab procedures, medications, diagnoses
   - Prior utilization features (ER visits, inpatient days)
   - Drug interaction indicators
   - Age/comorbidity interaction features

3. Model training (Weeks 4-5)
   - Logistic Regression (interpretable baseline)
   - Random Forest, XGBoost, LightGBM
   - SMOTE/ADASYN for class imbalance
   - Stratified 5-fold cross-validation

4. Explainability (Week 6-7)
   - SHAP values for global and local feature importance
   - Patient-level explanations (why this patient is high-risk)
   - Error analysis: where does the model fail?

5. Canadian context & write-up (Week 8)
   - Frame with CIHI Canadian readmission statistics
   - Compare against LACE score baseline
   - Discuss policy implications (no readmission penalties in Canada, unlike US)
```

---

## Strengths

- **Well-established problem** with extensive literature and benchmarks
- **101K records immediately available** — no access barriers
- **Multiple GitHub reference implementations** for comparison
- **Alberta GBM study (AUC 0.83)** provides strong Canadian ML benchmark
- **SHAP/LIME analysis** elevates beyond standard classification exercise
- **Policy discussion angle** — Canada lacks US-style readmission penalties

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Dataset is US-based, not Canadian | Frame with Canadian CIHI statistics; discuss transferability |
| Low AUC for general readmission (~0.68 median) | Focus on feature engineering; disease-specific models perform better |
| Similar to past shelter forecasting projects | Differentiate via healthcare/clinical focus and SHAP explainability |
| Class imbalance (~11% positive) | Pre-plan SMOTE/ADASYN from Week 3 |

---

## References

- CIHI: All Patients Readmitted to Hospital: https://www.cihi.ca/en/indicators/all-patients-readmitted-to-hospital
- Alberta Population-Level Study (AUC 0.83): https://pmc.ncbi.nlm.nih.gov/articles/PMC9700920/
- UBC Heart Disease Study: https://pmc.ncbi.nlm.nih.gov/articles/PMC10257109/
- Scoping Review (43 studies): https://pmc.ncbi.nlm.nih.gov/articles/PMC8101040/
- UCI Dataset: https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008
- GitHub Reference Implementation: https://github.com/moggirain/Hospital_readmission_prediction
