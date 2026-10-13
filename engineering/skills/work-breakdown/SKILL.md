---
name: ghosts:work-breakdown
description: Design-only recursive work breakdown of a destination into independently reviewable work packages with interfaces, dependencies, and execution order.
disable-model-invocation: true
---

Given a destination, recursively decompose it into independently reviewable work packages. Do not implement; the only deliverable is the confirmed work breakdown.

- Keep each leaf within the review budget, normally `<= 1000 LOC`.
- Define the upper-layer interface before decomposing its children.
- Prefer end-to-end slices that can be tested and merged independently.
- Stop when every leaf is reviewable, testable, and mergeable.
- Use `ghosts:grill-me` to resolve material design or decomposition trade-offs with the user. Investigate facts yourself and preserve decisions already agreed.

For each package, capture its scope, rough LOC estimate, dependencies, and status:

- `TODO`: not started
- `DOING`: in progress
- `REVIEW`: pull request open
- `DONE`: pull request merged into the base branch

## Output

After confirmation, write in the user's language using these sections:

### Work packages

Group packages under meaningful outcomes or components and show their hierarchy. Within each group, use a table with stable package IDs, scope, rough LOC estimate, dependencies, and status. Use the same IDs throughout the output.

### Dependency DAG

Draw a Mermaid DAG with a node for every leaf package and subgraphs for the groups. An arrow `A → B` means B requires A; show dependencies across groups explicitly. Group membership is not a dependency. Keep independent nodes unconnected and explain what each non-obvious dependency provides. Resolve cycles before presenting the graph.

### Execution order

List dependency-ordered stages, grouping packages that can proceed in parallel. Reference the same package IDs and identify prerequisites that prevent a stage from starting. Keep this order consistent with the DAG.
