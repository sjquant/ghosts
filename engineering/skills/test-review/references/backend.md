# Backend Testing Guide

This document defines the shared testing standards for backend teams. Tests are not written just to see `Pass`. They are written to fail quickly and clearly when important behavior is broken.

Repository structure, fixture names, and test commands may differ by repository. This guide focuses on shared judgment criteria for writing and reviewing backend tests, rather than repository-specific usage.

## 1. Testing Philosophy

### 1.1 Meaningful Failure

- A test should fail when the behavior it protects is broken.
- A test that keeps passing after a requirement change or bug does not provide safety. It only adds maintenance cost.
- If a refactor breaks a test while observable behavior remains the same, the test is likely coupled too tightly to implementation details.
- Regression tests and snapshot tests are useful when they protect contracts that must not change accidentally.
- If a test failure does not reveal which requirement was broken, improve the test name, setup, or assertions.

### 1.2 Choose Test Targets By Value

Apply [Test Target Value](common.md#test-target-value), and:

- When an integration test already protects a behavior, do not automatically repeat it in unit tests for every participating layer. Add focused tests where they provide additional protection or clearer checks of important edge cases.

High-priority targets:

- Business-critical flows such as payment, authentication, authorization, subscriptions, and event publishing
- Tasks and workers that are expensive to recover from when they fail
- Complex queries, pagination, cursors, ordering, locks, and idempotency
- Logic that interprets external system responses and mutates local state
- Edge-case-heavy logic such as dates, timezones, market holidays, exchange rates, decimals, and discounts

Lower-priority targets:

- Simple getters, setters, and DTO declarations
- Behavior already guaranteed by the library
- Shape errors that static analysis, type checkers, or linters catch better
- Tests that only repeat the implementation without improving behavioral safety

## 2. Test Scope Strategy

Prefer tests that keep the real collaboration needed to deliver a feature intact. A test can exercise an API, service, repository, and DB together while protecting one clearly defined behavior. The number of participating components and the number of concerns being tested are separate choices.

Apply [Focused Scenarios](common.md#focused-scenarios).

Recommended approach:

1. First check whether the behavior can be tested through an existing public entrypoint from the perspective of a user or external system. Do not expand production interfaces solely for testing convenience.
2. Prefer integration tests when API, service, repository, DB, and cache behavior can be verified together clearly.
3. Narrow the scope one level when the integration test becomes too slow, too hard to set up, or too hard to debug.
4. Use unit tests directly for naturally small units such as pure calculations, parsers, and validators.
5. Replace external systems we do not control at the test boundary, such as third-party APIs, payment providers, email, and object storage.

Why we prefer larger tests:

- They catch real wiring, transaction, serialization, and dependency override issues.
- They remain stable when internal calls change but the feature behavior stays the same.
- They produce a signal closer to production behavior than tests with heavy mocking.

When to narrow the scope:

- The setup is so large that the important condition is hard to see.
- The failure cause is difficult to isolate.
- Replacing external dependencies takes up most of the test.
- Slow tests start hurting the feedback loop.
- One complex rule needs many focused edge-case checks.

## 3. Test Naming And Grouping

Test names should reveal both the situation and the expected outcome.

Basic rules:

- Use `test_<situation>_<expected_outcome>` for test function names.
- Every test should have a docstring.
- For complex tests, use the docstring to describe the requirement or intent more specifically.
- Prefer capability- and outcome-oriented names over implementation-shaped names.
- Describe what the test actually exercises and observes. Do not claim to verify behavior that has been replaced by a test double.
- Use `pytest.mark.parametrize` with readable `ids` for cases of the same behavior that share an execution flow. Split cases when combining them introduces branches that obscure their different scenarios.

Example:

```python
async def test_expired_subscription_removes_user_role(...) -> None:
    """An expired subscription removes the user's role."""
```

Avoid implementation-shaped names:

```python
async def test_calls_delete_role(...) -> None:
    ...
```

### 3.1 Class Grouping

Use classes when related tests are easier to read as one group. Standalone test functions are appropriate when grouping adds no clarity.

- Group tests by feature or public entrypoint.
- Do not use classes to hide important setup or build complex lifecycles.
- Each test inside the class should still be understandable on its own.

## 4. AAA Pattern

Write test bodies in the `given / when / then` flow.

- `given`: Data, fixtures, mocks, and fixed time required for the scenario
- `when`: The behavior under test
- `then`: Observable results of `when`, such as the response, DB state, events, and external calls

Example:

```python
async def test_expired_subscription_removes_user_role(...) -> None:
    """An expired subscription removes the user's role."""
    # given
    subscription = create_subscription(status="active", expired=True)

    # when
    await expire_subscriptions()

    # then
    assert not user_has_role(subscription.user_id, "premium")
```

Notes:

- If `when` contains several independent actions, it becomes unclear which action caused the failure.
- One test may verify multiple results, but they should all come from the same behavior.
- Use helpers when setup becomes long, but keep the important scenario conditions visible in the test body.

## 5. Layer-Specific Guidelines

Use the largest layer that still gives a clear signal.

- API tests are a good default when behavior is observable through HTTP. Verify the response contract and important side effects.
- Service or domain tests are useful when the business rule is the main concern and an API test would be too heavy.
- Repository or DAO behavior is usually covered through a higher-level test. Test it directly only when the query contract itself is the main risk.
- Task and worker tests should focus on operational concerns such as duplicate handling, retries, partial failures, and idempotency.
- Avoid API loops for large setup. Insert data directly or use helpers/factories when setup is not the behavior under test.

## 6. Fixture And Test Data

Fixtures are tools for readability. They should not hide the important conditions of a test.

Good fixtures:

- Hide repeated infrastructure setup.
- Provide common dependencies such as DB sessions, clients, caches, repositories, and services.
- Make their provided state clear from the name.

Fixtures to be careful with:

- Fixtures that automatically create too many rows and make test conditions hard to trace.
- Fixtures that hide the core condition of a scenario.
- Fixtures that accept many scenario-specific parameters and become a small DSL.
- Deep fixture dependency chains that make failures hard to diagnose.

Recommended approach:

- Promote helpers or fixtures to a shared place when multiple domains reuse them.
- Keep domain-specific helpers near that domain.
- Keep scenario-specific core conditions in the test body.
- Reuse established setup helpers when their behavior is outside the test's concern.
- Extract helpers to make scenarios easier to understand, not just to remove repeated lines. A little duplication is preferable to an abstraction that hides the important conditions or execution flow.
- Use helper and factory names that reveal intent. Examples: `create_expired_subscription`, `create_verified_user`
- Create only the minimum rows required by the test.

### 6.1 DB Setup

- Isolate DB changes with transaction rollback whenever possible.
- Use `flush` when DB-generated values or query-visible rows are needed.
- Use `commit` only when verifying behavior that is visible only after commit, across separate transactions, or through task/worker entrypoints.
- Do not clean tables manually in tests. Before adding cleanup fixtures, confirm why transaction rollback cannot solve the problem.
- Prefer DB bulk inserts over API loops for large setup.

### 6.2 Cache And External State

- Prefer shared fixtures for cache cleanup, dependency overrides, monkeypatches, and environment overrides.
- Do not repeat cleanup setup in individual tests when the repository already handles it globally.
- Verify cache keys, TTLs, and session values directly when they are part of the contract.

## 7. Test Double Policy

Use test doubles to move the external world and unstable inputs to the test boundary.

Good targets for test doubles:

- Payment providers, Google Play, Apple, Firebase, S3, Discord, email, and Kafka producers
- Other servers or external HTTP clients
- Current time, randomness, and UUIDs
- Very slow or nondeterministic library calls

Avoid replacing when possible:

- Services, repositories, and DAOs in the same process
- Internal helpers called by the function under test
- Private properties or private methods
- The DB session itself
- The entire service behind an endpoint

Guidelines:

- Test doubles should make the test condition clearer.
- If replacing internal collaborators makes the test fragile during refactoring, switch to a larger-scope test.
- If a dependency is already mocked at an upper boundary, do not also mock the lower DAO unnecessarily.
- Use `spec` or real-object-based `patch.object` for `Mock` and `AsyncMock` whenever possible.
- Patch where the object is used, not where it is defined.

Partial replacement can be better than replacing the whole object. For example, instead of replacing an entire external client, create the client through the real factory and patch only the failing method. This keeps more framework wiring intact.

## 8. Time, Randomness, And Determinism

Tests should produce the same result every time they run.

- Freeze or patch the current time.
- When timezone behavior matters, assert the base timezone, UTC conversion, and epoch values explicitly.
- Use fixed values when randomness, UUIDs, or current time appear in DB values or responses.
- For ordering-sensitive tests, make `created_at`, `id`, and cursor values explicit.
- External API response fixtures should contain only the fields needed, but enough fields to represent the edge case.

## 9. Assertions

Good assertions make it clear what broke when the test fails.

Recommended:

- In API tests, assert `status_code` first.
- Use snapshots or exact dictionaries when the whole response is the contract.
- Assert only the important fields explicitly when only some fields are contractual.
- Verify DB side effects by reading them back through a repository or query.
- Assert downstream contracts directly, such as event payloads, unique keys, and published flags.
- For lists, assert length, order, and important identifiers together.

Avoid:

- Assertions that provide little signal, such as `assert response.json() is not None`
- Overly broad snapshots that fail on unrelated field changes
- Tests that only assert mock call counts without verifying actual state changes

## 10. Snapshot Usage

Snapshots are useful when protecting large JSON responses or complex payload contracts.

Use snapshots when:

- The entire response structure is part of the API contract.
- Volatile values are stabilized with matchers, fixed time, or fixed IDs.
- Snapshot updates are intentional and reviewed in the same PR as the code change.
- The diff is small enough for reviewers to understand.

Avoid snapshots when:

- Only a few fields matter.
- The collection ordering is not stable.
- Timestamps, UUIDs, or ordering change on every run.
- The payload is so large that failures are hard to interpret.

## 11. Coverage

Coverage is a signal, not the quality goal itself.

- Whether changed code protects important branches and failure cases matters more than total coverage.
- If PR coverage is low, explain why the code does not need tests or which higher-level test covers it.
- Use missing lines in the coverage report to find candidate test targets.
- Do not add meaningless tests just to increase coverage.

## 12. Review Checklist

Apply the [Review Checklist](common.md#review-checklist), and check the implementation and remaining risks:

- If the scope was narrowed, is the reason clear?
- Do the name and docstring accurately describe what the test exercises and observes?
- Is the `given / when / then` flow clear?
- Can DB, cache, and dependency overrides leak between tests?
- Are time, UUIDs, randomness, and ordering deterministic?
- Are necessary failure, permission, and authentication cases covered?
- Are backend-specific concerns such as pagination, cursors, idempotency, and transactions covered?
- If a snapshot is used, can reviewers understand the diff?
- If test doubles keep increasing, should the test move to a larger scope?
- If fixtures hide too many conditions, should those conditions move back into the test body?
