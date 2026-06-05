---
name: review
description: Review code, branches, PRs, diffs, or proposed changes. Use for read-only review, not implementation or autofix.
disable-model-invocation: true
---

Review for actionable defects introduced or materially worsened by the change. Do not modify code, push commits, or hide reviewer results.

## Reviewer Routing

Use every reviewer whose trigger matches. Exclude lockfiles, generated files, vendored code, formatting-only diffs, and documentation-only diffs from LOC, file-count, and directory-count triggers unless they affect behavior or policy.

- `quality-reviewer`: use for any non-trivial behavior change, security/auth/data change, migration, config change, API contract change, or changed code `>= 20` LOC.
- `test-reviewer`: use when source behavior changes, tests are added/changed/deleted/skipped, or non-excluded source code changes are `>= 50` LOC. When coverage tools exist, use them inside the review.
- `architecture-reviewer`: use when public interfaces, module boundaries, ownership, dependency direction, state ownership, or cross-layer calls change; also use when changed code spans `>= 3` directories or `>= 150` LOC.
- `performance-reviewer`: use when a known hot path changes, unbounded loops or large-collection work changes, repeated I/O/serialization/parsing is added, caching/resource lifetime changes under load, or async/background work changes concurrency, backpressure, or retry behavior; also use when changed code in a likely hot path is `>= 80` LOC.
- `slop-reviewer`: use when non-excluded changed code is `>= 100` LOC, non-excluded changed files are `>= 5`, or the diff adds wrappers, duplicated logic, broad cleanup, generated-looking code, or unclear abstractions.

Add an explicit consistency, concurrency, repo-rule, migration, or release-safety check when the diff includes that risk and no installed reviewer covers it.

## Finding Standard

Report a finding only when all are true:

- Exact changed or adjacent `path:line` exists.
- The issue is introduced or materially worsened by the change.
- Evidence shows a concrete failure path, leak, regression, or maintainability risk.
- The suggested fix is local and proportionate.

Suppress style-only comments, generic framework advice, pre-existing unrelated issues, duplicate findings, and issues already guaranteed by lint/typecheck/CI unless release-critical.

Normalize findings to:

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

Verify reviewer findings before presenting them. Reject or downgrade findings without exact location, change causality, concrete evidence, or proportionate fix.

Show every received reviewer result after deduplication. If a reviewer finding is rejected or downgraded, include it under `Rejected/Adjusted` with the reason instead of silently omitting it.

## Output

Use the user's language and keep enum values in English.

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

## Re-review

For updated reviews, check prior findings first, verify fixes, look for new regressions, and keep still-relevant prior findings visible.
