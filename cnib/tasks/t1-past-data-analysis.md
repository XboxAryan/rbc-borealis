# T1: Past Data Analysis

Owner: Aryan (picked up, originally unassigned)

Objective: Pull initial insights and patterns from the existing post-course survey data, flag what it can and cannot tell us, and translate gaps into requirements for T2 (Backend Design).

Source data: `cnib/data/post-survey-responses.csv` (33 responses from 55 enrolled learners, ~60% response rate). The workbook has not been shared with the team yet and is therefore out of scope for this first pass.

---

## What the data is — and is not

- 33 responses, schema defined in `cnib/data/post-survey-schema.csv`. 19 columns: 5 metadata (4 of which are empty or constant — `Email` is always "anonymous", `Name` is always blank, `Last modified time` is blank, `Language` is blank for most), 4 ordinal Likert scales, 1 binary categorical (completed program Yes/No), 5 open-ended free text.
- **Anonymous by design**: responses cannot be linked back to individual learners. No demographics, no pre-course assessment linkage, no per-week trajectory. This is the single biggest limit on what the data can support.
- **Post-only**: no within-person delta (confidence before vs after, skills before vs after). "Improvement" can only be estimated from self-report.
- **Self-report**: all metrics are learner-reported. No instructor corroboration and no passive behavioural data.

---

## Quantitative findings

All numbers below were computed directly from the CSV, not estimated.

### Completion (self-reported)

| Completed full 6-week program | Count (of 33) |
|---|---|
| Yes | 28 |
| No | 5 |

Note: this is 28 of the 33 **respondents**, not 28 of the 55 enrolled. The 22 non-respondents are a silent selection-bias problem — we have no idea how many of them completed.

### Post-course confidence ("how much more confident do you feel using AT in a work setting")

| Rating | Count |
|---|---|
| Somewhat confident | 16 |
| Very confident | 13 |
| Extremely confident | 3 |
| Not at all confident | 1 |

97% report at least "Somewhat confident," but the one "Not at all confident" response is not noise — it's a learner (ID 29) who wrote extensively about feeling the program was for screen-reader users and not low-vision mouse users. Treat this as a cohort-mismatch signal, not an outlier.

### Lecture, lab, and homework effectiveness

| Dimension | Very / Yes-definitely | Somewhat | Not very / Not really | Not effective at all / Not at all |
|---|---|---|---|---|
| Morning lectures | 21 | 10 | 2 | 0 |
| Labs (Wed + Friday) | 23 | 6 | 1 | 3 |
| Homework / workbook / capstone | 24 | 6 | 1 | 2 |

Lectures are the most uniformly positive. Labs and homework have a bimodal pattern — a clear majority love them, but a small group (4 for labs, 3 for homework) rated them at the bottom of the scale. Worth understanding whether those negative ratings cluster on the same people or on specific content.

### Practice frequency outside sessions

| Frequency | Count |
|---|---|
| Several times a week | 19 |
| Daily | 9 |
| Rarely | 4 |
| Never | 1 |

85% practice at least several times a week. The 5 who practice rarely or never are worth looking at closely — they are likely the population the Early Warning Model would most want to catch.

### Non-completer profile (5 respondents)

Pulled individually because the group is small enough to look at case-by-case:

| ID | Confidence | Lectures | Labs | Homework | Practice |
|---|---|---|---|---|---|
| 2 | Somewhat | Somewhat | Somewhat | Yes, definitely | Several/week |
| 13 | Very | Very | Very | Yes, definitely | Rarely |
| 14 | Somewhat | Somewhat | Not at all | Not really | Rarely |
| 17 | Somewhat | Somewhat | Somewhat | Somewhat | Rarely |
| 27 | Very | Very | Very | Yes, definitely | Daily |

Two patterns jump out:
- IDs 13 and 27 rated everything positively and still didn't complete. This suggests non-completion is driven by factors outside program quality — life circumstances, health, scheduling — not by the content failing them. An Early Warning Model built only on performance signals will miss these learners.
- ID 14 is the opposite — uniformly negative across labs and homework, and didn't complete. Catchable via performance signals.
- 3 of the 5 non-completers practice "Rarely" — this looks like the strongest performance-based flag in the post-survey, but with n=5 it is directional, not conclusive.

### Practice frequency × homework effectiveness

14 of 19 "several times a week" practicers rated homework "Yes, definitely" effective. 8 of 9 daily practicers did too. The 4 "Rarely" practicers split: 2 found it definitely effective, 1 somewhat, 1 not really. Low practice correlates with less homework value, consistent with a motivation / engagement gradient.

---

## Qualitative themes (free text)

Coded across the 6 free-text columns. Counts are the number of respondents (out of 33) who mentioned each theme at least once.

| Theme | Respondents mentioning |
|---|---|
| Pacing / mixed skill levels in cohort | 12 |
| AI / Copilot (as a positive highlight) | 8 |
| Device fragmentation (Apple vs PC, JAWS vs VoiceOver) | 7 |
| Request for more 1-on-1 support / smaller breakouts | 7 |
| MS Forms (as a tool they valued learning) | 7 |
| Confidence / anxiety / struggle language | 7 |
| Request for tip sheets before the Monday lecture | 6 |
| Linktree (as a highlight) | 6 |
| Workbook mentions | 6 |
| Calendly (as a highlight) | 5 |
| Excel / spreadsheets | 4 |
| PowerPoint | 4 |
| Workload felt too high or too long | 4 |
| Troubleshooting / setup requests | 3 |
| Classroom chatter / interruptions | 2 |
| JAWS volume interfering with instructor voice | 2 |
| Desire for certificate of completion | 1 |

Takeaways:
- **Pacing and mixed skill levels is the single most frequent complaint** (12 of 33). Learners propose splitting the cohort by experience level, by AT device type, or by OS. Roughly every third respondent raised this unprompted.
- **Device fragmentation is structural, not anecdotal**. Different screen readers use different keyboard shortcuts and different navigation models. When an instructor demos on JAWS and a learner is on VoiceOver, the demo doesn't directly transfer.
- **Advance materials would be cheap and high-impact**. 6 respondents explicitly asked for tip sheets before the Monday lecture. This is a change in scheduling, not in teaching.
- **1-on-1 and small breakouts are wanted** by 7 respondents — consistent with the mixed-skill complaint.
- **AI modules landed well**. 8 respondents cited AI / Copilot as a highlight, which validates keeping AI modules in future cohorts and suggests the Clarity chatbot will be received positively.
- **Instructor-side feedback surfaces through learners**: 2 respondents mention the instructor's JAWS output overlapping with their voice during lectures. Small fix, but a signal that class-production accessibility matters.

---

## What the survey cannot tell us

These are the gaps that T2 (Backend Design) must address:

1. **Per-learner trajectory**. Anonymous post-survey = no way to measure confidence change per person, no way to check whether the "Not at all confident" responder had been "Very confident" at intake, no way to link survey responses to homework completion or attendance.
2. **Pre-course baseline**. No objective measure of starting competency. "Confidence gain" is self-assessed relative to a remembered past self, not to a measured baseline.
3. **Weekly granularity**. The survey is end-of-program. We have no idea when in the 6 weeks confidence dropped, when people started disengaging, or which specific modules were hardest.
4. **Non-respondent data**. 22 enrolled learners didn't respond. They may disproportionately be the struggling or non-completing population. Without a mandatory or non-survey data source, they are invisible.
5. **Behavioural signals**. No practice-session telemetry, no per-exercise error logs, no attendance at optional labs, no breakout-room participation. Everything is self-report.
6. **Disability profile beyond vision**. The survey does not capture hearing loss, motor impairment, cognitive differences, or deafblind status. The T4 research brief argues this materially affects outcomes.
7. **AT profile**. No capture of what OS or screen reader the respondent uses, despite 7 respondents explicitly naming fragmentation as a problem.
8. **Instructor-side data**. No trainer notes, no observations, no per-learner pacing judgements. One side of the conversation is entirely missing from the dataset.
9. **Workbook data**. The workbook itself is mentioned by 6 respondents but we have no access to it yet. Whatever completion and correctness data it contains is currently out of reach.

---

## Implications for T2

Direct requirements, derived from the gaps above:

- **Pseudonymous per-learner ID** from intake through post-course follow-up. Anonymisation can be preserved for analysis, but longitudinal linkage must not be broken.
- **Mandatory pre-course intake form** covering AT profile (OS, screen reader, magnifier, braille display), prior AT experience level, disability profile beyond vision, learning goals. This alone unlocks subgroup analysis.
- **Weekly confidence pulse** (Leitner scale, same instrument as post-survey) rather than only at program end. Weekly confidence delta is likely the single strongest leading indicator per the Apr 2 meeting notes.
- **Per-exercise tracking** for workbook and homework, not just per-week. This is what enables Idea B (Skill Bottleneck Detection) as future work.
- **Passive attendance and engagement capture** — attendance at optional Friday labs, 1:1 requests, breakout participation. These should be logged automatically, not self-reported.
- **Non-respondent fallback**: some data collection should be passive or built into the program, not dependent on survey submission.
- **Trainer note structuring**: move from free text to a lightweight structured template so notes are machine-readable.
- **Workbook access**: formal request to CNIB for workbook data (or access to the workbook platform) as part of the data request.

---

## Trainer questions for T1

Folded into `trainer-questions.md`. Specifically:
- Q1, Q5 (what's tracked, where)
- Q2 (signals used to identify struggle at weeks 1–2)
- Q3 (confidence drop points)
- Q6 (whether splitting by level has been tried)
- Q11, Q12, Q13, Q14, Q15 (Section A detail on data shape)
