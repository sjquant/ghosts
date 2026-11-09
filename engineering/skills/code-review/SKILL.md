---
name: ghosts:code-review
description: Use only when the user explicitly requests a code review or invokes this skill. Do not trigger for implementation, debugging, refactoring, or routine verification requests. Performs a broad, read-only code review using general agents and complete result synthesis.
---

Review the change read-only. Use two general subagents by default. Give each the change context, the common instructions below, and its assigned question blocks. Do not add roles, review commands, or extra prompts.

Before assigning questions, the main agent identifies the key assumptions the change depends on and the affected boundaries, then uses them to guide its own verification in proportion to risk.

Consider every question below. Mark irrelevant questions `N/A — <reason>`. The main agent answers each applicable question. Assign applicable questions once across the selected subagents without overlap.

Common instructions:

```text
Review the change read-only:

Write findings and summaries using ISO 24495-1:2023 Plain Language principles.

AI-generated changes can overcomplicate simple problems; question whether added code or tests are needed at all, and consider omission before adding another layer.

Report findings with locations, evidence, and the smallest useful fix. Say when no actionable issue is found.
```

Question blocks:

```text
- Any correctness risks, including bugs or unhandled edge cases?
- Any race conditions, resource leaks, or lifecycle ordering risks?
- Any performance bottlenecks or scalability concerns?
- Any security issues?
```

```text
- Any downstream contract breaks affecting callers, persisted data, wire formats, cross-language consumers, or feature flags?
- Trace concrete failure paths beyond the diff, including transitive dependencies.
- Check pinned dependency versions and local patches where behavior depends on them.
```

```text
- Any design or API issues from the intended caller’s perspective, using outside-in and deep-module perspectives?
- Does the module expose internal collaboration methods or make callers manage state, lifecycle, ordering, or other hidden obligations?
- Any awkward call sites, leaky abstractions, circular dependencies, or dependency-direction issues?
```

```text
- Any unnecessary variables or intermediate state?
- Any unnecessary interfaces or abstractions?
- Could omission, standard features, existing code reuse, a different design, or clearer naming solve the problem more simply?
```

```text
- Any brittle or implementation-coupled tests, over-mocking, unclear intent, or tautological assertions that repeat the implementation or only verify mock setup?
- Any missing negative-path coverage or surviving mutants that reveal meaningful gaps?
- Any `if` statements or conditional expressions in tests, including setup, helpers, and assertions? Flag each; require separate cases or parameterization with inputs and expected outcomes defined before execution.
- Any tests that only recheck declared configuration or documented dependency behavior? Do not request or retain them; require a credible application-specific regression and an observable outcome.
- Any one-off checks kept as permanent tests, or concurrency or timing tests without a credible execution path and meaningful failure impact?
- Any redundant or low-signal tests whose costs outweigh their added confidence? Compare scenarios and assertions with existing tests beyond the diff, including public entrypoints. Prefer removal, consolidation, or extending an existing case when meaningful behavior, edge-case, and risk coverage is preserved.
```

After all agents respond and before synthesizing the final findings, triage every candidate point through this question: `Does this feedback identify a real, evidenced, material issue, or would addressing it add unnecessary complexity, flag a nonexistent or unsupported bug, or provide little value?` Judge the feedback itself, not only whether another agent made the same point. Do not omit any candidate point. Assign `P0`, `P1`, `P2`, or `P3` when it is actionable; assign `SKIP` only as a priority label when it is false, unsupported, duplicate, contradicted, out of scope, or not worth acting on. `SKIP` never means remove the item: every candidate must remain in `Findings` with its priority and the reason for that judgment. Do not leave skipped candidates only in `Reviewer Results`.

- Write in the user's language.
- The main agent assesses finding validity and review coverage separately; close material coverage gaps before concluding, or state what remains unverified and why. Absence of findings is not evidence of sufficient coverage.
- If a GitHub URL is supplied, use a bare, commit-pinned `blob` permalink with the smallest relevant line range in each `Location`.
- Otherwise, use repository-relative paths.
- `P0` is release-blocking, `P1` major, `P2` actionable, and `P3` low-priority.

```markdown
## Findings

### <P0|P1|P2|P3|SKIP> - <title>

- Location: [path/to/file.ext](path/to/file.ext:Lx)
- Kind: bug|performance|security|design|test|simplification|other
- Triage: <priority> — <why this feedback received this priority, including why it is low-value or unsupported when priority is `SKIP`>
- Evidence: <why this matters>
- Impact / fix: <impact and smallest useful action>

## Review Summary

- Agents used: `<n>`
- Verdict: `no blocking findings|findings require attention|manual review still required`
- Coverage: <key assumptions and affected boundaries checked, evidence, and material gaps or limitations>

## Reviewer Results

- `<agent>`: <every response and the corresponding Findings item>
```

For GitHub-linked reviews, make `Location` a bare GitHub permalink, for example: `- Location: https://github.com/acme/project/blob/0123abc/src/parser.ts#L42-L48`.

If there are no actionable findings, say so while retaining every candidate in `Findings` with `SKIP` priority and its reason.
