# Idea #8: Predicting Antimicrobial Resistance Patterns in Canadian Healthcare

**Acceptance Likelihood: 4.2/5 — Good Pick**

---

## The Problem

Antimicrobial resistance (AMR) is one of the top global health threats, and Canada is not immune. **14,000 deaths** are associated with resistant infections in Canada annually, with catastrophic economic projections if resistance continues rising.

### Key Statistics
- **26% of bacterial infections** in Canada are resistant to first-line treatment (2018 baseline)
- **14,000 deaths/year** associated with AMR; **5,400 directly attributable**
- **$1.4 billion** in direct healthcare costs; **$2 billion** in lost GDP
- **By 2050:** 13,700 deaths/year; $388 billion cumulative GDP loss; $120 billion cumulative healthcare costs
- VRE (vancomycin-resistant enterococcus) increased **23.3%** from 2019-2023
- CPE (carbapenemase-producing Enterobacterales) **doubled** 2019-2023
- **84.2% of CPE** cases are domestically acquired
- Data from **109 sentinel hospitals**, ~1.14 million admissions and ~8.9 million patient days in 2023

### Why It Matters
Predicting which pathogens will become resistant — and where — enables targeted antibiotic stewardship, hospital infection control, and public health resource allocation.

---

## Why Machine Learning Can Help

Resistance patterns are influenced by pathogen genetics, antibiotic usage, geography, and healthcare setting. ML can predict resistance probability for specific pathogen-antibiotic combinations from clinical and epidemiological features.

### ML Task
**Classification:** Predict resistant vs. susceptible for a given pathogen-antibiotic pair using patient demographics, geography, specimen type, and temporal trends.

### Proven Approaches
- **XGBoost on surveillance data:** AUC **0.95-0.96**
- **S. aureus WGS classifiers:** AUC **0.93-0.9995**
- **Deep learning from EHR (MRSA):** AUC **0.911** internal, **0.859** external
- **MALDI-TOF + LightGBM (DRIAMS):** AUC **0.74-0.80**
- **McMaster CARD database** now includes ML support for 413 pathogens

---

## Datasets

### 1. AMRNet Clinical Data (Primary — Open Canadian)
- **Source:** Public Health Agency of Canada
- **URL:** https://health-infobase.canada.ca/amrnet/clinical-data.html
- **Contains:** Susceptibility testing from blood/urine, 2020-2024, 8 provinces/territories
- **Format:** CSV
- **Access:** Open download

### 2. Pfizer ATLAS via Vivli AMR Register
- **URL:** https://amr.vivli.org/
- **Size:** 6.5M MICs, 633K patients, 70 countries (2004-2017)
- **Contains:** Raw MICs with patient metadata
- **Access:** Open by request (short review period); Excel download (121MB)

### 3. CARD — Comprehensive Antibiotic Resistance Database (McMaster)
- **URL:** https://card.mcmaster.ca/download
- **Contains:** 6,442 reference sequences, 4,480 SNPs, 5,057 AMR detection models
- **Access:** Open (CC-BY 4.0 for ontology)

### 4. Kaggle AMR Dataset
- **URL:** https://www.kaggle.com/datasets/amritpal333/antimicrobial-resistance-data
- **Contains:** Tabular susceptibility data across multiple pathogens
- **Access:** Free download

---

## Proposed ML Pipeline

```
1. Data acquisition (Weeks 1-2)
   - Download AMRNet CSV (Canadian clinical data)
   - Request ATLAS dataset via Vivli (short review period)
   - Download Kaggle AMR dataset as fallback

2. EDA & feature engineering (Week 3)
   - Pathogen-antibiotic pair analysis
   - Patient demographics, specimen type, geography
   - Temporal trends in resistance rates
   - Class imbalance characterization

3. Model training (Weeks 4-6)
   - Logistic Regression (baseline)
   - Random Forest, XGBoost, LightGBM
   - Handle class imbalance: SMOTE, class weights
   - Cross-validation with temporal splits

4. Canadian-specific analysis (Week 7)
   - Filter ATLAS to Canadian isolates
   - Compare Canadian vs. global resistance patterns
   - Feature importance via SHAP

5. Report & deliverable (Week 8)
   - Resistance prediction model with Canadian framing
   - SHAP analysis of risk factors
   - Policy implications for antibiotic stewardship
```

---

## Strengths

- **Strong Canadian institutional backing** — PHAC (AMRNet), McMaster (CARD)
- **Published AUC 0.74-0.96** provides achievable benchmark range
- **AMRNet CSV is openly downloadable** — genuine Canadian data
- **$388 billion projected GDP impact** makes economic case compelling
- **McMaster CARD** is a world-leading Canadian AMR resource
- **PLOS tutorial** for AMR ML was explicitly designed for undergraduates

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Microbiology domain knowledge needed | Follow PLOS Comp Bio tutorial (designed for undergrads) |
| AMRNet data may be limited in scope | Supplement with ATLAS (6.5M records) filtered to Canada |
| Class imbalance (most isolates susceptible) | SMOTE, class weights, AUC/F1 metrics |
| Complex data preprocessing | Start with Kaggle dataset for prototyping |

---

## References

- CARSS 2025 Key Findings: https://www.canada.ca/en/public-health/services/publications/drugs-health-products/canadian-antimicrobial-resistance-surveillance-system-2025-key-findings.html
- When Antibiotics Fail (CCA): https://cca-reports.ca/reports/the-potential-socio-economic-impacts-of-antimicrobial-resistance-in-canada/
- AMRNet Clinical Data: https://health-infobase.canada.ca/amrnet/clinical-data.html
- CARD Database: https://card.mcmaster.ca/
- Vivli AMR Register: https://amr.vivli.org/
- PLOS Tutorial — ML for AMR: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012579
- AMR Prediction (Nature Sci Reports 2025): https://www.nature.com/articles/s41598-025-14078-w
