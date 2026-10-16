## Avoid unnecessary complexity

- AI-generated work tends to overcomplicate simple problems and overfill documents and interfaces. Keep the solution proportionate to the actual need; question added abstractions, tests, structure, explanations, and controls that do not help the intended audience understand, decide, or act.
- Simplify when it reduces the audience's total reading, reasoning, or interaction burden. Brevity alone is not the goal: preserve necessary behavior, context, navigation, accessibility, and meaningful risk coverage, and do not force cleanup when no useful improvement is evident.

## Agent Browser CLI

- Standardize the startup routine to `agent-browser close` → `agent-browser --profile <abs-path>`.
- Restrict profile paths to `~/.agent-browser/profiles/sjquant`; if login is required, relaunch headed and ask the user to authenticate before proceeding.

## Obsidian CLI

- If the obsidian CLI is unavailable, start the Obsidian desktop app first and retry.
