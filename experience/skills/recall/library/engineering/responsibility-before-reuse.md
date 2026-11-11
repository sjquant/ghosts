---
title: "Base reuse on shared responsibility"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-a12f9118de168e849eeb9f63"]
---

# Base reuse on shared responsibility

First consider extending an existing boundary that owns the same responsibility. Similar-looking concepts should remain separate when their meaning or reasons for change differ.

## Example

A deidentified interface-extension fragment: the host project supplies the existing data-volume factory and access-mode enum. Extend that factory instead of requiring callers to coordinate a second writer-specific wrapper.

### Before

```python
pod_config = get_data_writer_pod_configs(
    get_data_volume_configs(),
)
```

### After

```python
pod_config = get_data_volume_configs(
    data_access=DataAccess.WRITE,
)
```

## When to keep concepts separate

Team and personal-space permission policies have different hierarchies. Combining their rules introduces ambiguity and couples changes, so keep these policies separate.

A wrapper can be useful when its name makes the intent easier to understand. Repeating an already clear operation at the same abstraction level adds another place to read.
