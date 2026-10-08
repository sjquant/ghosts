# Common Testing Standards

Sections shared by [frontend.md](frontend.md) and [backend.md](backend.md).

## Meaningful Failure

Tests should fail when the behavior they protect is broken and make the broken requirement clear. Improve the name, setup, or assertions when a failure is hard to interpret. If a refactor breaks a test without changing observable behavior, reconsider its implementation coupling.

## Test Target Value

Do not try to test all code at the same density. Evaluate the protection each test adds to the existing suite against the cost of writing, reading, running, and maintaining it. The goal is reliable protection of important behavior, not the fewest tests or the highest coverage number.

- Before adding or retaining a test, identify the important regression it catches that existing tests do not adequately cover.
- When a new feature reuses shared behavior, check what existing tests already protect. Add tests for how the feature uses that behavior and for any differences in its contract, rather than copying all tests for the shared behavior.
- When an integration test already protects a behavior, add narrower tests only when they provide independent protection or clearer checks of important edge cases.
- Before removing a test, confirm that important requirements and failure cases remain protected.
- Give lower priority to simple getters, setters, type declarations, and behavior already guaranteed by libraries or static analysis. Test application requirements those guarantees do not cover.

## Test Scope

Start from an existing public entrypoint and preserve the real collaboration needed to deliver the behavior. A test can involve several components while protecting one focused concern. Prefer integration tests when they give a clear signal; unit tests suit naturally small rules such as calculations, parsers, and validators.

- Narrow the scope when setup obscures the scenario, failures are difficult to isolate, dependency replacement dominates the test, execution cost hurts feedback, or one rule needs many focused edge cases. Keep the reason clear and check what integration protection remains.
- Replace external or unstable dependencies at the test boundary without replacing the behavior under test. If internal mocks keep increasing or make refactoring fragile, reconsider a larger scope.
- Before changing production code for testability, check existing public interfaces. Do not expose private members or add abstractions solely for testing convenience; require a clear behavioral testing benefit for design changes.

## Focused Scenarios

Keep each scenario focused on its intended behavior. Combine multiple actions when their sequence is itself the requirement, not merely because they can be placed in one workflow. Do not extend an existing test with unrelated assertions for a new feature when that behavior belongs in another test.

- Make each test understandable on its own, including when setup is shared. Names and descriptions should reveal the scenario and observable outcome; do not claim to verify behavior replaced by a test double.
- Keep setup, action, and observable results in the Given / When / Then flow. Multiple assertions should describe results of the same behavior.
- Parameterize cases of the same behavior with readable case names when they share an execution flow. Split cases when branches obscure their distinct scenarios.

## Fixtures And Isolation

- Reuse established setup for infrastructure outside the test's concern, while keeping scenario-specific conditions and actions visible.
- Create only the data required for the scenario, with enough fields and variation to represent its edge cases.
- Avoid helpers that create excessive data, accept many scenario-specific parameters, or hide conditions behind deep dependency chains.
- Extract helpers for clarity; a little duplication is preferable to hiding the scenario. Use names that reveal the provided state, share helpers when multiple features reuse them, and keep feature-specific helpers near the feature.
- Ensure mutable state and test overrides cannot leak between tests. Choose isolation or restoration appropriate to the resource; reuse established cleanup instead of repeating it when the environment already handles it.

## Deterministic Inputs

Control unstable inputs when they affect the behavior or assertions.

- Use fixed or controlled time, randomness, and UUIDs when their values matter to the scenario.
- For ordering-sensitive behavior, make sort inputs explicit and verify the required order.
- When timezone behavior is contractual, verify the relevant timezone, conversion, or epoch values.

## Assertions And Failure Cases

- Derive expected outcomes from requirements, independently of production logic. Avoid tautological tests that repeat production logic or assert only mock setup.
- Assert the observable results and outgoing interactions that form the contract. Check specific fields when only those fields matter, and exact objects when the whole payload is contractual.
- For lists, verify length, order, and item identities when those properties are requirements.
- Existence checks or mock call counts are sufficient only when existence or call count is itself the contract, such as preventing duplicate sends. Otherwise verify the intended result or payload.
- Cover failure, permission, and authentication cases relevant to the changed behavior through observable outcomes at the tested boundary.

## Snapshots

Use snapshots when the full shape of a focused output is a stable contract and reviewers can understand its diff.

- Stabilize volatile values and ordering using appropriate matchers or controlled inputs.
- Update snapshots intentionally and review their changes with the code change.
- Prefer explicit assertions when only a few fields matter. Avoid snapshots covering unrelated output or producing too much data to interpret.

## Coverage

Coverage is a signal for finding test gaps, not a quality goal. Protection of important branches and failure cases matters more than the percentage. Use uncovered code to identify candidate scenarios, explain protection elsewhere or low-value targets when relevant, and do not add meaningless tests to raise coverage.

## Review Checklist

Start with the test's purpose and contribution to the suite:

1. What important behavior does this test protect beyond the protection already provided by other tests?
2. Does it contain only the setup, actions, and assertions needed for that behavior?
3. Can a reader immediately understand the conditions, action, and expected outcome?

Then check:

- Would this test actually fail if that behavior broke, or do its assertions merely repeat production logic or mock setup?
- Does it preserve useful collaboration between real components while keeping its concern focused?
- If the scope was narrowed, is the reason clear and is necessary integration protection retained?
- Do the name and description accurately reflect the scenario and observable outcome, with a clear Given / When / Then flow?
- Does the test verify externally observable behavior instead of internal implementation?
- Do test doubles replace external or unstable dependencies without replacing the behavior under test?
- Do fixtures expose the important conditions with only the necessary data, or should hidden setup move into the test body?
- Can mutable state or test overrides leak between tests?
- Are inputs that affect the result controlled, including time, UUIDs, randomness, and ordering?
- Do assertions verify the required results, payloads, or interactions rather than incidental properties?
- Are relevant failure, permission, and authentication cases covered?
- If a snapshot is used, does it protect a focused contract with a readable diff?
