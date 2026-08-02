---
name: loop-coding
description: Approval-gated coding loop for building, changing, fixing, or refactoring code.
disable-model-invocation: true
---

Before doing any work, create a task-specific checklist at
`/tmp/loop-coding-<safe-task-slug>.md`, replacing the placeholder with a
unique short slug or timestamp. Keep it updated after every completed item; do
not mark future items in advance. Use `[x]` only after the item is actually
complete and `[-]` only with a reason. Do not move to the next required item
while the current one is unchecked. Record a short outcome beside each item.
If a fix could invalidate a completed review or validation item, reset the item
to `[ ]` and process it again.

Use a checklist with at least these items:

```text
- [ ] Understand the request and inspect the relevant code
- [ ] Any implementation plan?
- [ ] Any materially better alternative?
- [ ] Which option best fits the requirements and constraints?
- [ ] Present the plan and receive approval
- [ ] Implement the approved plan
- [ ] Run relevant checks
- [ ] Any correctness or operational risks, including bugs, edge cases, race conditions, resource leaks, performance bottlenecks, scalability concerns, or security issues?
- [ ] Any design or API issues when viewed from outside-in, deep-module, and dependency-direction perspectives, including hidden obligations, awkward call sites, leaky abstractions, or circular dependencies?
- [ ] Any opportunities to simplify or clarify the code through better naming, standard libraries, utilities, or existing abstractions?
- [ ] Any test smells, such as brittle or implementation-coupled tests, over-mocking, unclear intent, missing negative-path coverage, or surviving mutants?
- [ ] Final validation
```

Process the checklist from top to bottom. Use the plan questions to evaluate
the request. Present the chosen plan, any relevant alternative and tradeoff,
affected files, and validation. Wait for explicit approval such as `go` or
`approve`, unless the user has already approved a specific plan. Do not
implement from a bare request.

After approval, implement the plan and run the relevant checks. Then review and
repair the change by processing each review question in the checklist one at a
time.

Whenever the answer is yes, make the smallest useful fix, run the relevant
checks again, and continue the questions from the beginning if the fix could
introduce another issue or side effect. Keep the checklist updated; do not make
the user prompt each review pass. Stop when the answers are no, the relevant
checks pass, and the diff remains within the approved scope. If the scope or
design must change materially, stop and present a revised plan for approval.

Keep the final response concise: summarize what changed, the checks run, and
any remaining uncertainty.
