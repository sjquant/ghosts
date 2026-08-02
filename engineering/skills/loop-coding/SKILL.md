---
name: loop-coding
description: Approval-gated implementation and self-review loop for coding tasks. Use when the user asks to build, change, fix, refactor, or implement code; do not activate for explanation-only, review-only, or planning-only requests.
---

# Loop Coding

Turn a coding request into an approval-gated implementation loop. Show the
implementation plan before making edits, then keep review, repair, regression
checks, and simplification internal until the change is ready to hand off.

## 1. Plan before editing

Understand the requested outcome, repository conventions, affected boundaries,
and likely validation needs. Make reasonable assumptions instead of asking for
details that do not change the design. Before modifying files, present a
concise plan containing:

- the goal and interpreted scope;
- the proposed design and important alternatives or tradeoffs;
- expected files or interfaces affected;
- tests and other validation to run; and
- material assumptions, risks, or irreversible actions.

Then wait for explicit approval. Treat `go`, `approve`, `yes`, or an equivalent
confirmation after the plan as approval. Do not start implementation from a
bare initial request. If the user has already explicitly approved a specific
plan, do not ask for approval again.

If implementation reveals a material scope or design change, pause, explain
the change and its tradeoff, and obtain approval for the new plan before
continuing. Do not silently expand the task or perform destructive or external
actions outside the approved scope.

## 2. Implement and validate

After approval, inspect the current code and tests, implement the smallest
coherent change, and run the most relevant checks. Prefer existing abstractions
and project conventions. Keep the diff focused and preserve unrelated user
changes.

## 3. Review and repair loop

After the first implementation:

1. Review the diff and validation results.
2. Invoke the available `code-review` skill for a broad read-only review. If it
   is unavailable, perform an equivalent review covering correctness,
   operational and security risks, design, simplification, and test quality.
3. Repair material findings using the smallest useful change.
4. Re-run the checks relevant to each repair.
5. Check whether a repair introduced regressions, side effects, broken
   assumptions, or new coupling.
6. Ask internally: “Any bugs or material issues that could change correctness,
   behavior, or scope?” Repair and re-check if the answer is yes.
7. Ask internally: “Any bloats, slops, or smells?” Remove unnecessary
   complexity, duplication, indirection, unclear naming, and brittle tests
   when doing so does not expand scope.

Repeat only while a material issue could change correctness, maintainability,
user intent, or validation confidence. Do not keep polishing after the change
is sound.

## 4. Finish

Before handoff, confirm that:

- the approved behavior is implemented;
- relevant tests, type checks, linters, builds, or other project checks pass;
- review findings are fixed or explicitly reported with their disposition;
- the final diff contains no accidental or unrelated changes; and
- remaining uncertainty or skipped validation is clearly stated.

Keep the internal loop and chain of thought private. In the final response,
summarize the implemented behavior, validation performed, notable review fixes,
and any remaining caveats.
