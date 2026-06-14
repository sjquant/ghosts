---
name: wdd
description: design-only framework that recursively decomposes a destination into a Waypoint tree to lock in milestones. Use when design and milestone planning is needed before implementation, or when "roadmap", "milestone", "Waypoint", or "WDD" is mentioned
disable-model-invocation: true
---

Given a destination, design and confirm a recursive Waypoint tree. Do not implement. The only deliverable is the confirmed Waypoint tree.

Plan to production standards: account for error handling, edge cases, security, performance, maintainability, external uncertainty, stack difficulty, and domain logic. Do not use toy-project estimates.

## Context Grounding

Before estimating W0, identify the context anchors that justify the destination and each Waypoint.

- Source anchors can be requirement IDs, section headings, issues, PRs, roadmap notes, design docs, code modules, CLI commands, schemas, artifacts, or user-request phrases.
- If no external anchor exists, use `user request`.
- Do not invent anchors. Label inferred links as `inferred from ...`.
- If W0 is ambiguous after context inspection, ask before decomposing.
- Mark unanchored production-critical work as `assumption` with a short reason.

## Core Model

A Waypoint is a decision unit. `W0` is the destination. Every Waypoint is either:

- Intermediate: must be decomposed further; no LOC limit.
- Leaf: confirmed only when estimated size is `<= 1000 LOC`.

There is no decomposition depth limit. Keep decomposing until every leaf is `<= 1000 LOC`.

## Workflow

1. List context anchors:

```text
Context anchors:
  - [anchor]: [contribution or constraint]
```

2. Estimate total W0 size before decomposition:

```text
W0 total estimate: ~{N} LOC
  -> Rationale: [1-2 lines based on similar projects or feature list]
```

3. For each decomposable Waypoint, define the upper-layer interface first so child Waypoints and integration-test boundaries follow the same contract.
4. Add source anchors to every proposed child Waypoint.
5. Propose candidates and let the user select.
6. Decompose the selected candidate into child Waypoints.
7. Repeat until every branch ends in confirmed leaves.
8. Output the final context map, Mermaid tree, parallel execution graph, and execution order list.

## Decomposition Candidate Format

Use 2 candidates for a clear yes/no split, 3 for strategy/technology/priority axes, and 4+ only for genuinely distinct paths.

```markdown
## [W-ID] Decomposition

> [One-line core question about how to split this Waypoint]

**Candidate A - [direction name]**

- Pros: [1 line]
- Risks: [1 line]

Waypoints:
  - [W-ID]-A1: [name] ~[N] LOC - [role, 1 line]
    Source: [requirement/doc/code/user-request anchors]
  - [W-ID]-A2: [name] ~[N] LOC - [role, 1 line]
    Source: [requirement/doc/code/user-request anchors]

**Candidate B - [direction name]**

- Pros: [1 line]
- Risks: [1 line]

Waypoints:
  - [W-ID]-B1: [name] ~[N] LOC - [role, 1 line]
    Source: [requirement/doc/code/user-request anchors]
  - [W-ID]-B2: [name] ~[N] LOC - [role, 1 line]
    Source: [requirement/doc/code/user-request anchors]

Recommendation: A / B - [reason, 1 line]
```

Candidates must differ by implementation direction, not just size splits.

## Final Output

After all Waypoints are confirmed, output all four sections.

### 0. Context Map

Map source anchors to Waypoints.

```markdown
## Context Map

Sources:
- [anchor]: [short description]

Waypoint trace:
- [W-ID]: [source anchors] - [why this Waypoint exists]
```

- Include every leaf Waypoint once.
- Include intermediate Waypoints only for major boundaries.
- Use `user request` when no external source exists.
- Use `assumption` only for production-critical work that is not directly specified.

### 1. Mermaid Tree

```mermaid
graph TD
  W0["[W0] {Destination} ~{N} LOC"]
  W1["[W1] {Name} ~{N} LOC"] --> W0
  W1a["[W1a] {Name} ~{N} LOC"] --> W1
```

- Node: `[<ID>] {name} ~{N} LOC`
- Edges: dependency direction
- No styles or colors

### 2. Parallel Execution Graph

Show dependency relationships and parallelism for all Waypoints, including intermediate nodes.

- `A --> B`: B can start after A is complete.
- `A & B --> C`: C can start after both A and B are complete.
- Nodes with no dependencies in the same column can run in parallel.
- Isolated nodes with no arrows can start at any time.

```mermaid
flowchart TD
  W1["[W1] Auth"] --> W1a["[W1a] Login"]
  W1["[W1] Auth"] --> W1b["[W1b] Token"]
  W1a --> W2["[W2] Dashboard"]
  W1b --> W2
```

### 3. Execution Order List

List tasks in dependency order for human readability. Each item includes one status:

- `TODO`: not yet started
- `DOING`: currently being worked on
- `REVIEW`: in pull request
- `DONE`: complete; skip when passing context to AI

```markdown
## Execution Order

1. [W-ID]: {name} (~{N} LOC) | [TODO]
   [scope, 1 line]
   Source: [source anchors]

Total {N} items | Total estimated LOC: ~{N}
Sum check: leaf total {N} LOC vs W0 estimate {N} LOC -> deviation {N}%
```

## Final Checklist

- W0 total LOC was estimated first.
- Each leaf Waypoint is `<= 1000 LOC`.
- Leaf total is within `+/-20%` of the W0 estimate.
- Each Waypoint's LOC reflects technical difficulty and operating environment.
- Every Waypoint is separable as an independent PR unit.
- Decomposition candidates differ by implementation direction.
- Context anchors were identified before decomposition.
- Every leaf Waypoint maps to at least one source anchor or explicit production assumption.
