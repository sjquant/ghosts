---
name: github-pr
description: Publish changes to GitHub by committing and pushing each logical change, and create or update its pull request when the user asks to publish, sync, or manage GitHub work.
---

## Git workflow

1. If the project's commit message style is unknown, execute `git log --oneline -n 2` to identify the existing pattern and language.
2. After this skill is triggered, always commit and push each change. If there's no PR yet, create it first.
- Use the `gh` CLI for GitHub-related work.

## Pull request

- Before updating a pull request, check its current title and body.

### Body

- Use `gh pr edit --body-file - <<'EOF'` as the default PR body path.
- Use `.github/pull_request_template.md` when present. Otherwise, structure the PR body with `## Why` and `## Changes` with bullet points.
  - Under `## Why`, explain the problem and its impact in 1–2 sentences.
  - Under `## Changes`, summarize the chosen solution direction and key behavioral changes.
- Keep the PR body concise and easy to understand. Do not enumerate every changed file, code modification, or implementation detail unless it is essential for review.
- Describe only the final state of the change and its user-visible impact. Never mention intermediate iterations, removed scope, review history, or abandoned approaches.

### Title and scope

- PR titles must follow the commit message convention.
- Never include internal planning IDs in the PR title or body, including Waypoint IDs, Task IDs, or roadmap labels such as `W1-A3`.

### Screenshots

- Upload PR screenshots by drag-and-drop into UI input `#fc-new_comment_field`, then format the uploaded URLs under `## 스크린샷` in Markdown tables with at most 4 columns per table.
