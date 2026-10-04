---
name: test-review
description: Read-only review of tests in a change, PR, or path against shared, frontend, and backend testing standards.
disable-model-invocation: true
---

# Test Review

Review the tests read-only. If no target is given, review the tests in the current branch's diff against the base branch. Write in the user's language.

Always apply [references/common.md](references/common.md). Add [references/frontend.md](references/frontend.md) for UI or browser tests and [references/backend.md](references/backend.md) for server, worker, or data tests; use both when the change spans them. For another stack, apply only `common.md`.

```text
[Scope] → [Map behavior → tests] → [Review each test] → [Any gap or unsupported finding?]
                                                          ├─ No → [Write review] → [Done]
                                                          └─ Yes → [Repair earliest affected step] ↺
```

## Runtime checklist

Before acting, create `/tmp/test-review-<safe-task-slug>.md` with `Current state: Pass 1 / Next: Scope`, the checklist below, and an empty append-only `Repair log:`. Process items in order, finish each before moving on, record a short outcome, and mark `[x]` only after completion; use `[-]` only with a reason. After a repair, append a numbered `[ ] Recheck Pn: ...` row for the earliest affected item and log the trigger, change, rechecked items, and result. Finish only after final validation.

```text
- [ ] Scope: identify the target tests, the production change, and the guides that apply
- [ ] Map each changed behavior to the existing and new tests that protect it
- [ ] Review each added, changed, or removed test against the guides' review checklists
- [ ] Any changed behavior left unprotected, or a removed test whose protection is not covered elsewhere?
- [ ] Any test that would keep passing if its behavior broke, or that only duplicates existing protection?
- [ ] Any finding without a location, a concrete failure scenario, and a guide rule behind it?
- [ ] Final validation and review
```

Answer each `Any ...?` row Yes or No. On Yes, repair the smallest issue, append the recheck row and repair-log entry, and return to the earliest affected step. Running existing tests is allowed to confirm a finding; editing code or tests is not.

## Findings

Report only findings tied to a guide rule and a concrete consequence. Prioritize:

- `P1`: a changed behavior has no test that would fail if it broke, or a test cannot fail for the regression it claims to catch.
- `P2`: implementation coupling, test doubles replacing the behavior under test, nondeterminism, leaking state, or redundant protection.
- `P3`: naming, structure, or readability.

Write the review following [templates/review.md](templates/review.md), replacing each placeholder or omitting the section as it directs.
