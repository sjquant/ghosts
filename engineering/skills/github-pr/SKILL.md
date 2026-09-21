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
- If `.github/pull_request_template.md` exists, preserve its required structure. Otherwise, structure the body with problem and changes sections as bullet lists.
  - Explain the problem and its impact in 1–2 sentences.
  - Summarize the chosen solution direction and key behavioral changes.
- Write for a reviewer who may not know the repository or the work's prior context. Use direct language, preserve precise domain terms, and make essential premises explicit.
- Treat length as a cost. Group related points with headings or lists, and include files or implementation details only when essential for review. For complex flows or relationships, use a compact diagram or table abstracted to the level needed to understand the overall change.
- Base the body on the final diff against the base branch. Recheck that diff before publishing, then remove intermediate iterations, reverted or removed work, review history, and abandoned approaches.

### Title and scope

- Follow the commit message convention for PR titles.
- Do not include internal planning IDs in the PR title or body, including Waypoint IDs, Task IDs, or roadmap labels such as `W1-A3`.

### Gotchas

- Use the same language as the commits being published for the PR title, body, and headings you add; do not default to English.
- Upload screenshots with the relevant `gh` CLI command and `--attach <file>#<alt text>`. If `--attach` is unavailable, upgrade `gh` first. Put the uploaded images in Markdown tables with at most 4 columns.

