---
name: loop-coding
description: Approval-gated coding loop for building, changing, fixing, or refactoring code. Do not activate for explanation-only, review-only, or planning-only requests.
---

# Loop Coding

For a coding task, first understand the request and inspect the relevant code.
Before editing, present a concise implementation plan covering the approach,
important alternatives or tradeoffs, affected files, and validation. Wait for
explicit approval such as `go` or `approve`, unless the user has already
approved a specific plan. Do not implement from a bare request.

After approval, implement the plan and run the relevant checks. Then review and
repair the change by asking yourself these questions one at a time:

- Any correctness, operational, or security issues?
- Any design or API issues?
- Any test issues?
- Any unintended side effects from the fixes?
- Any bloats, slops, or smells?

Whenever the answer is yes, make the smallest useful fix, run the relevant
checks again, and continue the questions from the beginning if the fix could
introduce another issue. Keep this loop internal; do not make the user prompt
each review pass. Stop when the answers are no, the relevant checks pass, and
the diff remains within the approved scope. If the scope or design must change
materially, stop and present a revised plan for approval.

Keep the final response concise: summarize what changed, the checks run, and
any remaining uncertainty.
