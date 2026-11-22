# Fluent Korean

한국어 답변, 작업 보고, 인계문을 쓸 때 생략된 문장 성분 때문에 뜻이 달라지는 문제를 다룬다. 적용 기준과 예문은 [SKILL.md](SKILL.md)에 있다.

## 참고한 자료

[snflkd/fluent-korean](https://github.com/snflkd/fluent-korean)의 두 출력 스타일을 참고했다. 기준 커밋은 [`ce8683f0eba8cddb91de4dcd151425ff73e60498`](https://github.com/snflkd/fluent-korean/commit/ce8683f0eba8cddb91de4dcd151425ff73e60498)이다.

| 파일 | 스킬에 반영한 내용 |
| --- | --- |
| [fluent-korean-not-coding.md](https://github.com/snflkd/fluent-korean/blob/ce8683f0eba8cddb91de4dcd151425ff73e60498/plugins/fluent-korean/output-styles/fluent-korean-not-coding.md) | 두 버전이 공유하는 한국어 산문 지침. 조사와 어미로 뜻을 구별하는 법, 문장을 완결하는 법, 비유와 전문 용어를 고르는 기준, 인용·코드·외국어의 처리 범위를 참고했다. |
| [fluent-korean.md](https://github.com/snflkd/fluent-korean/blob/ce8683f0eba8cddb91de4dcd151425ff73e60498/plugins/fluent-korean/output-styles/fluent-korean.md) | 코딩용 버전에 추가된 에이전트 간 전달 지침. 한국어 작업 지시를 보내기 전과 결과를 사용자에게 전달할 때 각각 문장을 점검하도록 반영했다. |

두 원본은 Claude Code의 출력 스타일이다. 여기서는 공통 지침을 하나의 스킬로 구성하고, 작업 보고와 인계 상황에 맞는 예문을 새로 썼다. 원본의 라이선스는 [MIT](https://github.com/snflkd/fluent-korean/blob/ce8683f0eba8cddb91de4dcd151425ff73e60498/LICENSE)이며 저작권자는 snflkd이다.
