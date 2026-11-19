---
title: "Name the meaning readers should predict"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-bb1e5f76070def1f7e4a5b3f"]
---

# Name the meaning readers should predict

When choosing a name, ask what a reader would predict about the value, state or action without opening its implementation. Grammatical formulas are useful only when they preserve that meaning.

## A decision is not a completed state

Executable Python reduction: the boolean decides whether the function will update a value.

### Before

```python
def set_value(state, replacement, value_updated):
    if value_updated:
        state["value"] = replacement
```

### After

```python
def set_value(state, replacement, update_value):
    if update_value:
        state["value"] = replacement
```

`value_updated` describes something already completed. `update_value` describes the decision being passed in. A longer `should_update_value` is also clear; length alone does not make it better.

## Make mutations visible

If an operation updates state, name the update rather than implying a read-only `get`.

A technology term is useful when it distinguishes the actual implementation: `SocketIORoom` is more precise than `SocketRoom` when the implementation depends on Socket.IO APIs.
