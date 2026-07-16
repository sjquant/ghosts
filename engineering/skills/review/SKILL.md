---
name: review
description: Read-only review for code, branches, PRs, diffs, or proposed changes.
disable-model-invocation: true
---

Review actionable defects introduced or materially worsened by the change. Do not modify code, push commits, or hide reviewer results.

## Routing

Use every reviewer whose trigger matches the material risks. Exclude lockfiles, generated files, vendored code, formatting-only diffs, and documentation-only diffs unless they affect behavior or policy.

- `change-reviewer`: use for non-trivial behavior, security/auth/data, migrations, configuration, API contracts, module boundaries, dependency direction, ownership, or unnecessary complexity.
- `test-reviewer`: use when source behavior changes, tests change, or the change leaves a concrete public-contract coverage question.
- `performance-reviewer`: add only when a likely hot path, large-collection work, repeated I/O, caching/resource lifetime, or asynchronous throughput changes.

Use a general reviewer only when an uncovered material risk remains and delegation is available and proportionate. Otherwise inspect that risk directly. Parallelize independent reviews only when capacity is available; synthesize all results before reporting.

## Main Agent Review

Inspect the changed code directly, including the touched flow and the highest-risk caller-visible behavior. For bug fixes, check sibling callers when the changed code is shared. Look for unnecessary behavior, duplicated logic, needless wrappers, and unverified risk; do not expand a focused review into an unrelated refactor.

## Synthesis

Show every received reviewer result after deduplication. Adjust severities as needed and apply the final severity directly to each finding.

## Output

Use the user's language. Keep enum values in English.

Use these severity values:

- `P0`: Release-blocking issue. Security incident, data loss, or whole-service outage risk.
- `P1`: Major regression that must be fixed. Core workflow breakage or broad user impact.
- `P2`: Standard actionable bug. Conditional functional failure, misleading UX, or missing validation.
- `P3`: Low-priority issue. Small accessibility, maintainability, quality, or edge-case risk.

```markdown
## Findings

### P1 - <title>

- Location: [path/to/file.ext](/absolute/path/to/repo/path/to/file.ext:Lx) `path/to/file.ext:Lx-Ly`
- Category: correctness|security|tests|architecture|performance|concurrency|consistency|code-quality|repo-rule
- Evidence: <why this is a real issue>
- Failure mode: <what breaks, leaks, or regresses>
- Suggested fix: <minimal fix direction>

## Review Summary

- Reviewed files: `<n>`
- Reviewers used: `<reviewer list>`
- Verdict: `no blocking findings|findings require attention|manual review still required`

## Reviewer Results

- `<reviewer>`: <received result summary or findings>
```

Include `## Simplification Points` when the review identifies a concrete behavior-preserving simplification. Omit the section when none exists.

If there are no findings, say so directly and list the highest-risk areas checked. Do not invent issues to fill the template.
