---
name: ghosts:delegate
description: Use when the user asks to hand work to another Orca agent or supervise delegated work through completion. Pass only the context the recipient needs.
---

Delegate the user's task through Orca. Read and follow the applicable `orca-cli` or `orchestration` skill.

Before continuing an existing thread, read the user's added instructions.

Prefer Markdown with bullets for the brief. Use an ASD-STE100-inspired style: short, direct sentences, explicit actions, and consistent terms. Omit rhetorical flourishes. Include only what is needed:

- References to issues, PRs, or existing threads.
- Goals, completion criteria, confirmed decisions, constraints, and excluded scope missing from those references.
- Skills the user requested.

Do not restate referenced content, reminders to read root instructions, general development or testing guidance, or skill-internal procedures and report formats. Do not omit important decisions or constraints for brevity.
