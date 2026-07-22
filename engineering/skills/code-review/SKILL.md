---
name: code-review
description: Broad, read-only code review using general agents and complete result synthesis.
disable-model-invocation: true
---

Review the change without modifying, committing, or pushing. Use general-purpose agents only; do not create role-specific reviewers or ad hoc prompts.

Read the request, diff, relevant callers, public boundaries, tests, and repository instructions. The main agent must answer all eight questions below. If subagents are available, ask the same questions exactly once across one, two, or three subagents, splitting them according to change size and complexity. Give each subagent only its assigned questions. If subagents are unavailable, review with the main agent only.

- `Any potential bugs or edge cases?`
- `Any performance bottlenecks?`
- `Any security issues?`
- `Any opportunities to simplify the code using utilities, standard libraries, or existing abstractions?`
- `Any structural improvements from deep-module and dependency-direction perspectives?`
- `Any unclear or misleading names?`
- `Any test readability issues, missing failure cases, or weaknesses that mutation testing would reveal?`
- `Any other design improvements?`

Verify the responses against the code and run relevant checks. Collect every distinct point from every agent. Deduplicate only; remove a point only when it is demonstrably false, duplicated, contradicted by the code or user's settled decision, or otherwise clearly not an issue. Keep uncertain, low-priority, design, performance, test, and simplification points as findings. Record every point and its disposition in `Reviewer Results`.

Write in the user's language. Use repository-relative paths only; never report absolute filesystem paths. Use `P0` for release-blocking risk, `P1` for major regression, `P2` for actionable bug, and `P3` for low-priority issue or improvement.

```markdown
## Findings

### P1 - <title>

- Location: [path/to/file.ext](path/to/file.ext:Lx) `path/to/file.ext:Lx-Ly`
- Kind: bug|performance|security|design|test|simplification|other
- Evidence: <why this matters>
- Impact: <what breaks, regresses, costs, or remains unverified>
- Suggested fix or next check: <smallest useful action>

## Review Summary

- Reviewed files: `<n>`
- Agents used: `<n>`
- Verdict: `no blocking findings|findings require attention|manual review still required`

## Reviewer Results

- `<agent>`: <every point and its disposition: `merged into Finding P#`, `preserved as Finding P#`, or `removed: <reason>`>
```

If there are no findings, say so, list the highest-risk areas checked, and still include the complete reviewer audit trail.
