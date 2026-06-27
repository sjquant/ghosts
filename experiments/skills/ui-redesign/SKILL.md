---
name: ui-redesign
description: "Experimental frontend skill for redesigning existing UI from a designer's perspective: visual direction, hierarchy, UX flow, accessibility, responsive behavior, state completeness, and visible component cleanup. Respects the existing design source and requires browser QA evidence."
---

# UI Redesign

Use for designer-led redesign of existing UI:

- visual polish
- redesign
- UX flow improvements
- accessibility fixes
- responsive fixes
- state completeness
- design-system cleanup tied to visible UI

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

Use `templates/DESIGN.md` only when extracting a full design contract is chosen or explicitly requested.

## Scope

Classify the redesign goal before editing:

- visual polish
- UX flow
- accessibility
- responsive behavior
- interaction states
- design-system cleanup

Rules:

- Do not perform unrelated redesign.
- Extend tokens, components, states, motion rules, accessibility rules, or accepted debt only when required.
- Do not introduce ad-hoc one-off styling unless scoped, necessary, and recorded as debt.

Reference files included:

- `references/design-ops/README.md`
- `references/design-ops/accessibility.md`
- `references/design-ops/critique.md`
- `references/design-ops/design-debt.md`
- `references/perfection/README.md`
- `references/perfection/accessibility-audit.md`
- `references/perfection/performance-audit.md`
- `references/visual-qa/README.md`
- `references/visual-qa/browser-capture.md`
- `templates/DESIGN.md`

## QA

- Capture before/after browser evidence when useful.
- Use the project's browser tooling first.
- If the project lacks a capture tool, use `scripts/capture-browser.mjs`.

Scripts included:

- `scripts/capture-browser.mjs`

Evidence must record:

- route/page
- viewport size
- state captured
- screenshot path
- command or tool used
- before/after paths when useful

## Completion Gate

- [ ] Existing design source respected or extraction decision made.
- [ ] Redesign goal identified.
- [ ] No unrelated redesign.
- [ ] No unrecorded one-off styling.
- [ ] Changed breakpoints checked.
- [ ] Changed states checked.
- [ ] Accessibility checks relevant to scope completed.
- [ ] Perceived performance checks relevant to scope completed.
- [ ] Browser evidence recorded.
- [ ] Before/after evidence recorded when useful.
