---
name: english-phrase
description: Create Korean-language learning guides for translating everyday Korean phrases into natural English by context.
disable-model-invocation: true
---

Create a learning guide for one everyday Korean phrase, written for Korean learners of English.

## Input

- One Korean phrase.

## Requirements

1. Explain the phrase's core meaning, formality level, and common usage contexts.
2. Write all headers and explanations in Korean.
3. Keep English translation candidates and English dialogue lines in English.
4. 실제 회화에서 자주 쓰이는 표현을 직역보다 우선한다.
5. Avoid listing grammar variants that mean nearly the same thing; choose expressions with distinct usage differences.
6. Start with 1-2 broadly useful English translations.
7. Add situation-specific translations under at least two short, conversational Korean context headings.
8. Use 1 expression per context by default; add a second only when it has a meaningfully different use.
9. For every English phrase, explain in Korean its nuance, feeling, and appropriate usage in a short paragraph.
10. Keep the main Korean section headers, but use readable spacing and avoid deep nested bullets or workbook-style formatting.
11. End with at least two realistic dialogue scenarios.
12. Each dialogue must use natural speaker names, include at least 6 English lines, alternate naturally in an A-B-A-B-A-B pattern, and include context, response, follow-up, and a small resolution.
13. Each English dialogue line must include a Korean translation.
14. Key phrases must exactly match phrases introduced earlier and be bolded.

## Output Format

```markdown
### **가장 자연스러운 표현**

**"[English Phrase]"**
[짧은 한국어 설명]

**"[English Phrase]"**
[짧은 한국어 설명]

### **상황별로 이렇게 말해요**

#### **[짧은 한국어 문맥]**

**"[English Phrase]"**
[짧은 한국어 설명]

#### **[짧은 한국어 문맥]**

**"[English Phrase]"**
[짧은 한국어 설명]

**"[English Phrase]"**
[짧은 한국어 설명; 의미 차이가 있을 때만 추가]

### **대화 예시**

#### **상황 1: [문맥 설명]**

> **Mina:** [English line with **bolded key phrase**]
> ([Korean translation])
>
> **Joon:** [English response]
> ([Korean translation])
>
> **Mina:** [English follow-up with **bolded key phrase**]
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

#### **상황 2: [다른 문맥 설명]**

> **Alex:** [English line with **bolded key phrase**]
> ([Korean translation])
>
> **Taylor:** [English response]
> ([Korean translation])
>
> **Alex:** [English follow-up with **bolded key phrase**]
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
