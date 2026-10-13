---
name: ghosts:github-issue
description: Use when the user asks to create or update GitHub issues, or publish an agreed work breakdown as issues with sub-issues and dependencies.
---

Use the `gh` CLI. Resolve the repository from the request or current checkout. Use the user's explicit issue request or confirmed work breakdown; resolve material open decisions before publishing. Do not require a work breakdown for a simple issue.

Search existing issues before creating duplicates. Before updating, read the issue and its relationships; preserve unrelated content. Follow repository issue templates when present, otherwise use the body below. Write in the user's language for someone who has not seen the conversation, using a concrete title and brief, grouped Markdown.

```markdown
## Problem

<What needs to change and why>

## Direction

- <Agreed approach and scope>
- <Important design choice and reason; omit when unnecessary>

## Done when

- [ ] <Observable completion criterion>

## Dependencies

- <Prerequisite issue and what it provides; omit when none>
```

For multiple work packages, create a parent issue for the overall outcome and a sub-issue for each reviewable task, preserving the agreed grouping. Keep a simple task as one issue. Use `--parent` for hierarchy and `--blocked-by` on creation or `--add-blocked-by` on edit for actual prerequisites. Parent membership is not a dependency; keep independent tasks independent. Map work-package IDs to issue URLs and update the parent with the issue-linked DAG when useful.

Pass multiline bodies through `--body-file`. Create prerequisites before dependent issues and connect relationships using real issue numbers or URLs, not planning IDs. Verify saved bodies and relationships before reporting success. If a write partially succeeds, inspect what exists and continue from it rather than creating duplicates.

Return created or updated issue links, grouped when useful, and any unresolved publication problem. Issue creation does not authorize implementation or PR submission.
