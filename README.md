# CNIB x RBC Borealis — Predicting Learner Support Needs

**RBC Borealis Let's SOLVE It Spring 2026**

ML project with the Canadian National Institute for the Blind (CNIB) to predict and support struggling learners in their Assistive Technology Academy — a 6-week bootcamp that equips blind, Deafblind, and low-vision Canadians with digital skills for employment.

## Problem

Trainers rely on manual observation to identify struggling learners. In a fast-paced cohort, patterns like repeated errors, inconsistent practice, and frustration signals get missed. ML can detect these early, explain *why* learners struggle, and suggest targeted interventions.

## Approach

1. **Early Warning Dashboard** — risk scores + explainability (SHAP) for trainers
2. **Learner Archetype Clustering** — unsupervised grouping to understand "why"
3. **Contextual Bandit Intervention Policy** — learn which interventions work for which profiles

Build strategy: rule-based alerts → anomaly detection → supervised models → RL.

## Key Dates

| Date | Event |
|------|-------|
| March 16 | Program start |
| April 24 | Request presentation office hours |
| May 1 | Confirm in-person presentation |
| May 27 | Deliverables due (report, code repo, optional white paper) |
| May 28 | Program end |

## Repository Structure

```
cnib/              Active CNIB project (proposal, agreements, meeting notes, roadmap)
program/           RBC Borealis LSi S26 program materials
archive/           Previous project tracks (data center siting, healthcare, general ideas)
```

## Data

Pending CNIB privacy and data governance approval. Expected data:
- Homework/workbook completion records
- Practice frequency and consistency
- Error patterns
- Trainer session notes (structured insights)
