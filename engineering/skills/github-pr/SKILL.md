---
name: github-pr
description: When the user asks to publish, sync, or manage GitHub work, commit and push each change and create or update its pull request.
---

## Git workflow

- If the project's commit message style is unknown, run `git log --oneline -n 2` to identify the existing pattern and language.
- After this skill is triggered, commit and push every change. If there is no PR yet, create it first.
- Use the `gh` CLI for GitHub-related work.

## Pull request

### Before updating

- Before updating a pull request, check its current title and body.

### Body

- Use `gh pr edit --body-file - <<'EOF'` as the default PR body path.
- If `.github/pull_request_template.md` exists, use it. Otherwise, structure the body with `## Why` and `## Changes` as bullet lists.
  - Under `## Why`, explain the problem and its impact in 1–2 sentences.
  - Under `## Changes`, summarize the chosen solution direction and key behavioral changes.
- Keep the PR body concise and easy to understand. Include changed files, code modifications, or implementation details only when essential for review.
- Describe only the final state and its user-visible impact. Do not mention intermediate iterations, removed scope, review history, or abandoned approaches.

### Title and scope

- Follow the commit message convention for PR titles.
- Do not include internal planning IDs in the PR title or body, including Waypoint IDs, Task IDs, or roadmap labels such as `W1-A3`.

### Screenshots

- Upload PR screenshots by dragging and dropping them into UI input `#fc-new_comment_field`. Format the uploaded URLs under `## 스크린샷` in Markdown tables with at most 4 columns per table.
