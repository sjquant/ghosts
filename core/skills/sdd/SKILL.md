---
name: sdd
description: Create SPEC documents, and TASKS only when asked, from a feature or project request. Use when the user mentions SDD, SPEC, or TASKS.
disable-model-invocation: true
---

Create a SPEC document from the user's request. If requirements are unclear, ask before continuing.

Generate `TASKS.md` only when asked, and derive it from the SPEC requirements. Load [references/tasks-template.md](references/tasks-template.md) only when generating `TASKS.md`.

## SPEC Template

```md
## Overview

## Goal
- 

## Context
- 

## Why
- 

## Requirements
- R1
- R2

## In Scope
- 

## Out of Scope
- 

## Constraints
- 
```
