---
name: ghosts:test-review
description: Read-only review of tests in a change, PR, or path against shared, frontend, and backend testing standards.
disable-model-invocation: true
---

# Test Review

Review the tests read-only. If no target is given, review the tests in the current branch's diff against the base branch. Write in the user's language.

Read and apply [references/common.md](references/common.md) for every review. Read [references/frontend.md](references/frontend.md) for UI or browser tests and [references/backend.md](references/backend.md) for server, worker, or data tests as supplements; use both when the change spans them. For another stack, apply only the common standards.

1. Map each changed behavior to the existing and new tests that protect it. Flag behavior no test would catch if it broke, and removed tests whose protection is not covered elsewhere.
2. Review each added, changed, or removed test against the guides' review checklists.
3. Keep only findings with a location, a concrete failure scenario, and a guide rule behind them. Running existing tests to confirm a finding is allowed; editing code or tests is not.

Prioritize findings:

- `P1`: a changed behavior has no test that would fail if it broke, or a test cannot fail for the regression it claims to catch.
- `P2`: implementation coupling, test doubles replacing the behavior under test, nondeterminism, leaking state, or redundant protection.
- `P3`: naming, structure, or readability.

Write the review following [templates/review.md](templates/review.md), replacing each placeholder or omitting the section as it directs.
