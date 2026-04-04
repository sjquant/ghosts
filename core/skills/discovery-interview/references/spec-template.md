# Spec Template

Load this file when you are ready to generate the spec.

## Summary Confirmation

Before writing the spec, confirm your understanding:

```text
Before I write the spec, let me confirm my understanding:

You're building [X] for [users] to solve [problem].
The core experience is [journey].
The must-have outcomes are [key outcomes].
The key product tradeoffs are [tradeoffs].

Is this accurate?
```

## Default Spec Template

```markdown
# [Project Name] Specification

## Executive Summary
[2-3 sentences: what, for whom, why]

## Problem Statement
[The problem this solves, current pain points, why now]

## Success Criteria
[Measurable outcomes that define success]

## Users and Stakeholders
[Who uses this, who else is affected, goals]

## User Journey
[Step-by-step flow of the core experience]

## Functional Requirements
### Must Have (P0)
- [Requirement with acceptance criteria]

### Should Have (P1)
- [Requirement with acceptance criteria]

### Nice to Have (P2)
- [Requirement with acceptance criteria]

## Non-Functional Requirements
- [User-facing performance, reliability, compliance, or support expectations]

## Out of Scope
[Explicitly what is not being built]

## Open Questions
[Unresolved product questions]

## Appendix: Research Findings
[Only if research was actually performed]
```

## Optional Spec Additions

Add these sections only if the matching optional module was explicitly used:
- `## Data and State Requirements`
- `## Roles and Permissions`
- `## Policy or Compliance Constraints`
- `## Technical Architecture`
- `## Implementation Plan`

Do not add empty optional sections.

## Requirements Completeness Checklist

```markdown
### Problem
- [ ] Problem statement is clear
- [ ] Success criteria are defined
- [ ] Stakeholders are identified

### Experience
- [ ] User journey is mapped
- [ ] Core actions are defined
- [ ] Failure states are covered
- [ ] Important edge cases are covered

### Scope
- [ ] Must-have requirements are listed
- [ ] Should-have requirements are listed
- [ ] Nice-to-have requirements are listed
- [ ] Out-of-scope boundaries are clear

### Decisions
- [ ] Key tradeoffs are explicit
- [ ] Open product questions are listed
- [ ] User confirmed the summary is accurate
```
