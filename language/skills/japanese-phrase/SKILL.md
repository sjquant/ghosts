---
name: japanese-phrase
description: Create Korean-language learning guides for translating everyday Korean phrases into natural Japanese by context, with pronunciation and word-level explanations.
disable-model-invocation: true
---

Create a Korean-language learning guide that translates one everyday Korean phrase into natural spoken Japanese.

## Input

$ARGUMENTS

## Requirements

- Write all headers and explanations in Korean; keep Japanese phrases and dialogue lines in Japanese.
- Translate one everyday Korean phrase into natural spoken Japanese.
- Prefer common real-life Japanese expressions over literal translations.
- Choose expressions with distinct usage differences; avoid near-duplicate variants.
- Keep phrase sections light:
  - `가장 자연스러운 표현`: 1-2 expressions.
  - `상황별로 이렇게 말해요`: 1 expression per context by default; add 2 only if meaningfully different.
- For every Japanese phrase, include:
  - `읽기`: hiragana reading.
  - `발음 참고`: Korean-style approximate pronunciation.
  - `공손도`: 반말, 정중체, 격식체, or 메시지체.
  - Short Korean nuance/usage explanation.
  - `단어/표현` bullets.
- Format `단어/표현` as short bullets, not slash-separated inline lists.
- Each `단어/표현` bullet should explain one word, particle, ending, or fixed expression and include its `읽기/발음 참고`.
- Avoid repeating the same word/grammar explanation across sections.
- Treat Korean-style pronunciation as a learning aid, not exact pronunciation.
- Mention long vowels, small っ, and ん only when useful; avoid lengthy repeated pronunciation notes.
- Use readable spacing and paragraph-style explanations; avoid workbook-like formatting and deep nesting.
- Do not add a separate long vocabulary section unless it adds non-repeated value.
- Dialogue examples must include:
  - At least 2 realistic scenarios.
  - Replace `[이름 A]` and `[이름 B]` in the template with natural speaker names of your choice. Keep the A/B-to-name mapping consistent within each scenario.
  - At least 6 Japanese lines per scenario.
  - Natural A-B-A-B-A-B turn flow.
  - Context, response, follow-up, and small resolution.
  - Korean translation for every Japanese line.
- In dialogues, combine reading and pronunciation compactly:
  - `읽기/발음: [ひらがな] / [한국어식 근사 발음]`
- Bolded key phrases in dialogues must exactly match introduced phrases.
- Use bold markers without internal spaces: `**やることは全部やったよ**`, not `** やることは全部やったよ **`.
- Do not add spaces between Japanese punctuation and bold markers:
  - Good: `宿題、**やることは全部やったよ**。`
  - Bad: `宿題、 **やることは全部やったよ** 。`
- Bold only the introduced phrase, excluding punctuation unless punctuation is part of the phrase.
- Dialogue examples must preserve conversational flow:
  - Use at least one bolded key phrase per scenario.
  - The key phrase does not have to appear in the first line. Place it wherever it fits naturally after the preceding context or trigger has been established.
  - Do not reserve a particular turn for the key phrase; choose the most natural position among the six lines.
  - Repeat a key phrase only when a new trigger appears in the prior turn or shared context.
  - After the key phrase, continue with a response, clarification, decision, or resolution.

## Output Format

```markdown
## ✅ 가장 자연스러운 표현

**「[Japanese Phrase]」**
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

단어/표현:
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [짧은 한국어 풀이]
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [짧은 한국어 풀이]

**「[Japanese Phrase]」**
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

단어/표현:
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [짧은 한국어 풀이]
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [짧은 한국어 풀이]

## 💬 상황별로 이렇게 말해요

### **[짧은 한국어 문맥]**

**「[Japanese Phrase]」**
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

단어/표현:
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [짧은 한국어 풀이]
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [짧은 한국어 풀이]

### **[짧은 한국어 문맥]**

**「[Japanese Phrase]」**
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

단어/표현:
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [짧은 한국어 풀이]
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [짧은 한국어 풀이]

## 🎭 대화 예시

### **상황 1: [문맥 설명]**

> **[이름 A]:** [Japanese opening line]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 B]:** [Japanese response or context-setting line]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 A 또는 이름 B]:** [Japanese line that continues the conversation]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 A 또는 이름 B]:** [Japanese response]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 A 또는 이름 B]:** [Japanese follow-up]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 A 또는 이름 B]:** [Japanese closing response]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])

### **상황 2: [다른 문맥 설명]**

> **[이름 A]:** [Japanese opening line]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 B]:** [Japanese response or context-setting line]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 A 또는 이름 B]:** [Japanese follow-up or clarification]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 A 또는 이름 B]:** [Japanese response]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 A 또는 이름 B]:** [Japanese follow-up]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
>
> **[이름 A 또는 이름 B]:** [Japanese closing response]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> ([Korean translation])
```
