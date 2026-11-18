---
title: "Base reuse on shared responsibility"
scope: "global"
status: "proposed"
confidence: "high"
candidate_ids: ["candidate-a12f9118de168e849eeb9f63", "candidate-fc6fc381e8b51926798bd565"]
---

# Base reuse on shared responsibility

First consider extending an existing boundary that owns the same responsibility. Similar-looking concepts should remain separate when their meaning, control flow, or reasons for change differ.

## Extend an existing boundary for shared configuration

A deidentified interface-extension fragment: the host project supplies the existing data-volume factory and access-mode enum. Extend that factory when callers are configuring the same operation rather than coordinating a second wrapper.

### Before

```python
pod_config = get_data_writer_pod_configs(
    get_data_volume_configs(),
)
```

### After

```python
pod_config = get_data_volume_configs(
    data_access=DataAccess.WRITE,
)
```

Explicit mode options also fit CLI commands or batch jobs when an operator chooses a backfill policy (such as `missing` versus `overwrite`).

## Split functions instead of adding internal mode flags

Do not add boolean flags or raw event arguments (`allow_not_found`, `reject_on_conflict`, `apply`, or `changeSettings(event)`) that make one function branch between distinct actions or suppress boundary errors.

Deidentified lookup fragment; the host project supplies the repository query and `SubscriptionNotFoundError`.

### Before

```python
def get_active_subscription(session, account_id: int, *, allow_not_found: bool = False):
    subscription = query_active_subscription(session, account_id)
    if subscription is None and not allow_not_found:
        raise SubscriptionNotFoundError(account_id)
    return subscription
```

### After

```python
def get_active_subscription(session, account_id: int):
    subscription = query_active_subscription(session, account_id)
    if subscription is None:
        raise SubscriptionNotFoundError(account_id)
    return subscription
```

- When a lookup or mutation has different preconditions or failure handling, raise a domain exception at the boundary and let callers handle the case they expect, or expose separate functions named for each action (`enable_notifications()` and `disable_notifications()`).
- Team and personal-space permission policies have different hierarchies. Combining their rules introduces ambiguity and couples changes, so keep those policies separate.
- A wrapper helps when its name clarifies intent; repeating an already clear operation at the same abstraction level adds another place to read.
