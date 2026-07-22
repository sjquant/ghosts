---
name: socratic-interview
description: Conduct a Socratic interview to resolve only material uncertainty, then provide a concise execution brief.
disable-model-invocation: true
---

Conduct a Socratic interview only when missing information could materially change the outcome, scope, behavior, safety, cost, or external action. Inspect context first and make normal in-scope assumptions when sufficient.

Ask the smallest useful question, one at a time. Do not collect background that will not change the work. Stop when remaining uncertainty is immaterial; state assumptions and proceed unless doing so could cause an unwanted or costly result.

Do not plan, implement, create tasks, write specs, or edit files during the interview.

When sufficient, summarize only the decisions needed to execute:

```md
# Execution Brief

- Outcome:
- Decisions:
- Scope and constraints:
- Assumptions:
```
