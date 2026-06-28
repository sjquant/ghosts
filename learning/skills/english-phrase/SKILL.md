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
4. Start with 2-3 broadly useful English translations.
5. Add situation-specific translations under at least two Korean-labeled context categories.
6. For every English phrase, explain in Korean its nuance, feeling, and appropriate usage.
7. End with at least two realistic dialogue scenarios.
8. Each dialogue must use script style with character names, English lines, Korean translations, and bolded key phrases from the guide.

## Output Format

```markdown
### **가장 흔하고 자연스러운 표현 (상황에 구애받지 않음)**

- **"[English Phrase]"**
  - [뉘앙스, 느낌, 적절한 사용 상황을 설명하는 한국어 문장]

- **"[English Phrase]"**
  - [뉘앙스, 느낌, 적절한 사용 상황을 설명하는 한국어 문장]

### **상황에 따른 표현**

### **1. [한국어 문맥 설명]**

- **"[English Phrase]"**
  - [뉘앙스, 느낌, 적절한 사용 상황을 설명하는 한국어 문장]

- **"[English Phrase]"**
  - [뉘앙스, 느낌, 적절한 사용 상황을 설명하는 한국어 문장]

### **2. [한국어 문맥 설명]**

- **"[English Phrase]"**
  - [뉘앙스, 느낌, 적절한 사용 상황을 설명하는 한국어 문장]

- **"[English Phrase]"**
  - [뉘앙스, 느낌, 적절한 사용 상황을 설명하는 한국어 문장]

### **대화 예시**

#### **상황 1: [문맥에 대한 한국어 설명]**

> **[Name]:** [English line with **bolded key phrase**]
> ([Korean translation])

#### **상황 2: [다른 문맥에 대한 한국어 설명]**

> **[Name]:** [English line with **bolded key phrase**]
> ([Korean translation])
```
