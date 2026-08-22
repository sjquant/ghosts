---
name: loop-skills
description: Simple loop for creating, reviewing, or improving concise agent skills.
disable-model-invocation: true
---

# Loop Skills

Create or improve an agent skill through a small feedback loop. The resulting
skill should contain only behavior-changing instructions: remove repetition,
long explanations, and optional rules. Add a reference only when it keeps the
main skill clearer. The resulting skill must also show its own compact
execution loop or graph, including an `Any ...?` gate. Even a one-shot skill
can use `Start → Action → Any ...? → Done`.

Before starting, create a checklist at
`/tmp/loop-skills-<safe-task-slug>.md`. Use it as a state log, not as a linear
form to complete once. When a repair is needed, return to the relevant earlier
state and check it again.

```text
- [ ] Understand the goal and inspect nearby skills
- [ ] Draft the smallest useful contract and execution graph
- [ ] Write or revise the concise skill
- [ ] Any missing loop, branch, or `Any ...?` gate?
- [ ] Any scope or boundary issue?
- [ ] Any unnecessary rule or duplication?
- [ ] Any unclear behavior or output?
- [ ] Repair and return to the Any checks when needed
- [ ] Done
```

Mark an item only after doing it. For a Yes answer, record the repair, return
to the state that can fix it, and re-check the affected questions; do not just
continue to the next box.

## Loop

Use this shape rather than a one-way checklist:

```text
[Understand] → [Draft] → [Write] → [Any ...?] ── No ──→ [Done]
                                      │
                                     Yes
                                      ↓
                                   [Repair]
                                  /        \
                    scope/boundary          wording/structure
                         ↓                         ↓
                      [Draft]                   [Write]
                          \                       /
                           └────→ [Any ...?]
```

### Understand

Decide whether this is a new skill, a revision, or a review. Read relevant
repository instructions and a few nearby skills. Ask a question only when the
answer would materially change the result; otherwise make a reasonable
assumption.

### Draft

Capture only the core contract:

- when the skill applies and when it does not;
- required input;
- main behavior;
- expected output;
- important boundary or failure case.

Also draw the next-state shape that the authored skill will use:

```text
[Start] → [Action] → [Any ...?] ── No ──→ [Done]
                         │
                        Yes
                         ↓
                 [Repair or next step] ──→ [Action]
```

Use more branches when the task needs them, but keep the graph small enough to
scan. Do not leave the loop only in the author's notes; include the relevant
shape in the resulting skill.

### Write

Create or revise `SKILL.md` with valid frontmatter, a specific description,
and direct instructions. Keep the file short enough to scan. Use judgment:
examples, tools, approval gates, and supporting files are optional unless they
make the behavior clearer or safer.

### Any checks

Answer the checklist's `Any ...?` questions with Yes or No before marking them
complete. If any answer is Yes, make the smallest useful repair and return to
the earliest state that can fix it (`Draft` for scope, `Write` for wording or
structure). Then answer the questions again. If all answers are No, finish.
Add another `Any ...?` question only when a material issue is specific to the
skill.

For a materially uncertain design, show a short plan and wait for approval. If
the request is clear, proceed without an unnecessary gate. In review mode,
report findings without editing the skill.

## Final response

Lead with the result. Mention the changed path, purpose, and final check. Keep
it brief and use the user's language.
