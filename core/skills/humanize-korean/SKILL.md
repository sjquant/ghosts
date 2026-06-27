---
name: humanize-korean
description: >
  한국어 글의 번역투, 기계적 구조, AI 관용구, 균일한 리듬, 접속사 남발,
  장식적 서식을 줄이고 의미, 사실, 장르, 문체 격식은 보존한다.
disable-model-invocation: true
---

한국어 글의 문체, 리듬, 표현만 다듬는다. 자연스러움보다 의미 보존이 먼저다.

## 철칙

1. 사실, 주장, 수치, 날짜, 고유명사, 직접 인용, 법률 조항, 공식, 표준 기술 약어는 원문 그대로 둔다.
2. [references/quick-rules.md](references/quick-rules.md)에 매핑되는 구간만 수정한다.
3. 장르와 문체 격식을 보존한다.
4. 변경률 30% 초과는 경고, 50% 초과는 중단 또는 롤백한다.
5. 원문에 없던 비유, 예시, 주장, 인용, 전환, 강조를 추가하지 않는다.
6. 맞춤법 교정, 번역, 요약, 사실 보강, 새 글 작성으로 확장하지 않는다.

## 절차

1. [references/quick-rules.md](references/quick-rules.md)를 읽는다.
2. 입력이 `.txt` 또는 `.md` 경로이면 해당 파일을 읽고, 아니면 붙여넣은 텍스트를 원문으로 사용한다.
3. 한국어가 아니면 이 스킬은 한국어 텍스트만 처리한다고 안내하고 종료한다.
4. 장르가 명시되지 않았으면 첫 300자로 `칼럼`, `리포트`, `블로그`, `공적` 중 하나를 추정한다.
5. 보존 대상 구간을 제외하고 AI 티 구간을 탐지한다.
6. 다음 순서로 국소 수정한다:
   D 관용구 -> A 번역투 -> I 형식명사 -> G 완곡 표현 -> H 접속사 -> F 수식/명사화 -> B 영어 과다 -> C/J 구조와 장식 -> E 리듬.
7. 6항 자체검증을 수행한다. 위반한 수정은 롤백하고 같은 구간만 최대 1회 다시 시도한다.
8. 윤문본과 검증 요약을 응답한다.

## 참조

- [references/quick-rules.md](references/quick-rules.md): 빠른 탐지와 윤문 규칙.
- [references/ai-tell-taxonomy.md](references/ai-tell-taxonomy.md): 전체 패턴 분류.
- [references/rewriting-playbook.md](references/rewriting-playbook.md): 패턴별 문장 수정 처방.
- [references/metrics.py](references/metrics.py): 쉼표, 반복 어휘, 번역투 신호를 계산하는 단일 Python 보조 도구.

`metrics.py`는 표준 라이브러리만 쓰므로 Python으로 실행한다. 수정한 뒤에는 로컬 설치 대신 `uvx`로 정리와 검증을 실행한다:

```bash
python references/metrics.py --input input.txt --genre essay
uvx ruff format references/metrics.py
uvx ruff check references/metrics.py
uvx ty check references/metrics.py
```

## 출력

```markdown
완료. 변경률 X% / 등급 Y / 자체검증 N/6 통과

<윤문본>

핵심 탐지:
- A-2: N -> M
- D-1: N -> M

주요 변경:
- before -> after
```

## 등급

- `A`: S1 잔존 0, S2 잔존 2 이하, 변경률 10-25%, 자체검증 6/6.
- `B`: S1 잔존 0, S2 잔존 4 이하, 자체검증 5/6 이상.
- `C`: S1 잔존 1-2, 자체검증 4/6 이하, 저윤문 또는 과윤문 위험.
- `D`: S1 잔존 3 이상 또는 변경률 50% 초과. 중단하고 보고한다.

## 부분 윤문 지시

- "이 문단만": 요청한 문단만 수정한다.
- "번역투만", "관용구만", "이모지만": 해당 카테고리만 적용한다.
- "강도 낮춰": S1 수정만 적용한다.
- "강도 높여": S1, S2, 신중한 S3 리듬 수정을 적용한다.
- "2차 윤문": 직전 결과를 입력으로 삼고 1차보다 좁게 수정한다.
