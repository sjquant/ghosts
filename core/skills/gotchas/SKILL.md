---
name: gotchas
description: Find reusable mistake-prevention rules from the full conversation.
disable-model-invocation: true
---

Find generally reusable mistake-prevention rules from the full conversation.

Do not write reflections, summarize the task, or store anything.

Default output: `NO_RULE`.

Use the full conversation, not just the final request or latest fix. Prefer the
earliest reusable cause to the latest symptom; use the last turn only when it
contains the lesson.

Create a rule only for a generally recurring lesson that would prevent future rework, rediscovery, or verification gaps, such as:
- correction that reveals a reusable workflow issue,
- repeated work or stuck state,
- non-obvious tool/API/file-format behavior,
- risky assumption,
- hidden constraint.

Skip one-off facts, temporary context, vague advice, obvious task requirements, duplicate rules, context-specific preferences, and lessons without a clear future trigger.

Output at most 3 rules. Each rule must be short, concrete, and reusable.

Format:
```markdown
RULE: When [specific trigger], do [specific action], avoid [specific failure].
SCOPE: [core|tool]
REASON: [one short sentence]
```

Scopes:
- `core`: general agent behavior.
- `tool`: tool, API, command, or file-format behavior.

Prefer `NO_RULE` when unsure.

Examples:
```markdown
RULE: When editing an existing file, inspect its current structure and formatting before making changes, avoid unintended destructive edits.
SCOPE: tool
REASON: File editing requires a reusable workflow.

RULE: When changing code, run the relevant validation before marking the task complete, avoid returning unverified edits.
SCOPE: core
REASON: Validation prevents repeated quality gaps.

RULE: When a task requires exact terminology, reuse the requested terms consistently, avoid introducing ambiguous synonyms.
SCOPE: core
REASON: Precise wording is generally reusable.

RULE: When a command may delete or overwrite important files, require explicit approval before execution, avoid irreversible destructive changes.
SCOPE: tool
REASON: Needs enforcement rather than guidance.
```
