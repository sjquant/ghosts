---
name: task-handoff
description: Generate concise task handoffs for independent implementation workstreams.
disable-model-invocation: true
---

Generate up to five concise English handoff messages for independent implementation tasks. Output each message in a code block; do not create a handoff document.

Use the configured project-notes and task-tracker system. If the source is unclear, ask which one to use before making updates.

Before writing:

1. Read relevant project notes and task entries.
2. Sync the base branch with the latest remote state.
3. Mark implementation tasks with merged PRs `DONE`; keep implemented but unmerged tasks `REVIEW`.
4. Select implementation tasks not marked `[DOING]` and mark selected tasks `[DOING]`.
5. If all tracked tasks are complete, report that instead of creating handoffs.

## Handoff Content

Include only:

- task
- problem
- solution direction
- completed work
- next task and starting point
- done criteria
- required project-notes and repository startup commands, including base-branch sync

Keep the problem and solution direction concise. Do not repeat commands already required by `AGENTS.md` or `CLAUDE.md`.

## Constraints

- Include only tasks that can proceed fully in parallel; do not combine tasks with ordering or dependency relationships.
- Do not mention branch or worktree details.
