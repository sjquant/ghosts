---
name: ghosts:docstring-review
description: Read-only review of function and method docstring or TSDoc summaries for domain purpose rather than implementation narration.
disable-model-invocation: true
---

Review function and method documentation summaries read-only. Use the user's target or the change being discussed; otherwise review the current branch's diff against its base, including uncommitted changes. Inspect the implementation and relevant callers to establish the function's purpose.

- Any function or method docstring or TSDoc summaries that narrate internal steps or enumerate permissions, side effects, and error handling instead of stating the function's purpose in domain terms?
- Recommend a concise purpose statement, usually one sentence. Use domain terms supported by the code; do not invent intent or guarantees.
- Preserve contract details callers need in separate documentation sections or paragraphs. Permissions, side effects, or failures may belong in the summary when they define the function's domain purpose; do not flag them merely for appearing there.

Report only summaries that obscure the function's purpose. Do not request missing docstrings, expand the review to unrelated documentation, or flag harmless wording preferences.

Write findings in the user's language. For each finding, include the file and line, the existing summary, why it obscures the purpose, and a proposed replacement summary. Use commit-pinned permalinks for GitHub targets. State when no actionable findings were found and disclose any material review limitations.
