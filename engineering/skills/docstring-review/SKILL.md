---
name: ghosts:docstring-review
description: Read-only review of docstrings, TSDoc, descriptions, and inline comments for standalone domain purpose rather than implementation details or implicit context.
disable-model-invocation: true
---

Review docstrings, TSDoc, schema/tool or test descriptions, and inline comments read-only. Use the user's target or the change being discussed; otherwise review the current branch's diff against its base, including uncommitted changes. Inspect the implementation and relevant callers to establish purpose.

- Any docstring, description, or comment that narrates internal steps, enumerates permissions, side effects, and error handling, or encodes implicit dependencies on callers, collaborators, or prior context instead of stating purpose in domain terms?
- Recommend a concise purpose statement (usually one sentence) or omission when the name and signature already make the purpose obvious. Prefer wording that remains accurate when implementation details (`how`), fields, or conditions change while the purpose (`what`) stays the same. Use domain terms supported by the code; do not invent intent or guarantees.
- Preserve contract details callers need in separate documentation sections or paragraphs. Permissions, side effects, or failures may belong in the summary when they define the function's domain purpose; do not flag them merely for appearing there.

Report only summaries, descriptions, or comments that obscure purpose or couple documentation to implementation details. Do not request missing docstrings, expand the review to unrelated documentation, or flag harmless wording preferences.

Write findings in the user's language. For each finding, include the file and line, the existing summary, why it obscures the purpose, and a proposed replacement summary. Use commit-pinned permalinks for GitHub targets. State when no actionable findings were found and disclose any material review limitations.

## Examples

Review summaries that start with the purpose but then append implementation steps or enumerate results. Details callers need do not all belong in the summary. Apply the examples using the implementation and relevant callers; do not infer unsupported purposes or guarantees from the wording alone.

### Revise

| Before | After |
| --- | --- |
| 조직을 조회하고 요청한 강도로 행을 잠급니다. | 조직 ID로 조직을 조회합니다. |
| 이메일 형식·차단 도메인·오타 도메인·MX 또는 A 레코드를 확인합니다. | 이메일 주소가 발송 검증 정책을 충족하는지 확인합니다. |
| 동일한 요청을 한 번만 발송하고 접수·제외·실패·결과 불명을 기록합니다. | 메일 요청의 중복 발송을 방지하고 처리 결과를 관리합니다. |
| 새 요청을 발송하고 결과를 반환하며 기존 요청은 duplicate로 제외합니다. | 중복 발송을 방지하며 메일을 전송합니다. |
| 이메일 도메인의 DNS 레코드를 조회하고 성공한 결과를 캐시합니다. | 이메일 도메인의 DNS 레코드를 조회합니다. |

Move removed contract details to separate documentation where needed:

- Lock options and mutually exclusive arguments → Args and Raises.
- Return statuses and duplicate-request handling → Returns.
