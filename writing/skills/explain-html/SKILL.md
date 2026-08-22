---
name: explain-html
description: Explain a supplied topic to a complete beginner in one self-contained HTML artifact with large visuals, sparse plain-language text, concrete examples, and accessible progressive disclosure.
disable-model-invocation: true
---

Explain the supplied topic to someone with no prior knowledge. Keep the explanation accurate and distinguish facts, assumptions, and unknowns. If the topic is missing, ask for it before acting; do not invent details to fill gaps.

## Runtime loop

Before acting, create `/tmp/explain-html-<safe-task-slug>.md`. Add `Current state: Pass 1 / Next: Understand`, a task-specific checklist, and an empty append-only `Repair log:`. Process checklist items from top to bottom: finish the current item before moving on, record a short outcome, update `Current state`, and mark `[x]` only after completion. Use `[-]` only with a reason; never erase or uncheck historical rows. After a repair, append a numbered `[ ]` recheck row for the earliest affected item and log the trigger, change, rechecked items, and result. Finish only after final validation.

Use this checklist, adding only items that materially affect the explanation:

```text
- [ ] Confirm the topic, intended takeaway, and any supplied evidence
- [ ] Reduce the topic to essential terms, relationships, and one concrete example
- [ ] Choose the smallest visual story that makes the idea visible
- [ ] Build the self-contained HTML artifact
- [ ] Validate beginner clarity, sparse copy, visual hierarchy, factual boundaries, accessibility, and local behavior
- [ ] Any missing visual, explanation, evidence, accessibility, or unnecessary complexity?
- [ ] Final validation and artifact delivery
```

Answer every `Any ...?` row with Yes or No in its outcome. On Yes, make the smallest repair, append a numbered recheck row from the earliest affected item, record it in `Repair log:`, and return to validation.

```text
[Start] → [Understand] → [Model] → [Build HTML] → [Validate] → Any issue?
                                                               ├─ No → [Deliver]
                                                               └─ Yes → [Repair earliest affected step] → [Validate]
```

## Explanation contract

1. Form one plain-language takeaway before naming implementation details. Introduce each necessary term with a familiar definition and a tiny example.
2. Tell a visual story: show the main actors or parts, then show the steps, flow, or before/after state. Keep each visual focused on one idea.
3. Prefer large HTML/CSS diagrams, cards, arrows, timelines, or inline SVG over prose; never use ASCII diagrams. Give every visual a short caption and accessible text. Do not add decorative complexity that does not teach.
4. Keep words scarce: use short headings, labels, and sentences; put optional depth in `details`/`summary`. Use concrete values, input→output examples, or a before→after comparison whenever the topic permits.
5. Use one small interaction (such as revealing a step or checking understanding) only when it reinforces the mental model. Make it keyboard accessible and give feedback that does not rely on color alone.

## Artifact requirements

- Produce one responsive, semantic HTML file with inline CSS and, when needed, inline JavaScript. Do not load fonts, scripts, images, or data from the network; use CSS shapes or inline SVG for visuals.
- Save it outside the repository at `/tmp/YYYY-MM-DD-explanation-<slug>.html`, using today’s date and a filesystem-safe slug. Return the absolute path.
- Use high-contrast, readable type, generous spacing, large visual targets, visible focus states, and headings in a logical order. Ensure the page remains understandable without color or interaction.
- If code appears, put it in `<pre><code>…</code></pre>` and preserve whitespace with `white-space: pre` or `white-space: pre-wrap`.
- Before delivery, verify the file exists, the page opens directly, internal links work, and any interaction behaves as intended. Check that every claim is supported by the supplied context or clearly labeled as an assumption or unknown.
