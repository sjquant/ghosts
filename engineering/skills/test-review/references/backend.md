# Backend Testing Guide

Backend-specific standards. Apply them together with `common.md`. Repository structure, fixture names, and test commands may differ by repository; these are shared judgment criteria, not repository-specific usage.

## 1. Test Targets

High-priority targets:

- Business-critical flows such as payment, authentication, authorization, subscriptions, and event publishing
- Tasks and workers that are expensive to recover from when they fail
- Complex queries, pagination, cursors, ordering, locks, and idempotency
- Logic that interprets external system responses and mutates local state
- Edge-case-heavy logic such as dates, timezones, market holidays, exchange rates, decimals, and discounts

Lower-priority targets:

- Simple getters, setters, and DTO declarations
- Behavior already guaranteed by the library
- Tests that only repeat the implementation without improving behavioral safety

## 2. Scope Strategy

A test can exercise an API, service, repository, and DB together while protecting one clearly defined behavior.

1. First check whether the behavior can be tested through an existing public entrypoint from the perspective of a user or external system.
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

### 2.1 Layer-Specific Guidelines

Use the largest layer that still gives a clear signal.

- API tests are a good default when behavior is observable through HTTP. Verify the response contract and important side effects.
- Service or domain tests are useful when the business rule is the main concern and an API test would be too heavy.
- Repository or DAO behavior is usually covered through a higher-level test. Test it directly only when the query contract itself is the main risk.
- Task and worker tests should focus on operational concerns such as duplicate handling, retries, partial failures, and idempotency.
- Avoid API loops for large setup. Insert data directly or use helpers/factories when setup is not the behavior under test.

## 3. Naming And Grouping

- Use `test_<situation>_<expected_outcome>` for test function names.
- Every test should have a docstring. For complex tests, use the docstring to describe the requirement or intent more specifically.
- Use `pytest.mark.parametrize` with readable `ids` for parameterized cases.

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

## 4. Given / When / Then In Tests

Mark each section with `# given`, `# when`, and `# then`. `given` includes fixed time; `then` covers the response, DB state, events, and external calls.

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

## 5. Fixtures And Test Data

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
- Use helper and factory names that reveal intent. Examples: `create_expired_subscription`, `create_verified_user`
- Create only the minimum rows required by the test.

### 5.1 DB Setup

- Isolate DB changes with transaction rollback whenever possible.
- Use `flush` when DB-generated values or query-visible rows are needed.
- Use `commit` only when verifying behavior that is visible only after commit, across separate transactions, or through task/worker entrypoints.
- Do not clean tables manually in tests. Before adding cleanup fixtures, confirm why transaction rollback cannot solve the problem.
- Prefer DB bulk inserts over API loops for large setup.

### 5.2 Cache And External State

- Prefer shared fixtures for cache cleanup, dependency overrides, monkeypatches, and environment overrides.
- Do not repeat cleanup setup in individual tests when the repository already handles it globally.
- Verify cache keys, TTLs, and session values directly when they are part of the contract.

## 6. Test Doubles

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

- If a dependency is already mocked at an upper boundary, do not also mock the lower DAO unnecessarily.
- Use `spec` or real-object-based `patch.object` for `Mock` and `AsyncMock` whenever possible.
- Patch where the object is used, not where it is defined.

Partial replacement can be better than replacing the whole object. For example, instead of replacing an entire external client, create the client through the real factory and patch only the failing method. This keeps more framework wiring intact.

## 7. Time, Randomness, And Ordering

- Freeze or patch the current time.
- When timezone behavior matters, assert the base timezone, UTC conversion, and epoch values explicitly.
- Use fixed values when randomness, UUIDs, or current time appear in DB values or responses.
- For ordering-sensitive tests, make `created_at`, `id`, and cursor values explicit.
- External API response fixtures should contain only the fields needed, but enough fields to represent the edge case.

## 8. Assertions

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
- Recomputing the expected value with the same logic as the implementation under test

## 9. Snapshot Usage

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

## 10. Coverage

Coverage is a signal, not the quality goal itself.

- Whether changed code protects important branches and failure cases matters more than total coverage.
- If PR coverage is low, explain why the code does not need tests or which higher-level test covers it.
- Use missing lines in the coverage report to find candidate test targets.
- Do not add meaningless tests just to increase coverage.

## 11. Review Checklist

In addition to the common checklist:

- If the scope was narrowed, is the reason clear?
- Does every test have a docstring that accurately describes what it exercises and observes?
- Can DB, cache, and dependency overrides leak between tests?
- Are necessary failure, permission, and authentication cases covered?
- Are backend-specific concerns such as pagination, cursors, idempotency, and transactions covered?
- If a snapshot is used, can reviewers understand the diff?
