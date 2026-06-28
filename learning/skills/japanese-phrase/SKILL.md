---
name: japanese-phrase
description: Create Korean-language learning guides for translating everyday Korean phrases into natural Japanese by context, with pronunciation and word-level explanations.
disable-model-invocation: true
---

Create a Korean-language learning guide that translates one everyday Korean phrase into natural spoken Japanese.

## Input

- One Korean phrase.

## Requirements

- Write all headers and explanations in Korean. Keep Japanese phrases and Japanese dialogue lines in Japanese.
- Explain the Korean phrase's core meaning, formality level, and common usage contexts.
- Prioritize expressions commonly used in real spoken Japanese over literal translations.
- Choose phrases with distinct usage differences. Avoid listing near-duplicate grammar variants.
- Show pronunciation for every Japanese phrase and every Japanese dialogue line.
- For each Japanese phrase, include a word and grammar breakdown covering all meaningful words, particles, endings, and fixed expressions.
- Mark politeness level clearly, such as 반말, 정중체, 격식체, or 메시지체.
- Use readable spacing and short Korean paragraphs. Use compact word breakdowns only where they help beginners parse the Japanese.

## Pronunciation Rules

- Provide `읽는 법` in hiragana for kanji/kana accuracy.
- Provide `발음 참고` in Korean-style pronunciation for beginner support.
- Mark long vowels, small っ, and ん when relevant.
- Do not imply Korean-style pronunciation is exact; label it as a learning aid.

## Sections

1. `가장 자연스러운 표현`: give 1-2 broadly useful Japanese translations.
2. `상황별로 이렇게 말해요`: use at least two short, conversational Korean context headings. Give 1 Japanese phrase per context by default; add a second only when the usage is meaningfully different.
3. `단어와 표현 풀이`: explain the key vocabulary, particles, endings, and cultural nuance needed to understand the introduced phrases.
4. `대화 예시`: include at least two realistic scenarios. Each scenario must use natural speaker names, include at least 6 Japanese lines, alternate in an A-B-A-B-A-B pattern, and include context, response, follow-up, and a small resolution.

For every Japanese phrase, add a short Korean paragraph explaining nuance, feeling, and appropriate usage. In dialogues, every Japanese line needs `읽는 법`, `발음 참고`, and a Korean translation. Bolded key phrases must exactly match phrases introduced earlier.

## Output Format

```markdown
## ✅ 가장 자연스러운 표현

**「[Japanese Phrase]」**
읽는 법: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

단어/표현:
[주요 단어와 문법 요소를 짧게 풀이]

**「[Japanese Phrase]」**
읽는 법: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

단어/표현:
[주요 단어와 문법 요소를 짧게 풀이]

## 💬 상황별로 이렇게 말해요

### **[짧은 한국어 문맥]**

**「[Japanese Phrase]」**
읽는 법: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

단어/표현:
[주요 단어와 문법 요소를 짧게 풀이]

### **[짧은 한국어 문맥]**

**「[Japanese Phrase]」**
읽는 법: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]

[짧은 한국어 설명]

단어/표현:
[주요 단어와 문법 요소를 짧게 풀이]

## 🔎 단어와 표현 풀이

[표현들에 반복해서 나오는 핵심 단어, 조사, 어미, 문화적 뉘앙스를 한국어로 정리]

## 🎭 대화 예시

### **상황 1: [문맥 설명]**

> **Mina:** [Japanese line with **bolded key phrase**]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Ren:** [Japanese response]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Mina:** [Japanese follow-up with **bolded key phrase**]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Ren:** [Japanese response]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Mina:** [Japanese follow-up]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Ren:** [Japanese closing response]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])

### **상황 2: [다른 문맥 설명]**

> **Yuna:** [Japanese line with **bolded key phrase**]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Haru:** [Japanese response]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Yuna:** [Japanese follow-up with **bolded key phrase**]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Haru:** [Japanese response]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Yuna:** [Japanese follow-up]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
>
> **Haru:** [Japanese closing response]
> 읽는 법: [ひらがな]
> 발음 참고: [한국어식 근사 발음]
> ([Korean translation])
```
