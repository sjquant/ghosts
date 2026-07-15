---
name: english-phrase
description: Create Korean-language learning guides for translating everyday Korean phrases into natural English by context.
disable-model-invocation: true
---

Create a Korean-language learning guide that translates one everyday Korean phrase into natural spoken English.

## Input

$ARGUMENTS

## Requirements

- Write all headers and explanations in Korean. Keep English phrases and English dialogue lines in English.
- Explain the Korean phrase's core meaning, formality level, and common usage contexts.
- Prioritize expressions commonly used in real spoken English over literal translations.
- Avoid near-duplicate grammar variants; choose phrases with distinct usage differences.
- Use readable spacing and short paragraph-style Korean explanations instead of deep nested bullets.

## Sections

1. `가장 자연스러운 표현`: give 1-2 broadly useful English translations.
2. `상황별로 이렇게 말해요`: use at least two short, conversational Korean context headings. Give 1 English phrase per context by default; add a second only when the usage is meaningfully different.
3. `대화 예시`: include at least two realistic scenarios. Each scenario must use natural speaker names, include at least 6 English lines, alternate in an A-B-A-B-A-B pattern, and include context, response, follow-up, and a small resolution.

For every English phrase, add a short Korean paragraph explaining nuance, feeling, and appropriate usage. In dialogues, every English line needs a Korean translation. Bolded key phrases must exactly match phrases introduced earlier.

Dialogue examples must preserve conversational flow:
- Use at least one bolded key phrase per scenario.
- Repeat a key phrase only when a new trigger appears in the prior turn or shared context.
- For `Since you brought it up,`, the other speaker must have introduced the topic first.
- After the key phrase, continue with a response, clarification, decision, or resolution.

## Output Format

```markdown
## ✅ 가장 자연스러운 표현

**"[English Phrase]"**
[짧은 한국어 설명]

**"[English Phrase]"**
[짧은 한국어 설명]

## 💬 상황별로 이렇게 말해요

### **[짧은 한국어 문맥]**

**"[English Phrase]"**
[짧은 한국어 설명]

### **[짧은 한국어 문맥]**

**"[English Phrase]"**
[짧은 한국어 설명]

**"[English Phrase]"**
[짧은 한국어 설명; 의미 차이가 있을 때만 추가]

## 🎭 대화 예시

### **상황 1: [문맥 설명]**

> **Mina:** [English line with **bolded key phrase**]
> ([Korean translation])
>
> **Joon:** [English response]
> ([Korean translation])
>
> **Mina:** [English follow-up or decision; use **bolded key phrase** only with a new trigger]
> ([Korean translation])
>
> **Joon:** [English response]
> ([Korean translation])
>
> **Mina:** [English follow-up]
> ([Korean translation])
>
> **Joon:** [English closing response]
> ([Korean translation])

### **상황 2: [다른 문맥 설명]**

> **Alex:** [English line with **bolded key phrase**]
> ([Korean translation])
>
> **Taylor:** [English response]
> ([Korean translation])
>
> **Alex:** [English follow-up or clarification; use **bolded key phrase** only with a new trigger]
> ([Korean translation])
>
> **Taylor:** [English response]
> ([Korean translation])
>
> **Alex:** [English follow-up]
> ([Korean translation])
>
> **Taylor:** [English closing response]
> ([Korean translation])
```
