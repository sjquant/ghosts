---
title: "Place tests alongside their target module structure"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-f12222dbee13b32d56d14d81"]
---

# Place tests alongside their target module structure

When adding or renaming tests, start with the file corresponding to the target module. A new feature, result or scenario alone does not call for another file.

These generalized paths illustrate placement; they do not describe a particular checkout.

### Before

```text
app/accounts/views/team.py
tests/accounts/views/test_team_search.py
tests/accounts/views/test_team_invitation.py

app/mail/services/delivery.py
tests/mail/test_delivery.py

src/use-quotes.ts
tests/use-prices.spec.ts
```

### After

```text
app/accounts/views/team.py
tests/accounts/views/test_team.py

app/mail/services/delivery.py
tests/mail/services/test_delivery.py

src/use-quotes.ts
tests/use-quotes.spec.ts
```

Group scenarios within the matching file; pytest test classes can provide that grouping. Check for duplicate coverage when the existing file already verifies the same behavior.
