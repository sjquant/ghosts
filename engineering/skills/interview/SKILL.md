---
name: interview
description: Clarify only the material uncertainty in a request, then provide a concise execution-ready brief.
disable-model-invocation: true
---

Clarify the user's real goal only when a missing fact, preference, or decision would materially change the work. Inspect available context before asking. Do not plan, implement, create tasks, write specs, or edit files during the interview.

## Decide Whether to Ask

Do not interview when the request, available context, and normal in-scope assumptions are sufficient to proceed. State the assumption and continue.

Ask when the missing information affects the outcome, scope, user-facing behavior, safety, cost, or an external action. Ask for the smallest missing decision; do not collect background that will not change the work.

## Questions

Ask one focused question at a time unless the available ask tool supports a compact set of independent choices. Include a brief current assumption only when it helps the user answer.

Use a pressure-test question only when a consequential tradeoff, safety risk, or ambiguous requirement remains. If a vague term has an observable interpretation from context, use it; otherwise ask for the minimum useful clarification.

## Stop Condition

Stop when the remaining uncertainty would not materially change the work. Do not require a confidence score, a fixed number of questions, a pressure test, or explicit confirmation by default.

If uncertainty remains, name the assumption and ask for confirmation only when proceeding could produce an unwanted or costly result.

## Final Brief

Summarize only the decisions needed to execute:

```md
# Execution Brief

- Outcome:
- Success criteria:
- Scope:
- Non-goals:
- Constraints:
- Key assumptions:
```

Proceed when the brief is sufficient. Request confirmation only for an unresolved material decision.
