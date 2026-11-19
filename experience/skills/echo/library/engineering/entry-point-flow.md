---
title: "Show the workflow at its entry point"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-bf4ca5945899f7ac3aa3d567"]
---

# Show the workflow at its entry point

When a script's main function hides its sequence inside one operation, expose the stages that let readers understand the work without opening implementations.

Deidentified orchestration fragments. The host script supplies `fetch_raw_data` and `update_records`; persistence receives the fetched data rather than fetching it again internally.

### Before

```python
async def main(date, field):
    await update_records(date, field)  # Also fetches the data internally.
```

### After

```python
async def main(date, field):
    data = await fetch_raw_data(date)
    await update_records(data, date, field)
```

A domain facade can use a name such as `apply` when that best expresses its purpose, rather than listing every internal stage. A one-off script does not always need a main-function split just for potential future reuse.
