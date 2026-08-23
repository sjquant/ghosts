---
name: explain-diff
description: Explain a complete code change, diff, branch, or PR as a visual, novice-first HTML lesson with large diagrams, few words, concrete examples, and an interactive quiz.
disable-model-invocation: true
---

Make the explanation visual-first. Explain like I'm someone who knows nothing about this topic, using an HTML artifact with big pictures and few words. Create one self-contained lesson for the complete target change; prose should label, orient, or clarify the visuals, not replace them. Tell one small visual story instead of dumping code line by line. If the target is missing, ask before acting. Do not invent behavior; distinguish observed facts, inferences, and unknowns.

## Scope and content

- Inspect the complete diff, every commit in the target branch or PR, and enough surrounding code to explain the change.
- Cover every changed file and symbol. Explain behavior changes; summarize the purpose of tests, configuration, documentation, and mechanical changes instead of omitting them.
- Use a small set of large HTML/CSS diagrams, cards, arrows, timelines, or inline SVG. Never use ASCII. Each visual has one idea, example data, a short caption, and accessible text, and the set covers every meaningful changed path.
- Assume zero domain knowledge. Use familiar words, define jargon only when needed, use one concrete example, and keep text blocks to one or two short sentences. Put optional technical depth in `details`.
- Include these sections in order: **Takeaway**, **Before**, **After**, **How it works**, **Why it matters**, and **Quiz**. Make **How it works** cover every changed path and connect it to the relevant code without adding a separate inventory section. Make **Quiz** five medium-difficulty interactive multiple-choice questions with concise feedback; avoid trivia and gotchas.
- Add one callout for the key definition, edge case, or tradeoff. Use progressive disclosure for low-impact or mechanical changes, but name their purpose so the whole change remains covered.

## Artifact requirements

- Write one responsive HTML file with a table of contents, semantic headings, inline CSS, and inline JavaScript. Do not load fonts, scripts, images, or data from the network.
- Save it outside the repository as `/tmp/YYYY-MM-DD-explanation-<slug>.html`, using today’s date and a filesystem-safe slug. Return the absolute path.
- Make visuals the dominant content and large enough to understand without zooming. Use high-contrast type, large visual targets, visible focus states, keyboard-accessible controls, and feedback that does not rely on color alone. Keep the page viewable by opening it directly.
- Put code in `<pre><code>…</code></pre>` and preserve whitespace with `white-space: pre` or `white-space: pre-wrap`.
- Verify links, quiz behavior, code blocks, full-scope coverage, accessibility, and final file existence before delivery.
