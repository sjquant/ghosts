---
title: "Keep operational signals people use"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-b4a3e9133e78faf331d1ed50"]
---

# Keep operational signals people use

When adding logs or notifications, identify who will inspect the signal and what it helps them check or diagnose. Duplicate execution tracking and unchecked start/end messages can obscure useful signals.

### Before

Every scheduled job sends start and completion notifications, although the scheduler already tracks execution and nobody checks most messages.

### After

Keep startup confirmation for the real-time feed that operators actually check. Let scheduler tracking cover routine execution. Retain progress reporting for a slow task when it helps operators see progress.

A normal event can still deserve a notification. Keep notification delivery separate from error tracing: a normal alert can be delivered without being marked for error tracing.

For user-correctable provider errors, such as an incorrect password, show the problem to the user instead of treating every occurrence as a developer alert. A targeted integrity-error log can remain useful when that is the specific failure being investigated.
