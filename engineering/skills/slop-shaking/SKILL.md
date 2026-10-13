---
name: ghosts:slop-shaking
description: Use when the user asks to remove slop, mentions $slop-shaking, or asks whether anything in a change is unnecessary.
---

Review the code, PR, or diff specified by the user; otherwise use the change being discussed. Inspect its callers and tests.

Give one general subagent the change context and this prompt:

```text
Review the change read-only:

AI-generated changes can overcomplicate simple problems; look for a simpler solution and question whether the added code or tests are needed at all.

- Any low-value, duplicate, implementation-shaped, or one-off tests that can be removed or combined without losing meaningful behavior, edge-case, or risk coverage? Any tests for hypothetical concurrency or timing risks without a credible execution path or meaningful failure impact?
- Any unnecessary variables or intermediate state that can be omitted, inlined, or reused without obscuring intent?
- Any unnecessary interfaces or abstractions? Would omission, existing code reuse, standard features, or a different design solve the same problem more simply from the caller's perspective? Any internal state, lifecycle, ordering, or retry details that callers must coordinate but the module could hide?

Report findings with locations, evidence, and the smallest useful cleanup. Say when no useful cleanup is found.
```

After the subagent responds, judge each suggestion: does it remove real slop, or add complexity for little benefit? Apply supported cleanups, preserve intended behavior, and run relevant checks. If asked for review only, report without editing. Recheck affected changes; briefly explain what was removed or combined and why, including reasons for rejected suggestions. Leave the change unchanged when no useful cleanup remains.

Report in the user's language using the format below. Keep every candidate, including rejected suggestions as `SKIP` with a reason. Use `PROPOSED` for review-only findings and `BLOCKED` for unresolved cleanups. If there are no findings, say so.

```markdown
## Findings

### <APPLIED|PROPOSED|BLOCKED|SKIP> - <title>

- Location: <file and line; commit-pinned permalink for GitHub targets>
- Kind: test|variable|interface
- Evidence / rule: <concrete evidence and the cleanup criterion>
- Change / reason: <what changed or is proposed, or why it was blocked or skipped>
```
