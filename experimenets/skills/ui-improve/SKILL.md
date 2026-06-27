---
name: ui-improve
description: "Experimental frontend skill for existing UI changes: visual polish, redesign, UX flow, accessibility, performance, responsive fixes, state completeness, and visible component cleanup. Respects the existing design source and requires browser QA evidence."
---

# UI Improve

Use for existing UI changes:

- visual polish
- redesign
- UX flow improvements
- accessibility fixes
- performance improvements
- responsive fixes
- state completeness
- component cleanup tied to visible UI

## Source

First identify the existing source:

1. Figma or external design system.
2. Repo tokens, components, theme, or shared CSS.
3. Existing `DESIGN.md`.
4. Current implemented UI patterns.

Follow an existing source before introducing new visual decisions.

If no source exists, ask whether to:

- preserve the current look with nearby edits
- extract lightweight implementation notes and reusable components first

## Scope

Classify the improvement goal before editing:

- visual polish
- UX flow
- accessibility
- performance
- responsive behavior
- interaction states
- implementation cleanup

Rules:

- Do not perform unrelated redesign.
- Extend tokens, components, states, motion rules, accessibility rules, or accepted debt only when required.
- Do not introduce ad-hoc one-off styling unless scoped, necessary, and recorded as debt.

## QA

- Capture before/after browser evidence when useful.
- Use the project's browser tooling first.
- If the project lacks a capture tool, use available browser automation.

Evidence must record:

- route/page
- viewport size
- state captured
- screenshot path
- command or tool used
- before/after paths when useful

## Completion Gate

- [ ] Existing design source respected or extraction decision made.
- [ ] Improvement goal identified.
- [ ] No unrelated redesign.
- [ ] No unrecorded one-off styling.
- [ ] Changed breakpoints checked.
- [ ] Changed states checked.
- [ ] Accessibility checks relevant to scope completed.
- [ ] Performance checks relevant to scope completed.
- [ ] Browser evidence recorded.
- [ ] Before/after evidence recorded when useful.
