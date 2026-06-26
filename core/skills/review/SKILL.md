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
- `slop-reviewer`: use when non-excluded changed code is `>= 120` LOC, non-excluded changed files are `>= 4`, or the diff adds wrappers, duplication, broad cleanup, generated-looking code, unclear abstractions, new dependencies, factories, adapters, config knobs, or helper layers.

Spawn a bounded general subagent for consistency, concurrency, repo-rule, migration, or release-safety risks when no installed reviewer covers that risk.

## Main Agent Review

While subagents are collecting results, inspect the changed code directly for simplification points. First ask whether the new behavior needs to exist. Then prefer, in order: existing codebase helpers, standard library, native platform features, already-installed dependencies, one-line expressions, and finally the smallest safe implementation. Look for needless variables, branches, helper functions, wrappers, intermediate state, duplicated control flow, indirect expressions, verbose phrasing, new dependencies, speculative config, single-implementation interfaces, or abstractions with one caller.

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

## Simplification Points

- `<path/to/file.ext:Lx>`: `<delete|stdlib|native|yagni|shrink>` <what to cut and what replaces it, or `None found`>
- `net: -<N> lines possible` when any simplification points exist
```

Always include `## Simplification Points`. Use `None found` when the direct review found no concise simplification opportunities.

If there are no findings, say so directly and list the highest-risk areas checked. Do not invent issues to fill the template.
