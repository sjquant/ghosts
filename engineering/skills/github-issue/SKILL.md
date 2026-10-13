---
name: ghosts:github-issue
description: Use when the user asks to create or update GitHub issues, including sub-issues and dependencies when needed.
---

Use the `gh` CLI. Resolve each issue's target repository from the request and task scope, using the current checkout when appropriate. Write from the user's request and relevant context. Keep unresolved choices as proposals or open questions rather than inventing agreement.

Search the target repositories for existing issues before creating duplicates. Before updating, read the issue and its relationships; preserve unrelated content. Follow each target repository's relevant issue template or issue form when present, preserving required fields. Otherwise use the body below. Write in the user's language for someone who has not seen the conversation, using a concrete, problem-focused title and brief, grouped Markdown.

```markdown
## Problem

<Who encounters the problem, when it happens, and why it matters>

## Desired outcome

<What should become possible or improve; keep separate from the proposed solution>

## Proposed direction

- <A possible approach and why it could solve the problem>
- <Material tradeoff or open question; omit when unnecessary>
```

Omit Proposed direction when the problem needs investigation before a useful approach can be proposed. Add completion criteria, supporting evidence, or dependencies when they clarify the issue.

Use sub-issues when the request calls for a hierarchy, and dependency links for actual prerequisites. Use `--parent` for hierarchy and `--blocked-by` on creation or `--add-blocked-by` on edit for prerequisites. Parent membership is not a dependency; keep independent issues independent.

When publishing an agreed work breakdown, map meaningful groups to parent issues and leaf tasks to sub-issues, preserving scope, agreed direction, and completion criteria. Map each DAG edge `A → B` to B blocked by A. Track task IDs against issue URLs and summarize linked tasks in their parent issue.

For work spanning repositories, create each task issue in its target repository with `--repo OWNER/REPO` and connect parents and prerequisites using full issue URLs. Sub-issues may be in another repository under the same owner; preserve the agreed hierarchy across repositories.

Pass multiline bodies through `--body-file`. When publishing several related issues, create prerequisites before dependent issues and connect relationships using real issue numbers or URLs. Verify saved bodies and relationships before reporting success. If a write partially succeeds, inspect what exists and continue from it rather than creating duplicates.

Return created or updated issue links, grouped when useful, and any unresolved publication problem.
