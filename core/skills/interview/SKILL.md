---
name: interview
description: Interview the user one question at a time until intent, scope, constraints, and success criteria are clear, then produce a concise execution-ready brief for confirmation.
disable-model-invocation: true
---

## Role

This skill clarifies what the user actually wants before planning or implementation.

Use it when the user asks for an interview, asks to clarify a vague request before execution, or wants an execution-ready brief before work begins.

Do not plan, implement, create tasks, write specs, or edit files during the interview.

## Opening

Start with exactly:

- `HYPOTHESIS:` one sentence describing what you think the user actually wants.
- `CONFIDENCE:` 0-100%, with a short reason if below 70%.

Then ask exactly one focused question.

Every question must include the current guess:

```text
Q: <one focused question>
GUESS: <your best guess and why you think that>
```

Wait for the user's answer before asking the next question.

## Interview Priorities

Clarify these in order:

1. Intent: why the user wants this.
2. Outcome: what end state the user actually wants.
3. User or audience: who benefits or uses it.
4. Scope: how far the change should go.
5. Non-goals: what must stay out of scope.
6. Constraints: technical, business, time, cost, UX, compatibility, privacy, and security.
7. Success criteria: how the user will know it worked.
8. Decision boundaries: what the agent may decide and what requires confirmation.
9. Existing context: codebase, product, users, docs, dependencies, and prior decisions.

For coding tasks, ask implementation-detail questions only after intent, outcome, scope, non-goals, and constraints are clear.

If an answer depends on facts available in the codebase or documents, inspect those facts instead of asking the user. Ask the user only for judgment, tradeoffs, priorities, business logic, or preferences.

## Question Rules

- Ask exactly one question at a time.
- After each answer, update the hypothesis and confidence.
- Do not batch questions.
- Do not accept vague words as final answers, including `scalable`, `robust`, `clean`, `modern`, `best practice`, `production-ready`, `intuitive`, and `enterprise-grade`.
- When the user gives vague wording, ask what it means concretely in this situation.

## Pressure Test

Ask at least one pressure-test question before ending the interview.

Use one of these forms:

- Example: "Can you give a concrete example or counterexample?"
- Assumption: "What assumption would make this wrong?"
- Tradeoff: "If we cannot have both A and B, which one wins?"
- Boundary: "What should we explicitly not do in the first pass?"
- Real want: "If you did not have to justify this to anyone, what would you actually want?"

## Stop Condition

Stop interviewing only when all of these are true:

- You can predict the user's reaction to the next 2 to 3 likely questions.
- Intent, outcome, scope, constraints, success criteria, non-goals, and decision boundaries are explicit.
- At least one pressure-test question has been asked.
- Another question would only polish wording and would not materially change the work.

If confidence is still low after several rounds, say what foundational piece is missing and ask one reframing question.

## Final Brief

When ready, produce this brief and ask for explicit confirmation:

```md
# Confirmed Intent Brief

- Outcome:
- User / audience:
- Why now:
- Success criteria:
- Scope:
- Non-goals:
- Constraints:
- Decision boundaries:
  - You may decide:
  - Ask me before deciding:
- Key assumptions:
- Open questions, if any:

Confirm / refine / reject?
```

Do not treat `whatever you think`, `sounds good`, or `sure` as strong confirmation. If confirmation is vague, ask what the user would refine before moving on.

## Related Skills

- Use `discovery-interview` after confirmation when the user wants a deeper product requirements workflow.
- Use `sdd` after confirmation when the user asks for a SPEC or TASKS document.
- Use `handoff` after confirmation when the clarified work needs to be packaged for another agent or future session.
- Use `gotchas` after confirmation when the clarified work is about capturing lessons, pitfalls, or operating constraints.
