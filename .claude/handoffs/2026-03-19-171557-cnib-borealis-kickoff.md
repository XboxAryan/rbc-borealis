# Handoff: CNIB x RBC Borealis — Project Kickoff & Strategy
- Branch: claude/20260301-160809 | 2026-03-19

## State
Completed initial analysis and strategic planning for CNIB Assistive Technology Academy ML project. No code written yet — this session was entirely scoping, research, and strategy. Team is in Phase 0 (Get Organized).

CNIB wants ML to detect struggling learners early in their 6-week assistive tech bootcamp for blind/low-vision Canadians, understand WHY they struggle, and surface actionable interventions for trainers.

**Current blockers:** No data access yet (privacy procedures pending). No defined deliverable from CNIB. Team of 4-6 (mixed technical/non-technical) had a kickoff but nobody was prepared.

## Files & Decisions
| Item | Details |
|------|---------|
| `RBC AI Borealis_CNIB Predicting Learner Support Needs.docx` | CNIB's original project proposal — extracted and analyzed. Key stats: ~42-54% employment rate for blind Canadians, 3x national unemployment avg |
| `.claude/plans/jaunty-cuddling-lake.md` | Full project roadmap: Phase 0-3 with timelines, team role assignments, 8 questions for CNIB, ML approach details, feature engineering table |
| PR #3 | Created on branch claude/20260301-160809 — committed the proposal doc |

## Key Decisions & Analysis

### ML Product Options Explored (8 total, ranked)
1. **Early Warning Dashboard** — strongest fit, most pragmatic. Risk scores + SHAP explanations + trainer-facing UI
2. **Learner Archetype Clustering** — works without outcome labels, gives "why" understanding
3. **Knowledge Graph of Skill Dependencies** — map curriculum as DAG, trace root skill gaps (high impact, buildable now)
4. **LLM Trainer Note Analyzer** — extract structured signals from free-text trainer notes (high impact, buildable now)
5. **Screen Reader Replay Analysis** — treat keystroke/navigation logs as clickstream data, sequence mining
6. **Frustration Detection** — behavioral signals (rage-typing, long pauses, session abandonment)
7. **Digital Twin Simulation** — agent-based modeling of cohorts, test interventions risk-free
8. **RL Intervention Policy** — contextual bandits that learn which interventions work for which learner profiles

### RL Intervention Policy (Deep Dive Completed)
User showed strong interest. Full MDP formulation written out:
- **State:** engagement metrics, error patterns, week number, previous interventions
- **Actions:** 9 intervention types (1:1 session, peer pairing, concept review, workload reduction, etc.)
- **Reward:** delta in homework/practice/error metrics + program completion
- **Algorithm:** LinUCB contextual bandits (not full RL — too data-hungry for small cohorts)
- **Cold start solution:** 4-layer bootstrap — expert prior from trainer interviews → simulation pre-training → EdTech transfer learning → online learning from real cohorts
- **Ethical approach:** Off-policy evaluation for first 2-3 cohorts (observe only), conservative exploration after that, always human-in-the-loop
- **Key risk:** Confounding — trainers pick interventions based on unobserved factors; need causal inference techniques

### Recommended Build Strategy
Layer 1→2→3: Rule-based alerts (immediate) → anomaly/change-point detection (week 1) → supervised models (when data permits). RL intervention policy as the ambitious differentiator.

## CNIB Research Findings (from web research agent)
- CNIB founded 1918, serves 1.5M+ Canadians with sight loss
- They did their own AI bias research (2022-2025) — found AI can discriminate against disabled populations due to training data underrepresentation. WE MUST ADDRESS THIS.
- 46% of blind Canadians don't own an advanced smartphone — tech gap affects Academy interactions
- No public RBC/Borealis x CNIB partnership exists yet — we're early/unannounced
- "Come to Learn" not found publicly — may be internal name. Closest: "Come to Camp" (Lake Joe) and CNIB Learning Academy
- Employment stats worse than proposal claims: research found ~42% (proposal said 54%)

## Next Steps
1. **Build synthetic data generator + Streamlit prototype** — unblocks team immediately, no CNIB data needed
2. **Build simulation environment + contextual bandit framework** — the RL foundation (user was about to greenlight this)
3. **Draft project charter** — 1-pager to align team and CNIB on scope/deliverables
4. **Draft formal data request for CNIB** — specific fields, formats, anonymization scheme
5. **Draft CNIB meeting agenda** — 8 questions from the roadmap
6. **Literature review** — Purdue Course Signals, OAAI, Georgia State advising model, Khan Academy mastery interventions

## Must-Know
- User is on a 4-6 person mixed team, they seem to be taking a leadership/technical-lead role
- Team is confused and needs direction — the roadmap and role assignments are critical deliverables themselves
- CNIB's own AI bias research means we need an ethics/fairness framework baked in from day 1, not bolted on later
- The "killer feature" pitch to CNIB: "We're not just telling you who's struggling — we're learning what to do about it and getting smarter every cohort"
- Small data is the defining constraint: dozens of learners per cohort, not thousands. Everything must be sample-efficient.
