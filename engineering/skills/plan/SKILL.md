---
name: ghosts:plan
description: Use when the user asks for a plan or wants to agree on a problem, approach, and dependency-ordered work before implementation.
---

Plan only: inspect code and context without modifying code, implementing tasks, or creating issues and PRs. Define the concrete problem, observable outcome, scope, and constraints.

Investigate facts yourself. Use `ghosts:grill-me` when material user decisions about outcome, scope, or tradeoffs remain unresolved; preserve decisions already agreed. Compare viable approaches, including a smaller change or omission when useful.

Apply the reviewable-slice and dependency criteria of `ghosts:work-breakdown`. Give each work package an outcome, scope, prerequisites, and completion evidence. Build a dependency DAG from actual prerequisites; keep independent work independent and small tasks unsplit when already reviewable.

- Any unresolved decision that could change the outcome or scope?
- Any unnecessary work or simpler approach?
- Any missing dependency, circular prerequisite, or unverifiable completion criterion?

Resolve material gaps and revise affected work before presenting the plan. Do not treat a proposed plan as approved.

## Output

Present the direction in the user's language as 2–3 bullets readable without scrolling: problem and approach, work order, and validation or the key tradeoff. Keep the supporting work packages and DAG concise, using a table or diagram when useful. Reflect the user's corrections and obtain confirmation before handing the agreed plan to issue creation or implementation; confirmation does not make this skill execute those steps.
