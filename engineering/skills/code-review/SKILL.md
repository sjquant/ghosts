---
name: code-review
description: Broad, read-only code review using general agents and complete result synthesis.
disable-model-invocation: true
---

Review the requested code change without modifying the worktree, committing, or pushing. Use general-purpose agents and one fixed set of review questions; do not create role-specific reviewers or add ad hoc prompts.

## Review approach

1. Establish the review scope from the user's request, repository instructions, and the actual diff. Read the changed code, its relevant callers, public boundaries, and tests. Inspect enough surrounding code to verify each concern; do not review only the patch in isolation.
2. If subagent delegation is available, use one, two, or three general-purpose subagents according to the size and complexity of the change. Do not route work to named or role-specific reviewers from `engineering/agents/`, and do not require any particular agent file.
3. Assign the fixed question set below across the chosen subagents without overlap. A small change may give all questions to one subagent; a medium change may split them across two; a large or complex change may split them across three. Every question must be asked exactly once across the subagents. Give each subagent the relevant change context and only its assigned questions. Do not add explanatory, role-specific, or miscellaneous prompts.

   - `Any potential bugs or edge cases?`
   - `Any performance bottlenecks?`
   - `Any security issues?`
   - `Any opportunities to simplify the code using utilities, standard libraries, or existing abstractions?`
   - `Any structural improvements from deep-module and dependency-direction perspectives?`
   - `Any unclear or misleading names?`
   - `Any test readability issues, missing failure cases, or weaknesses that mutation testing would reveal?`
   - `Any other design improvements?`

   If delegation is unavailable, ask the same fixed question set yourself and say so in the output.
4. Independently inspect the highest-risk behavior and verify subagent claims against the code. Agent output is evidence to investigate, not a reason to pre-filter results.
5. Run applicable repository checks, tests, or build commands when they are available. Report failures and limitations; do not silently treat an unverified change as verified.
6. Synthesize every response after all questions finish. Deduplicate semantically identical points, but do not summarize away, rank away, or silently omit a distinct concern.

## Result handling

Preserve every distinct point raised by every agent in the audit trail, including performance suggestions, design alternatives, test gaps, low-severity issues, and observations that are not defects. The synthesis may remove a point from the final review sections only when it is genuinely not an issue, for example:

- the cited behavior is not present or the proposed failure cannot occur;
- the point is a duplicate of another point;
- the point directly contradicts an explicit user requirement or a conclusion already settled with the user; or
- the point is based on a misunderstanding that is disproved by the code or repository context.

Do not discard a point merely because it is low priority, difficult to reproduce, stylistic, speculative, inconvenient, or not worth a code comment. If it is plausible but cannot be confirmed, preserve it as an explicitly qualified review note. When removing a point, record the point and the concrete reason in `Reviewer Results`.

For duplicates, keep one consolidated finding with the best evidence and record every source point as merged into it. Put valid observations that are not defects—such as performance opportunities, design alternatives, test gaps, and behavior-preserving simplifications—into `Findings` as well. Label their kind so readers can distinguish a confirmed bug from a suggestion or verification gap. `Findings` is the deduplicated view; `Reviewer Results` is the audit trail of all agent output.

Use repository and user context to adjust severity. Do not invent issues to fill the report, and do not turn a settled user decision into a new finding.

## Output

Write in the user's language. Keep severity enum values in English:
Use repository-relative paths in every location. Never report absolute filesystem paths.

- `P0`: Release-blocking security incident, data loss, or whole-service outage risk.
- `P1`: Major regression with broad user or workflow impact.
- `P2`: Standard actionable bug or meaningful conditional failure.
- `P3`: Low-priority correctness, quality, maintainability, performance, or edge-case risk.

Return this structure:

```markdown
## Findings

### P1 - <title>

- Location: [path/to/file.ext](path/to/file.ext:Lx) `path/to/file.ext:Lx-Ly`
- Kind: bug|performance|design|test-gap|simplification|other
- Category: correctness|security|tests|architecture|performance|concurrency|consistency|code-quality|repo-rule
- Evidence: <why this is a real, plausible, or useful review point>
- Failure mode or impact: <what breaks, regresses, costs, or remains unverified>
- Suggested fix or next check: <smallest safe fix, simplification, measurement, or follow-up>

## Review Summary

- Reviewed files: `<n>`
- General agents used: `<n>` (or `none; reviewed directly`)
- Verdict: `no blocking findings|findings require attention|manual review still required`

## Reviewer Results

- `agent 1`: <each point raised, with `merged into Finding P#`, `preserved as ...`, or `removed: <concrete reason>`>
- `agent 2`: <each point raised and its disposition>
- `main review`: <each independently identified point and its disposition>
```

If no findings remain after deduplication and evidence checks, say that directly, list the highest-risk areas checked, and still include every preserved agent result. A clean verdict does not justify omitting the audit trail.
