---
name: simplify
description: Apply the smallest safe implementation: delete what is unnecessary, reuse existing code, prefer stdlib/native features, and avoid speculative abstractions. Use when the user says simplify, simplest solution, minimal solution, YAGNI, do less, shortest path, or complains about over-engineering.
disable-model-invocation: true
---

Build the smallest safe version that satisfies the request.

## Ladder

After reading the touched flow, stop at the first rung that works:

1. Skip behavior that does not need to exist.
2. Reuse code that already exists in the repo.
3. Use the standard library.
4. Use a native platform feature.
5. Use an already-installed dependency.
6. Collapse it to one clear expression.
7. Keep only the minimum custom code.

## Rules

- Fix the root cause in the shared path instead of patching each caller.
- Do not add abstractions, config, factories, wrappers, or dependencies for one use.
- Delete dead code before adding new code.
- Keep tests at the public behavior boundary; do not expose private methods for testing.
- For non-trivial logic, leave the smallest runnable check that would fail if the logic breaks.
- Mark deliberate shortcuts with `ponytail: <ceiling>, <upgrade trigger>`.

## Do Not Simplify Away

- Trust-boundary validation.
- Data-loss-preventing error handling.
- Security or accessibility requirements.
- Explicitly requested behavior.
- Hardware calibration or other real-world tuning knobs.

## Output

Ship the code first. Then state, in at most three short lines, what was skipped
and when to add it.
