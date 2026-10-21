---
name: ghosts:delegate
description: Use when the user asks to hand work to another agent or supervise delegated work through completion. Pass only the context the recipient needs.
---

Default to Orca for new delegations unless the user specifies another tool. When continuing an existing session, use the tool managing that session. A request for Claude Code or Codex as the receiving agent does not by itself change the delegation tool.

For Orca, follow the applicable `orca-cli` or `orchestration` skill. For Paseo, Claude Code, Codex, or another tool, use the session controls available in the current environment. Read the applicable skill or tool instructions; consult official documentation or CLI help when needed to determine how to launch an agent, inspect its result, and send follow-up instructions.

Keep the recipient's agent or session identifier and reuse it to continue the same conversation for each stage.

Before continuing an existing thread, read the user's added instructions.

Prefer Markdown with bullets for the brief. Follow ISO 24495-1:2023 Plain Language principles so the recipient can find, understand, and use the information they need. Use direct sentences, explicit actions, and consistent terms. Omit rhetorical flourishes. Include only what is needed:

- References to issues, PRs, or existing threads.
- Goals, completion criteria, confirmed decisions, constraints, and excluded scope missing from those references.
- Skills the user requested for the current stage.

Do not restate referenced content, reminders to read root instructions, general development or testing guidance, or skill-internal procedures and report formats. Do not omit important decisions or constraints for brevity.

Supervise delegated implementation by default unless the user explicitly requests a handoff without supervision. Send implementation first, then wait for and inspect each stage's result before instructing the same agent to continue. Code review, fixes for applicable findings, and slop-shaking are part of supervised implementation unless the user explicitly excludes them:

1. Inspect the implementation result, then request code review.
2. Inspect the review findings, then request fixes for applicable findings.
3. Inspect the completed review or fixes, then request slop-shaking in a separate message.

Skip fixes when there are no applicable findings. Continue supervising until all included stages finish or a blocker requires user input. Base each instruction on the preceding result. Do not combine code review or review fixes with slop-shaking, or bundle later stages into the initial prompt, unless the user explicitly requests it.

For a full handoff without supervision, deliver the current stage and leave later instructions to the user.
