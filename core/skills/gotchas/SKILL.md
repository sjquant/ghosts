---
name: gotchas
description: Decide whether a completed task produced reusable mistake-prevention rules.
disable-model-invocation: true
---

Decide whether a completed task produced reusable mistake-prevention rules.

Do not write reflections, summarize the task, or store anything.

Default output: `NO_RULE`.

Create a rule only for a recurring lesson that would prevent future rework, rediscovery, or verification gaps, such as:
- user correction,
- repeated work or stuck state,
- non-obvious tool/API/file-format behavior,
- risky assumption,
- hidden constraint.

Skip one-off facts, temporary context, vague advice, obvious task requirements, duplicate rules, and lessons without a clear future trigger.

Output at most 3 rules. Each rule must be short, concrete, and reusable.

Format:
```markdown
RULE: When [specific trigger], do [specific action], avoid [specific failure].
SCOPE: [core|domain|tool|user]
REASON: [one short sentence]
```

Scopes:
- `core`: general agent behavior.
- `domain`: repo, project, or domain behavior.
- `tool`: tool, API, command, or file-format behavior.
- `user`: stable user preference or correction.

Prefer `NO_RULE` when unsure.

Examples:
```markdown
RULE: When editing an existing file, inspect its current structure and formatting before making changes, avoid unintended destructive edits.
SCOPE: tool
REASON: File editing requires a reusable workflow.

RULE: When modifying this repo, run the required test command before marking code changes complete, avoid returning unverified edits.
SCOPE: domain
REASON: Repo-wide agent behavior.

RULE: When the user corrects terminology, use the corrected term consistently in the remaining task, avoid reverting to the old wording.
SCOPE: user
REASON: User-specific repeated preference.

RULE: When a command may delete or overwrite important files, require explicit approval before execution, avoid irreversible destructive changes.
SCOPE: tool
REASON: Needs enforcement rather than guidance.
```
