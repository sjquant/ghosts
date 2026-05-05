---
name: gotchas
description: Extract 1-3 reusable gotchas from the current session. Use when the user wants concise lessons about tooling mistakes, verification gaps, or process issues to avoid next time.
disable-model-invocation: true
---

From this session, extract 1-3 gotchas that would help us move faster next time. No gotchas are acceptable.

Prioritize:
1. tooling command mistakes or rediscovery costs
2. verification flow gaps
3. process mistakes that caused rework

Include agent/CLI/browser invocation confusion if it happened.
Prefer the highest time-cost mistakes, not just code/design issues.
Call out assistant-side execution mistakes too.

## Format:

1. **Problem**: ...
   **Next Time**: ...
2.  **Problem**: ...
   **Next Time**: ...

## Rules:
- Use max 1-3 lines per gotcha.
- Only include unresolved issues or pitfalls likely to recur.
- Skip one-off issues that were fully fixed in this session.
- Focus on things that would save time in a future session.
- When multiple tools/paths were used for the same task, say which path should become the default next time.
- If the issue suggests standardization, explicitly say so and propose one concrete follow-up such as: add a runbook, document the preferred CLI path, or update the verification checklist.

## Examples

### Good example:
1. **Problem**: We changed implementation details before agreeing on the intended UX, so review comments and docs were correct for the code but wrong for the product.
    **Next Time:** Lock the user-facing contract first, then align implementation, tests, and docs to that contract.

### Bad example:
1. **Problem**: src/foo.ts used the wrong helper.
    **Next Time**: Use bar() instead.
