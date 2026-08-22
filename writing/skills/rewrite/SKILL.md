---
name: rewrite
description: Rewrite a prompt for maximum signal-to-noise without changing its intended behavior.
disable-model-invocation: true
---

$ARGUMENTS

Rewrite the supplied prompt, not the task it requests. If no prompt is supplied, ask for it. Preserve every detail that can change the result; remove text that cannot.

## Procedure

1. Extract the goal, role or audience, context, inputs, constraints, priorities, output format, success criteria, dependencies, and edge cases.
2. Put the main task first. Group related instructions and order them by priority.
3. Remove filler, repetition, decorative wording, generic advice, and irrelevant context. Keep examples only when they disambiguate behavior.
4. Replace vague requirements with observable criteria when their meaning is clear. Add the smallest qualifier needed for an ambiguous term.
5. Preserve conditions, uncertainty, conflicts, and other behavior-changing wording. Do not invent facts, tools, policies, sources, requirements, or priorities.
6. Compare the rewrite with the source: the goal, constraints, inputs, outputs, priorities, and edge cases must still be present, while the wording is shorter and clearer.

If a missing detail or conflict makes a safe rewrite impossible, ask one focused clarification instead of guessing. Otherwise return the rewritten prompt only, using the requested format when one is specified.

## Execution loop

```text
[Start: receive source] → [Any prompt missing or essential ambiguity/conflict?]
                    ├─ Yes → [Ask one focused question] → [Done]
                    └─ No  → [Parse] → [Draft rewrite] → [Validate against source]
                                                        → [Any meaning, scope, or clarity failure?]
                                             ├─ No  → [Return rewritten prompt] → [Done]
                                             └─ Yes → [Repair earliest affected step] → [Validate]
```

## Runtime checklist

Before acting, create `/tmp/rewrite-<safe-task-slug>.md`. Use it as a state log:

- Process task-specific items in order and finish the current item before moving on.
- Mark `[x]` only after an item is complete; use `[-]` only when it is inapplicable and record why.
- Keep `Current state` and an append-only `Repair log` in the file.
- After a repair, keep completed rows, append a numbered recheck row for the earliest affected item, and log the trigger, change, rechecked items, and result.
- Finish only after final validation.

Use these items, adapting the wording to the prompt:

```text
- [ ] Parse goal, audience, context, inputs, constraints, outputs, and edge cases
- [ ] Draft the shortest faithful rewrite
- [ ] Validate preservation, clarity, and reduced noise
- [ ] Any meaning, scope, or clarity failure?
- [ ] Repair and append the earliest affected recheck row
- [ ] Final validation and return the rewrite or one clarification question
```
