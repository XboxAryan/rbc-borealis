# Idea #6: Predicting Surgical Wait Times and Healthcare Delays

**Acceptance Likelihood: 4.3/5 — Strong Pick**

---

## The Problem

Canada's surgical wait time crisis has reached alarming levels. The median wait from GP referral to treatment is **28.6 weeks** — more than triple the 9.3 weeks in 1993. Patients are dying while waiting for care.

### Key Statistics
- **28.6 weeks** median total wait (2025 Fraser Institute), **208% longer** than 1993
- **23,746 patients died** on healthcare waitlists in the most recent fiscal year — a **64% increase** over five years
- **937,000 fewer surgeries** performed during the first 31 months of the pandemic
- Neurosurgery: **49.9 weeks**; Orthopaedic surgery: **48.6 weeks**
- New Brunswick: **60.9 weeks** (longest); Ontario: **19.2 weeks** (shortest)
- MRI scans: **18.1 weeks** nationally (up to 52 weeks in PEI)
- Hip replacement within 6 months: only **68%** (below pre-pandemic)
- Hospital staff worked **26+ million overtime hours** in 2021-2022

### Why It Matters
Accurate wait time forecasting enables better scheduling, resource allocation, and policy intervention. Even modest improvements in prediction accuracy can reduce patient harm and save lives.

---

## Why Machine Learning Can Help

Wait times are driven by complex, interacting factors: patient volume, procedure type, staffing, seasonal patterns, and cascading backlog effects. ML models — particularly time series methods — can capture these dynamics.

### ML Task
**Dual approach:**
1. **Time series forecasting:** Predict future wait times by procedure type and province
2. **Classification:** Predict whether a procedure category will exceed benchmark wait times

### Proven Approaches
- **RF for outpatient scheduling:** **94.88% accuracy**; outperformed XGBoost (68%)
- **XGBoost for ED overcrowding:** AUROC **0.81**
- **ARIMA-ANN hybrid for surgical demand:** MAE 0.26-0.76 for 2-week forecasts
- **Ontario mental health RF:** Minimum RMSE for 4/8 clinics using deidentified data
- **SickKids Toronto:** ML predicts patient surges >1 week in advance using 3 years of historical data

---

## Datasets

### 1. CIHI Wait Times Data Tables (Primary)
- **URL:** https://www.cihi.ca/en/topics/access-and-wait-times/data-tables
- **Format:** XLSX, free download
- **Contains:** National/provincial/regional waits for hip/knee replacement, cataract, CABG, radiation therapy, hip fracture, 5 cancer surgeries, MRI, CT. Time series from 2008-2024.

### 2. BC Surgical Wait Times
- **URL:** https://open.canada.ca/data/en/dataset/7c1bf2a8-96bb-4ad5-888d-a90672eb306e
- **Format:** XLSX
- **Contains:** Quarterly data from 2009-2025, 50th/90th percentile waits by procedure

### 3. Nova Scotia Surgical Wait Times
- **URL:** https://data.novascotia.ca/Health-and-Wellness/Surgical-Wait-Times/wu5w-qxki
- **Format:** CSV
- **Contains:** Wait times by facility and procedure

### 4. Quebec ER Occupancy (Hourly)
- **URL:** https://open.canada.ca/data/en/dataset/d4541afe-9391-44bf-a78f-dae3c9cf1217
- **Format:** CSV, updated hourly
- **Contains:** Patients on stretchers, 24h+ and 48h+ stretcher patients, by facility

---

## Proposed ML Pipeline

```
1. Data acquisition (Weeks 1-2)
   - Download CIHI wait time tables (XLSX)
   - Download BC surgical wait times (2009-2025)
   - Download Nova Scotia CSV data
   - Parse, clean, harmonize across provinces

2. Feature engineering (Week 3)
   - Temporal: month, quarter, year, COVID period flag, seasonal indicators
   - Procedure type, province/region
   - Historical trends (lag features, rolling averages)
   - Optional: workforce data (CIHI physician counts) as features

3. Model training (Weeks 4-6)
   - Time series: ARIMA, Prophet
   - Classification: Random Forest, XGBoost
   - Target: benchmark exceedance (binary) and wait duration (regression)
   - Time-based cross-validation (no future leakage)

4. Evaluation & deliverable (Weeks 7-8)
   - MAE, RMSE for regression; AUC, F1 for classification
   - SHAP feature importance
   - Province-by-province comparison dashboard
```

---

## Strengths

- **Urgent national crisis** — 23,746 waitlist deaths provides compelling motivation
- **Multiple free, downloadable datasets** in XLSX/CSV format
- **Well-established ML methods** (ARIMA, RF, XGBoost) — standard undergrad toolkit
- **SickKids and Unity Health** provide real-world Canadian deployment examples
- **Ontario surgical backlog tool** has open-source code on GitHub

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Similar to past EDforecast project | Differentiate: surgical (not ED), multi-province, multi-procedure scope |
| Aggregate data lacks granularity | Frame as population-level forecasting (what policymakers need) |
| CIHI XLSX requires parsing | Straightforward with pandas `read_excel`; budget 1-2 days |
| Short time series for deep learning | Use ARIMA/Prophet as primary; LSTM as stretch goal |

---

## References

- Fraser Institute — Waiting Your Turn 2025: https://www.fraserinstitute.org/studies/waiting-your-turn-wait-times-for-health-care-in-canada-2025
- CIHI Wait Times 2025: https://www.cihi.ca/en/wait-times-for-priority-procedures-in-canada-2025
- 23,746 Waitlist Deaths: https://thehub.ca/2025/11/26/nearly-24000-canadian-patients-died-while-on-health-care-waitlists-in-canada-last-year-report/
- Ontario Surgical Backlog Tool (GitHub): https://github.com/wangjona/surgicalbacklog
- Ontario Mental Health Wait Time ML: https://mental.jmir.org/2022/8/e38428
- SickKids ED Prediction: https://healthydebate.ca/2020/03/topic/predicting-emergency-department-crowding-artificial-intelligence-mar2020/
