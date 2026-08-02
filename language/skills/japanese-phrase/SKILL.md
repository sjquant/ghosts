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
  - `가장 자연스러운 표현`: 1 primary expression by default; add a second only when its meaning or nuance is genuinely different.
  - `상황별로 이렇게 말해요`: optional; include it only when a context-specific expression adds meaning that the primary expression does not. Use at most 1 expression per context.
- For every introduced Japanese phrase, include:
  - `읽기`: hiragana reading.
  - `발음 참고`: Korean-style approximate pronunciation.
  - `공손도`: 반말, 정중체, 격식체, or 메시지체.
  - Short Korean nuance/usage explanation.
  - A short `문장 구조` line that breaks the phrase into meaningful units in Japanese word order.
  - `단어/문법` bullets.
- Explain phrases for a beginner who may not know the parts inside a compound or conjugated form:
  - When a compound contains a part the learner may not know, break it into useful parts, such as `やること` → `やる` (하다) + `こと` (일/것).
  - Explain the base form and the change in conjugated forms, such as what `やった` is derived from and what its past tense means.
  - Explain particles and sentence endings by their function in this phrase, not only by a Korean gloss. Mention omitted subjects only when they affect the meaning.
- Format `단어/문법` as short bullets, not slash-separated inline lists. Each bullet should cover one word, particle, ending, or fixed expression and include its `읽기/발음 참고`.
- Include only the components needed to understand the phrase, usually 3-5 bullets. If understanding the phrase requires more, include those essential components rather than leaving them unexplained. Avoid repeating a word or grammar explanation across phrase sections; when it has already been explained, state only the new nuance.
- Do not add separate vocabulary or grammar explanations for ordinary dialogue lines; explain only the introduced key phrases.
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

문장 구조: [일본어 구성 요소를 실제 어순대로 나누고, 전체 뜻을 짧게 연결]

단어/문법:
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]

**「[Japanese Phrase]」** <!-- 두 번째 표현이 실제로 필요할 때만 -->
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

문장 구조: [일본어 구성 요소를 실제 어순대로 나누고, 앞 표현과 다른 점을 짧게 설명]

단어/문법:
- [새로 배울 단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]
- [새로 배울 단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]

## 💬 상황별로 이렇게 말해요

<!-- 앞 표현과 의미가 겹치지 않는 상황별 표현이 있을 때만 이 섹션을 추가합니다. -->

### **[짧은 한국어 문맥]**

**「[Japanese Phrase]」**
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

문장 구조: [일본어 구성 요소를 실제 어순대로 나누고, 이 상황에서의 의미를 짧게 설명]

단어/문법:
- [앞에서 설명하지 않은 단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]
- [앞에서 설명하지 않은 단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]

### **[짧은 한국어 문맥]** <!-- 정말 다른 쓰임이 있을 때만 -->

**「[Japanese Phrase]」**
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

문장 구조: [일본어 구성 요소를 실제 어순대로 나누고, 앞 표현과 다른 점을 짧게 설명]

단어/문법:
- [앞에서 설명하지 않은 단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]
- [앞에서 설명하지 않은 단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]

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
