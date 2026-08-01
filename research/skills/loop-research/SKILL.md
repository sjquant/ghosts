---
name: loop-research
description: Evidence-backed explanations and research for current, contested, comparative, or learning-oriented questions. Use when the user wants sources, a deep explanation, or an investigation; do not activate for simple stable answers.
---

# Loop Research

Turn a short user request into a bounded research-and-explanation loop. The
default deliverable is a clear answer with traceable evidence and visible
uncertainty, not a search log or an unnecessarily long report.

## Loop contract

- **Trigger:** an evidence-backed explanation, investigation, comparison,
  learning material, or explicit research request.
- **Goal:** make the topic accurate, useful, and understandable for this user.
- **Working state:** intent brief, research axes, sources, material claims,
  unresolved questions, and useful leads for the current run.
- **Verification:** evidence, contradictions, freshness, and teachability.
- **Stop:** a supported explanation, diminishing returns, a named terminal state,
  or the configured effort cap.

Do not equate more sources or more iterations with better research.

## Effort routing

- **Quick:** narrow, stable, low-risk question. Answer directly; do not show a
  plan or force web research.
- **Standard:** current, comparative, multi-faceted, or learning-oriented
  question. Show a one-sentence plan, search, maintain a light claim ledger, and
  run one review pass.
- **Strict:** high-stakes, contested, numerical, legal, medical, financial,
  security-related, or explicitly exhaustive request. Prefer primary sources,
  run counter-searches, and use an independent review lens.

Default caps: two repair passes, five expansion waves, and stop after two
successive passes produce no material finding. An explicit exhaustive request
may raise effort only within a named budget and depth limit.

Ask at most one clarifying question when a missing choice materially changes
scope, audience, safety, or cost. Otherwise state an assumption and proceed.
Never expose hidden chain-of-thought; expose only the question, coverage, and
verification status.

## Semantic anchors

Use a few high-signal terms of art as protocol handles. Do not paste a complete
rubric into every prompt.

| Anchor | Activate |
|---|---|
| `mental model` | Map entities, relationships, and causal structure before details. |
| `source triangulation` | Compare independent sources and record disagreement. |
| `counter-search` | Search for evidence that would weaken or falsify a claim. |
| `red-team` | Look for hidden assumptions, missing risks, and plausible failure modes. |
| `teach-back` | Check whether the explanation can be restated simply without losing its core. |

Use ordinary phase instructions for examples, primary-source preference,
counterexamples, and diminishing returns; they are not separate mandatory
review categories.

## Protocol

### 1. Compress intent

Extract:

```text
Core question:
User goal:
Audience / assumed knowledge:
Scope and time boundary:
Desired output:
Risk and freshness:
```

Create two to five research axes only when the topic needs them. Each axis needs
a distinct question and an observable completion signal.

### 2. Gather evidence

Search broadly enough to map the topic, then follow high-value leads. Add the
current date or date range when freshness matters. Read important sources beyond
search snippets.

Prefer the source class appropriate to the claim:

1. original papers, standards, laws, filings, datasets, and first-party docs;
2. peer-reviewed research, official statistics, and authoritative institutions;
3. reputable secondary analysis for context;
4. commentary or social sources for leads and examples, not automatic proof.

For important sources, retain only the useful source note: title, author/date,
URL or DOI, role, relevant evidence, supported claims, and limitations.

If a public source is blocked, use an accessible public alternative. Never bypass
login, paywall, CAPTCHA, or authentication boundaries. If the current harness
has no browsing or worker capability, continue sequentially in the main thread
and disclose the limitation.

### 3. Track material claims

Use a working claim ledger for claims that materially affect the answer:

```text
claim | type | risk | supporting sources | contradicting sources
counter-search | status: supported / partial / refuted / unresolved
```

This is a reasoning aid unless a deterministic checker is actually available;
do not claim that a prompt-only ledger mechanically proves correctness.

For high-risk claims, seek a primary or first-party source where one exists,
independent corroboration where appropriate, and an explicit counter-search. A
single authoritative source can be the right exception for a law, standard,
filing, or other first-party fact; record why.

If sources conflict, explain the difference in scope, method, date, or definition.
Do not average disagreement into false certainty. Do not state unresolved or
refuted claims as settled facts.

### 4. Explain

Convert evidence into the smallest useful teaching structure:

1. direct answer or mental model;
2. intuitive-to-precise explanation;
3. worked example when useful;
4. limitations, counterexamples, and uncertainty;
5. practical implications;
6. references near the claims they support.

Match vocabulary and depth to the inferred audience. Preserve domain terms when
they carry more signal than a vague paraphrase, and define them on first use.

### 5. Review open-endedly, then classify

The first review pass is discovery, not checklist compliance. Use one short
high-signal probe:

```text
Any material issues?
Return only findings that would change trust, safety, or usefulness,
with evidence and the smallest useful repair.
```

Choose a domain probe when needed:

```text
Any security issues?
```

```text
Would a motivated beginner understand this?
```

Only after a finding appears, classify it with detailed fields such as severity,
exploitability, confidence, citation status, or remediation. The review
question discovers; the rubric validates.

### 6. Repair and stop

Repair the identified gap rather than rewriting everything. Re-run only the
relevant search or review lens when evidence is missing, a credible contradiction
appears, a source is stale, a conceptual jump is too large, or a high-risk issue
needs confirmation.

Pass the gate when material claims are supported or marked as inference,
important contradictions are visible, the explanation has a coherent model and
useful example, and the latest review found no material issue. Otherwise continue
within the caps or finish with uncertainty.

## Compact worker contract

Use workers only for independent axes or review lenses, and only when the current
harness exposes them. Keep synthesis and claim state owned by one coordinator.

```text
TASK: [one imperative sentence]
GOAL: [user-relevant outcome]
LENS: [one to three semantic anchors]
EVIDENCE: [source territory or artifact]
DONE WHEN: [observable completion condition]
RETURN: [small result, leads, and uncertainty]
```

Do not inject the whole policy, every failure mode, or a long checklist into a
worker prompt.

## Recovery and terminal states

- **Ambiguous goal:** make one material clarification or state an assumption.
- **Insufficient evidence:** narrow the claim or report the gap.
- **Conflicting evidence:** preserve and explain the disagreement.
- **Blocked source/tool:** use a public alternative, continue smaller, or disclose
  the limitation.
- **No progress:** stop instead of looping for appearance.

Use one of these terminal states for material runs:

- `COMPLETE`
- `COMPLETE_WITH_UNCERTAINTY`
- `NEEDS_USER_INPUT`
- `BLOCKED_OR_BUDGET_EXHAUSTED`

Show the answer first, followed by a concise uncertainty note and references.
