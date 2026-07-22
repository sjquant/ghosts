---
name: memory
description: Capture and refine durable knowledge from conversational friction in Obsidian.
disable-model-invocation: false
---

Use the Obsidian CLI. Default to no-op; write memory only when the conversation contains a high-signal `FRICTION` event:

- a correction, retry, backtrack, or failed assumption;
- surprising tool, API, repository, or workflow behavior;
- a non-obvious decision, constraint, or reusable solution.

Skip temporary context, one-off facts, obvious advice, duplicates, secrets, and uncertain guesses.

Store candidates in `memory/agent/INBOX.md` and refined knowledge in `memory/agent/MEMORY.md`. Read both before writing. Keep each entry atomic and searchable:

```markdown
## <short, searchable title>

- Trigger: <when this matters>
- Lesson: <reusable knowledge>
- Action: <what to do next time>
- Scope: <where it applies>
- Verified: <YYYY-MM-DD>
```

When an inbox candidate is durable, merge it into the relevant memory entry, deduplicate related entries, and remove the processed candidate. Keep `MEMORY.md` as a small index of durable knowledge, not a conversation log.

If the Obsidian CLI is unavailable, start Obsidian and retry. If the lesson is not clearly reusable, do nothing and do not report it.
