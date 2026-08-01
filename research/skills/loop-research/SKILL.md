---
name: loop-research
description: Explain or investigate a topic through a bounded research loop: compress the user's intent, gather traceable evidence, challenge material claims, and refine the explanation until it is accurate, understandable, and defensible. Use for explanations, learning materials, comparisons, current topics, and citation-backed research; scale effort to risk and complexity.
---

# Loop Research

Produce explanations that are both useful to learn from and defensible to check.
The deliverable is not a search log or a long report by default. It is a clear
answer whose material claims can be traced to evidence, whose uncertainty is
visible, and whose explanation has survived a targeted review loop.

## Core contract

Treat every run as a bounded loop specification:

- **Trigger:** the user asks to explain, teach, investigate, compare, verify, or
  create learning material about a topic.
- **Goal:** help this user understand the topic accurately enough for the stated
  purpose.
- **Memory:** retain the intent brief, research axes, source cards, claim ledger,
  unresolved questions, and the next useful leads for the current run.
- **Verification:** check evidence, contradictions, freshness, and teachability;
  use external verification when the claim can be tested or the risk justifies it.
- **Stop:** stop when the answer is sufficiently supported and understandable,
  when further research is unlikely to change it materially, or when a named
  terminal state is reached.

Never confuse more iterations, more sources, or a more elaborate plan with a
better result. Optimize for evidence quality, explanatory value, and useful
uncertainty.

## Activation and effort

Use this skill when the request benefits from more than ordinary recall or when
the user asks for sources. Do not force a research workflow onto a simple,
stable question that can be answered directly.

Infer normal defaults instead of interrogating the user. Ask at most one
clarifying question when the missing choice would materially change the answer's
scope, audience, safety, or cost. Otherwise state a short assumption and proceed.

Choose effort adaptively:

- **Quick:** stable, narrow, low-risk question; answer directly or use a small
  number of authoritative checks.
- **Standard:** current, multi-faceted, comparative, or learning-oriented
  question; plan, search, claim-check, and run one review pass.
- **Strict:** high-stakes, contested, numerical, legal, medical, financial,
  security-related, or explicitly exhaustive request; use primary sources,
  counter-searches, stronger claim gates, and an independent review lens.

An explicit request for `ulw`, `ultra`, or exhaustive research permits expansion
waves, but still requires a maximum depth, a budget, and named stop conditions.
Never treat “exhaustive” as permission to search forever.

## High-signal language

Prefer a few terms of art over a long checklist. A high-signal term is a handle
that activates a known research or review protocol; it is not a claim that every
sub-rule must be printed in every prompt.

Use these semantic anchors when they fit the task:

| Anchor | Internal behavior |
|---|---|
| `mental model` | Map the main entities, relationships, and causal structure before details. |
| `source triangulation` | Compare independent sources and record disagreements. |
| `primary-source first` | Prefer the original paper, standard, law, filing, dataset, or first-party document. |
| `claim ledger` | Link each material claim to supporting and contradicting evidence. |
| `counter-search` | Actively search for evidence that would weaken or falsify the claim. |
| `red-team` | Look for missing risks, hidden assumptions, and plausible failure modes. |
| `worked example` | Turn an abstract explanation into a concrete application. |
| `counterexample` | Show where an apparent rule or analogy stops applying. |
| `teach-back` | Check whether the explanation can be restated simply without losing the core idea. |
| `diminishing returns` | Stop expanding when another pass is unlikely to change the conclusion. |

Do not expand these anchors into a giant user-facing rubric. Keep the detailed
rules in the appropriate phase and load only the relevant lens.

## The research loop

### 1. Compress intent

Extract a compact brief:

```text
Core question:
User goal:
Audience / assumed knowledge:
Scope and time boundary:
Desired output:
Risk and freshness:
```

Translate the brief into two to five distinct research axes only when the topic
needs them. Each axis must have a reason to exist and a useful completion signal.

For material work, show a one- or two-sentence plan preview and continue unless
the user asks to change it. Do not expose hidden chain-of-thought; expose the
research question, planned coverage, and relevant constraints.

### 2. Plan with terms of art

Choose the smallest set of high-signal lenses that covers the actual goal.
Examples:

- Explain a technology: `mental model`, `worked example`, `limitations`.
- Compare tools: `comparison criteria`, `primary-source first`, `counterexample`.
- Investigate a claim: `claim ledger`, `source triangulation`, `counter-search`.
- Review a design or implementation: `red-team`, `any security issues?`,
  `operational failure modes`.
- Create learning material: `prerequisites`, `mental model`, `teach-back`,
  `misconceptions`.

Do not predetermine every finding category. Let the model perform an open-ended
discovery pass, then use structured criteria to validate the findings it found.

### 3. Gather evidence

Search broadly enough to map the topic, then pivot to targeted searches driven by
new leads. When freshness matters, include the current date or date range in the
query. Read important sources beyond their search snippets.

Prefer, in order appropriate to the domain:

1. primary sources and first-party documentation;
2. peer-reviewed research, standards, official statistics, and authoritative
   institutional material;
3. reputable secondary analysis for context and synthesis;
4. commentary or social sources for leads, examples, and reported experience,
   never as automatic proof of a material claim.

Capture a source card for important material:

```text
source_id:
title / author / date:
url or DOI:
source role and quality:
relevant evidence:
claims supported:
scope and limitations:
```

If a public source is blocked, try an available public-content fallback such as
an official mirror, feed, API, archive, or browser route. Never bypass a login,
paywall, CAPTCHA, or authentication boundary. Record the limitation and find an
accessible alternative when possible.

### 4. Maintain a claim ledger

Do not write high-risk claims directly from raw search results. For every
material claim, track:

```text
claim_id:
claim:
claim type: descriptive | numeric | causal | legal | recommendation
risk: normal | high
supporting sources:
contradicting sources:
counter-search result:
status: supported | partial | refuted | unresolved
```

For high-risk claims, require a primary or first-party source where one exists,
independent corroboration where appropriate, and an explicit counter-search. A
single authoritative source may be the correct exception for a law, standard,
official filing, or other first-party fact; record why.

If evidence is conflicting, do not average it into a false consensus. Explain the
scope, method, date, or definition that makes the sources disagree. If a claim
remains unresolved, do not state it as settled fact.

### 5. Draft for understanding

Convert the evidence into an explanation rather than a source dump. Use the
smallest structure that serves the user, usually:

1. direct answer or mental model;
2. progressive explanation from intuitive to precise;
3. one or more concrete examples;
4. limitations, counterexamples, and uncertainty;
5. practical implications or next steps;
6. references placed close to the claims they support.

Match depth and vocabulary to the inferred audience. Define necessary terms,
but preserve useful domain terminology when it carries more signal than a vague
paraphrase.

### 6. Review with open-ended probes first

The first review pass should be short and open-ended. Do not paste the full
quality rubric into the reviewer prompt.

Use the smallest relevant probe, for example:

```text
Review this explanation.

Any material errors, unsupported claims, misleading simplifications,
missing context, or important counterexamples?

Return only material findings with:
- finding
- evidence or reason
- impact
- smallest useful repair
```

For a security-sensitive task:

```text
Any security issues?

Look for unexpected attack surfaces, trust-boundary mistakes,
unsafe assumptions, and realistic exploit paths.
Report only actionable findings with evidence.
```

For educational quality:

```text
Would a motivated beginner understand this?

Find the biggest conceptual jump, unexplained term,
misleading analogy, or missing example.
Suggest the smallest repair.
```

Only after a finding appears should the next pass classify it with detailed
criteria such as severity, exploitability, confidence, citation status, or
remediation. The review question discovers; the rubric validates.

### 7. Repair narrowly and gate the result

Repair the identified gap rather than rewriting everything. Re-run the relevant
search or review lens when:

- a material claim lacks adequate evidence;
- a credible contradiction appears;
- a source is stale or outside the claim's scope;
- the explanation makes an unjustified conceptual jump;
- a high-risk issue needs independent confirmation.

Use at most two ordinary repair passes by default. Use strict mode for additional
adversarial checks when the risk or user request warrants it.

The answer may pass when:

- material claims are source-grounded or clearly marked as inference;
- unresolved and refuted claims are not stated as settled facts;
- important contradictions are represented;
- the explanation has a coherent mental model and at least one useful example;
- the last review found no material issue, or remaining issues are disclosed;
- another search pass is unlikely to change the practical conclusion.

If the gate fails, continue the targeted loop or end with an honest incomplete
state. Never manufacture certainty to satisfy the output format.

## Prompt contracts for internal workers

Keep worker prompts compact and use this shape:

```text
TASK: [one imperative sentence]
GOAL: [the user-relevant outcome]
LENS: [one to three high-signal terms of art]
EVIDENCE: [source territory or artifact to inspect]
DONE WHEN: [observable completion condition]
RETURN: [small structured result, including leads or uncertainty]
```

Do not include the entire policy, all possible failure modes, or a long review
checklist in every worker prompt. The orchestrator owns the loop policy; the
worker receives only the context and lens needed for its current pass.

Use parallel workers only for genuinely independent axes or independent review
lenses. Keep the main synthesis and claim ledger in one owner to avoid conflicting
state. Escalate from one agent to parallel or specialist work only when the task
requires it.

## Failure and recovery

- **Ambiguous goal:** state the most reasonable assumption or ask one material
  question; do not invent a broad research agenda.
- **No useful evidence:** narrow the claim, search a different source class, or
  report that the evidence is insufficient.
- **Conflicting sources:** preserve the disagreement and explain its scope.
- **Blocked source:** use a public alternative or disclose the access limitation;
  never pretend to have read it.
- **Tool or worker failure:** retry narrowly, then continue with a smaller plan or
  mark the affected axis incomplete.
- **No progress across passes:** stop with `COMPLETE_WITH_UNCERTAINTY` rather than
  looping for appearance.
- **High-stakes uncertainty:** use `NEEDS_USER_INPUT` or recommend qualified
  professional review instead of overclaiming.

## Named terminal states

End every material run in one of these states:

- `COMPLETE` — the answer meets the evidence and explanation gates.
- `COMPLETE_WITH_UNCERTAINTY` — useful answer delivered with material limits.
- `NEEDS_USER_INPUT` — a missing decision materially changes the result.
- `BLOCKED_BY_SOURCE_ACCESS` — required evidence is inaccessible and no reliable
  alternative was found.
- `BUDGET_EXHAUSTED` — the configured effort limit was reached before full
  convergence.

In the final response, show the answer first. Then include a concise uncertainty
note and references. Mention the terminal state only when it is not `COMPLETE` or
when it materially affects how the answer should be used.
