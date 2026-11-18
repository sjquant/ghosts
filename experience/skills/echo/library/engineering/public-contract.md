---
title: "Expose only the contract consumers need"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-d6fdbcd11ee5cbf95bb7fb03"]
---

# Expose only the contract consumers need

When adding response fields, component props or composable return values, expose the parts consumers currently need. An unused public field is still an interface that consumers can start depending on and that later costs more to remove.

A generalized response-shape example follows. `position` belongs to a different operation, so adding a nullable value does not make it useful here.

### Before

```json
{"name": "Example", "position": null}
```

### After

```json
{"name": "Example"}
```

Keep a field when an existing consumer uses it. For an already published field, check consumers before removal. An exception to versioning a field removal requires establishing both frontend and server non-use and documenting that reason.
