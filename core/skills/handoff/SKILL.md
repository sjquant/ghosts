---
name: handoff
description: Generate concise implementation handoff messages from Obsidian workbench notes and task trackers.
disable-model-invocation: true
---

Write separate English handoff messages in individual code blocks only for fully independent workstreams that can be executed 100% in parallel with no ordering dependency. (MAX 5)

Your output should be a handoff message in code block to the user, not a document edit.

Before writing the handoff:
- Use Obsidian in vault "<VAULT_NAME>".
- Look for relevant workbench notes under "<WORKBENCH_PATH>".
- Read the relevant notes if they exist.
- If there is a task-tracking note, identify the latest merged/completed implementation task that should now be marked as DONE (edit is allowed here).
- If this session added useful context or gotchas, update the relevant Obsidian note first.
- If any Obsidian update is needed, do it by local file editing after resolving the vault path.
- If all tracked tasks are already complete, do not create handoff messages; instead state that all tasks are complete and ask whether the user wants suggestions for follow-up work.

Use these commands:
- `obsidian vault=<VAULT_NAME> vault info=path`
- `obsidian vault=<VAULT_NAME> files folder="<WORKBENCH_PATH>"`
- `obsidian vault=<VAULT_NAME> read path="<FILE_PATH>"`
- `obsidian --help`

## Handoff
Keep it short and practical.
Include:
- completed work
- next task
- where to start
- done criteria
- the exact Obsidian commands the next AI should run first
- the exact repo commands the next AI should run first
- say that it must sync the base branch with the latest remote state
- say it must sync the base branch and mark each target task as [DOING] in the task tracker before implementation

## Constraints
- do not mention branch or worktree details
