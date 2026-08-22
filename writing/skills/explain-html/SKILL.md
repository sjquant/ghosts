---
name: explain-html
description: Explain any supplied topic to a complete beginner as a self-contained HTML artifact with big visuals, few words, and simple examples.
disable-model-invocation: true
---

Explain the supplied topic to someone with no prior knowledge. Use plain language, one clear visual story, and short concrete examples. Keep claims accurate; label assumptions or unknowns. If the topic is missing, ask for it.

## Runtime loop

Before acting, create `/tmp/explain-html-<safe-task-slug>.md` with `Current state: Pass 1 / Next: Understand`, a task-specific checklist, and an empty append-only `Repair log:`. Process items in order, finishing each before moving on; record an outcome and mark `[x]` only after completion. Use `[-]` only with a reason and never uncheck history. After a repair, append a numbered `[ ]` recheck row for the earliest affected item, log the trigger, change, rechecked items, and result, and finish only after final validation.

```text
- [ ] Confirm the topic and one-sentence takeaway
- [ ] Choose one concrete example and visual story
- [ ] Build the standalone HTML artifact
- [ ] Check beginner clarity, factual boundaries, accessibility, and local behavior
- [ ] Any missing visual, clarity, or validation?
- [ ] Final validation and deliver the artifact
```

Record Yes or No for the `Any ...?` row. On Yes, make the smallest repair, append the recheck row and repair-log entry, then return to validation.

```text
[Start] → [Understand] → [Build HTML] → [Validate] → Any issue?
                                             ├─ No → [Deliver]
                                             └─ Yes → [Repair] → [Validate]
```

## Output

- Build one responsive HTML file with semantic headings and inline CSS/SVG/JavaScript only. Use large, high-contrast visuals, short labels, and no ASCII diagrams or network assets. Any interaction must be keyboard accessible.
- Save it outside the repository at `/tmp/YYYY-MM-DD-explanation-<slug>.html` and return the absolute path.
- Before delivery, verify that the file opens directly, the visual makes the takeaway clear, and links or interactions work.
