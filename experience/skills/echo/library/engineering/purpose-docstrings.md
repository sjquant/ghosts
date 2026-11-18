---
title: "Write standalone docstrings, test descriptions, and comments"
scope: "global"
status: "proposed"
confidence: "high"
candidate_ids: ["candidate-c1327ad5524041c30971ca26", "candidate-46ef2c855b57d7228147a72b", "candidate-a6e6e50105e0bbddd31ae68d"]
---

# Write standalone docstrings, test descriptions, and comments

Write summaries, test descriptions, and inline comments for a reader who only sees the current code, not the pull request or refactoring history.

## Summaries and public contracts

Describe a function or result object's domain purpose in words that remain accurate when fields or filters are added. Keep caller-required contract details (`Args`, `Returns`, `Raises`) in structured Google-style sections on public functions and methods rather than packing every filter into the summary line or omitting parameter descriptions.

### Before

```python
def find_invitations(email: str, include_expired: bool = False) -> list[dict]:
    """Find invitation records by email using the shared lookup generator."""
    return [{"email": email, "expired": include_expired}]
```

### After

```python
def find_invitations(email: str, include_expired: bool = False) -> list[dict]:
    """Look up invitation records.

    Args:
        email: Recipient email address to match.
        include_expired: Whether to include expired invitations.

    Returns:
        Matching invitation records.
    """
    return [{"email": email, "expired": include_expired}]
```

## Context-free test descriptions

State what the function or test guarantees now in plain language. Avoid phrases that depend on prior code or PR discussion (`"common generator"`, `"per existing policy"`, `"and does not hang"`), omit incidental fixture names when the rule does not depend on them, and match the verb to what every parameterized case actually asserts.

Deidentified parameterized test fragment; the host project supplies the scheduling check and mocked notifier.

### Before

```python
@pytest.mark.parametrize("offset_hours", [0, 10])
def test_notify_window(offset_hours: int, notifier) -> None:
    """Sends a notification at the Sydney boundary per existing policy and does not hang."""
    notify_if_open(offset_hours=offset_hours, notifier=notifier)
    notifier.assert_called_once()
```

### After

```python
@pytest.mark.parametrize("offset_hours", [0, 10])
def test_notify_window(offset_hours: int, notifier) -> None:
    """Calls the notifier when the scheduled window opens regardless of timezone offset."""
    notify_if_open(offset_hours=offset_hours, notifier=notifier)
    notifier.assert_called_once()
```

## Inline comments at call sites

Do not add call-site comments that restate what a language primitive, framework hook, or helper already guarantees. If the mechanism itself needs explanation, document it once on the primitive or helper definition. Reserve call-site comments for non-obvious domain invariants or explicit `TODO` markers for temporary rollout compatibility.

Deidentified lock usage fragment; the host project supplies `acquire_row_lock` and `recalculate_balance`.

### Before

```python
# Acquire a row-level lock to serialize concurrent requests and prevent race conditions.
with acquire_row_lock(session, account_id):
    recalculate_balance(session, account_id)
```

### After

```python
with acquire_row_lock(session, account_id):
    # Keep the balance check inside the lock until the legacy writer is retired (TODO: remove after v2 rollout).
    recalculate_balance(session, account_id)
```
