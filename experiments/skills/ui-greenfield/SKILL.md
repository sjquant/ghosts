---
name: ui-greenfield
description: "Experimental frontend skill for new UI work without a concrete visual reference: apps, pages, landing pages, flows, and component systems. Uses the most authoritative available design source or lightweight implementation notes. Requires browser QA evidence."
disable-model-invocation: true
---

# UI Greenfield

Use for new UI from scratch when the user does not provide a concrete visual reference.

## Inputs

Identify:

- product context
- target audience
- ambition lane
- available design source, if any

Design source priority:

1. Figma design system, variables, components, or tokens.
2. Existing repo tokens, components, theme, or shared CSS.
3. Existing `DESIGN.md`.
4. Newly created lightweight implementation notes.

If no source exists, create lightweight implementation notes before UI code.

Use `templates/DESIGN.md` only when a full design contract is useful or explicitly requested.

## References

When using references:

1. Read `references/design/_INDEX.md`.
2. Shortlist 2-3 plausible Layer B visual/design-system directions.
3. Select exactly one Layer A style/execution reference from `references/design/taste-*.md`.
4. Select exactly one Layer B brand/design-system reference from `references/design/brand-*.md`.
5. Extract concrete decisions:

- color tokens or palette
- typography
- spacing
- layout grammar
- component anatomy
- interaction states
- motion rules

Do not copy logos, trademarked assets, brand-specific copy, or private data from references.

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
- `references/ui-ux-db/README.md`
- `references/ui-ux-db/palettes.csv`
- `references/ui-ux-db/font-pairings.csv`
- `references/ui-ux-db/ux-guidelines.csv`
- `templates/DESIGN.md`

## Implementation

- Build or identify reusable primitives before product screens.
- Avoid generic flat UI output.
- Use `scripts/search-uiux-db.mjs` when palette, font pairing, layout, chart, or UX heuristic lookup helps.
- Capture browser evidence with the project's tooling; if none exists, use `scripts/capture-browser.mjs`.

## Responsive Spacing QA

If responsive spacing changes, inspect desktop and mobile screenshots before completion.

Check:

- spacing rhythm at desktop and mobile widths
- visible alignment across neighboring sections and repeated components
- hidden overflow, clipping, and accidental scroll
- real content density, not empty or idealized states

For report spacing/layouts:

- inspect wrapper, card, and table borders together
- avoid double outlines and cramped nested surfaces
- do not squeeze multiple wide tables into columns

Scripts included:

- `scripts/search-uiux-db.mjs`
- `scripts/capture-browser.mjs`

Evidence must record:

- route/page
- viewport size
- state captured
- screenshot path
- command or tool used

## Completion Gate

- [ ] Design source or lightweight implementation notes identified.
- [ ] Tokens/source styles identified.
- [ ] Primitives or existing components identified.
- [ ] Mobile/tablet/desktop QA completed.
- [ ] Desktop and mobile spacing screenshots checked.
- [ ] Alignment, overflow, and report density checked.
- [ ] Relevant interaction states checked.
- [ ] Accessibility checks completed.
- [ ] Browser screenshot evidence recorded.
- [ ] No generic flat output.
