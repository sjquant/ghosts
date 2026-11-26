---
name: ghosts:coding
description: Use when writing, modifying, or refactoring code, including tests. Apply these coding standards during implementation.
---

Use the checklist below during implementation. Before writing, identify the applicable items and inspect existing code with a similar role to guide the implementation.

After implementation, verify every applicable item against the final diff, relevant surrounding code, and checks where needed. Fix unmet items and recheck them; rerun affected checks after changes. Mark an item complete only when supported by what you inspected or ran, and mark irrelevant items `N/A` with a reason.

- [ ] Prefer omission, existing code reuse, and language or standard-library features over unnecessary variables, interfaces, abstractions, or tests.
- [ ] Design outside-in from caller usage and domain invariants.
- [ ] Hide internal state, lifecycle, ordering, and retry details that callers need not manage.
- [ ] Revisit abstractions that require repeated workarounds or type escape hatches. If successive fixes fail under the same premise, challenge that premise before patching again.
- [ ] Prefer a rerunnable tool when it reduces execution or verification cost.
- [ ] Follow naming, structure, error-handling, and abstraction conventions from nearby code or code with a similar role, unless there is a concrete reason to differ.
- [ ] Order functions so each callee appears below its caller.
- [ ] Write function, method, and schema/tool docstrings or descriptions as concise statements of purpose in domain terms; omit them when the name and signature already make the purpose obvious. Describe what it accomplishes without narrating internal steps, enumerating permissions, side effects, or error handling, or encoding implicit dependencies on callers, collaborators, or prior context—keep wording valid if the implementation (`how`) changes while the purpose (`what`) stays the same. Add contract details separately only when callers need them to use it correctly. Prefer one sentence; expand only when necessary.
- [ ] Write tests as behavioral specifications: each test docstring, doc comment, or description (`it(...)` / `test(...)`) must stand alone, state the scenario and observable outcome, and avoid surrounding context, comparative wording, or implementation details (such as internal helpers, mocks, or incidental fixtures). Keep names concise and behavior-based, and structure the body with Gherkin keywords (`Given`, `When`, `Then`, `And`) as appropriate.
- [ ] Never use `if` statements or conditional expressions in test code, including setup, helpers, and assertions. Define each case's inputs and expected outcomes before execution; use separate cases or parameterization instead of branching.
- [ ] When complex setup, concurrency, timing, or multi-step control flow makes a test hard to follow, add concise comments at key transitions to explain the scenario and synchronization; do not narrate obvious code.
- [ ] Add tests only for meaningful current, externally observable behavior or substantive regression risks; prefer outside-in integration tests through public interfaces. Avoid brittle, implementation-coupled, over-mocked tests and assertions that merely restate literals, constants, configuration wiring, or documented dependency guarantees. Do not add temporary tests for intermediate layers better covered by a planned integration test unless omission leaves an immediate regression or safety gap.
- [ ] Search existing tests beyond the diff and compare scenarios and assertions before adding coverage. Extend an existing case or suite when it clearly covers the behavior; add separate tests only for independent behavioral confidence or a distinct regression risk. Update or remove obsolete tests, including tests for intentionally removed paths.
- [ ] Do not expose private members solely for testing.
- [ ] Do not preserve backward compatibility. Remove obsolete paths instead of adding compatibility layers, fallbacks, or migrations.
