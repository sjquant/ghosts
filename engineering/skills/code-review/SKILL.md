---
name: code-review
description: Broad, read-only code review using general agents and complete result synthesis.
disable-model-invocation: true
---

Review the change read-only. Use general agents; give them the change context and questions only—no roles, review commands, or extra prompts.

Consider every question below. Mark irrelevant questions `N/A — <reason>`. The main agent answers each applicable question. Assign applicable questions once across one, two, or three agents without overlap.

- `Any correctness or operational risks, including bugs, edge cases, race conditions, resource leaks, performance bottlenecks, scalability concerns, or security issues?`
- `Any design or API issues when viewed from outside-in, deep-module, and dependency-direction perspectives, including hidden obligations, awkward call sites, leaky abstractions, or circular dependencies?`
- `Any opportunities to simplify or clarify the code through better naming, standard libraries, utilities, or existing abstractions?`
- `Any test smells—such as brittle or implementation-coupled tests, over-mocking, unclear intent, missing negative-path coverage, or surviving mutants?`

After all agents respond and before synthesizing the final findings, triage every candidate point through this question: `Does this feedback identify a real, evidenced, material issue, or would addressing it add unnecessary complexity, flag a nonexistent or unsupported bug, or provide little value?` Judge the feedback itself, not only whether another agent made the same point. Do not omit any candidate point. Assign `P0`, `P1`, `P2`, or `P3` when it is actionable; assign `SKIP` only as a priority label when it is false, unsupported, duplicate, contradicted, out of scope, or not worth acting on. `SKIP` never means remove the item: every candidate must remain in `Findings` with its priority and the reason for that judgment. Do not leave skipped candidates only in `Reviewer Results`.

- Write in the user's language.
- If a GitHub URL is supplied, use a bare, commit-pinned `blob` permalink with the smallest relevant line range in each `Location`.
- Otherwise, use repository-relative paths.
- `P0` is release-blocking, `P1` major, `P2` actionable, and `P3` low-priority.

```markdown
## Findings

### <P0|P1|P2|P3|SKIP> - <title>

- Location: [path/to/file.ext](path/to/file.ext:Lx)
- Kind: bug|performance|security|design|test|simplification|other
- Triage: <priority> — <why this feedback received this priority, including why it is low-value or unsupported when priority is `SKIP`>
- Evidence: <why this matters>
- Impact / fix: <impact and smallest useful action>

## Review Summary

- Agents used: `<n>`
- Verdict: `no blocking findings|findings require attention|manual review still required`

## Reviewer Results

- `<agent>`: <every response and the corresponding Findings item>
```

For GitHub-linked reviews, make `Location` a bare GitHub permalink, for example: `- Location: https://github.com/acme/project/blob/0123abc/src/parser.ts#L42-L48`.

If there are no actionable findings, say so while retaining every candidate in `Findings` with `SKIP` priority and its reason.
