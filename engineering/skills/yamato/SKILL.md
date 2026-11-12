---
name: ghosts:yamato
description: Implement a task, then run independent review, fixes, and cleanup for a configurable number of cycles (default one).
disable-model-invocation: true
---

Run these stages in order in the current session. Read and follow each skill when its stage begins:

Default to one cycle. If the user specifies a positive integer cycle count, such as `x2` or `x3`, use that count instead.

1. Apply $ghosts:coding to implement the task and verify its checklist.
2. Run the following cycle for the selected number of cycles:
   - Run $ghosts:code-review with independent reviewer subagents against the current change, including any fixes and cleanups from the previous cycle.
   - Fix applicable findings and verify the fixes. Skip fixes if there are none.
   - Run $ghosts:slop-shaking and apply useful cleanups.

Continue through the selected cycles unless a blocker requires user input. After the final cycle, report any unresolved issues without starting another cycle.
