---
name: gotchas
description: Extract 1-3 reusable gotchas from the current session. Use when the user wants concise lessons about tooling mistakes, verification gaps, or process issues to avoid next time.
disable-model-invocation: true
---

Extract 1-3 reusable gotchas from this session. No gotchas is acceptable.

Core question: would remembering this prevent likely rework, rediscovery, or verification gaps in a future session?

## Selection

Review mistakes, slowdowns, repeated confusion, skipped checks, and assistant-side execution errors. Keep only recurring, high time-cost lessons.

Prioritize:

1. Tooling command mistakes or rediscovery costs.
2. Verification flow gaps.
3. Process mistakes that caused rework.
4. Agent, CLI, browser, or invocation confusion.

Skip one-off issues, fully resolved problems, code-specific nits, and obvious best practices. If a lesson needs standardization, propose one concrete follow-up. If multiple tools or paths were used for the same task, name the default path for next time.

## Output

```markdown
## Gotchas

**Total:** X

[TOOLING] Short title
Problem: What slowed us down or caused confusion.
Next time: Concrete default, check, or follow-up.
```

Use categories only when useful: `TOOLING`, `VERIFICATION`, `PROCESS`, `CONTEXT`.
Keep each gotcha to the title plus `Problem` and `Next time`.

If there are no gotchas, output:

```markdown
## Gotchas

No reusable gotchas from this session.
```
