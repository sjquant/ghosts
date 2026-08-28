---
name: github-pr
description: Commit, push, and manage GitHub pull requests for changes after explicit invocation.
disable-model-invocation: true
---

Use this skill only after the user explicitly invokes it. This skill is the opt-in boundary for GitHub side effects: before invocation, do not commit, push, create a pull request, or edit a pull request as part of ordinary work. After invocation, apply the workflow below to every subsequent change in the current task until the user says to stop.

Do not retroactively publish work completed before invocation unless the user explicitly asks for it.

## Change publishing

- Inspect the working tree, current branch, remotes, and any existing pull request before mutating repository or GitHub state.
- If the project's commit message style is unknown, run `git log --oneline -n 2` to identify the existing pattern and language.
- Treat each completed logical change as its own publish unit. For every unit, run the relevant checks, stage only its intended files, commit using the project's convention, and immediately push the commit to the current branch with `git push`.
- Do not accumulate later changes just to reduce the number of pushes. If a push fails, stop and report the failure; do not force-push or rewrite history unless the user explicitly authorizes it.
- If no pull request exists, push the first committed change and then create the pull request with `gh pr create`. Continue pushing each later logical change as soon as it is complete.
- Use the `gh` CLI for GitHub-related work.

## Pull request updates

- Before updating a pull request, check its current title and body.
- Use `gh pr edit --body-file - <<'EOF'` as the default PR body path.
- Use `.github/pull_request_template.md` when present. Otherwise, structure the PR body with `## Why` and `## Changes` with bullet points.
  - Under `## Why`, explain the problem and its impact in 1–2 sentences.
  - Under `## Changes`, summarize the chosen solution direction and key behavioral changes.
- Keep the PR body concise and easy to understand. Do not enumerate every changed file, code modification, or implementation detail unless it is essential for review.
- Describe only the final state of the change and its user-visible impact. Never mention intermediate iterations, removed scope, review history, or abandoned approaches.
- PR titles must follow the commit message convention.
- Never include internal planning IDs in the PR title or body, including Waypoint IDs, Task IDs, or roadmap labels such as `W1-A3`.
- Upload PR screenshots by drag-and-drop into UI input `#fc-new_comment_field`, then format the uploaded URLs under `## 스크린샷` in Markdown tables with at most 4 columns per table.
