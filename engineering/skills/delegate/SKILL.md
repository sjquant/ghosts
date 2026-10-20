---
name: ghosts:delegate
description: Use when the user asks to hand work to another agent or supervise delegated work through completion. Pass only the context the recipient needs.
---

Default to Orca for new delegations unless the user specifies another tool. When continuing an existing session, use the tool managing that session. A request for Claude Code or Codex as the receiving agent does not by itself change the delegation tool; use their standalone CLIs when the user requests direct CLI delegation.

Read the selected tool's applicable skill when available; otherwise inspect its official documentation or CLI help before launching agents or sending instructions. Check installed CLI help for version-specific options.

| Tool | Follow-up mechanism |
| --- | --- |
| Orca (default) | Follow `orca-cli` or `orchestration` for launch, result inspection, and follow-up delivery. |
| [Paseo](https://paseo.sh/docs/cli) | Launch with `paseo run`; inspect results with `paseo logs <agent-id>`; send the next stage with `paseo send <agent-id> "<instruction>"`. |
| [Claude Code CLI](https://code.claude.com/docs/en/cli-reference) | Start with `claude -p "<instruction>" --output-format json`; continue with `claude -p --resume <session-id> "<instruction>" --output-format json`. |
| Codex CLI | Start with `codex exec --json "<instruction>"`; continue with `codex exec resume <session-id> "<instruction>" --json`. |

Keep the recipient's exact agent or session ID from the tool output and reuse it for each stage. For standalone CLIs, run in the intended working directory and inspect each completed command's output before resuming. Avoid “latest session” shortcuts when coordinating multiple agents. For other delegation tools, discover the equivalent launch, result inspection, and follow-up controls.

Before continuing an existing thread, read the user's added instructions.

Prefer Markdown with bullets for the brief. Follow ISO 24495-1:2023 Plain Language principles so the recipient can find, understand, and use the information they need. Use direct sentences, explicit actions, and consistent terms. Omit rhetorical flourishes. Include only what is needed:

- References to issues, PRs, or existing threads.
- Goals, completion criteria, confirmed decisions, constraints, and excluded scope missing from those references.
- Skills the user requested for the current stage.

Do not restate referenced content, reminders to read root instructions, general development or testing guidance, or skill-internal procedures and report formats. Do not omit important decisions or constraints for brevity.

When supervising work, send implementation first. For requested follow-up stages, instruct the same agent one stage at a time:

1. Inspect the implementation result, then request code review.
2. Inspect the review findings, then request fixes for applicable findings.
3. Inspect the completed fixes, then request slop-shaking in a separate message.

Skip stages the user did not request and fix instructions when there are no applicable findings. Base each instruction on the preceding result. Do not combine code review or review fixes with slop-shaking, or bundle later stages into the initial prompt, unless the user explicitly requests it.

For a full handoff without supervision, deliver the current stage and leave later instructions to the user.
