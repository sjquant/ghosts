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
2. Before judging merged status or writing handoffs, fetch all remote updates and sync the base branch to the latest remote state.
3. If there is a task tracker, identify the latest implementation task whose PR is merged into the base branch and mark it `DONE`; this edit is allowed. Keep implemented but unmerged PRs as `REVIEW`.
4. When selecting target tasks for handoff, exclude tasks already marked `[DOING]`.
5. If this session added useful context or gotchas, update the relevant Obsidian note first.
6. Make required Obsidian updates by local file editing after resolving the vault path.
7. If all tracked tasks are complete, do not create handoff messages; state that all tasks are complete and ask whether the user wants follow-up suggestions.

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
- Do not repeat commands from `AGENTS.md` or `CLAUDE.md` in handoff messages.
