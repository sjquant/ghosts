---
name: loop-skills
description: Approval-gated iterative loop for designing, creating, reviewing, or refining reusable agent skills.
disable-model-invocation: true
---

# Loop Skills

Turn a skill idea into a small, explicit, testable `SKILL.md` and only the
supporting resources it needs. Use a bounded loop: understand the job, inspect
local conventions, design the contract, obtain approval, implement, exercise
representative cases, pressure-test the result, and repair material problems.

This skill is for authoring skills, not for carrying out the task that the new
skill will eventually handle. In review mode, do not edit anything.

## Execution state

Before doing any work, create a task-specific checklist at
`/tmp/loop-skills-<safe-task-slug>.md`, replacing the placeholder with a unique
short slug or timestamp. Keep it updated after every completed item; do not
mark future items in advance. Use `[x]` only after the item is actually
complete and `[-]` only with a reason. Record a short outcome beside each
item.

Add newly discovered requirements, material leads, or unresolved dependencies
to the checklist. If a change could invalidate a completed contract, approval,
implementation, or validation item, reset the affected item to `[ ]` and
process it again. Do not move to the next required item while the current one
is unchecked.

Use a checklist with at least these items:

```text
- [ ] Define the authoring mode, user outcome, audience, and scope
- [ ] Inspect repository instructions and nearby skills
- [ ] Specify the skill contract and invocation boundary
- [ ] Any materially better design or existing skill to reuse?
- [ ] Choose the smallest design that meets the request
- [ ] Present the plan and receive approval
- [ ] Implement or revise the skill and only needed resources
- [ ] Run structural and representative behavioral checks
- [ ] Any correctness or operational risks in the skill's behavior, failure paths, permissions, or side effects?
- [ ] Any trigger, contract, dependency, or instruction-order issues when viewed from outside-in?
- [ ] Any opportunity to simplify or clarify the skill through existing conventions, references, or tools?
- [ ] Any validation or test smells, such as wording-only checks, brittle examples, over-mocking, or untestable criteria?
- [ ] Repair and re-check any material issue
- [ ] Finalize the skill, validation evidence, and unresolved items
```

## Modes

Select the mode before editing:

- **Create:** the requested skill does not exist. Add its directory and
  `SKILL.md`.
- **Refine:** the requested skill exists and the user wants behavior changed.
  Preserve useful behavior, remove obsolete instructions, and re-check every
  affected contract item.
- **Review:** the user asks whether a skill is sound. Inspect and report; do
  not write files.

Do not silently turn a review into an implementation or a refinement into a
new, unrelated skill. If the requested change materially expands the scope,
stop and present a revised plan for approval.

## Workflow

### 1. Frame the authoring task

Identify:

- the real user outcome the skill should produce;
- who or what will invoke it and the expected input shape;
- the output artifact, format, language, and success criteria;
- whether invocation should be explicit or automatic;
- tools, external systems, side effects, safety limits, and freshness needs;
- clear non-goals and the nearest out-of-scope requests.

Ask at most one clarifying question when a missing choice would materially
change behavior, scope, safety, cost, or the output contract. Otherwise state an
assumption and continue.

### 2. Inspect the local skill system

Read applicable `AGENTS.md` files before editing. Inspect the nearest skills,
their directory layout, frontmatter, naming, tone, references, scripts, and
validation conventions. Search for an existing skill that already covers the
request or could be composed instead of duplicated.

Treat neighboring skills as evidence, not a template to copy blindly. Follow
repository-local instructions when they are stricter than this skill. Do not
invent host-specific metadata, tools, or runtime behavior; use fields and
capabilities already supported by the local system.

### 3. Specify the skill contract

Design the contract before prose. It must make these answers observable:

1. **Trigger:** what requests are in scope, and what similar requests are not?
2. **Inputs:** what is required, optional, inferred, or rejected?
3. **Process:** what must happen, in what order, and at which decision gates?
4. **Output:** what must be returned or written, where, and in what format?
5. **Quality bar:** how can the agent tell that the result is complete and
   correct?
6. **Failure boundary:** what happens when information, access, or evidence is
   missing?
7. **Authority:** which user, repository, tool, and safety instructions win if
   they conflict?

Keep hard requirements separate from useful preferences. Prefer observable
rules (`include two scenarios`, `cite each material claim`) over vague advice
(`be helpful`, `make it polished`). Define terms that could be interpreted in
more than one way.

### 4. Choose the smallest useful design

Compare at least one credible alternative when the design is non-trivial—for
example, a single self-contained skill versus a small skill plus a reference,
or an automatic trigger versus explicit invocation. Choose the option with the
lowest complexity that still protects the required behavior.

Use progressive disclosure:

- Keep the main `SKILL.md` focused on decisions and execution.
- Add a reference only when detail is needed during execution, and link to it
  from the exact step that requires it.
- Add a script or asset only when it provides repeatable value that prose
  cannot. Do not add speculative scaffolding or generated output.

For tool access, request the narrowest supported permission. For side effects,
state the confirmation, target, and failure behavior explicitly. Never smuggle
credentials, hidden policy, or unrelated workflow into a skill.

### 5. Plan and obtain approval

Before creating or changing files, present a concise plan containing:

- the chosen authoring mode and target path;
- the contract and user-visible behavior;
- the relevant alternative and its tradeoff;
- files or resources to add, change, or remove;
- validation and representative cases;
- assumptions and any remaining uncertainty.

Wait for explicit approval such as `go` or `approve`, unless the user has
already approved that specific plan. A request to “make this skill” approves
the goal, but not an unannounced expansion of its scope or side effects.

### 6. Implement the skill

Create or revise the smallest complete set of files. The frontmatter must be
valid for the host and should include, at minimum, a stable lowercase-hyphen
`name` and a concrete `description`. Keep the directory name and skill name
aligned unless the repository convention explicitly says otherwise.

Write instructions as an executable contract:

- put the main behavior and ordering where the agent will need it;
- make approval, stopping, retry, and escalation rules explicit;
- include input and output examples only when they prevent a likely mistake;
- link references with repository-relative paths and ensure every link exists;
- remove obsolete or conflicting paths instead of layering compatibility prose;
- preserve the user's language and requested format where the contract allows.

Do not implement the target application, fabricate evidence, or claim a check
was run when it was only described.

### 7. Validate structurally and behaviorally

Run the repository's available checks first. At minimum, inspect the final diff
and verify:

- frontmatter opens and closes correctly and required fields are present;
- the declared name, directory, links, references, scripts, and assets resolve;
- instructions do not contradict one another or the repository policy;
- the trigger is neither so broad that it hijacks unrelated work nor so narrow
  that the requested case misses it;
- every required output has a format, location, and completion criterion;
- permissions and side effects are no broader than the task requires.

Exercise the contract with representative prompts, using the host's skill
harness if one exists or a documented dry run otherwise:

1. a normal in-scope request;
2. the closest out-of-scope request;
3. a request with missing or ambiguous input;
4. a failure, empty-result, or unavailable-tool case;
5. a side-effecting case, if the skill can change external state.

Record what the skill should do and what it actually does. Do not add tests
that merely assert wording or internal step order when the behavior can be
checked through the public invocation contract.

### 8. Review, pressure-test, and repair

After drafting, process the following `Any ...?` questions one at a time. Mark
each answer in the checklist and record a short finding:

```text
Any correctness or operational risk in the skill's behavior, failure paths,
permissions, or side effects?

Any trigger, contract, dependency, or instruction-order issue when viewed from
outside-in, including hidden obligations or an awkward invocation boundary?

Any opportunity to simplify or clarify the skill through an existing convention,
reference, utility, or narrower permission?

Any validation or test smell, such as a wording-only assertion, brittle example,
over-mocking, unclear intent, missing negative path, or untestable criterion?

Any material ambiguity, overlap, contradiction, unsupported dependency, or
missing failure path that could change the skill's behavior or usefulness?
```

Then ask:

```text
What is the smallest useful repair for each “yes” answer?
```

If any answer is yes, make the smallest useful repair, run the affected checks
again, and continue the review from the beginning when the repair can affect a
previous conclusion. If the repair changes the approved scope or design,
stop and request approval for the revised plan.

Stop when the contract is explicit, representative cases are covered, no
material issue remains, and the diff contains no unnecessary resource or
compatibility layer. If a limitation cannot be resolved, narrow the contract
and state it rather than pretending the skill supports it.

## Final response

Write in the user's language and lead with the outcome. Keep the handoff
concise:

```markdown
완료. `<path>/SKILL.md`를 <created|refined|reviewed>했습니다.

핵심 계약:
- 트리거/범위: ...
- 입력/출력: ...
- 주요 게이트와 실패 경계: ...

검증:
- 구조 점검: ...
- 대표 사례: ...
- 남은 불확실성: ...
```

For review mode, replace the completion statement with the findings and do not
claim that files were changed. Mention only checks that actually ran and link
the changed files when the host supports clickable local paths.
