# Common Testing Standards

Sections shared by [frontend.md](frontend.md) and [backend.md](backend.md).

## Test Target Value

Do not try to test all code at the same density. Evaluate the protection each test adds to the existing suite against the cost of writing, reading, running, and maintaining it. The goal is reliable protection of important behavior, not the fewest tests or the highest coverage number.

- Before adding or retaining a test, identify the important regression it catches that existing tests do not adequately cover.
- When a new feature reuses shared behavior, check what existing tests already protect. Add tests for how the feature uses that behavior and for any differences in its contract, rather than copying all tests for the shared behavior.
- Before removing a test, confirm that important requirements and failure cases remain protected.

## Focused Scenarios

Keep each scenario focused on its intended behavior. Combine multiple actions when their sequence is itself the requirement, not merely because they can be placed in one workflow. Do not extend an existing test with unrelated assertions for a new feature when that behavior belongs in another test.

## Review Checklist

Start with the test's purpose and contribution to the suite:

1. What important behavior does this test protect beyond the protection already provided by other tests?
2. Does it contain only the setup, actions, and assertions needed for that behavior?
3. Can a reader immediately understand the conditions, action, and expected outcome?

Then check:

- Would this test actually fail if that behavior broke?
- Does it preserve useful collaboration between real components while keeping its concern focused?
- Does the test verify externally observable behavior instead of internal implementation?
- Do test doubles replace external or unstable dependencies without replacing the behavior under test?
