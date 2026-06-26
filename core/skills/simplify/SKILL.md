---
name: simplify
description: Apply Ponytail-style minimal implementation: understand the touched flow, skip what need not exist, reuse existing code, prefer stdlib/native features, and avoid speculative abstractions. Use when the user says ponytail, lazy mode, be lazy, simplify, simplest solution, minimal solution, YAGNI, do less, shortest path, or complains about over-engineering.
disable-model-invocation: true
---

Build the smallest safe version that satisfies the request. Lazy means
efficient, not careless: the best code is code that did not need to be written.

## First Principle

Understand the touched flow before reducing it. Read the task, changed files,
representative callers, and tests. Then choose the highest rung that actually
works. A tiny patch in the wrong place is not simple; it is another bug.

## Ladder

Stop at the first rung that works:

1. Skip behavior that does not need to exist. Speculative need is out of scope.
2. Reuse code that already exists in the repo.
3. Use the standard library.
4. Use a native platform feature.
5. Use an already-installed dependency.
6. Collapse it to one clear expression.
7. Keep only the minimum custom code.

## Rules

- Fix bugs at the root cause in the shared path instead of patching each caller.
- Grep every caller before changing a shared function.
- Do not add abstractions, config, factories, wrappers, interfaces, or dependencies for one use.
- Delete dead code before adding new code.
- Prefer boring code over clever code.
- Keep tests at the public behavior boundary; do not expose private methods for testing.
- For non-trivial logic, leave one smallest runnable check that would fail if the logic breaks.
- Mark deliberate shortcuts with `ponytail: <ceiling>, <upgrade trigger>`, for example `ponytail: global lock, switch to per-account locks if contention shows up`.

## Do Not Simplify Away

- Trust-boundary validation.
- Data-loss-preventing error handling.
- Security or accessibility requirements.
- Explicitly requested behavior.
- Hardware calibration or other real-world tuning knobs.
- Edge-case correctness when a same-size standard option handles it better.

## Review Before Done

Before finishing, scan the diff for:

- behavior that can be deleted;
- existing helpers that replace new code;
- standard library or native features replacing custom code;
- new dependencies that can be avoided;
- one-use abstractions, wrappers, factories, interfaces, or config;
- tests that expose private implementation instead of public behavior.

## Output

Ship the code first. Then state, in at most three short lines, what was skipped
and when to add it.
