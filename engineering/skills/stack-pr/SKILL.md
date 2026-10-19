---
name: ghosts:stack-pr
description: Use when the user asks to implement GitHub issues in parallel and build stacked pull requests in dependency order.
---

Read the requested issues, sub-issues, dependencies, relevant comments, and existing PRs with `gh`. Resolve each task's repository, scope, completion criteria, and actual prerequisites. Parent membership is not a dependency. Reuse existing work rather than starting duplicate branches or PRs.

Use `ghosts:delegate` to run independent, ready issues in parallel and supervise them through completion, with one implementation agent per issue in an isolated worktree. Assign each worker an exact base commit and verify the checkout starts from it before implementation. The main agent owns scheduling, branch topology, and publication; workers return their change, review results, and checks.

Any missing decision, dependency cycle, or overlapping ownership that makes parallel work unsafe? Resolve it before starting the affected tasks; continue unrelated work. Use `ghosts:grill-me` for material decisions and `ghosts:work-breakdown` when an issue still needs decomposition.

## Each issue

```text
Implement → relevant checks → code-review → fix findings
          → slop-shaking → checks on the final change → commit → github-pr
```

Use `ghosts:code-review` with exactly one review subagent covering all applicable questions on the issue's diff against its immediate base, apply actionable findings, then use `ghosts:slop-shaking`. Resolve outstanding findings before publishing; repeat review where subsequent changes alter correctness or design. Keep meaningful behavioral coverage without adding tests merely to document intermediate work.

A prerequisite is ready for downstream implementation once its review, cleanup, and checks pass and its final change is committed. Its PR need not be merged. Start newly ready issues as workers finish, rather than waiting for an entire batch. A PR being open does not mean the issue is complete; completion requires its intended change to land on the default branch.

## Stack and publish

Check the installed `gh stack --help` and relevant subcommand help before use. Start a chain with `gh stack init <branch>`. After a predecessor is ready, extend its stack with `gh stack add <next-branch>` and start the successor from that reviewed commit. For branches already created by Orca, adopt them instead of creating duplicates: `gh stack init <bottom-branch> <next-branch> ...` lists them bottom to top; verify their ancestry first.

Stacks are linear. Keep independent tasks in separate stacks; a fork can start a separate stack with `--base <predecessor-branch>`. For a task requiring multiple branches, wait until all required changes are available on one reviewed base, usually after their merges; do not silently introduce dependencies between independent tasks. Across repositories, use separate stacks and check that required interfaces or artifacts are actually available to the consumer.

Use `ghosts:github-pr` to create or update each reviewed issue's PR, explicitly targeting its immediate predecessor branch, or the trunk for the bottom layer. Follow the repository template and describe only that layer's final diff. Include `Closes #N`, or `Closes OWNER/REPO#N` for an issue in another repository, only for issues the change fully resolves; use ordinary links for partial work and parent issues.

Once every branch in the active stack has a reviewed PR, run `gh stack submit --auto` to publish its stack relationship and verify the resulting PR bases, bodies, and issue references. This command pushes all stack branches and can create missing PRs: never include unfinished branches. Serialize stack mutations and publication within a clone, since linked worktrees share stack metadata; keep affected workers idle during history rewrites.

When an earlier layer changes or merges, inspect the stack and use `gh stack sync` to rebase, push, and synchronize existing PRs. If conflicts stop sync, resolve them with `gh stack rebase`, then retry sync. Recheck affected diffs and repeat necessary review, cleanup, and checks after synchronization; commit any resulting fixes and update the PRs through `ghosts:github-pr`, then sync again. Recheck any changes introduced by that sync before treating a layer as ready for successors or reporting it ready for review. Closing keywords take effect when a PR targets the default branch; verify issue links after retargeting. Leave review and merging to the user.

## Output

Report in the user's language, grouped by repository and stack. Show dependencies in a compact code block and list each issue with its PR, review/cleanup/check result, and any blocker or next ready task. Distinguish published work from merged work; do not report unresolved work as complete.
