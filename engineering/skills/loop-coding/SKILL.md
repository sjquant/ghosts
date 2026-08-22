---
name: loop-coding
description: Approval-gated loop for building, changing, fixing, or refactoring code.
disable-model-invocation: true
---

# Loop Coding

Use this skill when the user asks for an implementation change. Do not use it
for read-only review, explanation, specification, or design-only work.

## Runtime loop

Before acting, create `/tmp/loop-coding-<safe-task-slug>.md` with a unique
short slug or timestamp. Add `Current state: Pass 1 / Next: Understand`, a
task-specific checklist, and an empty append-only `Repair log:`. Process the
checklist top to bottom: finish the current item before moving on, record a
short outcome, update `Current state`, mark `[x]` only after completion, and
use `[-]` only with a reason. Never erase or uncheck historical rows. After a
repair, append a numbered `[ ]` recheck row for the earliest affected item,
update `Current state`, and log the trigger, change, rechecked items, and
result. Finish only after final validation.

Answer every `Any ...?` row Yes or No in its outcome. On Yes, use the earliest
affected state and append a row such as
`- [ ] Recheck P2: Run relevant checks` before continuing.

Use this checklist, adding only task-specific items that materially affect the
work:

```text
- [ ] Understand the request and inspect the relevant code
- [ ] Draft the plan: behavior, scope, affected files, validation, and any materially better alternative
- [ ] Any unresolved ambiguity or material design choice? (Ask before implementation when Yes.)
- [ ] Present the chosen plan and receive explicit approval, unless the user already approved that specific plan
- [ ] Implement the approved plan
- [ ] Run relevant checks
- [ ] Any correctness or operational risk: bugs, edge cases, races, leaks, performance, scalability, or security?
- [ ] Any design or API issue from outside-in, deep-module, or dependency-direction perspectives?
- [ ] Any opportunity to simplify or clarify through naming, standard libraries, utilities, or existing abstractions?
- [ ] Any test smell: brittleness, implementation coupling, over-mocking, unclear intent, missing negative paths, or surviving mutants?
- [ ] Final validation
```

For the plan, state the chosen direction, relevant alternative and tradeoff,
affected files, and validation. Wait for explicit approval such as `go` or
`approve`; a bare request is not approval unless it already specifies the plan.
If requirements or a material scope/design choice remain unresolved, stop and
ask the user rather than guessing.

After implementation and checks, answer each review question in order. For a
Yes, make the smallest useful repair, rerun relevant checks, append the
required recheck row and repair-log entry, then resume from the earliest
affected state. A material scope or design change requires a revised plan and
approval. Stop when every answer is No, checks pass, and the diff stays within
the approved scope.

```text
[Start] → [Understand] → [Plan + approval] → [Implement] → [Checks] → [Review] → Any issue?
                                                                            ├─ No → [Final validation] → [Done]
                                                                            ├─ scope/design → [Re-plan + approval] → [Implement]
                                                                            └─ code/tests/checks → [Repair] → [Checks] → [Review]
```

Final response: summarize what changed, the checks run, and any remaining
uncertainty.
