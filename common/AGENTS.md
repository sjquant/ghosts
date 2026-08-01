## Coding
- Organize code in a **top-down** order.
- Write tests as **behavioral specifications** using descriptive `it(...)` titles and **Given–When–Then** sections.
- Avoid brittle or implementation-coupled tests, over-mocking. Prefer **outside-in, integration tests** through public interfaces.
- Do not expose private members solely for testing.

## PR
- Use gh pr edit --body-file - <<'EOF' as the default PR body path
- Before updating a pull request, check its current title and body.
- Use `.github/pull_request_template.md` when present. Otherwise, structure the PR body with `## Why` and `## Changes` with bullet points.
	- Under `## Why`, explain the problem and its impact in 1–2 sentences.
	- Under `## Changes`, summarize the chosen solution direction and key behavioral changes.
- Keep the PR body concise and easy to understand. Do not enumerate every changed file, code modification, or implementation detail unless it is essential for review.
- Describe only the final state of the change and its user-visible impact. Never mention intermediate iterations, removed scope, review history, or abandoned approaches.
- PR titles must follow the commit message convention.
- Never include internal planning IDs in the PR title or body, including Waypoint IDs, Task IDs, or roadmap labels such as `W1-A3`.
- Upload PR screenshots by drag-and-drop into UI input #fc-new_comment_field, then format the uploaded URLs under ## 스크린샷 in Markdown tables with at most 4 columns per table.

## Git workflow
1. If the project's commit message style is unknown, execute `git log --oneline -n 2` to identify the existing pattern.
2. After finishing, always commit and push your changes. If there's no PR yet, create it first.

## Agent Browser CLI
- Standardize the startup routine to `agent-browser close` → `agent-browser --profile <abs-path>`.
- Restrict profile paths to `~/.agent-browser/profiles/sjquant`; if login is required, relaunch headed and ask the user to authenticate before proceeding.

## Obsidian CLI
- If the obsidian CLI is unavailable, start the Obsidian desktop app first and retry.
