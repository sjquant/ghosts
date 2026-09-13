---
name: loop-plan
description: Planning-only loop for complex development and design problems, adaptable to other domains; uses evidence, alternatives, counterarguments, and premortems to resolve material uncertainty or costly tradeoffs. Skip routine implementation planning.
disable-model-invocation: true
---
# Loop Plan

Create a plan another person or agent can execute without rediscovering key
decisions. Inspect context and write planning artifacts only; stop before
implementation or invoking an execution skill. Scale depth to uncertainty and
the cost of a wrong decision, not the number of tasks or document length. For
other domains, replace files, interfaces, and tests with the relevant
deliverables, dependencies, and verification; omit software-only checks.

## Runtime loop

Before acting, create `/tmp/loop-plan-<safe-task-slug>.md` with a unique slug
or timestamp, `Current state: Pass 1 / Next: Understand`, the checklist below,
and an empty append-only `Repair log:`. Process items in order, finish each
before moving on, record a short outcome, and update `Current state`. Mark
`[x]` only after completion and `[-]` only with a reason; never erase or
uncheck historical rows. After a repair, append a numbered `[ ] Recheck P2: ...`
row for the earliest affected item and record the trigger, change, rechecked
items, and result in the repair log. Finish only after final validation.

```text
- [ ] Understand the outcome, constraints, and relevant evidence
- [ ] Resolve research and user-decision dependencies before framing
- [ ] Frame success, scope, principles, and decision drivers
- [ ] Set the review budget from uncertainty, impact, and reversibility
- [ ] Compare viable approaches and choose a provisional direction
- [ ] Draft ordered work packages and validation
- [ ] Challenge the design and run a premortem
- [ ] Any unsupported assumption, unresolved decision, or stronger alternative that changes the plan?
- [ ] Any unaddressed failure, dependency, or unverifiable completion criterion?
- [ ] Any unnecessary scope, complexity, or detail?
- [ ] Final validation and delivery of the plan
```

Answer every `Any ...?` row Yes or No. On Yes, repair the smallest material
issue and return to the earliest affected step before repeating the review. If
progress depends on missing evidence or a user decision, identify the exact
blocker instead of repeating the review or claiming readiness.

## Adaptive review

Do not make the user choose a mode. After framing, keep a decision ledger with
each material decision's impact, uncertainty, reversibility, and needed
evidence. Use qualitative `low`, `medium`, or `high` values and states such as
`open`, `investigating`, `supported`, `disputed`, `gated`, and `closed`.
Require at least one independent targeted review for a decision with high
impact and high uncertainty, low reversibility, or cross-component effects. A
request for `ralplan` or subagents raises the review budget without imposing a
fixed ceremony.

```text
[Understand] → [Route unknowns]
                  ├─ evidence → [$loop-research] ┐
                  ├─ user decision → [$socratic-interview] ├→ [Frame + ledger] → [Draft]
                  └─ known →─────────────────────┘              ↓
                                                     [Any high-impact uncertainty?]
                                                       ├─ No → [Self challenge]
                                                       └─ Yes → [Targeted subagent questions]
                                                                   → [Synthesize] → [Revise] ↺
                                                         → [Premortem] → [Any material issue?]
                                                         → [Validate + deliver]
```

For each unresolved ledger item, record a question ID, covered decision IDs,
capability, required inputs, `depends_on` question IDs, decision criterion,
and required evidence. Dispatch only ready questions; run independent ones in
parallel and refresh the snapshot after upstream results.

Choose a narrow capability rather than a permanent role:

- **Investigation:** establish a missing fact, constraint, dependency, or
  feasibility signal.
- **Design challenge:** test boundaries, responsibilities, dependency
  direction, and the strongest case against the chosen approach.
- **Execution challenge:** test prerequisites, rollout, recovery,
  observability, and demonstrable completion.
- **Adversarial challenge:** identify a credible failure or attack path when
  relevant.

Give each subagent the exact question, context snapshot, candidate options,
decision criterion, and required evidence. Keep it read-only and request
`finding`, `evidence`, `consequence`, and `recommendation`. Record each call as
`complete`, `failed`, `timed_out`, or `invalid`. Retry or reassign once when
useful, counting that attempt against the single follow-up budget; then use
self-review only when the risk permits. An unresolved high-impact item stays
`conditional` or `blocked`.

When two independent reviews are warranted, give them the same snapshot without
either review's findings, then record disagreements and their resolution. The
primary agent alone synthesizes the findings, records which decision changed
and why, and revises the draft.

When a finding changes a material decision, scope, or acceptance criterion,
send the revised delta to the relevant completed reviewer for one confirmation
pass. Ask whether the original concern is resolved, what new consequence the
revision creates, and whether a material objection remains. Record the response
and any objection in the question record and Review manifest. Skip the pass
when no material change occurred; when used, it counts against the single
follow-up budget and is review evidence, not user approval.
Preserve blind independence for reviews that have not run. If confirmation is
unavailable or a material objection remains, keep the item `conditional` or
`blocked`.

Set a bounded budget at delegation: one initial question per high-impact item,
one follow-up per item for conflicting, insufficient, or materially changed
evidence or drafts (including retry, reassignment, or confirmation), and at
most five synthesis passes. Repeat only while a material item lacks support or
a credible objection remains. Stop when high-impact decisions have evidence or
explicit gates, no unresolved objection changes the recommendation, and
acceptance and verification criteria are concrete. If the budget is exhausted
or the same material objection survives two revisions, deliver `conditional`
or `blocked` with the exact reason. If delegation is unavailable, perform the
same questions as self-review and state that no independent review occurred.
Subagent findings are review evidence, never user approval or authorization to
implement.

For high-risk work, deepen relevant challenges with three premortem scenarios
and the verification levels the problem needs. Do not add irrelevant test
layers to a design-only problem.

## Understand and frame

Inspect relevant code, documents, existing plans, and constraints before asking
questions that inspection can answer. Distinguish observed facts, inferences,
and assumptions; cite supporting files or sources. Identify the observable
outcome, non-goals, affected users or systems, and material constraints.

Route unresolved inputs before making design decisions. Use `$loop-research` for
repository or document investigation, current or contested evidence,
comparisons, feasibility checks, or source citations; it returns verified
claims, provenance, uncertainty, and leads that could change the plan. Use
`$socratic-interview` for choices only the user can make, such as outcome,
scope, priority, risk tolerance, or external action; it asks one focused
question at a time and returns an execution brief, but does not plan or edit.
Do not ask the user for facts inspection or research can establish, and do not
replace a user decision with an inferred preference. Carry both outputs into
the decision ledger.

Ask the smallest question when an unknown could change scope, success, or a
costly decision; continue independent inspection while waiting. State ordinary
assumptions and proceed. If feasibility remains unestablished, put the cheapest
useful investigation first with a decision criterion and keep dependent work
conditional rather than inventing certainty. State task-specific principles,
rank decision drivers, resolve conflicts explicitly, and define observable
success before choosing.

## Compare and draft

Compare at least two genuinely viable approaches against the same principles
and drivers, including a smaller change or no change when viable. Give each its
strongest case, cost, and downside. If only one survives the constraints,
explain why the alternatives fail. Recommend a direction, name the accepted
tradeoff, and state what evidence would reverse it.

Break the direction into dependency-ordered, independently verifiable work
packages. For each, name the outcome, affected components or files, important
interfaces, prerequisites, and completion evidence. Prefer end-to-end slices;
mark proposed paths as new and verify existing references. Specify correctness
contracts and ordering without prescribing incidental implementation details.
Do not invent precise estimates or parallelism without a basis.

Map success criteria to concrete checks, including material failure paths and
relevant existing tests. Add tests only for meaningful behavior. Include
rollout, observability, recovery, or stop conditions when operational
consequences require them.

## Challenge and repair

Review a fixed draft in two separate self-review passes before revising:

1. **Design challenge:** make the strongest case against the recommendation;
   check principle violations, responsibility boundaries, dependency direction,
   and whether a simpler alternative achieves the outcome. Resolve a real
   tension through evidence or an explicit tradeoff.
2. **Execution challenge:** walk through representative work packages as an
   implementer, including a failure path; check prerequisites, missing
   decisions, feasibility, and demonstrable completion.

These are not independent agent consensus. If the user requests separate
reviewers, give them the same draft and source context without the other
review's conclusions, combine findings only after both finish, and do not claim
independent review unless it occurred.

Run a premortem: assume failure at a meaningful milestone and trace the most
consequential plausible failures to plan details. For each, capture the causal
sequence, enabling assumption, likelihood and impact separately, earliest
warning, check time, mitigation, and revision or stop trigger. Label unverified
scenarios as hypotheses and thresholds as provisional; do not invent numerical
probabilities or promise to eliminate every risk. Include an adversary's
response only when adversarial behavior is relevant to the actual problem.

Use findings to change the plan and give a short reason for each material
revision. Put cheap checks of critical assumptions before expensive dependent
work. Resolve material objections or expose them as blockers; do not bury them
in a risk list. Recheck affected decisions and packages after each repair.

## Deliver

Save the plan to the user-specified path if one is given; otherwise use
`/tmp/loop-plan-<safe-task-slug>-result.md` (append a timestamp when a collision
is possible). Keep the runtime log separate. Make the plan understandable
without the preceding conversation and include only what the task needs:

- Outcome, success criteria, scope, constraints, and evidence or assumptions.
- Decision principles, ranked drivers, alternatives, chosen direction, and
  accepted consequences or conditions that would change the decision.
- Decision ledger with material uncertainties, review evidence, revisions, and
  explicit gates.
- Review manifest mapping each material decision to question or call IDs,
  initial and follow-up evidence, confirmation status, affected plan section,
  verification criterion, and unresolved disagreement.
- Ordered work packages, dependencies, affected files or interfaces, and
  completion checks.
- Premortem findings, mitigations, early signals, and revision or stop criteria.
- Unresolved questions or prerequisite investigations, material review changes,
  and readiness: `ready for approval`, `conditional`, or `blocked`, with reasons.

Before delivery, verify references are accurate, critical assumptions are
validated or explicitly gated, acceptance checks cover intended behavior, and
another implementer can proceed without hidden design decisions.
Readiness describes the plan; it is not user approval or evidence that planned
checks passed. If handing the document to `loop-coding`, preserve explicit
approval of that plan and let its implementation workflow own execution. End
with the plan path, chosen direction, and remaining decisions.
