---
name: ghosts:task-handoff
description: Use when the user asks to prepare handoff text for independent implementation tasks without dispatching agents.
disable-model-invocation: true
---

Generate up to two concise English handoffs for independent implementation tasks by default. If the invocation specifies a positive maximum N, generate up to N handoffs; treat N as a cap. Output each handoff in a code block; do not create a handoff document, dispatch agents, update task status, or change Git state.

Read relevant entries in the configured project-notes and task-tracker system. If the source is unclear, ask which one to use.

Select tasks that can proceed fully in parallel with their prerequisites satisfied. Exclude tasks already in progress, awaiting review, or complete. Treat tasks with merged PRs as complete and implemented but unmerged tasks as awaiting review. Choose the eligible set of up to N tasks that minimizes overlap in files or modules they are likely to modify. If all tracked tasks are complete, report that; if none are ready, report the blockers instead of creating handoffs.

Prefer Markdown with bullets inside each code block. Use ASD-STE100 style: short, direct sentences, explicit actions, and consistent terms. Omit rhetorical flourishes. Include only what the recipient needs:

- References to issues, PRs, or existing threads.
- Goals, completion criteria, confirmed decisions, constraints, and excluded scope missing from those references.
- Skills the user requested.

Do not restate referenced content, reminders to read root instructions, general development or testing guidance, or skill-internal procedures and report formats. Do not omit important decisions or constraints for brevity. Do not include branch or worktree details.
