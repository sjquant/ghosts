---
name: explain-diff
description: Explain a code change, diff, branch, or PR as a novice-first visual lesson in one self-contained HTML artifact with big diagrams, few words, concrete examples, and an interactive quiz.
disable-model-invocation: true
---

# Explain Diff

Explain the change as if teaching a curious five-year-old who knows nothing about the topic, while keeping the facts technically accurate. Use an HTML artifact with big pictures and few words; teach the change as a small visual story, not as a line-by-line code dump.

If the target diff, branch, PR, or repository path is missing, ask for it before acting. Do not invent behavior: distinguish observed facts, reasonable inferences, and unknowns.

## Runtime loop

Before acting, create `/tmp/explain-diff-<safe-task-slug>.md`. Add `Current state: Pass 1 / Next: Inspect`, a task-specific checklist, and an empty append-only `Repair log:`. Process items top to bottom: finish the current item before moving on, record a short outcome, update `Current state`, and mark `[x]` only after completion. Use `[-]` only with a reason; never erase or uncheck historical rows. After a repair, append a numbered `[ ]` recheck row for the earliest affected item and log the trigger, change, rechecked items, and result. Finish only after final validation.

Use this checklist, adding only items that materially affect the explanation:

```text
- [ ] Confirm the target and inspect the diff plus surrounding code
- [ ] Reduce the change to its actors, old behavior, new behavior, and concrete example
- [ ] Sketch the smallest useful before/after and data-flow visuals
- [ ] Build the self-contained HTML artifact
- [ ] Validate novice clarity, visual hierarchy, evidence boundaries, and interactions
- [ ] Scan every code block for whitespace-preserving CSS
- [ ] Any missing visual, explanation, evidence, accessibility, or interaction?
- [ ] Final validation and artifact delivery
```

Answer every `Any ...?` row with Yes or No in its outcome. On Yes, make the smallest repair, append a numbered recheck row from the earliest affected item, record it in `Repair log:`, and return to validation.

```text
[Start] → [Inspect] → [Model old/new] → [Build HTML] → [Validate] → Any issue?
                                                                  ├─ No → [Deliver]
                                                                  └─ Yes → [Repair] → [Build or Validate]
```

## Explanation contract

1. Inspect the change and enough surrounding code to explain why it exists, what it touches, and what a user or caller observes.
2. Build a simple mental model before naming implementation details. Define jargon at first use, prefer familiar nouns and verbs, and keep each text block to a short sentence or two.
3. Make visuals carry the explanation. Use large HTML/CSS diagrams, cards, arrows, timelines, or inline SVG when useful—never ASCII diagrams. Give each visual one idea, show example data or messages, and add a short caption and accessible text.
4. Include these sections in this order:
   - **Takeaway:** one sentence saying what changed and why it matters.
   - **Before:** the old path, with a simple visual and one concrete example.
   - **After:** the new path, highlighting the changed step or boundary.
   - **How it works:** a visual data-flow or sequence using the actual components and example values.
   - **Code map:** a high-level map from behavior to changed files, symbols, or tests; show only small, relevant snippets.
   - **Why it matters:** user impact, important edge cases, and explicit unknowns or tradeoffs.
   - **Quiz:** five medium-difficulty multiple-choice questions. On selection, show the correct answer and concise feedback; avoid gotchas and do not test trivia.
5. Use progressive disclosure (`details`/`summary`) for deeper background and a callout for the one key definition, edge case, or tradeoff the reader must remember. Keep diagrams prominent and prose sparse; do not replace missing evidence with decorative complexity.

## Artifact requirements

- Write one long, responsive HTML file with a table of contents, semantic headings, inline CSS, and inline JavaScript. Do not load fonts, scripts, images, or data from the network.
- Save it outside the repository at `/tmp/YYYY-MM-DD-explanation-<slug>.html`, using today’s date and a filesystem-safe slug. Return the absolute path.
- Use high-contrast, readable type, large visual targets, keyboard-accessible controls, and feedback that does not rely on color alone.
- Put code in `<pre>` (normally `<pre><code>…</code></pre>`). Before saving, scan every code block in the HTML source and confirm its CSS preserves whitespace with `white-space: pre` or `white-space: pre-wrap`.
- Keep the page self-contained and viewable by opening the file directly; verify links, quiz behavior, and the final file’s existence before delivery.
