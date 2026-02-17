# Idea #1: Predicting Adverse Drug Reactions from Canadian Pharmacovigilance Data

**Acceptance Likelihood: 4.8/5 — Top Healthcare Pick**

---

## The Problem

Adverse drug reactions (ADRs) are Canada's **4th leading cause of death**, killing between **10,000 and 22,000 Canadians per year**. An estimated 200,000 severe ADRs occur annually, costing the healthcare system **$13.7-17.7 billion**.

### Key Statistics
- **27% of Canadian seniors** take 5+ medications regularly (polypharmacy)
- **12% of seniors on 5+ meds** experienced a side effect requiring medical attention
- Only **1-10% of ADRs** are actually reported to regulators — the true burden is 10-100x larger
- ADR-related hospitalization costs: **$7,528 per case** (Ontario ICES study)
- **5% of all hospital admissions** are attributed to ADRs internationally

### Why It Matters
Most ADRs follow predictable patterns based on patient demographics, drug combinations, and clinical context. ML can detect safety signals faster than traditional surveillance, potentially preventing thousands of deaths annually.

---

## Why Machine Learning Can Help

The Canada Vigilance database contains 60+ years of ADR reports with structured data on drugs, reactions, patient demographics, and outcomes. Traditional pharmacovigilance uses statistical disproportionality measures (PRR, ROR) that ML can significantly outperform.

### ML Task
**Two-stage approach:**
1. **Signal detection:** Identify drug-reaction pairs reported more frequently than expected (classification)
2. **Outcome prediction:** Predict ADR seriousness (hospitalization, death, disability) from patient/drug features

### Proven Approaches
- **Meta-analysis of 54 studies:** Average AUC 76.68%, with ANN/GBM/CatBoost/XGBoost all achieving >80%
- **Random Forest:** Most frequently used algorithm; strong for structured pharmacovigilance data
- **GBM and RF** outperform traditional disproportionality methods for safety signal detection
- **SHAP analysis** identifies which drug classes and patient profiles drive highest risk

---

## Datasets

### 1. Canada Vigilance Adverse Reaction Database (Primary)
- **Source:** Health Canada via Open Government Portal
- **URL:** https://open.canada.ca/data/en/dataset/9cbaef00-b52c-4a70-9fed-d9aa8263ab74
- **Coverage:** 1965 to present, updated monthly
- **Format:** Dollar-sign delimited flat files (13 files), ZIP download
- **Contains:** Report demographics (age, sex, weight), drug details (name, dosage, route), reactions (MedDRA coded), seriousness indicators (death, hospitalization, disability), reporter info
- **API:** JSON/XML at `health-products.canada.ca/api/canada-vigilance/`
- **Access:** Fully open, no registration needed

### 2. Health Canada Drug Product Database (DPD)
- **Source:** Health Canada
- **URL:** https://open.canada.ca/data/en/dataset/bf55e42a-63cb-4556-bfd8-44f26e5a36fe
- **Contains:** 47,000 approved drug products with ATC classifications, ingredients, pharmaceutical forms
- **Use:** Enrich Canada Vigilance data with drug properties for feature engineering

### 3. FDA FAERS (Supplementary)
- **Source:** US FDA
- **URL:** https://open.fda.gov/data/faers/
- **Contains:** Millions of ADR reports, structurally similar to Canada Vigilance
- **Use:** Cross-validation, comparison of Canadian vs. US patterns

---

## Proposed ML Pipeline

```
1. Data acquisition & cleaning
   - Download Canada Vigilance extract (13 flat files)
   - Parse and join into unified analysis table
   - Download DPD for drug feature enrichment

2. Signal detection baseline
   - Implement PRR, ROR using vigipy Python library
   - Validate against known drug withdrawals/warnings

3. ML classification
   - Target: seriousness outcome (hospitalization, death)
   - Features: patient age/sex, concomitant drug count, drug ATC class,
     MedDRA SOC, route of administration, indication
   - Models: Logistic Regression → Random Forest → XGBoost → LightGBM
   - Handle class imbalance with SMOTE / class weights

4. Evaluation
   - AUC-ROC, precision-recall, F1
   - SHAP feature importance analysis
   - Compare ML vs. traditional disproportionality methods

5. Deliverable
   - Risk scoring dashboard for drug-patient combinations
   - Feature importance visualization
   - Canadian-specific ADR pattern analysis
```

---

## Strengths

- **Fully open 60-year Canadian dataset** — no ethics approval, no data access delays
- **Genuinely underused for ML** — very few published ML studies on Canada Vigilance specifically
- **Published benchmarks exist** (AUC ~0.77 average across 54 studies) for comparison
- **Python tooling ready** — vigipy, MDDC, faerslib libraries handle signal detection
- **Never done in past cohorts** — completely novel for Let's SOLVE It
- **Clear policy impact** — faster signal detection saves lives

## Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Class imbalance (rare serious outcomes) | SMOTE, class weights, precision-recall metrics |
| Underreporting bias (only 1-10% reported) | Acknowledge as limitation; database still has 60+ years of data |
| MedDRA coding complexity | Use SOC level (broad categories) to reduce dimensionality |
| No ground truth for "true" signals | Validate against known Health Canada drug recalls/warnings |

---

## References

- ADR Canada — 4th Leading Cause of Death: https://adrcanada.org/
- Canadian Adverse Events Study: https://pmc.ncbi.nlm.nih.gov/articles/PMC408508/
- Predicting ADE Using ML (Systematic Review, 2024): https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2024.1497397/full
- Canada Vigilance Data Structure: https://www.canada.ca/en/health-canada/services/drugs-health-products/medeffect-canada/adverse-reaction-database/canada-vigilance-adverse-reaction-online-database-data-structures.html
- vigipy Python Library: https://github.com/Shakesbeery/vigipy
- FAERS Jupyter Notebook: https://github.com/DSimoens/FAERS_PHARMACOVIGILANCE_ANALYSIS
