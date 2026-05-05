---
name: discovery-interview
description: Requirements-first discovery workflow that turns vague ideas into clear product specs. Use when the user has a vague product or feature idea and wants to clarify requirements, scope, user journeys, priorities, edge cases, or a product spec.
disable-model-invocation: true
---

## Role

This skill turns a vague idea into a clear requirements spec.

Default scope:
- problem statement
- users and stakeholders
- user journey
- functional scope
- priorities (`P0`, `P1`, `P2`)
- success criteria
- edge cases and failure states
- out-of-scope boundaries
- open product questions

Do not default into:
- stack selection
- technical architecture
- deployment design
- implementation planning

Those are optional modules and require explicit user intent.

## Default Workflow

### Phase 1: Orientation
Ask 2 to 3 broad questions:
- what problem are you solving?
- who is this for?
- is this new or a change to something existing?

Use the answers only to guide requirement questions. Do not jump into solution design.

### Phase 2: Requirements Discovery
Work through these categories in order. Ask 2 to 4 questions per category when needed.

1. Problem and outcomes
2. Users and stakeholders
3. User journey
4. Functional scope
5. Priorities and constraints
6. Edge cases and failure states

Focus on what the user needs, what success looks like, and where the boundaries are.

### Phase 3: Conflict Resolution
When requirements conflict, surface the tradeoff explicitly and ask the user to prioritize or refine.

### Phase 4: Completeness Check
Before writing the spec, confirm you have:
- a clear problem statement
- success criteria
- identified users and stakeholders
- a mapped core journey
- `P0`, `P1`, and `P2` scope
- edge cases and failure states
- explicit out-of-scope boundaries
- open product questions

Do not block spec generation on architecture details unless the user explicitly asked for the technical module.

## Optional Modules

Only load these when relevant:

- Optional modules and transition rules:
  [references/optional-modules.md](references/optional-modules.md)
- Question phrasing, knowledge-gap handling, and interview heuristics:
  [references/questioning-guidance.md](references/questioning-guidance.md)
- Spec template and optional spec sections:
  [references/spec-template.md](references/spec-template.md)

### Module Activation Rules

- `Product Deep Dive`: use when requirements need more depth around data, roles, policy, or operational behavior.
- `Research`: use when the user is unsure or asks for examples, references, or comparisons.
- `Technical Architecture`: use only when the user explicitly asks for stack, architecture, infrastructure, or deployment decisions.
- `Implementation Planning`: use only after a requirements spec exists and the user asks for build planning.

If the user asks for stack or architecture advice, ask whether they want to enter the technical module before continuing.

## Spec Generation

After the default completeness check passes:
1. summarize your understanding
2. confirm it with the user
3. write the spec to `specs/YYYY-MM-DD-<name>.md`

Use the default template in [references/spec-template.md](references/spec-template.md).
Only add optional sections if the matching optional module was explicitly used.

## Interaction Rules

- Default to requirements discovery only.
- Keep questions product-facing unless the user explicitly opts into technical design.
- Use research when it reduces ambiguity.
- Do not write a shallow spec after only a few questions.
- Do not assume the next step is technical architecture.

## Handoff

After the spec is written, ask what the user wants next:
- refine the requirements spec
- run a product deep dive
- enter technical architecture mode
- create an implementation plan
