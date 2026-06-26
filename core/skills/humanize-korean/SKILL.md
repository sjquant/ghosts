---
name: humanize-korean
description: >
  한국어 글의 번역투, 기계적 구조, AI 관용구, 균일한 리듬, 접속사 남발,
  장식적 서식을 줄이고 의미, 사실, 장르, 문체 격식은 보존한다.
disable-model-invocation: true
---

한국어 글의 문체, 리듬, 표현만 다듬는다. 자연스러움보다 의미 보존이 먼저다.

## 철칙

1. 사실, 주장, 수치, 날짜, 고유명사, 직접 인용, 법률 조항, 공식, 표준 기술
   약어는 원문과 정확히 일치해야 한다.
2. [references/quick-rules.md](references/quick-rules.md)에 매핑되는 구간만
   수정한다.
3. 장르를 보존한다. 칼럼, 리포트, 블로그, 공적 문서는 원래 장르 안에 남겨둔다.
4. 문체 격식을 보존한다. 격식체는 격식체로, 구어체는 구어체로 둔다.
5. 과윤문을 피한다. 변경률 30% 초과는 경고, 50% 초과는 중단 또는 롤백한다.
6. 원문에 없던 비유, 예시, 주장, 인용, 전환, 강조를 추가하지 않는다.
7. 맞춤법 교정, 번역, 요약, 사실 보강, 새 글 작성처럼 내용이 바뀌는 작업으로
   확장하지 않는다.

## 절차

1. [references/quick-rules.md](references/quick-rules.md)를 읽는다.
2. 입력이 `.txt` 또는 `.md` 경로이면 해당 파일을 읽고, 아니면 붙여넣은 텍스트를
   원문으로 사용한다.
3. 한국어가 아니면 이 스킬은 한국어 텍스트만 처리한다고 짧게 안내하고 종료한다.
4. 사용자가 장르를 명시하지 않았으면 첫 300자로 장르를 추정한다:
   `칼럼`, `리포트`, `블로그`, 또는 `공적`.
5. 빠른 규칙으로 AI 티 구간을 찾는다. 보존 대상 구간은 모두 제외한다.
6. 다음 순서로 국소 수정한다:
   D 관용구 -> A 번역투 -> I 형식명사 -> G 완곡 표현 -> H 접속사 ->
   F 수식/명사화 -> B 영어 과다 -> C/J 구조와 장식 -> E 리듬.
7. 빠른 규칙의 6항 자체검증으로 결과를 점검한다. 철칙을 깨는 수정은 롤백하고
   해당 국소 수정만 최대 1회 다시 시도한다.
8. 사용자가 인라인 결과를 원하면 본문을 바로 반환한다. 주변 에이전트 흐름이
   산출물을 저장하는 방식이면 `_workspace/{YYYY-MM-DD-NNN}/final.md`에 쓰고
   응답은 짧게 유지한다.

## 참조 자료

- [references/quick-rules.md](references/quick-rules.md): 빠른 탐지와 윤문에 쓰는 S1/S2 핵심 룰.
- [references/ai-tell-taxonomy.md](references/ai-tell-taxonomy.md): 10대 분류와 세부 패턴의 SSOT.
- [references/rewriting-playbook.md](references/rewriting-playbook.md): 탐지 결과를 실제 문장 수정으로 옮기는 처방집.
- [references/scholarship.md](references/scholarship.md): 한국어 번역투와 후편집 관련 학술 근거.
- [references/metrics.py](references/metrics.py), [references/metrics_v2.py](references/metrics_v2.py): 표준 라이브러리 기반 정량 지표 계산기.
- [references/baseline.json](references/baseline.json), [references/baseline_v2.json](references/baseline_v2.json): 정량 지표 baseline.
- [references/web-service-spec.md](references/web-service-spec.md): 웹 서비스 확장 시에만 참고하는 옵션 스펙.

## 출력

기본 응답:

```markdown
완료. 변경률 X% / 등급 Y / 자체검증 N/6 통과

<윤문본>

핵심 탐지:
- A-2: N -> M
- D-1: N -> M

주요 변경:
- before -> after
```

사용자가 파일을 제공했거나 출력이 길면 전체 결과는
`_workspace/{YYYY-MM-DD-NNN}/final.md`에 저장하고, 상태, 핵심 탐지, 변경
하이라이트 1건, 파일 경로만 반환한다.

## 등급

- `A`: S1 잔존 0, S2 잔존 2 이하, 변경률 10-25%, 자체검증 6/6.
- `B`: S1 잔존 0, S2 잔존 4 이하, 자체검증 5/6 이상.
- `C`: S1 잔존 1-2, 자체검증 4/6 이하, 또는 저윤문/과윤문 위험이 뚜렷함.
- `D`: S1 잔존 3 이상 또는 변경률 50% 초과. 중단하고 보고한다.

## 부분 윤문 지시

- "이 문단만": 요청한 문단만 수정한다.
- "번역투만", "관용구만", "이모지만": 해당 카테고리만 적용한다.
- "강도 낮춰": S1 수정만 유지한다.
- "강도 높여": S1, S2, 신중한 S3 리듬 수정을 적용한다.
- "2차 윤문": 직전 결과를 입력으로 삼되 철칙을 그대로 지키고, 2차 수정 범위는
  1차보다 좁게 잡는다.
