---
name: ghosts:work-breakdown
description: Use when the user asks to plan work, agree on an approach, or break a problem into reviewable tasks with dependencies and execution order.
---

Inspect code and context without modifying code, implementing tasks, or creating issues and PRs. Define the concrete problem, observable outcome, scope, and constraints.

For large work, start with a rough breakdown to expose uncertain decisions; do not require a detailed plan for the whole problem first. Investigate facts yourself. Use `ghosts:grill-me` for unresolved material user decisions about outcome, scope, or tradeoffs, preserving decisions already agreed. Compare simpler approaches or omission when useful, then refine the affected work.

Give each package an outcome, scope, prerequisites, and completion evidence. Prefer reviewable end-to-end slices and split only when needed. Keep small, clear work as one package without a separate planning exercise. Build a dependency DAG from actual prerequisites; keep independent work independent.

- Any unresolved decision that could change the outcome or scope?
- Any unnecessary work, premature detail, or simpler approach?
- Any missing dependency, circular prerequisite, or unverifiable completion criterion?

Resolve material gaps and revise affected packages. Do not treat a proposed direction as approved.

## Output

Present the direction in the user's language as 2–3 bullets readable without scrolling: problem and approach, work order, and validation or the key tradeoff. Show supporting work packages and dependencies concisely, using a table or DAG when useful. Reflect the user's corrections and obtain confirmation before handing the agreed breakdown to issue creation or implementation; this skill does not execute those steps.
