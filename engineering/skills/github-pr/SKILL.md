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
- Use closing keywords for linked issues the PR fully resolves.
- Write for a reviewer who may not know the repository or the work's prior context. Use direct language, preserve precise domain terms, and make essential premises explicit.
- Write the summary like release notes: explain what changes for callers or users through the public interface; state breaking changes and required actions. For internal-only changes, state their purpose without inventing user-visible benefits.
- Show a minimal before/after usage example for each materially changed public interface, including concrete inputs or actions and observable results. For additions or removals, show the supported usage and explain what became available or is no longer supported.
- Put code and text-based requests and responses in fenced code blocks, not inline fragments. For UI changes, show the interaction and resulting state.
- Keep the body concise, preferably within one screen without scrolling, without omitting required usage examples. Include files or implementation details only when essential for review.
- Always group related points under subheadings or nested lists instead of one flat list.
- Use a compact diagram for public-interface interactions or observable state transitions, or a table for behavior across cases, only when clearer than prose or a usage example; make it self-contained with concrete inputs/actions and observable outcomes, including internals only to explain relevant guarantees or tradeoffs.
- Base the body on the final diff against the base branch. Recheck that diff before publishing, then remove intermediate iterations, reverted or removed work, review history, and abandoned approaches.

### Title and scope

- Follow the commit message convention for PR titles.
- Do not include internal planning IDs in the PR title or body, including Waypoint IDs, Task IDs, or roadmap labels such as `W1-A3`.

### Gotchas

- Use the same language as the commits being published for the PR title, body, and headings you add; do not default to English.
- Upload screenshots with the relevant `gh` CLI command and `--attach <file>#<alt text>`. If `--attach` is unavailable, upgrade `gh` first. Put the uploaded images in Markdown tables with at most 4 columns.

