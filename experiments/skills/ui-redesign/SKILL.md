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
- visual direction
- hierarchy
- UX flow
- accessibility
- responsive behavior
- interaction states
- design-system cleanup

When the existing source lacks enough visual direction:

1. Read `references/design/_INDEX.md`.
2. Shortlist 2-3 plausible Layer B visual/design-system directions.
3. Select exactly one Layer A style/execution reference from `references/design/taste-*.md`.
4. Select exactly one Layer B brand/design-system reference from `references/design/brand-*.md`.
5. Extract only the decisions needed for this redesign:

- color palette or token changes
- typography and hierarchy
- spacing rhythm
- surface material, depth, radius, and shadow
- component anatomy
- interaction states
- motion rules

## Structure

This is not CSS-only. Change HTML/DOM structure when needed for:

- visual hierarchy
- semantic structure
- accessibility
- responsive ordering
- component anatomy
- interaction states

Constraints:

- Do not change markup only for styling convenience.
- Preserve behavior, data flow, routes, forms, and event handlers.
- Prefer existing components and tokens before adding structure.
- Record structural changes in notes or `DESIGN.md` when they affect the design contract.

Rules:

- Do not perform unrelated redesign.
- Extend tokens, components, states, motion rules, accessibility rules, or accepted debt only when required.
- Do not introduce ad-hoc one-off styling unless scoped, necessary, and recorded as debt.

Reference files included:

- `references/design/_INDEX.md`
- `references/design/taste-default.md`
- `references/design/taste-premium.md`
- `references/design/taste-minimal.md`
- `references/design/taste-experimental.md`
- `references/design/brand-linear.md`
- `references/design/brand-stripe.md`
- `references/design/brand-supabase.md`
- `references/design/brand-vercel.md`
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

## Responsive Spacing QA

If responsive spacing changes, inspect desktop and mobile screenshots before completion.

Check:

- spacing rhythm at desktop and mobile widths
- visible alignment across wrappers, content edges, cards, tables, and actions
- hidden overflow, clipping, and accidental scroll
- real content density, not empty or idealized states

For report spacing/layouts:

- inspect wrapper, card, and table borders together
- avoid double outlines and cramped nested surfaces
- do not squeeze multiple wide tables into columns

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
- [ ] Visual direction, hierarchy, and material decisions identified when changed.
- [ ] No unrelated redesign.
- [ ] No unrecorded one-off styling.
- [ ] HTML/semantic structure checked.
- [ ] Changed breakpoints checked.
- [ ] Desktop and mobile spacing screenshots checked.
- [ ] Alignment, overflow, and report density checked.
- [ ] Changed states checked.
- [ ] Accessibility checks relevant to scope completed.
- [ ] Perceived performance checks relevant to scope completed.
- [ ] Browser evidence recorded.
- [ ] Before/after evidence recorded when useful.
