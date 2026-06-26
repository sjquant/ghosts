---
name: humanize-korean
description: >
  Humanize Korean AI-written text by removing translationese, mechanical
  structure, signature AI phrases, uniform rhythm, excessive connectors, and
  decorative formatting while preserving meaning, facts, genre, and register.
  Use when the user asks to make Korean text sound less like AI, remove GPT or
  ChatGPT style, fix Korean translationese, or rewrite Korean text as if a
  person wrote it.
disable-model-invocation: true
---

Humanize Korean text by changing only style, rhythm, and expression. Preserve
meaning before naturalness.

## Scope

Use this skill for Korean text when the user asks for:

- AI 티 제거, GPT/ChatGPT 문체 제거, AI 윤문, 휴머나이저.
- 번역투 제거, 사람이 쓴 것처럼 자연스럽게 다듬기.
- 특정 문단, 특정 카테고리, or second-pass humanizing.

Do not use it for plain spelling correction, translation, fact expansion, new
writing, summarization, or content changes.

## Hard Rules

1. Preserve facts, claims, numbers, dates, proper nouns, direct quotes, legal
   clauses, formulas, and standard technical abbreviations exactly.
2. Only edit spans that map to [references/quick-rules.md](references/quick-rules.md).
3. Preserve genre: column, report, blog, and formal writing must stay in their
   original lane.
4. Preserve register. Formal Korean remains formal; casual Korean remains
   casual.
5. Avoid over-polish. Warn above 30% change rate and stop or rollback above
   50%.
6. Do not add metaphors, examples, claims, citations, transitions, or emphasis
   that were not already present.

## Workflow

1. Load [references/quick-rules.md](references/quick-rules.md).
2. If the input is a `.txt` or `.md` path, read that file. Otherwise use the
   pasted text as the source.
3. Reject non-Korean input with a short note that this skill only handles Korean
   text.
4. Infer the genre from the first 300 characters unless the user supplied one:
   `칼럼`, `리포트`, `블로그`, or `공적`.
5. Identify AI-tell spans using the quick rules. Exclude every Do-NOT span.
6. Rewrite locally in this order:
   D signature phrases -> A translationese -> I bound nouns -> G hedging ->
   H connectors -> F modifiers -> B English overuse -> C/J structure and
   decoration -> E rhythm.
7. Self-check the result against the six-item checklist in quick rules. Roll
   back any edit that breaks a hard rule, then retry that local edit at most
   once.
8. Return the final text inline when the user wants an inline answer. If the
   surrounding agent workflow stores artifacts, write
   `final.md` under `_workspace/{YYYY-MM-DD-NNN}/` and keep the response brief.

## Output

Default response:

```markdown
완료. 변경률 X% / 등급 Y / 자체검증 N/6 통과

<윤문본>

핵심 탐지:
- A-2: N -> M
- D-1: N -> M

주요 변경:
- before -> after
```

If the user provided a file or the output is long, save the full result to
`_workspace/{YYYY-MM-DD-NNN}/final.md` and return only the status, key findings,
one highlight, and the file path.

## Grading

- `A`: S1 remaining 0, S2 remaining <= 2, change rate 10-25%, self-check 6/6.
- `B`: S1 remaining 0, S2 remaining <= 4, self-check >= 5/6.
- `C`: S1 remaining 1-2, self-check <= 4/6, or clear under/over-editing risk.
- `D`: S1 remaining >= 3 or change rate > 50%. Stop and report.

## Follow-Up Requests

- "이 문단만": edit only the requested paragraph.
- "번역투만", "관용구만", "이모지만": apply only matching categories.
- "강도 낮춰": keep only S1 fixes.
- "강도 높여": apply S1, S2, and careful S3 rhythm fixes.
- "2차 윤문": use the previous output as input, but preserve all hard-rule
  constraints and keep the second pass narrower than the first.
