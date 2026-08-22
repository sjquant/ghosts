---
name: explain-diff
description: Explain a code change, diff, branch, or PR as a novice-first visual lesson in one self-contained HTML artifact with big diagrams, few words, concrete examples, and an interactive quiz.
disable-model-invocation: true
---

Explain the change to a reader with no prior knowledge while keeping the facts technically accurate. Use big visuals, few words, and a small visual story rather than a line-by-line code dump. If the target is missing, ask before acting; do not invent behavior, and distinguish observed facts, inferences, and unknowns.

## Runtime loop

Before acting, create `/tmp/explain-diff-<safe-task-slug>.md` with `Current state: Pass 1 / Next: Inspect`, a task-specific checklist, and an empty append-only `Repair log:`. Process items in order, finishing each before moving on; record outcomes and mark `[x]` only after completion. Use `[-]` only with a reason and never uncheck history. After a repair, append a numbered `[ ]` recheck row for the earliest affected item, log the trigger, change, rechecked items, and result, and finish only after final validation.

```text
- [ ] Confirm the target and inspect the diff plus surrounding code
- [ ] Model the actors, old/new behavior, and one concrete example
- [ ] Choose the smallest useful before/after and data-flow visuals
- [ ] Build the self-contained HTML artifact
- [ ] Validate novice clarity, evidence boundaries, accessibility, interactions, and code whitespace
- [ ] Any missing visual, explanation, evidence, accessibility, or interaction?
- [ ] Final validation and artifact delivery
```

Answer every `Any ...?` row Yes or No. On Yes, make the smallest repair, append the recheck row and repair-log entry, and return to validation.

```text
[Start] → [Inspect] → [Model old/new] → [Build HTML] → [Validate] → Any issue?
                                                                  ├─ No → [Deliver]
                                                                  └─ Yes → [Repair] → [Build or Validate]
```

## Explanation contract

1. Inspect enough surrounding code to explain why the change exists, what it touches, and what a user or caller observes.
2. Build the mental model first: define jargon at first use, prefer familiar nouns and verbs, and keep text blocks short.
3. Make visuals carry the explanation. Use large HTML/CSS diagrams, cards, arrows, timelines, or inline SVG—never ASCII. Give each visual one idea, example data, a short caption, and accessible text.
4. Include, in order: **Takeaway**, **Before**, **After**, **How it works**, **Code map**, **Why it matters**, and **Quiz** (five medium-difficulty multiple-choice questions with concise feedback, not trivia).
5. Use `details`/`summary` for optional depth and one callout for the key definition, edge case, or tradeoff. Keep diagrams prominent and prose sparse.

## Artifact requirements

- Write one responsive HTML file with a table of contents, semantic headings, inline CSS, and inline JavaScript. Do not load fonts, scripts, images, or data from the network.
- Save it outside the repository at `/tmp/YYYY-MM-DD-explanation-<slug>.html`, using today’s date and a filesystem-safe slug. Return the absolute path.
- Use high-contrast type, large visual targets, visible focus states, keyboard-accessible controls, and feedback that does not rely on color alone. Keep the page viewable by opening it directly.
- Put code in `<pre><code>…</code></pre>` and preserve whitespace with `white-space: pre` or `white-space: pre-wrap`; verify links, quiz behavior, code blocks, and final file existence before delivery.
