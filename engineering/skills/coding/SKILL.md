---
name: ghosts:coding
description: Use when writing, modifying, or refactoring code, including tests. Apply these coding standards during implementation.
---

AI-generated code can overcomplicate simple problems. First consider omission, existing code reuse, and language or standard-library features; question whether added variables, interfaces, abstractions, or tests are needed at all.

Design outside-in from caller usage and domain invariants. Repeated workarounds or type escape hatches are evidence to revisit the abstraction. If successive fixes fail under the same premise, challenge that premise before patching again. Prefer a rerunnable tool when it reduces execution or verification cost.

- Order functions so each callee appears below its caller.
- Write tests as behavioral specifications: each test docstring or doc comment must stand alone, describe the scenario and observable outcome, and avoid relying on surrounding context, implementation details, or comparative wording. Keep names concise and behavior-based (JS/TS `it(...)` / `test(...)` descriptions suffice), and use `Given` / `When` / `Then` sections in the body.
- When complex setup, concurrency, timing, or multi-step control flow makes a test hard to follow, add concise comments at key transitions to explain the scenario and synchronization; do not narrate obvious code.
- Avoid low-value, brittle, implementation-coupled, or over-mocked tests—including tests that merely restate literals, constants, or configuration wiring; prefer outside-in integration tests through public interfaces, and add tests only when they specify meaningful externally observable behavior or guard against a substantive regression.
- Treat test-suite growth as a cost: avoid redundant or low-signal tests whose behavior is already meaningfully covered elsewhere, including tests that only recheck documented dependency guarantees, unless they add independent behavioral confidence or protect a distinct regression risk.
- Do not expose private members solely for testing.
- Keep tests focused on current, externally observable behavior: do not add temporary tests solely for intermediate layers when a planned integration test better specifies the behavior, or regression tests for intentionally removed code paths; add tests only when omitting them leaves an immediate regression or safety gap, and update or remove obsolete tests instead.
- Do not preserve backward compatibility. Remove obsolete paths instead of adding compatibility layers, fallbacks, or migrations.
