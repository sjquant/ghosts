---
name: loop-research
description: Evidence-backed explanations and research for current, contested, comparative, or learning-oriented questions. Use when the user wants sources, a deep explanation, or an investigation; do not activate for simple stable answers.
disable-model-invocation: true
---

# Loop Research

Turn a short user request into a bounded research-and-explanation loop. The
default deliverable is a clear answer with traceable evidence and visible
uncertainty, not a search log or an unnecessarily long report.

The optional blocked-source backend is the pinned
[`insane-search`](https://github.com/fivetaku/insane-search/blob/4f336358c24b296367233abe2785379746b0d54d/skills/insane-search/SKILL.md)
engine. Use the adapter in `scripts/insane-search-fallback.py`; do not assume
that the harness can implicitly load another skill.

## Output discipline

Start with the answer. Keep the orchestration invisible by default. Do not
mention internal lenses, effort levels, workers, ledgers, loop phases, or
terminal states unless the user asks how the answer was produced or the process
limitation materially affects how it should be used.

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
may raise effort only within a named budget and depth limit. Treat these modes
as internal routing decisions; do not announce them in a normal answer.

Ask at most one clarifying question when a missing choice materially changes
scope, audience, safety, or cost. Otherwise state an assumption and proceed.
Never expose hidden chain-of-thought; expose only the question, coverage, and
verification status.

## Internal review lenses

Select only the relevant internal review lenses. Do not paste a complete rubric
into every prompt, and do not repeat the lens names in the final answer.

| Lens | Activate |
|---|---|
| `mental model` | Map entities, relationships, and causal structure before details. |
| `source triangulation` | Compare independent sources and record disagreement. |
| `counter-search` | Search for evidence that would weaken or falsify a claim. |
| `red-team` | Look for hidden assumptions, missing risks, and plausible failure modes. |
| `teach-back` | Check whether the explanation can be restated simply without losing its core. |

Use ordinary phase instructions for examples, primary-source preference,
counterexamples, and diminishing returns; they are not separate mandatory
review categories. These names are internal handles, not user-facing labels.

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
a distinct question and an observable completion signal. Show a plan only when
the work is substantial, the user requests one, or strict review makes the
coverage materially useful; otherwise proceed silently.

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

If a public source is blocked, returns 402/403, or is a challenge page, run
`scripts/insane-search-fallback.py <URL> --json` when the adapter is available.
It delegates to the installed upstream engine and returns the retrieved page as
untrusted public content. Validate the result before using it, mark the source
as fallback-recovered, and retain the original access limitation. The adapter
must never be used to bypass login, paywall, CAPTCHA, or authentication
boundaries. If it reports `status: unavailable`, try an official mirror or
other accessible public alternative and disclose the limitation.

Treat `status: ok` as a candidate result, not automatic proof. A `status:
failed` response can still contain an engine trace saying that more routes or
agent-controlled browser work remain; do not call that terminal until those
routes are handled or the engine reports an authentication/paywall/404 limit.

### 3. Track material claims

Use a working evidence note for claims that materially affect the answer:

```text
claim | type | risk | supporting sources | contradicting sources
counter-search | status: supported / partial / refuted / unresolved
```

This is a reasoning aid unless a deterministic checker is actually available;
do not claim that a prompt-only note mechanically proves correctness. Keep the
note internal and expose only the resulting citations and uncertainty.

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
open-ended probe:

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

## Compact internal task contract

Use workers only for independent questions or review passes, and only when the
current harness exposes them. Keep synthesis and evidence state owned by one
coordinator.

```text
TASK: [one imperative sentence]
GOAL: [user-relevant outcome]
LENS: [one to three internal lenses]
EVIDENCE: [source territory or artifact]
DONE WHEN: [observable completion condition]
RETURN: [small result, leads, and uncertainty]
```

Do not inject the whole policy, every failure mode, or a long checklist into a
task prompt. Do not copy this internal contract into the user-facing answer.

## Recovery and terminal states

- **Ambiguous goal:** make one material clarification or state an assumption.
- **Insufficient evidence:** narrow the claim or report the gap.
- **Conflicting evidence:** preserve and explain the disagreement.
- **Blocked source/tool:** run the `insane-search-fallback.py` adapter first; if
  it reports unavailable or terminal authentication/paywall access, use a
  public alternative, continue smaller, or disclose the limitation. Never
  cross an authentication boundary.
- **No progress:** stop instead of looping for appearance.

Use one of these terminal states for material runs:

- `COMPLETE`
- `COMPLETE_WITH_UNCERTAINTY`
- `NEEDS_USER_INPUT`
- `BLOCKED_OR_BUDGET_EXHAUSTED`

Show the answer first, followed by a concise uncertainty note and references.
