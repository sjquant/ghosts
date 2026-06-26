---
name: gotchas
description: Decide whether the full conversation produced reusable mistake-prevention rules.
disable-model-invocation: true
---

Decide whether the full conversation produced generally reusable mistake-prevention rules.

Do not write reflections, summarize the task, or store anything.

Default output: `NO_RULE`.

Review the whole conversation, not only the final request or most recent fix.
Prefer the earliest reusable cause over the latest symptom. Do not overweight
the last turn unless it contains the actual recurring lesson.

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
