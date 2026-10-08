---
name: ghosts:github-pr
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
- If the repository has a pull request template that GitHub recognizes, preserve its required structure. Otherwise, follow [templates/pull_request_template.md](templates/pull_request_template.md) and replace each placeholder or omit the section as it directs.
- Write for a reviewer who may not know the repository or the work's prior context. Use direct language, preserve precise domain terms, and make essential premises explicit.
- Keep the body readable in one screen without scrolling. Include files or implementation details only when essential for review.
- Always group related points under subheadings or nested lists instead of one flat list.
- When the change alters a flow or relationship between components, summarize it with a compact diagram; when it compares behavior across several cases, use a table. Abstract either to the level needed to understand the overall change.
- Base the body on the final diff against the base branch. Recheck that diff before publishing, then remove intermediate iterations, reverted or removed work, review history, and abandoned approaches.

### Title and scope

- Follow the commit message convention for PR titles.
- Do not include internal planning IDs in the PR title or body, including Waypoint IDs, Task IDs, or roadmap labels such as `W1-A3`.

### Gotchas

- Use the same language as the commits being published for the PR title, body, and headings you add; do not default to English.
- Upload screenshots with the relevant `gh` CLI command and `--attach <file>#<alt text>`. If `--attach` is unavailable, upgrade `gh` first. Put the uploaded images in Markdown tables with at most 4 columns.

