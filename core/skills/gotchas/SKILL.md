---
name: gotchas
description: Extract 1-3 reusable gotchas from the current session. Use when the user wants concise lessons about tooling mistakes, verification gaps, or process issues to avoid next time.
disable-model-invocation: true
---

Extract 1-3 reusable gotchas from this session. No gotchas is acceptable.

Core test: would remembering this prevent likely rework, rediscovery, or verification gaps in a future session?

Prefer high time-cost lessons over code-specific nits. Call out assistant-side execution mistakes.

## Method

1. Review the session for mistakes, slowdowns, repeated confusion, and skipped checks.
2. Keep only issues likely to recur.
3. Prefer the smallest durable lesson over a long narrative.
4. If multiple tools or paths were used for the same task, name the default path for next time.
5. If the lesson needs standardization, propose one concrete follow-up.

## Selection

Prioritize:

1. Tooling command mistakes or rediscovery costs.
2. Verification flow gaps.
3. Process mistakes that caused rework.
4. Agent, CLI, browser, or invocation confusion.

Skip:

- One-off issues that were fully resolved.
- Pure implementation details unlikely to recur.
- Lessons that only restate obvious best practices.

## Output

```markdown
## Gotchas

**Total:** X

[TOOLING] Short title
Problem: What slowed us down or caused confusion.
Next time: Concrete default, check, or follow-up.

[VERIFICATION] Short title
Problem: What check was missing, late, or noisy.
Next time: Exact check or verification order to use.
```

Use categories only when useful: `TOOLING`, `VERIFICATION`, `PROCESS`, `CONTEXT`.
Keep each gotcha to 2 lines after the title.

If there are no gotchas, output:

```markdown
## Gotchas

No reusable gotchas from this session.
```
