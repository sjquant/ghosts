---
name: handoff
description: Generate concise implementation handoff messages from Obsidian workbench notes and task trackers.
disable-model-invocation: true
---

Write separate English handoff messages in code blocks only for fully independent workstreams that can run 100% in parallel with no ordering dependency. Maximum: 5.

Output handoff messages to the user; do not edit a document for the handoff itself.

## Before Writing

Use Obsidian in vault `<VAULT_NAME>`:

- Resolve the vault path: `obsidian vault=<VAULT_NAME> vault info=path`
- List workbench notes: `obsidian vault=<VAULT_NAME> files folder="<WORKBENCH_PATH>"`
- Read relevant notes: `obsidian vault=<VAULT_NAME> read path="<FILE_PATH>"`
- Use `obsidian --help` as needed.

Then:

1. Read relevant workbench notes under `<WORKBENCH_PATH>` if they exist.
2. If there is a task tracker, identify the latest merged/completed implementation task that should be marked `DONE`; this edit is allowed.
3. If this session added useful context or gotchas, update the relevant Obsidian note first.
4. Make required Obsidian updates by local file editing after resolving the vault path.
5. If all tracked tasks are complete, do not create handoff messages; state that all tasks are complete and ask whether the user wants follow-up suggestions.

## Handoff Content

Keep each handoff short and practical. Include:

- completed work
- next task
- where to start
- done criteria
- exact Obsidian commands the next AI should run first
- exact repo commands the next AI should run first
- instruction to sync the base branch with the latest remote state
- instruction to sync the base branch and mark each target task as `[DOING]` in the task tracker before implementation

## Constraints

- Do not mention branch or worktree details.
