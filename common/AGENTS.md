## Coding

- Order functions so each callee appears below its caller.
- Write tests as behavioral specifications using descriptive `it(...)` titles and Given–When–Then sections.
- Avoid brittle or implementation-coupled tests, over-mocking. Prefer outside-in, integration tests through public interfaces.
- Do not expose private members solely for testing.
- Implementation-coupled tests, over-mocking, and brittle tests are not allowed.
- Do not add temporary tests solely for intermediate layers when the behavior is better specified and covered by a planned integration test; add a test now only if omitting it leaves an immediate regression or safety gap.
- Do not preserve backward compatibility. Remove obsolete paths instead of adding compatibility layers, fallbacks, or migrations.

## Agent Browser CLI

- Standardize the startup routine to `agent-browser close` → `agent-browser --profile <abs-path>`.
- Restrict profile paths to `~/.agent-browser/profiles/sjquant`; if login is required, relaunch headed and ask the user to authenticate before proceeding.

## Obsidian CLI

- If the obsidian CLI is unavailable, start the Obsidian desktop app first and retry.
