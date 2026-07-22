---
name: task-handoff
description: Generate concise task handoffs for independent implementation workstreams. Use when the user asks for a "task handoff" or "parallel task handoffs".
disable-model-invocation: true
---

Generate up to five concise English handoff messages for workstreams that can proceed fully in parallel. Output each message in a code block; do not create a handoff document.

## Before Writing

Use the configured project-notes and task-tracker system, such as Obsidian or Notion. If the source is unclear from context, ask which one to use before making updates.

1. Read relevant project notes and task-tracker entries.
2. Sync the repository base branch with the latest remote state before judging merge status.
3. Mark the latest merged implementation tasks `DONE`.
4. Select tasks not already marked `[DOING]` and mark selected tasks `[DOING]` before implementation.
5. If all tracked tasks are complete, do not create handoffs; report that and ask whether follow-up suggestions are wanted.

## Handoff Content

Include only:

- completed work
- next task and where to start
- done criteria
- the project-notes and repository commands the next AI must run first

Tell the next AI to sync the base branch before implementation. Do not repeat commands already required by `AGENTS.md` or `CLAUDE.md`.

## Constraints

- Do not include tasks with ordering or dependency relationships in the same parallel set.
- Do not mention branch or worktree details.
- Update project notes or task status when required, but do not create a separate handoff document.
