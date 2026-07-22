---
name: work-breakdown
description: Design-only recursive work breakdown of a destination into independently reviewable work packages with interfaces, dependencies, and execution order.
disable-model-invocation: true
---

Given a destination, recursively decompose it into independently reviewable work packages. Do not implement; the only deliverable is the confirmed work breakdown.

- Keep each leaf within the review budget, normally `<= 1000 LOC`.
- Define the upper-layer interface before decomposing its children.
- Prefer end-to-end slices that can be tested and merged independently.
- Stop when every leaf is reviewable, testable, and mergeable.
- Use Socratic questioning only for material design or decomposition trade-offs.

For each package, capture its scope, rough LOC estimate, dependencies, and status:

- `TODO`: not started
- `DOING`: in progress
- `REVIEW`: pull request open
- `DONE`: pull request merged into the base branch

After confirmation, output:

1. The hierarchical work-breakdown tree.
2. The dependency and parallel-execution graph.
3. The dependency-ordered execution list.
