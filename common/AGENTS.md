## Simplicity

- Judge code, documents, and UI by whether each element helps the user understand, decide, or act. Remove or combine unnecessary or duplicate content, structure, tests, state, and abstractions.
- Reduce total reading, reasoning, and interaction burden; fewer elements alone are not the goal. Preserve necessary behavior, information, navigation, accessibility, and meaningful risk coverage.

## Agent Browser CLI

- Standardize the startup routine to `agent-browser close` → `agent-browser --profile <abs-path>`.
- Restrict profile paths to `~/.agent-browser/profiles/sjquant`; if login is required, relaunch headed and ask the user to authenticate before proceeding.

## Obsidian CLI

- If the obsidian CLI is unavailable, start the Obsidian desktop app first and retry.
