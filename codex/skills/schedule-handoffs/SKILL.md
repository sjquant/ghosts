---
name: schedule-handoffs
description: Create Codex app automations from handoff tasks. Use when the user wants to schedule repo implementation work as worktree cron automations or thread follow-ups as heartbeat automations.
disable-model-invocation: true
---

Create Codex app automations for these handoff tasks.

## Rules
- Use `automation_update` only.
- Repo tasks must use `kind: "cron"` and `executionEnvironment: "worktree"`.
- Always include for cron: `mode`, `kind`, `name`, `prompt`, `rrule`, `cwds`, `executionEnvironment`, `model`, `reasoningEffort`, `status`.
- Prefer the current thread’s model/reasoning. If unknown, use `model: "gpt-5.4"` and `reasoningEffort: "high"`.
- Default behavior: schedule each repo task to start at the next valid wall-clock time about 1 minute from now in the user’s local timezone, and set `status: "ACTIVE"`.
- Do not use minute-only cron for repo tasks.
- Thread follow-ups under an hour must use `kind: "heartbeat"` and `destination: "thread"`.
- The prompt must include the full handoff text, plus these two extra lines at the end:
  - If code changes are made, create a PR after implementation.
- At the start of execution, remove or pause this same automation using `automation_update`, unless the user explicitly wants recurrence.
- Never delete unrelated automations.

## Cron example
~~~json
{
  "mode": "create",
  "kind": "cron",
  "name": "Example Repo Task",
  "prompt": "Full handoff text here...\n\nIf code changes are made, create a PR after implementation.\nAfter successful completion, remove or pause this same automation using `automation_update`, unless the user explicitly wants recurrence.",
  "rrule": "FREQ=WEEKLY;BYDAY=MO;BYHOUR=9;BYMINUTE=0",
  "cwds": ["/absolute/repo/path"],
  "executionEnvironment": "worktree",
  "model": "gpt-5.4",
  "reasoningEffort": "medium",
  "status": "ACTIVE"
}
~~~

## Heartbeat example
~~~json
{
  "mode": "create",
  "kind": "heartbeat",
  "destination": "thread",
  "name": "Example Follow-up",
  "prompt": "Follow up on the previous task and report the result.",
  "rrule": "FREQ=MINUTELY;INTERVAL=30",
  "status": "ACTIVE"
}
~~~
