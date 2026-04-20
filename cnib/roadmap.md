# CNIB Project Roadmap

## Phase 0: Get Organized (Weeks 1-2) — IN PROGRESS
- [x] Kickoff meeting with CNIB
- [x] Analyze CNIB project proposal
- [x] Evaluate ML product options (8 explored, Early Warning Dashboard selected)
- [x] Sign tri-party participation agreement
- [ ] Draft project charter (1-pager for team + CNIB alignment)
- [ ] Draft formal data request for CNIB (specific fields, formats, anonymization)
- [ ] Assign team roles and responsibilities
- [ ] Set up weekly meeting cadence with team

## Phase 1: Foundation (Weeks 3-4)
- [ ] Build synthetic data generator (unblocks development pre-data)
- [ ] Build Streamlit prototype for Early Warning Dashboard
- [ ] Literature review: Purdue Course Signals, OAAI, Georgia State, Khan Academy
- [ ] Define feature engineering table
- [ ] Begin CNIB data onboarding (if privacy approved)

## Phase 2: Core ML (Weeks 5-6)
- [ ] Implement rule-based alert layer
- [ ] Implement anomaly/change-point detection
- [ ] Train supervised models (if real data available)
- [ ] Build SHAP-based explainability for trainer-facing insights

## Phase 3: Polish & Present (Weeks 7-8)
- [ ] Contextual bandit framework (LinUCB) — if time permits
- [ ] Final dashboard with risk scores + explanations + interventions
- [ ] Write one-page report
- [ ] Prepare 15-min presentation
- [ ] Finalize public code repository

---

## Questions for CNIB (Next Meeting)

1. What data fields are currently tracked per learner? (homework, practice logs, error logs, session notes?)
2. What does a "struggling learner" look like to trainers? What are the early signs?
3. How many learners per cohort? How many cohorts have completed the Academy?
4. What interventions do trainers currently use when they notice someone struggling?
5. What technology platform does the Academy use? (LMS, screen reader logs, etc.)
6. What are CNIB's privacy/data governance requirements for this project?
7. What would the ideal output look like for trainers? (dashboard, alerts, reports?)
8. Are there specific curriculum modules where learners struggle most?

---

## ML Product Decision

**Selected: Early Warning Dashboard** (ranked #1 of 8 options evaluated)

Why: Most pragmatic, immediate value for trainers, works with small data, explainable.

Other options explored (available for future phases):
- Learner Archetype Clustering
- Knowledge Graph of Skill Dependencies
- LLM Trainer Note Analyzer
- Screen Reader Replay Analysis
- Frustration Detection
- Digital Twin Simulation
- RL Intervention Policy (contextual bandits — the ambitious differentiator)

---

## Key Constraints

- **Small data**: Dozens of learners per cohort, not thousands. Everything must be sample-efficient.
- **Ethics**: CNIB has done AI bias research (2022-2025). Fairness framework must be baked in from day 1.
- **No data yet**: Privacy procedures pending. Synthetic data generator is the immediate unblock.
- **10 hrs/week**: Expected time commitment per team member.
