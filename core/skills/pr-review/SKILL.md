---
name: pr-review
description: Review a PR, branch, or diff against a base branch. Use for read-only code review, not implementation or autofix unless explicitly requested.
disable-model-invocation: true
---

Review the change for actionable defects introduced or materially worsened by the PR. Default to read-only: do not edit files, push commits, run destructive commands, or post GitHub comments unless explicitly asked.

## Inputs

Infer missing inputs when safe:

- Base: PR base if available; otherwise `origin/main`, `main`, `origin/master`, then `master`.
- Head: current `HEAD`.
- Output: final response only unless the user asks to post to GitHub.

Ask only when the base or scope cannot be inferred and the wrong choice would change the review.

## Review Mode

Use the cheapest sufficient path:

- Summary-only: generated, vendored, formatting-only, lockfile-only, or documentation-only diffs without behavior or policy impact.
- Single-agent: small, localized, low-risk diffs.
- Multi-reviewer: broad, risky, cross-boundary, security-sensitive, test-sensitive, performance-sensitive, migration, concurrency, or hard-to-understand diffs.

When using multiple reviewers, keep fan-out bounded and synthesize only after all results are checked.

## Reviewer Lenses

Use installed agents when their lens materially improves coverage; otherwise perform the equivalent read-only check yourself.

- `quality-reviewer`: spec fit, correctness, security, maintainability, verification.
- `test-reviewer`: public-contract tests, coverage output, uncovered code, covered-path edge cases.
- `architecture-reviewer`: ownership, caller knowledge, interface depth, test-only exposure.
- `performance-reviewer`: hot paths, complexity, memory, I/O, caching, profiling evidence.
- `slop-reviewer`: behavior-preserving cleanup risk, dead code, duplication, needless wrappers.

Add ad hoc checks for repo rules, consistency, concurrency, migrations, or release safety when the diff makes them relevant.

## Finding Standard

Publish a finding only when all are true:

- Exact changed or adjacent `path:line` exists.
- The PR introduced or materially worsened the issue.
- Evidence shows a concrete failure path, leak, regression, or maintainability risk.
- Confidence is `>= 0.75`.
- The suggested fix is local and proportionate.

Suppress style-only comments, generic framework advice, pre-existing unrelated issues, duplicate findings, and issues already guaranteed by lint/typecheck/CI unless release-critical.

Normalize findings to:

```json
{
  "severity": "P0 | P1 | P2 | Nit",
  "confidence": 0.9,
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

Severity:

- `P0`: critical vulnerability, data loss, severe outage, or irreversible production break.
- `P1`: likely serious bug, security issue, data leak, auth/tenant bypass, migration break, or high-impact regression.
- `P2`: real issue with moderate impact or narrower triggering conditions.
- `Nit`: low-risk issue; omit unless requested or hiding a real defect.

## Synthesis

Verify every reviewer finding before presenting it. Reject or downgrade findings without exact location, PR causality, concrete evidence, or proportionate fix. Merge duplicates; raise confidence only when independent evidence supports the same issue.

## Output

Unless the user requests another language, write the final review in Korean and keep enum values in English.

```markdown
## 발견 사항

### P1 - <제목>

- Location: `path/to/file.ext:Lx-Ly`
- Category: correctness|security|tests|architecture|performance|concurrency|consistency|code-quality|repo-rule
- 신뢰도: 0.xx
- 근거: <왜 실제 문제인지>
- 실패 모드: <무엇이 깨지거나 회귀되는지>
- 제안 수정: <최소 수정 방향>

## 리뷰 요약

- Base: `<base>`
- Head: `<head>`
- 리뷰한 파일 수: `<n>`
- 리뷰 모드: `summary-only|single-agent|multi-reviewer`
- 판정: `no blocking findings|findings require attention|manual review still required`

## 참고 사항

- <중요한 관찰만 포함. 없으면 생략.>

## 리뷰 커버리지

- <사용한 reviewer lens와 확인 범위>
```

If there are no findings, say so directly and list the highest-risk areas checked. Do not invent issues to fill the template.

## GitHub Posting

Do not post to GitHub unless explicitly asked. If asked, post inline comments only for `P0` and `P1`; include `P2` in a summary comment; omit `Nit` unless requested.

## Re-review

For updated PRs, check prior findings first, verify fixes, look for new regressions, and suppress old nits unless still materially relevant.
