## Coding

- Order functions so each callee appears below its caller.
- Write tests as behavioral specifications: concise behavior-based names, a short docstring or doc comment explaining the scenario and expected behavior (JS/TS `it(...)` / `test(...)` descriptions suffice), and `Given` / `When` / `Then` sections in the body.
- When complex setup, concurrency, timing, or multi-step control flow makes a test hard to follow, add concise comments at key transitions to explain the scenario and synchronization; do not narrate obvious code.
- Avoid low-value, brittle, implementation-coupled, or over-mocked tests—including tests that merely restate literals, constants, or configuration wiring; prefer outside-in integration tests through public interfaces, and add tests only when they specify meaningful externally observable behavior or guard against a substantive regression.
- Do not expose private members solely for testing.
- Keep tests focused on current, externally observable behavior: do not add temporary tests solely for intermediate layers when a planned integration test better specifies the behavior, or regression tests for intentionally removed code paths; add tests only when omitting them leaves an immediate regression or safety gap, and update or remove obsolete tests instead.
- Do not preserve backward compatibility. Remove obsolete paths instead of adding compatibility layers, fallbacks, or migrations.

## Agent Browser CLI

- Standardize the startup routine to `agent-browser close` → `agent-browser --profile <abs-path>`.
- Restrict profile paths to `~/.agent-browser/profiles/sjquant`; if login is required, relaunch headed and ask the user to authenticate before proceeding.

## Obsidian CLI

- If the obsidian CLI is unavailable, start the Obsidian desktop app first and retry.
