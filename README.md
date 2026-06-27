# ghosts

Reusable agent skills and reviewers.

Default bias: delete needless layers, reuse what exists, and keep the smallest
safe instruction that preserves the behavior.

## Checks

`core/skills/humanize-korean/references/metrics.py`는 표준 라이브러리만 쓰는
단일 스크립트다. 스크립트 자체는 Python으로 실행하고, 수정 후 정리와 검증
도구는 로컬에 설치하지 말고 `uvx`로 실행한다.

```bash
python core/skills/humanize-korean/references/metrics.py --input input.txt --genre essay
uvx ruff format core/skills/humanize-korean/references/metrics.py
uvx ruff check core/skills/humanize-korean/references/metrics.py
uvx ty check core/skills/humanize-korean/references/metrics.py
```

## Attribution

`core/skills/humanize-korean`의 reference corpus는
[`epoko77-ai/im-not-ai`](https://github.com/epoko77-ai/im-not-ai)의
`.claude/skills/humanize-korean/references`를 기반으로 포함했습니다.
가져온 기준 commit은 `14aeb52d13e737beb4e999cb7cb92275d0969689`이며,
원본 저장소는 MIT 라이선스로 공개되어 있습니다.
