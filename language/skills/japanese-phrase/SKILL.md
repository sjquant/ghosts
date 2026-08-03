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
  - `상황별로 이렇게 말해요`: use 2 short Korean context headings by default; add a third only when it represents a meaningfully different use. Give 1 expression per context.
- For every introduced Japanese phrase, include:
  - `읽기`: hiragana reading.
  - `발음 참고`: Korean-style approximate pronunciation.
  - `공손도`: 반말, 정중체, 격식체, or 메시지체.
  - Short Korean nuance/usage explanation.
  - A short `문장 구조` line that breaks the phrase into meaningful units in Japanese word order.
  - `단어/문법` bullets.
- Explain each phrase for a beginner who may not know the parts inside a compound or conjugated form:
  - When a compound contains a part the learner may not know, break it into useful parts, such as `やること` → `やる` (하다) + `こと` (일/것).
  - Explain the base form and the change in conjugated forms, such as what `やった` is derived from and what its past tense means.
  - Explain particles and sentence endings by their function in this phrase, not only by a Korean gloss. Mention omitted subjects only when they affect the meaning.
- In phrase sections, use short `단어/문법` bullets. Each bullet should cover one word, particle, ending, or fixed expression and include its `읽기/발음 참고`. Explain the components needed to understand the phrase, and avoid repeating the same explanation across phrase sections.
- After each dialogue scenario, add `대화 문장 해설` as a beginner-level mini-lecture for all six Japanese lines.
  - Explain every word, particle, ending, interjection, and fixed expression in each line in order. Do not skip small words such as `は`, `も`, `し`, `けど`, `ね`, or `よ`.
  - For every line, show the sentence structure, including the omitted subject or object when it matters, and explain how the parts combine into the Korean meaning.
  - For every vocabulary or grammar item, include `읽기/발음 참고`, a basic meaning, and its function in that sentence. For conjugated forms, give the dictionary form and explain the change.
  - Explain the six lines in dialogue order, even when a word was introduced earlier. If an item is repeated, state its meaning in this line briefly instead of leaving it unexplained.
- Treat Korean-style pronunciation as a learning aid, not exact pronunciation. Mention long vowels, small っ, and ん only when useful.
- Use readable spacing and paragraph-style explanations. The dialogue lecture may use a clear per-line structure with nested bullets.
- Dialogue examples must have at least 2 realistic scenarios. Each scenario has 6 Japanese lines in a natural A-B-A-B-A-B flow, natural and consistent speaker names, Korean translation for every line, a clear context, and a small resolution.
- After each scenario, add `대화 문장 해설` for all 6 lines. Use the format below for each line in order:
  - Show the sentence structure and any meaningful omitted subject or object.
  - Explain every word, particle, ending, interjection, and fixed expression, including small items such as `は`, `も`, `し`, `けど`, `ね`, and `よ`.
  - Include `읽기/발음 참고`, basic meaning, and sentence function for every item. For conjugated forms, give the dictionary form and explain the change.
  - If an item repeats, explain its role briefly in that line instead of copying a long explanation.
- In each scenario, use at least one introduced key phrase at a natural point after its context or trigger. Bold only the exact introduced phrase, with no spaces between it and nearby punctuation. Continue after it with a response, clarification, decision, or resolution; repeat it only when a new trigger appears.

## Output Format

```markdown
## 💬 상황별로 이렇게 말해요

### **[짧은 한국어 문맥]**

**「[Japanese Phrase]」**
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

문장 구조: [일본어 구성 요소를 실제 어순대로 나누고, 이 상황에서의 의미를 짧게 설명]

단어/문법:
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]
- [단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]

### **[짧은 한국어 문맥]**

**「[Japanese Phrase]」**
읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

문장 구조: [일본어 구성 요소를 실제 어순대로 나누고, 앞 표현과 다른 점을 짧게 설명]

단어/문법:
- [앞에서 설명하지 않은 단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]
- [앞에서 설명하지 않은 단어/조사/어미/고정 표현 하나] (읽기/발음 참고: [ひらがな] / [한국어식 근사 발음]) - [초보자용 짧은 풀이]

### **[짧은 한국어 문맥]** <!-- 세 번째로 의미가 확실히 다른 쓰임이 있을 때만 추가 -->

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

#### 대화 문장 해설

각 대화 문장을 1번부터 6번까지 아래 형식으로 모두 설명합니다.

1. **[Japanese line]**
   - 문장 구조: [어순, 구성, 생략된 주어/목적어, 전체 뜻]
   - 단어/문법:
     - [문장에 나온 모든 단어/조사/어미/추임새/고정 표현을 순서대로 필요한 만큼 나열하고, 각각의 읽기·발음·뜻·기능을 설명]

2-6. 위 형식을 반복해 각 문장을 빠짐없이 해설합니다.

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

#### 대화 문장 해설

상황 1과 동일한 형식으로 1번부터 6번까지 모든 문장을 해설합니다.
```
