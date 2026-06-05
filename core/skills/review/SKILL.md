---
name: review
description: Review code, branches, PRs, diffs, or proposed changes. Use for read-only review, not implementation or autofix.
disable-model-invocation: true
---

Review for actionable defects introduced or materially worsened by the change. Do not modify code, push commits, or hide reviewer results.

## Reviewer Routing

Use every reviewer whose trigger matches. Exclude lockfiles, generated files, vendored code, formatting-only diffs, and documentation-only diffs from line-count triggers unless they affect behavior or policy.

- `quality-reviewer`: use for any non-trivial behavior change, security/auth/data change, migration, config change, API contract change, or changed code `>= 20` LOC.
- `test-reviewer`: use when source behavior changes, tests are added/changed/deleted/skipped, coverage tools exist for the touched area, or changed code `>= 20` LOC.
- `architecture-reviewer`: use when public interfaces, module boundaries, ownership, dependency direction, state ownership, or cross-layer calls change; also use when changed code spans `>= 3` directories or `>= 150` LOC.
- `performance-reviewer`: use when loops, large collections, I/O, caching, serialization, async/background work, resource lifetime, or hot-path code changes; also use when changed code in a likely hot path is `>= 80` LOC.
- `slop-reviewer`: use when non-excluded changed code is `>= 100` LOC, changed files are `>= 5`, or the diff adds wrappers, duplicated logic, broad cleanup, generated-looking code, or unclear abstractions.

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

Show every received reviewer result after deduplication. If a reviewer finding is rejected or downgraded, include it under `검토 제외/조정` with the reason instead of silently omitting it.

## Output

Unless the user requests another language, write the final review in Korean and keep enum values in English.

```markdown
## 발견 사항

### HIGH - <제목>

- Location: `path/to/file.ext:Lx-Ly`
- Category: correctness|security|tests|architecture|performance|concurrency|consistency|code-quality|repo-rule
- 근거: <왜 실제 문제인지>
- 실패 모드: <무엇이 깨지거나 회귀되는지>
- 제안 수정: <최소 수정 방향>

## 리뷰 요약

- 리뷰한 파일 수: `<n>`
- 사용한 reviewer: `<reviewer list>`
- 판정: `no blocking findings|findings require attention|manual review still required`

## reviewer 결과

- `<reviewer>`: <받은 결과 요약 또는 finding 목록>

## 검토 제외/조정

- <reject/downgrade한 reviewer finding과 이유. 없으면 생략.>
```

If there are no findings, say so directly and list the highest-risk areas checked. Do not invent issues to fill the template.

## Re-review

For updated reviews, check prior findings first, verify fixes, look for new regressions, and keep still-relevant prior findings visible.
