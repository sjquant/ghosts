---
name: ghosts:delegate
description: Use when the user asks to hand work to another agent or supervise delegated work through completion. Pass only the context the recipient needs.
---

Default to Orca for new delegations unless the user specifies another tool. When continuing an existing session, use the tool managing that session. A request for Claude Code or Codex as the receiving agent does not by itself change the delegation tool.

For Orca, follow the applicable `orca-cli` or `orchestration` skill. For Paseo, Claude Code, Codex, or another tool, use the session controls available in the current environment. Read the applicable skill or tool instructions; consult official documentation or CLI help when needed to determine how to launch an agent, inspect its result, and send follow-up instructions.

Keep the recipient's agent or session identifier and reuse it for follow-ups.

Before continuing an existing thread, read the user's added instructions.

Prefer Markdown with bullets for the brief. Follow ISO 24495-1:2023 Plain Language principles so the recipient can find, understand, and use the information they need. Use direct sentences, explicit actions, and consistent terms. Omit rhetorical flourishes. Include only what is needed:

- References to issues, PRs, or existing threads.
- Goals, completion criteria, confirmed decisions, constraints, and excluded scope missing from those references.
- Skills the user requested and when to apply them.

Do not restate referenced content, reminders to read root instructions, general development or testing guidance, or skill-internal procedures and report formats. Do not omit important decisions or constraints for brevity.

For delegated implementation, send the task and the complete workflow in one prompt. Unless the user excludes a stage, include these instructions for the recipient:

```text
1. Implement the task.
2. After implementation, invoke ghosts:code-review. When the read-only review is complete, fix applicable findings. Skip fixes if there are none.
3. After review and any fixes, invoke ghosts:slop-shaking and apply useful cleanups.

Apply each skill at its stage. Complete the workflow and report results, or explain what blocks completion.
```

Supervise through completion by default: wait for and inspect the recipient's final result, then follow up on incomplete work or blockers. The recipient owns transitions between stages; do not send separate stage-triggering messages unless the user requests stage-by-stage supervision.

For a full handoff without supervision, send the complete requested workflow and leave execution with the recipient.
