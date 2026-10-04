# Common Testing Guide

Shared standards for frontend and backend tests. Tests are not written just to see `Pass`. They are written to fail quickly and clearly when important behavior is broken.

## 1. Meaningful Failure

- A test should fail when the behavior it protects is broken.
- A test that keeps passing after a requirement change, bug, or meaningful regression does not improve safety. It only adds maintenance cost.
- If a refactor breaks a test while observable behavior remains the same, the test is coupled too tightly to implementation details.
- Regression tests and snapshot tests are useful when they protect behavior or contracts that must not change accidentally.
- If a test failure does not reveal which requirement was broken, improve the test name, setup, or assertions.
- If a test does not meaningfully fail for any realistic change, reconsider whether it should exist at all. In many cases, deleting it is the better choice.

## 2. Choose Test Targets By Value

Do not try to test all code at the same density. Evaluate the protection each test adds to the existing suite against the cost of writing, reading, running, and maintaining it. The goal is reliable protection of important behavior, not the fewest tests or the highest coverage number.

- Before adding or retaining a test, identify the important regression it catches that existing tests do not adequately cover.
- When a new feature reuses shared behavior, check what existing tests already protect. Add tests for how the feature uses that behavior and for any differences in its contract, rather than copying all tests for the shared behavior.
- When an integration test already protects a behavior, do not automatically repeat it in unit tests for every participating unit. Add focused tests where they provide additional protection or clearer checks of important edge cases.
- Before removing a test, confirm that important requirements and failure cases remain protected.
- Do not duplicate coverage for shape errors that static analysis, type checkers, or linters catch better.

## 3. Test Scope

Prefer tests that keep the real collaboration needed to deliver a feature intact. A test can exercise several components or layers together while protecting one clearly defined behavior. The number of participating components and the number of concerns being tested are separate choices.

Keep each scenario focused on its intended behavior. Combine multiple actions when their sequence is itself the requirement, not merely because they can be placed in one workflow. Do not extend an existing test with unrelated assertions for a new feature when that behavior belongs in another test.

## 4. Black-box Tests And Testability

Test externally observable behavior, not internal implementation details.

- Do not read private properties, private methods, or internal state directly.
- Write tests from a black-box perspective: if input A is applied, does the user or external system observe result B?
- First check whether the behavior can be verified through an existing public entrypoint before changing production code for testability.
- Do not expand production interfaces or add abstractions solely for testing convenience. Change the design only when the testing value clearly outweighs the design cost; improving a function interface is usually better than making the design more complex.

## 5. Naming

- Make test names specific enough to reveal both the situation and the expected outcome.
- Prefer capability- and outcome-oriented names over implementation-shaped names.
  Example: `user can checkout with a valid cart` is better than `calls submitOrder with transformed payload`.
- Describe what the test actually exercises and observes. Do not claim to verify behavior that has been replaced by a test double.
- Use parameterized tests with readable case names for cases of the same behavior that share an execution flow. Split cases when combining them introduces branches that obscure their different scenarios.

## 6. Given / When / Then

Every test body follows the `given / when / then` flow, with each section marked by a comment.

- `given`: Initial state, data, dependencies, test doubles, and fixed inputs required for the scenario
- `when`: The behavior under test
- `then`: Observable results of `when`

Notes:

- If `when` contains several independent actions, it becomes unclear which action caused the failure.
- One test may verify multiple results, but they should all come from the same behavior.
- Add supporting comments when they improve readability.

## 7. Setup Helpers And Fixtures

- Reuse established setup helpers for dependencies outside the test's concern instead of recreating them in each test.
- Keep scenario-specific conditions and the execution flow visible in the test body.
- Extract helpers to make scenarios easier to understand, not just to remove repeated lines. A little duplication is preferable to an abstraction that hides the important conditions or execution flow.
- Use helper names that reveal intent.

## 8. Test Doubles

Limit test doubles to the external world we do not control and to unstable inputs.

- Test doubles should make the test condition clearer, and their reason should be easy to explain.
- Do not increase test double usage just to make the test easier to write.
- Do not replace the behavior under test or the in-process collaborators that deliver it.
- If replacing internal collaborators makes the test fragile during refactoring, or test doubles keep increasing, switch to a larger-scope test.

## 9. Determinism

Tests should produce the same result every time they run. Move unstable values such as current time, randomness, and UUIDs to the test boundary and fix them in the test.

## 10. Review Checklist

Start with the test's purpose and contribution to the suite:

1. What important behavior does this test protect beyond the protection already provided by other tests?
2. Does it contain only the setup, actions, and assertions needed for that behavior?
3. Can a reader immediately understand the conditions, action, and expected outcome?

Then check how the test provides that protection:

- Would this test actually fail if that behavior broke?
- Does it preserve useful collaboration between real components while keeping its concern focused?
- Do the name and description accurately reflect what the test exercises and observes?
- Is the `given / when / then` flow clear?
- Does the test verify externally observable behavior instead of internal implementation?
- Do test doubles replace external or unstable dependencies without replacing the behavior under test?
- Are time, UUIDs, randomness, and ordering deterministic?
- If fixtures or helpers hide too many conditions, should those conditions move back into the test body?
