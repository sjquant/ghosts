# Engineering

Open a document only when its decision matches the current task.

- A function returns several values. Keep a tuple or introduce a result type? → [Return values](meaning-at-call-sites.md)
- Extend an existing boundary, extract a helper, or reuse another module? → [Responsibility and reuse](responsibility-before-reuse.md)
- A script entry point hides fetching, processing or persistence. Should those stages be visible? → [Entry-point flow](entry-point-flow.md)
- A name suggests the wrong state or action. What should callers predict? → [Names and effects](names-and-effects.md)
- Two variables or declarations represent the same fact. Store both or derive one? → [Repeated state](single-source-state.md)
- Understanding a test requires jumping between parameters, body and helpers. Where should its conditions be visible? → [Test scenarios](visible-test-scenarios.md)
- Where should a new or renamed test go? → [Test file placement](test-file-placement.md)
- Does this test protect a distinct boundary, or repeat wiring and incidental presentation? → [Test value](test-value.md)
- Should a response field or component control become public? → [Public contracts](public-contract.md)
- Should an event describe an occurrence or request one handler action? → [Events and commands](events-and-commands.md)
- Which logs or notifications will someone actually inspect? → [Operational signals](operational-signals.md)
- How much implementation detail belongs in a docstring summary? → [Docstrings](purpose-docstrings.md)
