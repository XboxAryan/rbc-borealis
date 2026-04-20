# Idea #9: Predicting Maternal Health Complications in Canadian Pregnancies

**Acceptance Likelihood: 4.2/5 — Good Pick**

---

## The Problem

Canada's maternal health outcomes are deteriorating. The maternal mortality rate spiked to **17 per 100,000** in 2020 — and the country significantly undercounts maternal deaths. Indigenous women face **2x the risk** of dying during pregnancy.

### Key Statistics
- Maternal mortality rate: **12 per 100,000** (2023); spiked to **17 per 100,000** in 2020
- **45.8% of maternal deaths** are missed by the standard 42-day postpartum tracking window
- **1.6% of all Canadian deliveries** experience severe maternal morbidity (SMM)
- SMM rate **tripled** from 4.38/1,000 (1991-2001) to 13.8/1,000 (2003-2007)
- **Indigenous women 2x more likely** to die than non-Indigenous women
- **Inuit preterm birth rate: 11.4%** vs. ~8% national
- SIDS rates **7x higher** for Indigenous infants (2.0 vs. 0.3 per 1,000)
- Only **48% of Indigenous mothers** had a regular healthcare provider in 2020 (vs. 97% non-Indigenous)
- Women traveling >1 hour for maternity services have **7x greater stress**

### Why It Matters
Predicting which pregnancies are at risk enables proactive monitoring, earlier specialist referrals, and targeted support — particularly for underserved Indigenous and rural communities.

---

## Why Machine Learning Can Help

Pregnancy complications arise from interactions between maternal age, health history, vital signs, and social determinants. ML models can identify high-risk pregnancies from routinely collected data.

### ML Task
**Multi-class classification:** Classify maternal health risk as low/medium/high from clinical and demographic features.

### Proven Approaches
- **PIERS-ML (UBC/Canada, 8,843 patients, 11 countries):** AUC **0.80** for preeclampsia
- **XGBoost for gestational diabetes:** AUC **0.946**
- **RF on UCI Maternal Health dataset:** Accuracy **86%**; LightGBM **88%**
- **UBC-MDS student project:** Decision Tree test accuracy **0.823**, high-risk F1 **0.90**
- **Neural network for preeclampsia:** AUC **0.920**

---

## Datasets

### 1. UCI/Kaggle Maternal Health Risk Dataset (Primary — Immediate Access)
- **URL:** https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data
- **Also:** https://archive.ics.uci.edu/dataset/863/maternal+health+risk
- **Size:** 1,014 samples, 6 features + target
- **Features:** Age, SystolicBP, DiastolicBP, BloodSugar, BodyTemp, HeartRate
- **Target:** RiskLevel (low/mid/high)
- **Access:** Free download, CC BY 4.0

### 2. Open Canada — Maternal Deaths & Mortality Rates
- **URL:** https://open.canada.ca/data/en/dataset/e8df1678-57e8-4166-b721-fb172696483d
- **Contains:** Deaths by cause, mortality rates (time-series)
- **Format:** CSV
- **Access:** Free download

### 3. Open Canada — Pregnancy Outcomes
- **URL:** https://open.canada.ca/data/en/dataset/1367e3a6-02f1-496f-9c0f-d078dbdd58d0
- **Contains:** Live births, induced abortions, fetal loss by age group (1974-2005)
- **Access:** Free download (CSV/XML)

### 4. Alberta Maternal & Child Health Indicators
- **URL:** https://open.canada.ca/data/en/dataset/c66629da-35d1-435b-bef8-14c83fb71283
- **Contains:** Local geographic area maternal/child health indicators (2021-2024)
- **Access:** Free download (XLSX)

### 5. BORN Ontario Registry (Restricted — Future Work)
- **Size:** ~140,000 births/year; 1.6M+ total
- **Access:** Requires formal Data Access Request — not feasible for 2-month project

---

## Proposed ML Pipeline

```
1. Data acquisition (Weeks 1-2)
   - Download Kaggle/UCI Maternal Health Risk dataset (1,014 samples)
   - Download Open Canada aggregate datasets for Canadian context
   - EDA: class distribution, feature correlations, missing values

2. Model development (Weeks 3-4)
   - Baseline: Logistic Regression, Decision Tree
   - Primary: Random Forest, XGBoost, LightGBM
   - Handle class imbalance across 3 risk levels
   - Cross-validation: stratified k-fold

3. Explainability (Weeks 5-6)
   - SHAP values for feature importance
   - Map findings to Canadian maternal health disparities
   - Discuss what additional features (SES, geography) would improve model

4. Canadian context & write-up (Weeks 7-8)
   - Frame with Open Canada mortality/outcome statistics
   - Discuss Indigenous maternal health disparities
   - Cite UBC-MDS student project as precedent
   - Discuss limitations: Bangladesh dataset, need for BORN/CIHI data
```

---

## Strengths

- **Perfect equity alignment** — Indigenous maternal health disparities are central
- **UBC student project precedent** — demonstrates this exact approach works for undergrads
- **Published baselines (82-98% accuracy)** — achievable benchmarks
- **Free instant download** — no access barriers
- **Open Canada aggregate data** adds Canadian contextualization

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| UCI dataset is from Bangladesh, not Canada | Discuss transferability; use Open Canada data for Canadian framing |
| Only 1,014 samples — limited generalizability | Acknowledge limitation; discuss what BORN data could enable |
| Only 6 features — real clinical prediction uses 18+ | Discuss what additional features would improve the model |
| BORN Ontario requires formal application | Frame as "future work" beyond 2-month scope |

---

## References

- PIERS-ML Preeclampsia Prediction (Lancet Digital Health 2024): https://www.thelancet.com/journals/landig/article/PIIS2589-7500(23)00267-4/fulltext
- Ontario 20-Year Maternal Mortality Study (JOGC 2024): https://www.sciencedirect.com/science/article/pii/S1701216324005127
- Indigenous Maternal Health (Frontiers 2025): https://www.frontiersin.org/journals/global-womens-health/articles/10.3389/fgwh.2025.1513145/full
- UCI Maternal Health Risk Dataset: https://archive.ics.uci.edu/dataset/863/maternal+health+risk
- UBC-MDS Student Project: https://github.com/UBC-MDS/maternal_health_risk_predictor
- Ensemble ML for Maternal Health Risk (Nature SR 2024): https://www.nature.com/articles/s41598-024-71934-x
- CBC: Canada Undercounts Maternal Deaths: https://www.cbc.ca/news/canada/canada-maternal-deaths-undercount-1.6600905
