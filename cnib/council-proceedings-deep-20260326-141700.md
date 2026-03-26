# Council Proceedings: CNIB Problem Framing

**Date:** 2026-03-26 14:17
**Preset:** deep (custom — cross-domain)
**Judge Mode:** Assistant-as-Judge
**Personas:** 5

## Question
What is the CNIB Assistive Technology Academy problem, and what are the genuinely different ways of looking at it?

## Context Summary
CNIB runs a 6-week Assistive Technology Academy bootcamp for blind/Deafblind/low-vision Canadians. Some learners fall behind. Trainers rely on manual observation. CNIB wants ML to detect early warning signs, understand barriers, and suggest interventions. Constraints: dozens of learners per cohort (tiny data), no data access yet, 9-week student team timeline, historically marginalized population, CNIB's own research found AI can discriminate against disabled populations.

---

## Deliberation

### Dr. Sarah Kizilcec — Learning Analytics Researcher
**Core argument:** Ground the system in validated learning constructs, not convenience metrics. Homework completion measures compliance, not learning. Before writing code, build a construct map with trainers using critical incident technique. Identify real dimensions: transfer, error recovery, task decomposition, self-monitoring. These give SHAP explanations pedagogical meaning.

**Sacrifice:** 1-2 weeks before anyone touches code.

### Chancey Fleet — Accessibility & Disability Justice Advocate
**Core argument:** The primary user must be the learner, not the trainer. A trainer-facing risk dashboard is structurally surveillance. Build a learner-facing reflection tool instead: same signals surfaced to the learner first, with granular consent. Trainers see aggregate cohort patterns only.

**Design test:** "If a learner found out exactly how this system works, would they feel supported or watched?"

**Sacrifice:** Trainer efficiency. Some struggling learners won't self-surface.

### The ML Pragmatist — Senior ML Engineer
**Core argument:** You don't have an ML problem. N=30 kills bandits, supervised learning, and clustering. Build a rule-based dashboard with trainer-defined thresholds. Add a trainer annotation layer (the real deliverable) that creates structured data for future ML. Optionally add isolation forest as a "supplement."

**Sacrifice:** Technical "wow factor." No SHAP plots or bandit convergence curves.

### Kim Scott — Organizational Change & Adoption Specialist
**Core argument:** Design the alert-to-action loop before model code. Shadow trainers through a full day, co-design 3 alert templates with feedback buttons, define escalation paths. The workflow IS the product.

**Success test:** By week 3, a trainer says unprompted "the system caught something I missed."

**Sacrifice:** Technical ambition in early weeks.

### The Systems Thinker — Structural Contrarian
**Core argument:** Monitor the curriculum, not the learner. Build a Module Difficulty Profile system — same data, but scored per-module not per-person. Completion rates, error clustering, time-to-competency variance, prior experience interaction — all aggregated at the curriculum level. Small-N works here because you're looking for patterns that repeat across people.

**Practical compromise:** Build both views from the same data pipeline, but make curriculum the primary analytical artifact.

**Sacrifice:** The "early warning" narrative. Curriculum heatmap feels like program evaluation, not ML.

---

## Synthesis

### Decision
Build a **dual-lens system**: curriculum-centric analysis (primary) + learner-level flags (secondary), grounded in a trainer-co-designed construct map, with a clear alert-to-action workflow and learner transparency.

### Reasoning
The Systems Thinker's reframing is the strongest contribution. "Monitor the curriculum, not the learner" solves three problems: statistically valid at small N, systemic improvements for future cohorts, and naturally avoids surveillance concerns. The ML Pragmatist is right about sample-size math but undersells what's possible at the curriculum level. The Learning Analytics and Org Change insights are non-negotiable process requirements regardless of approach. The Disability Justice advocate's principles are integrated as design constraints.

### Compelling Arguments
1. Curriculum-level analysis works at small N where learner-level prediction fails (Systems Thinker)
2. The math on sample size is non-negotiable (ML Pragmatist)
3. Construct validity is upstream of everything (Learning Analytics)
4. The alert-to-action loop is the product, not the model (Org Change)

### Overruled Dissent
**Chancey Fleet** argued the dashboard must be learner-facing only. Overruled because: self-reporting misses the learners who most need help, and the student team can't build two interfaces in 9 weeks. However, her transparency and consent principles are integrated as design constraints.

### Caveats
- CNIB asked for learner monitoring — curriculum framing must be positioned carefully
- If data doesn't arrive by week 4, pivot to synthetic data + construct map as deliverable
- The program expects "ML" — a rule-based system needs framing as "ML-informed" with anomaly detection layer

---

## Key Tensions

1. **Learner-centric vs. Curriculum-centric (Kizilcec/Fleet vs. Systems Thinker):** Resolved by dual-lens — both views from same pipeline, curriculum as primary.
2. **ML ambition vs. Statistical reality (team plan vs. ML Pragmatist):** Resolved by honest assessment — rules at learner level, real analysis at curriculum level.
3. **Surveillance vs. Support (Fleet vs. Scott):** Resolved by integrating transparency principles — learners know what's tracked, trainers see curriculum context first.
4. **Speed vs. Rigor (ML Pragmatist vs. Learning Analytics):** Resolved by parallelizing — construct map interviews happen in weeks 1-2 while dashboard scaffolding is built.

## Open Questions
- How many historical cohorts has CNIB run? (determines statistical power for curriculum analysis)
- What does the curriculum structure look like? (modules, sequence, dependencies)
- What LMS/technology platform does the Academy use? (determines data granularity)
- What are CNIB's expectations for "ML" in the deliverable?
