---
name: frontend
description: "Umbrella router for frontend, web UI, UX, visual design, styling, redesign, React setup, design QA, performance, accessibility, screenshots, Figma exports, generated mockups, and any visible UI change. Routes by work mode to ui-design-to-code, ui-greenfield, or ui-redesign when available. Keeps fallback references, scripts, and browser QA gates for standalone use."
disable-model-invocation: true
---

# Frontend

Use this as the umbrella router. Prefer a specialized skill when available; otherwise use the fallback references and scripts below.

## Routing Priority

1. Concrete visual reference, Figma, screenshot, mockup, source capture, annotated packet, or designer spec exists -> `ui-design-to-code`.
2. New UI with no concrete visual reference -> `ui-greenfield`.
3. Existing UI redesign from a designer's perspective -> `ui-redesign`.

State the selected route and loaded references in one sentence before implementation.

## Design Source

Use the most authoritative available source:

1. Figma design system, variables, components, or tokens.
2. Existing repo tokens, components, theme, or shared CSS.
3. Existing `DESIGN.md`.
4. Newly created lightweight implementation notes.

`DESIGN.md` is one possible design contract, not the default source of truth.

## Fallback References

| Request involves | Read |
|---|---|
| Any UI implementation, styling, redesign, mockup, or visual decision | `references/design/README.md` |
| Writing or modifying frontend code, performance, SEO, accessibility, or quality | `references/perfection/README.md` |
| Screenshot, Figma export, generated mockup, annotated reference, source-site capture | `references/design/image-to-code-skill.md` + `references/visual-qa/reference-fidelity.md` |
| Looking up palettes, font pairings, layouts, chart styles, UX heuristics | `references/ui-ux-db/README.md` |
| Personas, cognitive accessibility, design critique, design debt, handoff, synthetic user testing | `references/design-ops/README.md` |
| React project setup or React UI work | `references/design/react-dev-tooling-skill.md` |

For implementation fallback work, load design and perfection together.

## Fallback Workflow

Use this only when specialized skills are unavailable:

1. Identify the work mode: design-to-code, greenfield, or redesign.
2. Identify the authoritative design source.
3. Read the smallest reference set that covers the work.
4. Create lightweight implementation notes when no source exists.
5. Build or identify reusable primitives before product screens.
6. Verify in a real browser before completion.

## Shared Fallback Rules

- Every color, font size, spacing value, radius, shadow, material, and motion rule traces to the selected design source or implementation notes.
- Concrete references must match pixels, copy, component structure, and responsive intent unless the user accepts a deviation.
- References are source material, not mood labels.
- Do not weaken UX, hide content, simplify interactions, or flatten material to improve scores.
- Use SVG icon sets or real assets, not emojis as icons.
- Animate with `transform`, `opacity`, and `filter`; avoid layout animation.
- Verify final UI in a real browser at mobile, tablet, and desktop widths, including relevant states.

## Quick routes

| Request | Load |
|---|---|
| "Build a landing page" with no direction | `ui-greenfield` or `design/README.md` + `design/_INDEX.md` shortlist -> one Layer A + one Layer B + `perfection/README.md` |
| "Premium SaaS hero like Stripe" | `design/README.md` + `design/taste-premium.md` + `design/brand-stripe.md` + `perfection/README.md` |
| "Linear-style product page" | `design/README.md` + `design/taste-minimal.md` + `design/brand-linear.md` + `perfection/README.md` |
| "Developer tool, dark, code-first" | `design/README.md` + `design/taste-premium.md` + `design/brand-supabase.md` or `brand-vercel.md` + `perfection/README.md` |
| "Redesign this existing dashboard" | `ui-redesign` or `design/README.md` + existing design source + `perfection/README.md` |
| "Build this screenshot / Figma / mock exactly" | `ui-design-to-code` or `design/README.md` + `design/image-to-code-skill.md` + `visual-qa/reference-fidelity.md` + `perfection/README.md` |
| "Audit my site" / "make this faster" | `perfection/README.md` + browser evidence |
| "Find a palette / font pairing" | `ui-ux-db/README.md` |
| "Add personas/accessibility/debt/handoff" | `design-ops/README.md` + `design/README.md` |

## Completion Gate

Do not report completion until all applicable items are true:

- [ ] Work mode selected before UI code.
- [ ] Required references loaded.
- [ ] Design source or lightweight implementation notes identified.
- [ ] Tokens/source styles identified.
- [ ] Component primitives defined before product screens.
- [ ] Required states implemented.
- [ ] Real browser QA run after the final edit.
- [ ] Mobile/tablet/desktop captures exist or a limitation is explicitly stated.
- [ ] Reference-fidelity QA run if concrete reference exists.
- [ ] No screenshot-as-background shortcut.
- [ ] No generic flat output.
- [ ] Performance/accessibility not sacrificed.
- [ ] Evidence paths are recorded.
