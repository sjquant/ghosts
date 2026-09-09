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
- If `.github/pull_request_template.md` exists, preserve its required structure. Otherwise, structure the body with problem/impact and changes/solution sections as bullet lists.
  - Explain the problem and its impact in 1–2 sentences.
  - Summarize the chosen solution direction and key behavioral changes.
- Keep the PR body concise and easy to understand. Include changed files, code modifications, or implementation details only when essential for review.
- Describe only the final state and its user-visible impact. Do not mention intermediate iterations, removed scope, review history, or abandoned approaches.

### Title and scope

- Follow the commit message convention, including language, for the PR title and body. Do not default to English.
- Do not include internal planning IDs in the PR title or body, including Waypoint IDs, Task IDs, or roadmap labels such as `W1-A3`.

### Screenshots

- Upload PR screenshots with `gh pr comment --body-file - --attach <file>#<alt text>`. If `--attach` is unavailable, upgrade `gh` first. Put the uploaded images in Markdown tables with at most 4 columns.
