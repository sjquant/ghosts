---
name: simplify
description: Simplify recently changed code for clarity, reuse, quality, and efficiency while preserving caller-visible behavior.
disable-model-invocation: true
---

Simplify recently changed code. Preserve caller-visible behavior exactly.

## Scope

Start from the current diff:

1. Use `git diff HEAD` to identify changed files.
2. If there is no diff, use files the user explicitly mentioned or recently edited.
3. Inspect representative callers, adjacent helpers, and relevant tests before editing.
4. Keep changes inside the requested scope. Do not broaden into unrelated cleanup.

## Review Passes

Check the scoped code through these lenses before editing:

- Reuse: replace duplicated or hand-rolled logic with existing utilities, components, types, constants, or patterns already used in the repo.
- Quality: remove needless variables, branches, wrappers, helper functions, intermediate state, duplicated control flow, dead code, debug leftovers, and self-explaining comments.
- Clarity: reduce verbose code or prose to concise wording when the shorter form preserves meaning and remains easier to read.
- Efficiency: simplify repeated I/O, parsing, serialization, allocation, loops, async work, or large-collection work without changing ordering, errors, or resource lifetime.
- Standards: follow the repo's existing style, naming, module boundaries, imports, tests, and local instructions.

## Editing Rules

- Prefer readable, explicit code over clever compact code.
- Do not optimize for fewer lines when it makes debugging or future edits harder.
- Do not change public APIs, output, data shape, error behavior, ordering, defaults, accessibility, timing assumptions, or persistence semantics unless the user explicitly asks.
- Do not expose private methods or properties for testing.
- Keep useful abstractions that encode ownership or reduce real complexity.
- Remove abstractions only when they are pass-through, duplicated, stale, or harder to understand than the direct expression.
- Keep comments that explain non-obvious constraints. Remove comments that restate obvious code.
- Preserve test intent. Prefer black-box integration coverage for behavior touched by the simplification.

## Workflow

1. Identify the changed behavior and the behavior that must stay fixed.
2. Search for existing patterns or utilities before introducing new helpers.
3. Make the smallest behavior-preserving edits that improve clarity, reuse, quality, or efficiency.
4. Run the narrowest meaningful validation first, then broader validation when risk or shared code warrants it.
5. If validation fails, fix the cause or revert only your own simplification.
6. Summarize what became simpler, what behavior was preserved, and what validation ran.

## Stop Conditions

Stop and report instead of editing when:

- The requested simplification requires behavior or API changes.
- The current behavior is ambiguous and tests or callers do not clarify it.
- Existing user changes conflict with the simplification.
- Validation cannot run for an environment reason outside the repo.
