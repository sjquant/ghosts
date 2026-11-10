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

A call-site excerpt using a volume configuration function and an access-mode enum.

### Before

```python
pod_config = get_factor_writer_pod_configs(
    get_pod_volume_configs(),
)
```

### After

```python
pod_config = get_pod_volume_configs(
    nfs_data_access=NfsDataAccess.WRITE,
)
```

## When to keep concepts separate

Organization and personal-channel permission policies have different hierarchies. Combining their rules introduces ambiguity and couples changes, so keep these policies separate.
