---
name: review
description: Read-only review for code, branches, PRs, diffs, or proposed changes.
disable-model-invocation: true
---

Review actionable defects introduced or materially worsened by the change. Do not modify code, push commits, or hide reviewer results.

## Routing

Use every reviewer whose trigger matches the material risks. Exclude lockfiles, generated files, vendored code, formatting-only diffs, and documentation-only diffs unless they affect behavior or policy.

- `change-reviewer`: use for non-trivial behavior, security/auth/data, migrations, configuration, API or extension-point contracts, module boundaries, dependency direction, ownership, or unnecessary complexity.
- `solution-reviewer`: use when the change introduces an abstraction, dependency, schema, cache, fallback, state owner, extension-point contract, lifecycle/initialization ordering, cross-layer interaction, or other structural choice with plausible alternatives or meaningful reversal cost.
- `test-reviewer`: use when source behavior changes, tests change, or the change leaves a concrete public-contract coverage question.
- `performance-reviewer`: add only when a likely hot path, large-collection work, repeated I/O, caching/resource lifetime, or asynchronous throughput changes.

Use a general reviewer only when an uncovered material risk remains and delegation is available and proportionate. Otherwise inspect that risk directly. Parallelize independent reviews only when capacity is available; synthesize all results before reporting.

## Main Agent Review

Inspect the changed code directly, including the touched flow and the highest-risk caller-visible behavior. For bug fixes, check sibling callers when the changed code is shared. Independently consider whether the chosen direction solves the right problem or whether a materially different design would improve ownership, cohesion, coupling, or failure handling. Look for unnecessary behavior, duplicated logic, needless wrappers, and unverified risk; do not invent alternatives or expand a focused review into an unrelated refactor.

## Synthesis

Report every distinct issue and design alternative raised by every reviewer after deduplication. Do not silently omit one based on perceived importance, confidence, or comment worthiness. Promote supported issues to `Findings`; if a reviewer is wrong, preserve the issue in `Reviewer Results` and explain the technical reason for rejecting it. Keep valid non-defect alternatives in `Design Alternatives`. Adjust severities as needed and apply the final severity directly to each finding.

## Output

Use the user's language. Keep enum values in English.
Use repository-relative paths in every location. Never report absolute filesystem paths.

Use these severity values:

- `P0`: Release-blocking issue. Security incident, data loss, or whole-service outage risk.
- `P1`: Major regression that must be fixed. Core workflow breakage or broad user impact.
- `P2`: Standard actionable bug. Conditional functional failure, misleading UX, or missing validation.
- `P3`: Low-priority issue. Small accessibility, maintainability, quality, or edge-case risk.

```markdown
## Findings

### P1 - <title>

- Location: [path/to/file.ext](path/to/file.ext:Lx) `path/to/file.ext:Lx-Ly`
- Category: correctness|security|tests|architecture|performance|concurrency|consistency|code-quality|repo-rule
- Evidence: <why this is a real issue>
- Failure mode: <what breaks, leaks, or regresses>
- Suggested fix: <minimal fix direction>

## Review Summary

- Reviewed files: `<n>`
- Reviewers used: `<reviewer list>`
- Verdict: `no blocking findings|findings require attention|manual review still required`

## Reviewer Results

- `<reviewer>`: <every distinct raised issue or alternative and its disposition>

## Design Alternatives

### Prefer <alternative>

- Current approach: <chosen direction>
- Alternative: <materially different direction>
- Why it may be better: <concrete benefit>
- Tradeoffs: <costs and drawbacks>
- Recommendation: `keep current|switch|spike`

- `None found` when no materially better direction exists

## Simplification Points

- `<path/to/file.ext:Lx>`: `<delete|stdlib|native|yagni|shrink>` <what to cut and what replaces it>
- `net: -<N> lines possible` when simplification points exist
- `None found` when no concrete behavior-preserving simplification exists
```

If there are no findings, say so directly and list the highest-risk areas checked. Do not invent issues to fill the template.
