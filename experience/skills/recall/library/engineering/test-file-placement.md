---
title: "Place tests alongside their target module structure"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-f12222dbee13b32d56d14d81"]
---

# Place tests alongside their target module structure

Start with the test file corresponding to the target module. A new feature, result or scenario alone does not call for another file.

## File layout

### Before

Separate files accumulate for features and results.

```text
app/account/views/channel.py
tests/account/views/test_channel_search.py
tests/account/views/test_channel_invitation.py

app/mail/services/delivery.py
tests/mail/test_delivery.py
```

### After

Match the target module’s path and filename, then organize scenarios within that file.

```text
app/account/views/channel.py
tests/account/views/test_channel.py

app/mail/services/delivery.py
tests/mail/services/test_delivery.py
```

Use test classes where grouping is needed. Check for duplicate coverage when the existing file already verifies the same behavior.
