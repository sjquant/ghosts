---
name: ui-greenfield
description: "Experimental frontend skill for building a new UI, app, page, landing page, flow, or component system from scratch when no concrete visual reference is provided. Uses authoritative design sources when present, otherwise creates lightweight implementation notes. Requires browser QA evidence before completion."
---

# UI Greenfield

Use for new UI work from scratch: apps, pages, landing pages, flows, components, or component systems.

## Before Implementation

Identify:

- product context
- target audience
- ambition lane
- available design source, if any

Use the most authoritative available design source:

1. Figma design system, variables, components, or tokens.
2. Existing repo tokens, components, theme, or shared CSS.
3. Existing `DESIGN.md`.
4. Newly created lightweight implementation notes.

If no source exists, create lightweight implementation notes before UI code.

## Reference Workflow

When using references:

1. Read `../frontend/references/design/_INDEX.md`.
2. Shortlist 2-3 plausible Layer B visual/design-system directions.
3. Select exactly one Layer A style/execution reference.
4. Select exactly one Layer B brand/design-system reference.
5. Extract concrete decisions:
   - color tokens or palette
   - typography
   - spacing
   - layout grammar
   - component anatomy
   - interaction states
   - motion rules

Do not copy logos, trademarked assets, brand-specific copy, or private data from references.

## Implementation

- Build or identify reusable primitives before product screens.
- Compose product screens from primitives.
- Avoid generic flat UI output.
- Use `../frontend/scripts/search-uiux-db.mjs` when palette, font pairing, layout, chart, or UX heuristic lookup helps.
- Use `../frontend/scripts/capture-browser.mjs` for browser screenshot evidence when the project lacks its own capture tool.

## Completion Gate

- [ ] Design source or lightweight implementation notes identified.
- [ ] Tokens/source styles identified.
- [ ] Primitives or existing components identified.
- [ ] Mobile/tablet/desktop QA completed.
- [ ] Relevant interaction states checked.
- [ ] Accessibility checks completed.
- [ ] Browser screenshot evidence recorded.
- [ ] No generic flat output.
