---
name: ghosts:test-review
description: Read-only review of test value, meaningful protection, and unnecessary complexity in a change, PR, or path.
disable-model-invocation: true
---

Review the tests read-only. Use the user's target or the change being discussed; otherwise review the current branch's diff against its base. Running existing tests to confirm findings is allowed; editing code or tests is not.

AI-generated tests can overcomplicate simple problems. First question whether a test is needed at all; judge its independent protection against maintenance and execution cost, not test count or coverage percentage.

- Any low-value, duplicate, implementation-shaped, tautological, obsolete, or one-off tests—including those that only recheck documented dependency guarantees—that can be removed or combined? Any hypothetical concurrency, timing, retry, or failure scenarios without a credible execution path or meaningful impact?
- Any behavior already protected by existing tests beyond the diff, including through public entrypoints? Search and compare scenarios and assertions, not names alone; cite the tests and assertions that retain protection when recommending removal or consolidation. Do not preserve incidental test behavior merely because it exists.
- Any important behavior, edge case, or material failure risk left unprotected by existing or new tests? Would the tests fail if that behavior broke? Could an existing case or suite be extended to cover the gap clearly? Recommend a separate test only when it gives clearer protection for a distinct behavior or regression risk.
- Any unnecessary setup, mocks, fixtures, assertions, or production interfaces added for testing? Could existing public entrypoints, real collaboration, or simpler cases give clearer protection? Keep narrower tests only when they add distinct value.

Apply these criteria where relevant:

- Assert observable outcomes and contractual side effects, with expected results derived from requirements rather than production logic. Verify relevant permissions and failures, including absence of unauthorized effects. Counts, ordering, exact payloads, and snapshots need a meaningful contract; snapshots must be focused, stable, and readable.
- Prefer integration through public entrypoints when it gives a clear signal; use focused tests for small rules. Replace external or unstable dependencies at the boundary without mocking away the behavior under test. Do not expose private members or add production abstractions solely for testing convenience.
- Keep scenario data minimal and visible, reuse established setup, and isolate mutable state and overrides. Control time, randomness, identifiers, and ordering when they affect results. Transaction setup must preserve the visibility the behavior requires.
- Make descriptions standalone and behavior-based, with Given / When / Then sections and concise explanations of non-obvious synchronization. Combine related cases when clearer, without bundling unrelated scenarios. Do not flag harmless style differences.
- For UI, query through accessible or user-visible context and wait for the intended rendered state. For servers, verify responses, persisted changes, and outgoing effects at the appropriate boundary. Reuse existing tools; do not expand a simple test into every testing layer.

Keep only evidenced, material findings. Recommend the smallest useful change, including removal or consolidation. Use `P1` for ineffective protection of important behavior or material risks, `P2` for unnecessary complexity, coupling, over-mocking, nondeterminism, or state leaks, and `P3` for readability that obscures the scenario or failure.

## Output

Write in the user's language. Omit empty sections and state when no actionable findings were found.

```markdown
## Findings

### <P1|P2|P3> - <title>

- Location: <file and line; commit-pinned permalink for GitHub targets>
- Evidence / criterion: <credible failure and impact, or unnecessary cost>
- Recommendation: <smallest useful change; meaningful protection retained if removing tests>
```
