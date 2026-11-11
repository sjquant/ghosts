---
id: "candidate-<derived-by-save>"
key: "semantic-api-contracts"
title: "Semantic API contracts"
summary: "Check semantic guarantees when changing a boundary."
type: "principle"
scope: "global"
repository: null
status: "candidate"
confidence: "medium"
captured_at: "2026-11-06T00:00:00Z"
updated_at: "2026-11-06T00:00:00Z"
source_refs: ["<precise source reference>"]
source_ids: ["<collection record ID>"]
---
# Semantic API contracts

## When
Changing a system boundary.
## Principle
Check meaning and guarantees as well as data shape.
## Why
An unchanged shape can hide changed consistency or concurrency guarantees.
## Limits
Specify the observed constraints; do not claim universal applicability.
## Evidence
List at least two independent situations: task/PR, source ID, exact user passage/locator, rejected option and chosen option. Copies and handoffs count once.
## Observation
Describe the user choices directly observed across those situations.
## Inference
State the recurring decision criterion as an interpretation; include contrary choices and unresolved scope.
