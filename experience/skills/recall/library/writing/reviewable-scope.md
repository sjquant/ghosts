---
title: "Group changes into reviewable decisions"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-140020b103ec3346e4f91762"]
---

# Group changes into reviewable decisions

When setting PR boundaries, group work by what a reviewer can assess together. Split an oversized change, while avoiding mechanical one-task-per-resource fragmentation that does not reduce the code reviewers must understand.

### Before

```text
One PR contains the whole observability migration.
```

### After

```text
Split the migration into related, assessable changes with explicit dependencies.
```

The opposite choice can also be appropriate:

### Before

```text
Each permission conversion gets its own PR even though the changes are small
and repeat the same surrounding code.
```

### After

```text
Group related conversions by the amount of code to review.
```

If a correction shares almost all of the current change and must prevent its release, keeping it in the same PR can reduce repeated review and avoid releasing the incomplete version. The evidence does not establish a universal line count or number of PRs.
