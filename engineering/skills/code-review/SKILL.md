---
name: code-review
description: Broad, read-only code review using general agents and complete result synthesis.
disable-model-invocation: true
---

Review the requested code change without modifying the worktree, committing, or pushing. This skill deliberately keeps the review prompts short: use general-purpose agents, collect what they notice, and let synthesis—not a detailed routing rubric—do the work.

## Review approach

1. Establish the review scope from the user's request, repository instructions, and the actual diff. Read the changed code, its relevant callers, public boundaries, and tests. Inspect enough surrounding code to verify each concern; do not review only the patch in isolation.
2. If general-agent delegation is available, run several independent review passes with the same change context. Do not route work to named or role-specific reviewers from `engineering/agents/`, and do not require any particular agent file.
3. Ask open questions rather than supplying a long checklist. Use prompts such as:

   - `Any bugs? Please report every concern with concrete file and line evidence.`
   - `Any performance improvement points? Please report every concern, including low-confidence ones, with evidence.`
   - `Any other risks, missing tests, or design concerns? Please report everything you notice.`

   Keep the prompts independent so agents can notice different things. Include the user's request and relevant context in every pass. If delegation is unavailable, perform the same broad passes yourself and say so in the output.
4. When a design-oriented pass would benefit from a shared concept, use one short optional lens question. For example:

   - `Any improvements based on deep modules?`
   - `Any improvements based on information hiding?`
   - `Any issues caused by temporal coupling?`
   - `Any unnecessary complexity or abstraction?`

   These are prompts for discovery, not mandatory criteria. Use only the lenses relevant to the change, do not require an issue for every lens, and do not let them narrow the rest of the review.
5. Independently inspect the highest-risk behavior and verify agent claims against the code. Agent output is evidence to investigate, not a reason to pre-filter results.
6. Run applicable repository checks, tests, or build commands when they are available. Report failures and limitations; do not silently treat an unverified change as verified.
7. Synthesize every response after all passes finish. Deduplicate semantically identical points, but do not summarize away, rank away, or silently omit a distinct concern.

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

- `P0`: Release-blocking security incident, data loss, or whole-service outage risk.
- `P1`: Major regression with broad user or workflow impact.
- `P2`: Standard actionable bug or meaningful conditional failure.
- `P3`: Low-priority correctness, quality, maintainability, performance, or edge-case risk.

Return this structure:

```markdown
## Findings

### P1 - <title>

- Location: [path/to/file.ext](/relative/path/to/file.ext:Lx) `path/to/file.ext:Lx-Ly`
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
