---
name: review
description: Read-only review for code, branches, PRs, diffs, or proposed changes.
disable-model-invocation: true
---

Review actionable defects introduced or materially worsened by the change. Do not modify code, push commits, or hide reviewer results.

## Routing

Use every reviewer whose trigger matches. Exclude lockfiles, generated files, vendored code, formatting-only diffs, and documentation-only diffs from LOC, file-count, and directory-count triggers unless they affect behavior or policy.

- `quality-reviewer`: use for any non-trivial behavior change, security/auth/data change, migration, config change, API contract change, or changed code `>= 20` LOC.
- `test-reviewer`: use when source behavior changes, tests are added/changed/deleted/skipped, or non-excluded source code changes are `>= 50` LOC.
- `architecture-reviewer`: use when public interfaces, module boundaries, ownership, dependency direction, state ownership, or cross-layer calls change; also use when changed code spans `>= 3` directories or `>= 150` LOC.
- `performance-reviewer`: use when a known hot path changes, unbounded loops or large-collection work changes, repeated I/O/serialization/parsing is added, caching/resource lifetime changes under load, or async/background work changes concurrency, backpressure, or retry behavior; also use when changed code in a likely hot path is `>= 80` LOC.
- `slop-reviewer`: use when non-excluded changed code is `>= 100` LOC, non-excluded changed files are `>= 5`, or the diff adds wrappers, duplication, broad cleanup, generated-looking code, or unclear abstractions.

Spawn a bounded general subagent for consistency, concurrency, repo-rule, migration, or release-safety risks when no installed reviewer covers that risk.

## Findings

Report only findings with:

- Exact changed or adjacent `path:line` exists.
- Change causality.
- Concrete failure path, leak, regression, or maintainability risk.
- Local, proportionate suggested fix.

Suppress style-only comments, generic advice, pre-existing unrelated issues, duplicates, and issues already guaranteed by lint/typecheck/CI unless release-critical.

Use this schema:

```json
{
  "severity": "CRITICAL | HIGH | MEDIUM | LOW",
  "title": "Short risk title",
  "file": "path/from/repo/root",
  "line_start": 1,
  "line_end": 1,
  "category": "correctness | security | tests | architecture | performance | concurrency | consistency | code-quality | repo-rule",
  "evidence": "Why this is a real issue.",
  "failure_mode": "What breaks, leaks, or regresses.",
  "suggested_fix": "Minimal fix direction."
}
```

## Synthesis

Show every received reviewer result after deduplication. If a reviewer finding is rejected or downgraded, include it under `Rejected/Adjusted` with the reason instead of silently omitting it.

## Output

Use the user's language. Keep enum values in English.

```markdown
## Findings

### HIGH - <title>

- Location: `path/to/file.ext:Lx-Ly`
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

## Rejected/Adjusted

- <rejected or downgraded reviewer findings and reasons. Omit if empty.>
```

If there are no findings, say so directly and list the highest-risk areas checked. Do not invent issues to fill the template.
