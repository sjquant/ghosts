---
name: humanize-korean
description: >
  한국어 글의 번역투, 기계적 구조, AI 관용구, 균일한 리듬, 접속사 남발,
  장식적 서식을 줄이고 의미, 사실, 장르, 문체 격식은 보존한다.
disable-model-invocation: true
---

한국어 글의 문체, 리듬, 표현만 국소적으로 다듬는다.

## 철칙

1. 의미 보존이 자연스러움보다 우선이다.
2. 사실, 주장, 수치, 날짜, 고유명사, 직접 인용, 법률 조항, 공식, 표준 기술 약어는 바꾸지 않는다.
3. [references/quick-rules.md](references/quick-rules.md)에 매핑되는 구간만 수정한다.
4. 장르와 문체 격식을 유지한다.
5. 원문에 없는 비유, 예시, 주장, 인용, 전환, 강조를 추가하지 않는다.
6. 변경률 30% 초과는 경고, 50% 초과는 중단 또는 롤백한다.
7. 맞춤법 교정, 번역, 요약, 사실 보강, 새 글 작성으로 확장하지 않는다.

## 절차

1. [references/quick-rules.md](references/quick-rules.md)를 반드시 읽는다.
2. 더 정밀한 분류나 처방이 필요할 때만 [references/ai-tell-taxonomy.md](references/ai-tell-taxonomy.md)와 [references/rewriting-playbook.md](references/rewriting-playbook.md)를 읽는다.
3. 입력이 `.txt` 또는 `.md` 경로이면 파일을 읽고, 아니면 붙여넣은 텍스트를 원문으로 사용한다.
4. 한국어가 아니면 이 스킬은 한국어 텍스트만 처리한다고 안내하고 종료한다.
5. 장르가 명시되지 않았으면 첫 300자로 `칼럼`, `리포트`, `블로그`, `공적` 중 하나를 추정한다.
6. 보존 대상 구간을 제외하고 AI 티 구간을 탐지한다.
7. `D -> A -> I -> G -> H -> F -> B -> C/J -> E` 순서로 해당 구간만 수정한다.
8. quick-rules.md의 `## 자체검증` 1-6번을 모두 수행한다. 실패한 수정은 롤백하고 같은 구간만 최대 1회 다시 시도한다.
9. 윤문본과 검증 요약을 응답한다.

## 보조 도구

[references/metrics.py](references/metrics.py)는 쉼표, 반복 어휘, 번역투 신호를 계산한다. 긴 글이거나 감으로 판단하기 애매할 때만 사용한다.

스킬 디렉터리 기준 `metrics.py` 사용법은 `--help`로 확인한다. 파일 또는 원문 문자열을 입력할 수 있다.

```bash
python references/metrics.py --help
python references/metrics.py --input input.txt --genre essay
python references/metrics.py --text $'첫 문장입니다.\n둘째 문장입니다.' --genre essay
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

## 부분 윤문 지시

- "이 문단만": 요청한 문단만 수정한다.
- "번역투만", "관용구만", "이모지만": 해당 카테고리만 적용한다.
- "강도 낮춰": S1 수정만 적용한다.
- "강도 높여": S1, S2, 신중한 S3 리듬 수정을 적용한다.
- "2차 윤문": 직전 결과를 입력으로 삼고 1차보다 좁게 수정한다.

## 등급

- `A`: S1 잔존 0, S2 잔존 2 이하, 변경률 10-25%, 자체검증 6/6.
- `B`: S1 잔존 0, S2 잔존 4 이하, 자체검증 5/6 이상.
- `C`: S1 잔존 1-2, 자체검증 4/6 이하, 저윤문 또는 과윤문 위험.
- `D`: S1 잔존 3 이상 또는 변경률 50% 초과. 중단하고 보고한다.
