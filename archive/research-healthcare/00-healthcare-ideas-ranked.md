# Healthcare Project Ideas — Ranked by Acceptance Likelihood

Healthcare is the #1 accepted category in past Let's SOLVE It cohorts (7/23 projects, 30%). Past healthcare projects: ED wait times, radiology, stroke risk, anesthesia depth, liver transplant, glioblastoma, food bank forecasting.

Scoring: Each factor rated 1-5. Weighted composite determines rank.

---

## Ranking Summary

| Rank | Idea | Novelty | Data | Canadian Focus | ML Fit | Feasibility | Equity | **Score** |
|---|---|---|---|---|---|---|---|---|
| **1** | Adverse Drug Reactions | 5 | 5 | 5 | 5 | 5 | 4 | **4.8** |
| **2** | Type 2 Diabetes Risk | 5 | 5 | 5 | 5 | 4 | 5 | **4.8** |
| **3** | Pediatric Asthma & Environment | 5 | 5 | 5 | 5 | 4 | 5 | **4.8** |
| **4** | Dementia Early Detection | 5 | 4 | 5 | 5 | 4 | 4 | **4.5** |
| **5** | Hospital Readmissions | 4 | 5 | 4 | 5 | 5 | 3 | **4.3** |
| **6** | Surgical Wait Times | 4 | 5 | 5 | 5 | 4 | 3 | **4.3** |
| **7** | Rural Healthcare Access | 5 | 5 | 5 | 4 | 4 | 5 | **4.5** |
| **8** | Antimicrobial Resistance | 5 | 4 | 5 | 5 | 3 | 3 | **4.2** |
| **9** | Maternal Health Complications | 5 | 3 | 4 | 5 | 3 | 5 | **4.2** |
| **10** | Mental Health Crisis Demand | 4 | 3 | 5 | 4 | 3 | 4 | **3.8** |

---

## 1. Predicting Adverse Drug Reactions from Canadian Pharmacovigilance Data

**Problem:** ADRs are Canada's 4th leading cause of death — 10,000-22,000 deaths/year, 200,000 severe cases, $13.7-17.7B cost. Only 1-10% of ADRs are reported.

**ML Approach:** Signal detection + classification of ADR seriousness from Canada Vigilance database (1965-2025, fully open). XGBoost/RF on drug-patient features.

**Key Data:** Canada Vigilance (Open Canada, 60+ years), Drug Product Database (47K products, open), FAERS (millions, open).

**Why #1:** Fully open Canadian dataset, 60 years of data, no ethics approval needed. Published baselines (AUC ~0.77). Genuinely underused for ML. Practical 2-month scope.

**Deep dive:** `01-idea-adverse-drug-reactions.md`

---

## 2. Predicting Type 2 Diabetes Risk in Canadian Communities

**Problem:** 3.7M Canadians with diabetes (9.4%). First Nations 3.4x higher prevalence. $27B cost in 2018, projected $39B by 2028.

**ML Approach:** XGBoost/RF classification on CCHS PUMF (~130K respondents). Social determinants + behavioral features predict diabetes status.

**Key Data:** CCHS PUMF (free via Borealis/StatCan), Open Canada diabetes aggregate data, CDC BRFSS (253K records, Kaggle).

**Why #2:** Canadian-specific ML gap. XGBoost AUC 0.92 achieved in Canadian CPCSSN study. Strong equity angle (income/Indigenous disparities).

**Deep dive:** `02-idea-diabetes-risk.md`

---

## 3. Predicting Pediatric Asthma Exacerbations from Environmental Factors

**Problem:** 10% of Canadian children have asthma. 1.5x higher hospitalization in low-income areas. First Nations 2x more likely to be hospitalized. Montreal study: 37% increase in ED visits with higher temperatures.

**ML Approach:** RF/XGBoost regression predicting aggregate asthma hospitalization counts from air quality (PM2.5, O3, NO2), weather, and socioeconomic features.

**Key Data:** NAPS air quality (260 stations, CSV, open), AQHI (open JSON/CSV), ECCC weather (open), CCDSS asthma surveillance (open).

**Why #3:** Entirely open data pipeline. Published RF AUC 0.856 with environmental factors. Climate change framing is timely. Strong equity lens (income quintile stratification).

**Deep dive:** `03-idea-pediatric-asthma.md`

---

## 4. Early Detection of Dementia Risk in Canadian Aging Population

**Problem:** 771,939 Canadians with dementia (2025). 414 new cases/day. $40B annual cost. 45% potentially preventable (Lancet 2024). Projected to triple by 2050.

**ML Approach:** XGBoost/RF on tabular clinical + lifestyle features. SHAP for explainability mapping to 14 Lancet modifiable risk factors.

**Key Data:** Kaggle AD dataset (2,149 patients, 34 features, free), OASIS-2 (free), CCHS PUMF for Canadian context.

**Why #4:** Massive Canadian public health crisis. Published XGBoost AUC 0.88-0.96. SHAP analysis maps to actionable prevention policies.

**Deep dive:** `04-idea-dementia-detection.md`

---

## 5. Predicting 30-Day Hospital Readmissions

**Problem:** ~200K unplanned readmissions/year in Canada. $1.8-2.9B cost. ~9.1% national rate. Heart failure and COPD: ~20% readmission rate.

**ML Approach:** XGBoost/RF classification on patient demographics, diagnoses, medications, lab results. SHAP for clinical interpretability.

**Key Data:** UCI Diabetes 130-Hospitals (101K records, free), MIMIC-III/IV (free with application). Canadian CIHI DAD restricted.

**Why #5:** Well-established problem with strong benchmarks (AUC 0.65-0.94). Multiple GitHub reference implementations. Good for demonstrating end-to-end ML pipeline.

**Deep dive:** `05-idea-hospital-readmissions.md`

---

## 6. Predicting Surgical Wait Times and Healthcare Delays

**Problem:** 28.6-week median wait (2025). 23,746 patients died on waitlists last year. 937,000 fewer surgeries during COVID. New Brunswick: 60.9 weeks.

**ML Approach:** Time series forecasting (ARIMA/Prophet/LSTM) + classification (RF/XGBoost) predicting benchmark exceedance by procedure/province.

**Key Data:** CIHI wait time tables (XLSX, free), BC surgical waits (2009-2025, open), Nova Scotia surgical waits (CSV, open), Quebec ER hourly (CSV, open).

**Why #6:** Urgent Canadian crisis. Multiple free datasets. Similar to past ED wait time project but broader scope.

**Risk:** Similar enough to past EDforecast project that reviewers might see overlap.

**Deep dive:** `06-idea-surgical-wait-times.md`

---

## 7. Predicting Healthcare Access Gaps in Rural Canada

**Problem:** 6.5M Canadians without a family doctor. Only 8-10% of physicians in rural areas (18-22% of population). 80,000 hours of Manitoba ER closures in 2023.

**ML Approach:** XGBoost/RF classification predicting underserved communities from remoteness, facility density, demographics. Geospatial features.

**Key Data:** ODHF (7,033 facilities with lat/long, open), Index of Remoteness (open), Census 2021 (open), CIHI physician tables (free).

**Why #7:** Novel geospatial ML approach. All data freely downloadable CSV. Strong equity angle (Indigenous, rural). Compelling map output.

**Deep dive:** `07-idea-rural-healthcare-access.md`

---

## 8. Predicting Antimicrobial Resistance Patterns

**Problem:** 14,000 AMR-associated deaths/year in Canada. $1.4B direct healthcare costs. VRE increased 23.3%. Projected: 13,700 deaths/year by 2050, $388B cumulative GDP loss.

**ML Approach:** XGBoost/RF on susceptibility testing data predicting resistance for pathogen-antibiotic pairs. Signal detection via disproportionality analysis.

**Key Data:** AMRNet (CSV, open), Pfizer ATLAS via Vivli (6.5M MICs, open by request), CARD (McMaster, open).

**Why #8:** Strong Canadian institutional backing (PHAC, McMaster CARD). Published AUC 0.74-0.96. Underused Canadian AMRNet data.

**Risk:** Microbiology domain knowledge needed. May be harder to scope for non-biology undergrads.

**Deep dive:** `08-idea-antimicrobial-resistance.md`

---

## 9. Predicting Maternal Health Complications

**Problem:** Canada's maternal mortality rate spiked to 17/100K in 2020. Indigenous women 2x more likely to die. SMM rate tripled since 1991. 45.8% of deaths missed by standard tracking.

**ML Approach:** Classification of risk levels (low/mid/high) using vital signs and demographics. XGBoost/RF with SHAP.

**Key Data:** UCI/Kaggle Maternal Health Risk (1,014 samples, free), Open Canada maternal deaths time-series (free). BORN Ontario restricted.

**Why #9:** Perfect equity alignment. Published baselines (accuracy 82-98%). UBC student project precedent exists.

**Risk:** Primary dataset is from Bangladesh, not Canada. Canadian-specific data (BORN) requires restricted access. Small dataset (1,014 samples).

**Deep dive:** `09-idea-maternal-health.md`

---

## 10. Predicting Mental Health Crisis Demand

**Problem:** 4,735 suicide deaths in Canada (2023). 988 crisis line. 44.5% of students battle severe depression. Wait times for mental health services: 30+ weeks.

**ML Approach:** XGBoost/RF classification predicting crisis demand from CCHS mental health module + demographic + seasonal features.

**Key Data:** CCHS PUMF (mental health module), CIHI data tables (aggregate). Individual-level crisis data is restricted.

**Why #10:** Urgent issue but similar to past MindTech chatbot project. Data access is the main barrier — individual crisis records are highly restricted.

**Risk:** Overdone territory (MindTech, Crisis Companion in past cohorts). Limited open data for ML.

**Deep dive:** Not included (insufficient differentiation from past projects).

---

## Recommendation

**Primary proposal (healthcare):** #1 (Adverse Drug Reactions) or #2 (Diabetes Risk) — both have fully open Canadian datasets, published ML baselines, strong equity angles, and clear 2-month feasibility.

**Secondary proposal (healthcare):** #3 (Pediatric Asthma) — entirely different domain, excellent open data pipeline, climate change framing, novel Canadian angle.

**Best overall from original research:** #1 from original ranking (Indigenous Water Quality) remains the strongest non-healthcare pick.
