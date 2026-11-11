---
title: "Make return values understandable by name"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-f9898f7d38f2932455c43604"]
---

# Make return values understandable by name

When callers must remember positions or internal implementation details to interpret return values, prefer named fields at the call site.

## Pydantic result model

A deidentified call-site fragment from an asynchronous service using Pydantic DTOs. Requires Pydantic. The host service supplies `validate_recipients` and changes its return type with the caller.

### Before

```python
roles, errors = await validate_recipients(recipients)
```

### After

```python
from pydantic import BaseModel

class ValidationResult(BaseModel):
    roles: dict[str, str]
    errors: dict[str, str]

# Change validate_recipients to return ValidationResult as well.
validation = await validate_recipients(recipients)
roles = validation.roles
errors = validation.errors
```

## Dataclass for internal context

A deidentified internal-context fragment. `Team` and `Role` are domain types supplied by the host service.

### Before

```python
team, actor_role = await self._get_member_context(team_id)
```

### After

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class _MemberContext:
    team: Team
    actor_role: Role

# Change the method to return _MemberContext as well.
context = await self._get_member_context(team_id)
team = context.team
actor_role = context.actor_role
```

Use Pydantic when runtime validation is needed; a lightweight dataclass can group internal data without adding that validation. A local tuple can remain suitable when its order directly matches the visible SQL select.
