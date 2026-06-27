---
name: frontend
description: "Use for frontend, web UI, UX, visual design, styling, redesign, React setup, design QA, performance, accessibility, screenshots, Figma exports, generated mockups, and any change to visible UI. Routes design, perfection, visual-qa, ui-ux-db, and design-ops references. Requires DESIGN.md before UI code, browser evidence before completion, and reference-fidelity QA when a concrete visual reference exists."
---

# Frontend

Route frontend work to the smallest reference set that covers the request. State the loaded references in one sentence before implementation.

## Completion Standard

A UI is complete only when it:

- follows `DESIGN.md`
- runs in a real browser
- passes responsive and state QA
- preserves accessibility and performance
- avoids generic flat output

Correct-but-flat is a failure.

## Route Before UI Work

| Request involves | Read |
|---|---|
| Any UI implementation, styling, redesign, mockup, or visual decision | `references/design/README.md` |
| Writing or modifying frontend code, performance, SEO, accessibility, or quality | `references/perfection/README.md` |
| Screenshot, Figma export, generated mockup, annotated reference, source-site capture | `references/design/image-to-code-skill.md` + `references/visual-qa/reference-fidelity.md` |
| Looking up palettes, font pairings, layouts, chart styles, UX heuristics | `references/ui-ux-db/README.md` |
| Personas, cognitive accessibility, design critique, design debt, handoff, synthetic user testing | `references/design-ops/README.md` |
| React project setup or React UI work | `references/design/react-dev-tooling-skill.md` |

For implementation work, load design and perfection together.

## Design Workflow

Choose one branch before editing UI code:

1. **Concrete visual reference:** screenshot, generated mockup, Figma export, overview, source-site capture, or annotated packet. Treat it as the visual contract. Load `references/design/image-to-code-skill.md`, relevant design/perfection files, and `references/visual-qa/reference-fidelity.md`. Extract tokens, geometry, copy, spacing, states, and responsive intent into `DESIGN.md`. QA actual captures against the reference and implementation quality.
2. **Greenfield or fresh setup:** no concrete reference. Use `references/design/_INDEX.md` to shortlist 2-3 Layer B references. Load exactly one Layer A style reference and one Layer B brand/design-system reference. Extract tokens, layout grammar, component anatomy, states, motion, and taste decisions into `DESIGN.md`. Do not copy logos, trademarked assets, or brand-specific copy.
3. **Existing project with `DESIGN.md` or components:** read and follow the existing system. Update it only when the request needs a new token, primitive, state, motion rule, accessibility rule, accepted debt, or reference-fidelity requirement.
4. **Existing UI with no design system:** ask whether to preserve the current look with nearby edits or extract `DESIGN.md` and reusable components first.

## Shared axioms

- `DESIGN.md` exists before new components.
- Every color, font size, spacing value, radius, shadow, material, and motion rule traces to `DESIGN.md` or the existing system.
- A concrete reference must match pixels, copy, component structure, and responsive intent unless the user accepts a deviation.
- References are source material, not mood labels.
- Do not weaken UX, hide content, simplify interactions, or flatten material to improve scores.
- Use SVG icon sets or real assets, not emojis as icons.
- Animate with `transform`, `opacity`, and `filter`; avoid layout animation.
- Verify final UI in a real browser at mobile, tablet, and desktop widths, including relevant states.

## Quick routes

| Request | Load |
|---|---|
| "Build a landing page" with no direction | `design/README.md` + `design/_INDEX.md` shortlist -> one Layer A + one Layer B + `perfection/README.md` |
| "Premium SaaS hero like Stripe" | `design/README.md` + `design/taste-premium.md` + `design/brand-stripe.md` + `perfection/README.md` |
| "Linear-style product page" | `design/README.md` + `design/taste-minimal.md` + `design/brand-linear.md` + `perfection/README.md` |
| "Developer tool, dark, code-first" | `design/README.md` + `design/taste-premium.md` + `design/brand-supabase.md` or `brand-vercel.md` + `perfection/README.md` |
| "Improve this existing dashboard" | `design/README.md` + existing `DESIGN.md` or stop for extraction decision + `perfection/README.md` |
| "Build this screenshot / Figma / mock exactly" | `design/README.md` + `design/image-to-code-skill.md` + `visual-qa/reference-fidelity.md` + `perfection/README.md` |
| "Audit my site" / "make this faster" | `perfection/README.md` + browser evidence |
| "Find a palette / font pairing" | `ui-ux-db/README.md` |
| "Add personas/accessibility/debt/handoff" | `design-ops/README.md` + `design/README.md` |

## Completion Gate

Do not report completion until all applicable items are true:

- [ ] Correct branch selected before UI code.
- [ ] Required references loaded.
- [ ] `DESIGN.md` created or updated.
- [ ] Tokens trace to references or existing system.
- [ ] Component primitives defined before product screens.
- [ ] Required states implemented.
- [ ] Real browser QA run after the final edit.
- [ ] Mobile/tablet/desktop captures exist or a limitation is explicitly stated.
- [ ] Reference-fidelity QA run if concrete reference exists.
- [ ] No screenshot-as-background shortcut.
- [ ] No generic-default drift.
- [ ] No flat expressive surface.
- [ ] Performance/accessibility not sacrificed.
- [ ] Evidence paths are recorded.
