---
name: japanese-phrase
description: Create Korean-language absolute-beginner Japanese lessons for everyday Korean phrases, with complete sentence explanations, pronunciation, and useful kanji connections.
disable-model-invocation: true
---

Create a Korean-language Japanese lesson based on one everyday Korean phrase.

## Input

$ARGUMENTS

If no phrase is provided, randomly choose one very common everyday Korean phrase.

## Learner Profile

The learner:

- Is a Korean speaker and an absolute beginner in Japanese.
- Can read some hiragana but does not yet understand many basic words, particles, conjugations, or kanji.
- Needs every Japanese sentence explained slowly and completely.
- Benefits from connecting Japanese kanji with Korean 한자 훈·음, such as `木 = 나무 목`.
- Finds long vocabulary lists and many similar expressions overwhelming.

## Core Teaching Principles

1. Teach one main expression thoroughly rather than introducing many expressions.
2. Use natural spoken Japanese, not word-for-word translation.
3. Keep every dialogue line short and beginner-friendly.
4. Introduce no more than one or two important new grammar points per line.
5. Do not leave unexplained Japanese words inside examples.
6. Follow this learning order:

   **전체 뜻 → 읽기와 발음 → 문장 구조 → 단어와 문법 → 한자 연결 → 대화 속 사용 → 회상 연습**

7. Use simple Korean explanations. Avoid linguistic jargon unless immediately explained.
8. Treat Korean-style pronunciation only as an approximate learning aid.
9. Explain long vowels, small `っ`, and `ん` only when they appear and affect pronunciation.

## Lesson Scope

### Main expression

Introduce one primary Japanese expression that best matches the Korean phrase.

Add one contrasting expression only when it has a clearly different real-life use. Do not provide near-duplicate alternatives merely to increase the number of expressions.

### Dialogue count

Use one dialogue scenario by default. Add a second scenario only when it demonstrates a clearly different meaning or situation that cannot be taught well in the first scenario.

Each scenario should contain 4–6 short Japanese lines in a natural A-B-A-B flow, ending with a small response, decision, or resolution.

## Required Explanation for Each Introduced Phrase

For every introduced Japanese phrase, include:

- `읽기`: full hiragana reading.
- `발음 참고`: Korean-style approximate pronunciation.
- `공손도`: 반말, 정중체, 격식체, or 메시지체.
- `자연스러운 뜻`: the meaning a Korean speaker would naturally use.
- `직역`: include only when it helps reveal the Japanese structure.
- A short Korean explanation of when and why the expression is used.
- `문장 구조`: break the expression into meaningful units in actual Japanese word order.
- `단어/문법`: explain every component necessary to understand the expression.

For conjugated forms:

- Give the dictionary form.
- Show the change step by step.
- Explain what the resulting form means in this sentence.

Example:

`痛くない`
→ 기본형 `痛い`
→ 마지막 `い`를 빼고 `くない`를 붙임
→ “아프지 않다”

For compounds and fixed expressions:

- Break them into useful parts.
- Explain the whole expression, not just the separate dictionary meanings.

Example:

`気にする`
→ `気` + `に` + `する`
→ 각각의 직역보다 “신경 쓰다”라는 고정 표현으로 이해

For particles and sentence endings:

- Explain their actual function in the sentence, not only a Korean one-word gloss.
- Explain small items such as `は`, `も`, `に`, `を`, `けど`, `し`, `ね`, and `よ` when they appear.
- Mention omitted subjects or objects only when they affect the interpretation.

In the phrase section, keep explanations focused on the components needed for that phrase. Do not repeat a long explanation across phrase entries.

## Phrase Section Format

```markdown
## 💬 오늘의 표현

한국어: **[Korean phrase]**

### **[짧은 한국어 상황]**

**「[Japanese phrase]」**

읽기: [ひらがな]
발음 참고: [한국어식 근사 발음]
공손도: [반말/정중체/격식체/메시지체]
자연스러운 뜻: [한국어 뜻]
직역: [구조 이해에 도움이 될 때만]

[이 표현을 언제 사용하는지 쉬운 한국어로 설명]

문장 구조: [일본어 실제 어순대로 의미 단위 분해]

단어/문법:

- **[구성 요소]**
  읽기/발음: [ひらがな] / [근사 발음]
  기본 뜻: [뜻]
  이 문장에서의 역할: [기능]
  형태 변화: [활용형일 때 기본형부터 설명]

- **[다음 구성 요소]**
  읽기/발음: [ひらがな] / [근사 발음]
  기본 뜻: [뜻]
  이 문장에서의 역할: [기능]
```

If a genuinely different contrasting expression is useful, add it after the main expression:

```markdown
### **비슷해 보이지만 다른 상황**

**「[Contrasting Japanese phrase]」**

[같은 형식으로 설명하되, 앞 표현과의 차이를 명확히 설명]
```

## Dialogue Requirements

Use natural Japanese names and keep them consistent.

Each dialogue must:

- Establish a clear context before the key expression appears.
- Use the introduced key expression at a natural point.
- Use 4–6 short Japanese lines in a natural A-B-A-B flow.
- Provide a Korean translation and compact reading/pronunciation for every line.
- Bold only the exact introduced phrase, with no internal spaces and with nearby punctuation outside the bold text.
- Continue after the key expression with a response, clarification, decision, or resolution.

Format:

```markdown
## 🎭 짧은 대화

### **상황: [Korean context]**

> **유키:** [Japanese line]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> 뜻: [자연스러운 한국어 번역]
>
> **하루:** [Japanese line]
> 읽기/발음: [ひらがな] / [한국어식 근사 발음]
> 뜻: [자연스러운 한국어 번역]
```

## Full Dialogue Lecture

After each dialogue scenario, add `대화 문장 강의` and explain all of its dialogue lines in order. Use the same format for every line:

```markdown
### 1. **[Japanese line]**

전체 뜻: [자연스러운 한국어 뜻]

문장 구조:
[일본어 실제 어순으로 나누기]
→ [각 부분을 합쳐 전체 뜻이 되는 과정]

단어/문법:

- **[첫 번째 요소]**
  읽기/발음: [ひらがな] / [근사 발음]
  기본 뜻: [뜻]
  이 문장에서의 역할: [기능]
  형태 변화: [필요할 때 기본형과 변화 설명]

- **[조사·어미·추임새]**
  읽기/발음: [ひらがな] / [근사 발음]
  이 문장에서의 역할: [기능과 뉘앙스]
```

In the dialogue lecture:

- Explain every word, particle, ending, interjection, and fixed expression in the order it appears. Do not skip small words.
- Explain meaningful omitted subjects and objects.
- At the first appearance of an important kanji, explain it fully in `한자 연결해서 외우기`. At later appearances, state only its reading and meaning in that sentence.
- If an item was already explained in the phrase section or an earlier line, briefly restate its role in the current sentence rather than copying the long explanation.
- Do not add unrelated grammar or alternative expressions.

## Kanji Teaching for Korean Learners

After all dialogue lectures, add `한자 연결해서 외우기` for only the important kanji actually used in the main expression or dialogue, usually 2–4 characters.

For each kanji, include:

- The kanji.
- Korean 훈·음, such as `足 = 발 족`.
- Its basic core image or meaning.
- Its reading in the current Japanese word.
- Whether that reading is `음독` or `훈독`.
- The full Japanese word containing it.
- A short memory connection.
- One useful Korean–Japanese cognate only when it genuinely helps.

Example:

**足**

- 한국 훈·음: 발 족
- 기본 이미지: 발, 다리
- 이 단어에서의 읽기: `あし`
- 읽기 종류: 훈독
- 현재 단어: `足（あし）`
- 기억법: 한자 하나보다 `足は平気？`라는 문장 속에서 `あし`로 기억

For Korean–Japanese sound connections, use them only as memory hints, not pronunciation rules. When a mnemonic is not the true historical origin of the character, call it an `암기용 이미지`. Do not imply that Korean 한자음 always predicts Japanese pronunciation.

Teach only the reading used in the current word, plus at most one highly useful additional reading. Point out when Korean and Japanese use the same characters but have different modern meanings, such as `大丈夫`.

Format:

```markdown
## 🈶 한자 연결해서 외우기

### **[Kanji] — [Korean 훈·음]**

- 기본 이미지: [meaning]
- 현재 단어: [Japanese word]
- 일본어 읽기: [reading]
- 읽기 종류: [음독/훈독]
- 한국어 연결: [Korean 한자어 또는 발음 연결]
- 암기용 이미지: [짧고 구체적인 기억법]
```

## Review Section

End with a short active-recall review:

```markdown
## 🧠 오늘 이것만 기억하세요

**[Japanese key phrase]**
[hiragana]
[자연스러운 한국어 뜻]

핵심 구조:
[짧은 구조 설명]

핵심 한자:

- [Kanji + Korean 훈·음 + current Japanese reading]
- [Kanji + Korean 훈·음 + current Japanese reading]

### 말해 보기

1. [Korean prompt to translate into Japanese]
2. [Simple variation using the same structure]

### 정답

1. [Japanese answer]
2. [Japanese answer]
```

## Length and Difficulty Control

- Prefer depth over breadth.
- Keep dialogue lines short enough that every component can be explained clearly.
- Do not introduce difficult vocabulary merely to make the dialogue realistic.
- Use previously explained words where possible.
- Do not create a separate long vocabulary list.
- Do not provide more than four important kanji in one lesson.
- Do not provide more than two substitution-practice sentences.
- Do not introduce multiple similar grammar patterns in the same lesson.
- When the output becomes long, reduce the number of dialogue lines or scenarios rather than shortening necessary explanations.
- Never assume the learner already knows a word merely because it is common.
