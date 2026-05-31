---
name: prompt-rewriter
description: Rewrite prompts to maximize signal-to-noise while preserving behavior-changing information.
disable-model-invocation: true
---

Rewrite prompts to maximize signal-to-noise: preserve behavior-changing information and remove everything else.

## Definitions

- **Signal**: intent, constraints, context, inputs, definitions, output format, success criteria, and edge cases.
- **Noise**: filler, repetition, vague advice, generic best practices, decorative wording, conflicts, and irrelevant detail.

## Rules

1. Put the main task first.
2. Preserve the user's real goal and meaningful constraints.
3. Use the shortest wording that reliably produces the intended behavior.
4. Remove anything that does not affect the output.
5. Group related instructions and order them by importance.
6. Replace vague requirements with observable criteria.
7. Use compact domain terms only when they clearly constrain behavior.
8. If a term has multiple interpretations, add the smallest qualifier needed.
9. Keep examples only when they prevent likely mistakes.
10. Do not invent facts, tools, policies, sources, or requirements.
11. Ask clarifying questions when the prompt cannot be safely or usefully rewritten without them.
