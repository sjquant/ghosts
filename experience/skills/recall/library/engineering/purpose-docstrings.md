---
title: "Describe the stable purpose in a docstring"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-c1327ad5524041c30971ca26"]
---

# Describe the stable purpose in a docstring

When writing a function or result-object summary, describe its domain purpose in words that remain accurate when fields or filters are added. Keep caller-required contract details separate from the summary.

### Before

```text
Find invitation records by email.
```

### After

```text
Look up invitation records.
```

Concise summaries do not replace useful public contracts. Keep Args descriptions and public-method documentation when callers need them.
