# Trainer Meeting — Consolidated Questions

Meeting: 2026-04-15

This is a consolidated, priority-ranked list of questions across all four tasks (T1 Past Data Analysis, T2 Backend Design, T3 UI/UX, T4 AT Research). The **Top 10 Must-Ask** are the questions to cover first if the meeting runs short. The sectioned list below is organized by theme for a longer conversation.

Question tags: `[T1]` past data, `[T2]` backend design, `[T3]` UI/UX, `[T4]` AT research.

---

## Top 10 Must-Ask (priority order)

Prioritized by information value × how much uncertainty we still have. Every question below either unblocks a specific design decision or kills an assumption we'd otherwise carry silently.

1. **What data do you currently track per learner, week by week? Is any of it linkable to an individual (even via a pseudonymous ID), or is everything aggregated or anonymous?** `[T1][T2]`
   *Why: the post-survey is anonymous, which means no pre/post delta per person. We need to know whether anything else is linkable before designing the Early Warning Model.*

2. **When you notice someone is falling behind at weeks 1 or 2, what specific signals do you use? Is it gut feel, or something more concrete like missed homework, silence in breakouts, or error patterns?** `[T1][T2]`
   *Why: directly defines the feature set for the Early Warning Model. "Gut feel" itself is a signal we need to capture in a structured way.*

3. **Is there a point in the curriculum where confidence tends to drop — not just where content gets harder, but where learners seem to mentally give up?** `[T1][T4]`
   *Why: distinguishes difficulty spikes from confidence collapse. Very different interventions for each.*

4. **How many participants in a typical cohort have additional disabilities beyond vision (hearing loss, motor impairments, cognitive differences)? Any deafblind participants? Does CNIB currently track this at intake?** `[T4][T2]`
   *Why: reshapes the tool design. Braille display compatibility, non-audio interaction, motor-access accommodations all depend on this.*

5. **What's stored in Salesforce versus in the workbook versus elsewhere, and what's the realistic access path for each?** `[T1][T2]`
   *Why: Salesforce is a CRM, not an LMS. The shape of its data determines whether per-exercise analysis is possible at all.*

6. **Have you ever tried splitting cohorts by experience level, AT device type, or disability profile — even informally? What happened?** `[T4][T1]`
   *Why: if splitting was tried and failed, the lessons are gold. If it was never tried, that's a low-cost high-value experiment on its own.*

7. **When you prepare for a class, do you open any tools beforehand to check student progress, or do you rely on memory and notes from the previous session?** `[T3]`
   *Why: determines whether a dashboard is additive or redundant to the instructor's current workflow.*

8. **In a virtual class where you can't see participants' faces, how do you currently sense emotional disengagement?** `[T3][T4]`
   *Why: the instructor tool's "pulse check" feature only makes sense if we understand what signal it's replacing.*

9. **How many participants use both a screen reader and a magnifier simultaneously? What's the typical OS and screen-reader mix you see per cohort (JAWS / NVDA / VoiceOver, Windows / Mac / iOS)?** `[T3][T4]`
   *Why: the research brief flags dual AT use as common. We need cohort-level numbers to decide whether the tool can assume either purely-audio or purely-visual interaction, and to design breakout grouping.*

10. **When Clarity launches, will instructors be able to see what topics students are asking about? Do you see that kind of query-log data as useful, or would it feel invasive?** `[T3][T2]`
    *Why: Clarity is the biggest passive data opportunity in this project. Worth sorting now whether instructors are on board.*

---

## Section A — Data that exists today `[T1][T2]`

11. What columns does your Salesforce database actually contain for this program? (Even a rough list helps — we can follow up in writing.)
12. Are training session notes written as free text, or do they follow a structured template?
13. For homework and workbook completion, is it tracked at the exercise level, or just "completed for the week"?
14. What length are trainer notes on average — a few lines, a paragraph, a page? Are they per-learner or per-session?
15. What pre-course data do you collect right now? Anything about prior AT experience, OS/screen-reader, or disability profile beyond vision?

## Section B — Learner signals trainers actually use `[T1][T2]`

(Questions 2, 3, 8 already in Top 10.)

16. What are the top two or three signs that predict someone WON'T complete the program? Not the obvious ones — the non-obvious tells.
17. When a learner stops submitting homework, is it usually because the content got too hard, or because of life circumstances outside the program?

## Section C — Cohort composition `[T4]`

(Questions 4, 9 already in Top 10.)

18. What percentage of each cohort, roughly, is newly disabled — people who experienced vision loss as adults — versus those who have been blind or low-vision for years?
19. For any deafblind participants you've had, how do you structure or communicate during a virtual session?

## Section D — Instructor workflow and tool fit `[T3]`

(Question 7 already in Top 10.)

20. Would using a voice command during a break feel natural, or would it feel like extra admin on top of teaching?
21. How much time do you realistically spend between sessions reviewing student progress — 5 minutes, or closer to an hour?
22. What screen reader and OS do you personally use day to day? (JAWS on Windows, VoiceOver on Mac or iPhone, NVDA, other?)
23. Are there any tools you already use — teaching-related or personal — that you find genuinely easy and intuitive? What makes them work well for you?

## Section E — Curriculum and pacing `[T1][T2]`

(Questions 6, 10 already in Top 10.)

24. How much of your instruction time is actual skill-building versus motivation and confidence support? Is that balance intentional?
25. What is one thing about the current program structure you wish you could change but haven't been able to?

---

## What the post-survey already hints at (so we don't waste meeting time re-asking)

Quick context from our analysis of the 33 responses — share only if a trainer brings up something that contradicts these, otherwise just use as a prior:

- ~85% of respondents report lectures "Very" or "Somewhat" effective; the weakest ratings are on labs (4 of 33 rated labs "Not very" or "Not at all" effective) and homework (3 of 33 "Not really" or "Not at all").
- Free-text feedback repeatedly flags: mixed skill levels in one cohort, device fragmentation (Apple vs PC, different screen readers), and classroom-management chatter.
- Confidence distribution skews positive but 1 respondent reports "Not at all confident" after the program — a real signal worth understanding rather than averaging away.
- Workbook-specific feedback is thin — worth asking whether the workbook is already tracked in a way we could access.
