# Idea #4: Early Detection of Dementia Risk in Canadian Aging Population

**Acceptance Likelihood: 4.5/5 — Strong Pick**

---

## The Problem

Canada faces a dementia crisis that will triple in scale by 2050. Nearly **772,000 Canadians** are living with dementia today, with **414 new cases diagnosed every day**. The economic burden is staggering — and 45% of cases may be preventable.

### Key Statistics
- **771,939 people** in Canada living with dementia (January 2025)
- **$40 billion/year** total economic burden (2022); projected **$153 billion by 2038**
- Prevalence doubles every 5 years after 65: from <1% (65-69) to ~25% (85+)
- **By 2050:** >1.7 million Canadians with dementia; 685 new cases/day
- **45% of dementia** is attributable to 14 modifiable risk factors (Lancet 2024)
- Caregivers provide equivalent of **$7.3 billion** of unpaid care annually
- **Indigenous populations:** ~10,800 people affected; delayed diagnosis due to lack of geriatric specialists in remote communities
- Caregivers provide an average of **26 hours/week** (vs. 17 hours for non-dementia caregivers)

### Why It Matters
Early detection enables intervention on modifiable risk factors (physical inactivity, hypertension, diabetes, social isolation) before irreversible cognitive decline. ML can identify high-risk individuals years before clinical diagnosis.

---

## Why Machine Learning Can Help

Dementia risk involves complex interactions between lifestyle, clinical, social, and genetic factors. ML models capture these non-linear relationships and — critically — can provide explainable predictions that map directly to actionable risk factors.

### ML Task
**Binary classification:** Predict dementia diagnosis (yes/no) from clinical, demographic, and lifestyle features.

### Proven Approaches
- **Systematic review (21 studies, >1M participants):** Average AUC **0.845**
- **XGBoost on SHARE European survey:** AUC **0.96**, accuracy 87%
- **XGBoost on population-based cohort:** AUC **0.95** (2,080 validation)
- **Random Forest on OASIS-2:** AUC **0.94**, accuracy 94.4%
- **Canadian CLSA + Random Forest:** Modest improvement by adding resting heart rate to CAIDE model

---

## Datasets

### 1. Kaggle Alzheimer's Disease Dataset (Primary — Immediate Access)
- **URL:** https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset
- **Size:** 2,149 patients, 35 columns
- **Contains:** Age, BMI, smoking, alcohol, physical activity, diet, sleep, family history, diabetes, hypertension, depression, cholesterol, MMSE, functional assessment, ADL, diagnosis (binary)
- **Access:** Free download, no registration

### 2. OASIS-2 Longitudinal (Secondary — Registration Required)
- **URL:** https://www.kaggle.com/datasets/pulavendranselvaraj/oasis-dataset
- **Size:** 150 subjects, 373 sessions
- **Contains:** Age, sex, education, SES, MMSE, CDR, brain volume measures
- **Access:** Free with registration

### 3. CCHS PUMF (Canadian Context)
- **URL:** https://www150.statcan.gc.ca/n1/en/catalogue/82M0013X
- **Contains:** Chronic conditions, physical activity, smoking, alcohol, chronic conditions, healthcare use
- **Use:** Canadian-specific statistics to contextualize model findings

### 4. Canadian Longitudinal Study on Aging (CLSA) — Future Work
- **Size:** 51,338 participants aged 45-85, followed 20 years
- **Contains:** 8 cognitive tests, demographics, health, lifestyle
- **Access:** Requires application (~6 months processing) — infeasible for 2-month project

---

## Proposed ML Pipeline

```
1. Data & EDA (Weeks 1-2)
   - Download Kaggle AD dataset (2,149 patients, 34 features)
   - Optionally supplement with OASIS-2 for validation
   - EDA: class distribution (35.6% AD / 64.4% no-AD), correlations

2. Model development (Weeks 3-4)
   - Baseline: Logistic Regression
   - Primary: Random Forest, XGBoost
   - Handle class imbalance: SMOTE or class weighting
   - Feature selection: mutual information, recursive elimination
   - Cross-validation: stratified k-fold (k=5 or 10)

3. Explainability & Canadian context (Weeks 5-6)
   - SHAP for global and local feature importance
   - Map top features to 14 Lancet Commission modifiable risk factors
   - Discuss implications for Canadian healthcare policy

4. Evaluation & write-up (Weeks 7-8)
   - AUC-ROC, accuracy, precision, recall, F1, confusion matrix
   - Compare against published baselines (XGBoost AUC 0.88-0.95)
   - Discuss CLSA as future work for Canadian-specific validation
```

---

## Strengths

- **Nationally significant** — 772K affected, $40B/year, projected to triple
- **Published XGBoost AUC 0.88-0.96** — achievable benchmarks for comparison
- **SHAP analysis** maps predictions directly to actionable public health interventions
- **Lancet 2024 Commission** provides timely policy framework (14 modifiable risk factors)
- **Reproducible** — uses public data and standard ML libraries
- **Never done in past cohorts** — completely novel for Let's SOLVE It

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| CLSA data takes 6 months to access | Use Kaggle + OASIS datasets; frame CLSA as "future work" |
| Primary dataset is not Canadian-specific | Frame through Canadian statistics; discuss transferability |
| Class imbalance (35.6% / 64.4%) | SMOTE, class weights, stratified sampling |
| Overfitting on small dataset (n=2,149) | Cross-validation, regularization, ensemble methods |

---

## References

- Alzheimer Society of Canada — Dementia Numbers: https://alzheimer.ca/en/about-dementia/what-dementia/dementia-numbers-canada
- CIHI — Dementia in Canada Summary: https://www.cihi.ca/en/dementia-in-canada/dementia-in-canada-summary
- Lancet Commission 2024 — Dementia Prevention: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(24)01296-0/abstract
- Systematic Review: ML for Dementia (Springer 2023): https://link.springer.com/article/10.1007/s10916-023-01906-7
- CANCEA Economic Burden Report: https://www.cancea.ca/wp-content/uploads/2023/07/CANCEA-Economic-Impact-of-Dementia-in-Canada-2023-01-08.pdf
- Kaggle AD Dataset: https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset
