---
name: review
description: Read-only review for code, branches, PRs, diffs, or proposed changes.
disable-model-invocation: true
---

Review actionable defects introduced or materially worsened by the change. Do not modify code, push commits, or hide reviewer results.

## Routing

Use every reviewer whose trigger matches. Exclude lockfiles, generated files, vendored code, formatting-only diffs, and documentation-only diffs from LOC, file-count, and directory-count triggers unless they affect behavior or policy.

- `quality-reviewer`: use for any non-trivial behavior change, security/auth/data change, migration, config change, API contract change, or changed code `>= 20` LOC.
- `test-reviewer`: use when source behavior changes, tests are added/changed/deleted/skipped, or non-excluded source code changes are `>= 200` LOC.
- `architecture-reviewer`: use when public interfaces, module boundaries, ownership, dependency direction, state ownership, or cross-layer calls change; also use when changed code spans `>= 3` directories or `>= 200` LOC.
- `performance-reviewer`: use when a known hot path changes, unbounded loops or large-collection work changes, repeated I/O/serialization/parsing is added, caching/resource lifetime changes under load, or async/background work changes concurrency, backpressure, or retry behavior; also use when changed code in a likely hot path is `>= 80` LOC.
- `slop-reviewer`: use when non-excluded changed code is `>= 200` LOC, non-excluded changed files are `>= 5`, or the diff adds wrappers, duplication, broad cleanup, generated-looking code, or unclear abstractions.

Spawn a bounded general subagent for consistency, concurrency, repo-rule, migration, or release-safety risks when no installed reviewer covers that risk.

## Synthesis

Show every received reviewer result after deduplication. If a reviewer finding is adjusted or downgraded, include it under `Adjusted` with the reason.

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

## Adjusted

- <adjusted or downgraded reviewer findings and reasons. Omit if empty.>
```

If there are no findings, say so directly and list the highest-risk areas checked. Do not invent issues to fill the template.
