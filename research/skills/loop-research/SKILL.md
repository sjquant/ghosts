---
name: loop-research
description: Evidence-backed explanations and research for current, contested, comparative, or learning-oriented questions. Use when the user wants sources, a deep explanation, or an investigation; do not activate for simple stable answers.
---

# Loop Research

Turn a short request into a bounded research-and-explanation loop. Deliver the
answer first, with traceable references and explicit uncertainty when needed.
Keep the research process invisible unless the user asks about it.

## Effort

- **Quick:** narrow, stable, low-risk question. Answer directly without forced
  web research or a visible plan.
- **Standard:** current, comparative, multi-faceted, or learning-oriented
  question. Search, maintain light evidence state, and run one review pass.
- **Strict:** high-stakes, contested, numerical, legal, medical, financial,
  security-related, or explicitly exhaustive question. Prefer primary sources,
  search for counter-evidence, and verify material findings independently.

Use bounded iteration. Repair a material finding once, then stop when another
pass produces no meaningful improvement. Show a one-sentence plan only when the
work is substantial or the user asks. Ask at most one clarifying question when
the missing choice changes scope, audience, safety, or cost; otherwise state an
assumption and proceed.

## Research loop

### 1. Define the task

Understand what the user is really trying to learn, the relevant scope,
audience, freshness, and risk. Decide for yourself which angles and evidence
are needed; do not force a fixed decomposition or search plan.

### 2. Gather evidence

Choose the most useful search angles and source types yourself. Search broadly
enough to find important leads, follow promising ones, and read important
sources beyond snippets. Prefer the most authoritative source for each claim,
especially primary or first-party sources; use secondary sources for context
and weaker sources mainly as leads or examples. Add a date boundary when
freshness matters.

Retain enough source provenance to support and qualify the answer.

### 3. Verify material claims

Track only claims that materially affect the answer, their supporting evidence,
important contradictions, and unresolved uncertainty. Prefer direct citations
near those claims. For contested or high-risk claims, look for an authoritative
source, independent corroboration where useful, and evidence that could weaken
the claim.

When sources disagree, explain differences in scope, method, date, or
definition. Do not average disagreement into false certainty.

### 4. Explain

Explain at the user's level, using a mental model, example,
limitation, or practical implication only when useful. Put references near the
claims they support and define necessary domain terms on first use.

### 5. Review and repair

Review the draft with one open-ended probe:

```text
Any material issues?
Return only findings that would change trust, safety, or usefulness,
with evidence and the smallest useful repair.
```

Repair the identified gap rather than rewriting everything. Re-run only the
relevant search or check when evidence is missing, a credible contradiction
appears, a source is stale, a conceptual jump is too large, or a high-risk
finding needs confirmation.

Stop when the material claims are supported or clearly marked as inference,
important contradictions are visible, the explanation is useful, and another
pass would not materially improve it. If evidence remains insufficient, narrow
the claim and say so.
