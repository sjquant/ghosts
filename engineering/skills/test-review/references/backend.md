# Backend Testing Guide

This document defines the shared testing standards for backend teams. Tests are not written just to see `Pass`. They are written to fail quickly and clearly when important behavior is broken.

Repository structure, fixture names, and test commands may differ by repository. This guide focuses on shared judgment criteria for writing and reviewing backend tests, rather than repository-specific usage.

## 1. Testing Philosophy

### 1.1 Meaningful Failure

Apply [Meaningful Failure](common.md#meaningful-failure).

### 1.2 Choose Test Targets By Value

Apply [Test Target Value](common.md#test-target-value).

High-priority targets:

- Business-critical flows such as payment, authentication, authorization, subscriptions, and event publishing
- Tasks and workers that are expensive to recover from when they fail
- Complex queries, pagination, cursors, ordering, locks, and idempotency
- Logic that interprets external system responses and mutates local state
- Edge-case-heavy logic such as dates, timezones, market holidays, exchange rates, decimals, and discounts

## 2. Test Scope Strategy

Apply [Test Scope](common.md#test-scope) and [Focused Scenarios](common.md#focused-scenarios). API, service, repository, DB, and cache integration tests can catch wiring, transaction, serialization, and dependency override issues.

## 3. Test Naming And Grouping

Apply [Focused Scenarios](common.md#focused-scenarios).

Basic rules:

- Use `test_<situation>_<expected_outcome>` for test function names.
- Every test should have a docstring.
- Use `pytest.mark.parametrize` with readable `ids` for cases that share an execution flow.

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

Apply [Focused Scenarios](common.md#focused-scenarios).

## 5. Layer-Specific Guidelines

Use the largest layer that still gives a clear signal.

- API tests are a good default when behavior is observable through HTTP. Verify the response contract and important side effects.
- Service or domain tests are useful when the business rule is the main concern and an API test would be too heavy.
- Repository or DAO behavior is usually covered through a higher-level test. Test it directly only when the query contract itself is the main risk.
- Task and worker tests should focus on operational concerns such as duplicate handling, retries, partial failures, and idempotency.
- Avoid API loops for large setup. Insert data directly or use helpers/factories when setup is not the behavior under test.

## 6. Fixture And Test Data

Apply [Fixtures And Isolation](common.md#fixtures-and-isolation). Backend fixtures commonly provide DB sessions, clients, caches, repositories, and services; scenario factories can use names such as `create_expired_subscription` or `create_verified_user`.

### 6.1 DB Setup

- Isolate DB changes with transaction rollback whenever possible.
- Use `flush` when DB-generated values or query-visible rows are needed.
- Use `commit` only when verifying behavior that is visible only after commit, across separate transactions, or through task/worker entrypoints.
- Do not clean tables manually in tests. Before adding cleanup fixtures, confirm why transaction rollback cannot solve the problem.
- Prefer DB bulk inserts over API loops for large setup.

### 6.2 Cache And External State

- Isolate cache state and restore dependency overrides, monkeypatches, and environment overrides through the established fixture lifecycle.
- Verify cache keys, TTLs, and session values directly when they are part of the contract.

## 7. Test Double Policy

Apply [Test Scope](common.md#test-scope) and [Deterministic Inputs](common.md#deterministic-inputs).

Good targets for test doubles:

- Payment providers, Google Play, Apple, Firebase, S3, Discord, email, and Kafka producers
- Other servers or external HTTP clients
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

## 8. Time, Randomness, And Determinism

Apply [Deterministic Inputs](common.md#deterministic-inputs). For ordering-sensitive queries and pagination, make `created_at`, IDs, and cursor values explicit. Verify timezone conversion or epoch values when they form the storage or response contract.

## 9. Assertions

Apply [Assertions And Failure Cases](common.md#assertions-and-failure-cases).

- In API tests, assert `status_code` first.
- Verify DB side effects by reading them back through a repository or query.
- Assert downstream contracts directly, such as event payloads, unique keys, and published flags.
- Verify authentication and authorization failures at the server boundary, including rejected requests and the absence of unauthorized side effects.

## 10. Snapshot Usage

Apply [Snapshots](common.md#snapshots). Response JSON and event payloads can be snapshot targets when their full shape is a stable backend contract.

## 11. Coverage

Apply [Coverage](common.md#coverage).

## 12. Review Checklist

Apply the [Review Checklist](common.md#review-checklist), and check the implementation and remaining risks:

- Can DB, cache, and dependency overrides leak between tests?
- Are server authentication and authorization enforced, including rejected requests and unauthorized side effects?
- Are backend-specific concerns such as pagination, cursors, idempotency, and transactions covered?
