---
name: ghosts:yamato
description: Implement a task, review and fix the change, then remove unnecessary complexity.
disable-model-invocation: true
---

Run these stages in order in the current session. Read and follow each skill when its stage begins:

1. Apply $ghosts:coding to implement the task and verify its checklist.
2. Run $ghosts:code-review. After the read-only review, fix applicable findings and verify the fixes. Skip fixes if there are none.
3. Run $ghosts:slop-shaking and apply useful cleanups.

Continue through all stages unless a blocker requires user input.
