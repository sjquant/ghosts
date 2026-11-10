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

A call-site excerpt from an asynchronous service using Pydantic DTOs.

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

A dataclass can group a domain object and a role for internal use. `orm.Organization` and `AccessRoleEnum` are domain types supplied by the service.

### Before

```python
organization, actor_role = await self._get_member_management_context(organization_id)
```

### After

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class _MemberManagementContext:
    organization: orm.Organization
    actor_role: AccessRoleEnum

# Change the method to return _MemberManagementContext as well.
context = await self._get_member_management_context(organization_id)
organization = context.organization
actor_role = context.actor_role
```
