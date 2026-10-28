---
name: ghosts:explain-change
description: Explain a PR, diff, branch, or code change read-only through public-interface behavior, before/after usage examples, and compatibility impact, in the style of release notes.
disable-model-invocation: true
---

Explain the change like release notes for someone who uses the affected interfaces. Read only: do not modify files, execute target code, or publish release notes, PR edits, or comments. Return the explanation in Markdown in the user's language.

## Scope

Use the supplied PR, diff, branch, or code target; otherwise use the current branch's diff against its base, including uncommitted changes. Ask only if the target or base cannot be established. Inspect the complete final diff and enough before/after definitions, callers, tests, and documentation to establish the observable contract. Treat PR descriptions and commit messages as context, not proof of behavior.

## Explanation

- Lead with what changes for callers or users through the public interface: API, CLI, UI, configuration, file format, or protocol. Group by capability or contract rather than changed files or commit history. Include relevant defaults, errors, side effects, and compatibility changes.
- Use concise before/after code snippets or concrete usage examples showing inputs or actions and observable outcomes. Use real interface names and supported syntax from the relevant revision; label illustrative data, pseudocode, and unexecuted examples. Do not invent prior capabilities or imply examples were run.
- Explain who is affected, why the change matters, and any required caller changes. Include implementation details only to explain an observable guarantee, limitation, or tradeoff. For internal-only changes, state their purpose and whether observable behavior changes; do not invent user benefits or deployment status.
- Use a table or compact diagram only when clearer than prose or a usage example. Keep it understandable through public interfaces without knowledge of internal collaboration.
- Link substantive claims and snippets to code or test evidence with file/line references; use commit-pinned permalinks for GitHub targets. Separate established behavior from inference and unknowns; state material limits of the supplied diff or available evidence.

Cover every material contract change, including removals and breaking changes. Keep the explanation proportional to the change; omit empty sections and file inventories. This is an explanation, not a code review or a release announcement.
