# Design Reference Router

Route UI work to the minimum design references needed, then convert them into `DESIGN.md` before implementation.

## Standard

Done means the UI has:

- a clear visual intent
- coherent tokens
- reusable primitives
- complete states
- responsive behavior
- accessibility
- real-browser evidence

For expressive briefs, include dimensional material: depth, light, hierarchy, and motion. Correct-but-flat is a failure.

## Reference layers

### Layer A - Style

Load one:

- `taste-default.md` - operational, neutral, utility-first UI.
- `taste-premium.md` - premium, glossy, startup-grade, brand-grade UI.
- `taste-minimal.md` - editorial, quiet, precise, restrained UI.
- `taste-experimental.md` - cinematic, high-variance, Awwwards-like UI.

### Layer B - Brand / design-system reference

Load one for most greenfield work:

- `brand-linear.md` - precise productivity software.
- `brand-stripe.md` - premium SaaS/fintech polish.
- `brand-supabase.md` - dark developer tool, code-first, emerald depth.
- `brand-vercel.md` - monochrome platform UI, sharp typographic discipline.

## Branches

### 1. Concrete visual reference

If the user provides a screenshot, Figma export, generated mock, source-site capture, or annotated packet, load `image-to-code-skill.md` and `../visual-qa/reference-fidelity.md`. Treat the reference as a contract.

### 2. Greenfield or fresh setup

If there is no concrete visual reference:

1. Read `_INDEX.md`.
2. Decide ambition: operational or expressive.
3. Shortlist 2-3 Layer B references.
4. Pick exactly one Layer A and one Layer B.
5. Extract their actual design decisions into `DESIGN.md`.
6. Define reusable primitives and states before product screens.

### 3. Existing system

If `DESIGN.md`, tokens, components, or a design system exists, read it first. Update it only when the requested work needs new tokens, primitives, states, motion, accessibility constraints, or accepted debt.

### 4. Existing UI without a design system

Stop and ask: preserve the current look with copy-nearby edits, or extract a real `DESIGN.md` and reusable primitives first? Do not silently choose.

## Ambition routing

| Brief signal | Lane | Default route |
|---|---|---|
| internal tool, admin, dashboard, usable | operational | `taste-default.md` + existing system or neutral Layer B |
| premium, glossy, beautiful, startup-grade, brand-grade | expressive | `taste-premium.md` + high-craft Layer B |
| Linear-like, Notion-like, editorial, quiet | minimal | `taste-minimal.md` + `brand-linear.md` |
| Stripe-like, fintech, polished SaaS | expressive | `taste-premium.md` + `brand-stripe.md` |
| devtool, code-first, dark platform | expressive/devtool | `taste-premium.md` + `brand-supabase.md` or `brand-vercel.md` |
| wow, cinematic, Awwwards | experimental | `taste-experimental.md` + high-craft Layer B |

Do not let an expressive brief fall through to the safe default.

## DESIGN.md Requirements

Before UI code, `DESIGN.md` must name:

- visual intent
- references loaded
- atmosphere
- signature material
- color story and ramp
- typography
- spacing
- radius
- shadow/depth/material
- motion
- component primitives
- variants and states
- responsive behavior
- accessibility constraints
- accepted design debt

## Expressive Material

For expressive briefs, verify:

1. Hero focal object: real light, shadow, gradient, depth; not flat circles or rounded rectangles.
2. Atmosphere: layered light, gradient, glow, band, image, or depth; not one flat fill.
3. Surface material: a repeatable recipe, not a single blur.
4. Color: perceptual ramp, not one brand hex at varied opacity.
5. Interaction: visible hover and active states; one signature interaction for hero/primary CTA.

## Design QA checklist

- [ ] `DESIGN.md` exists.
- [ ] All visual values trace to `DESIGN.md`.
- [ ] Fonts actually load.
- [ ] Color ramp is used, not a single tint.
- [ ] Required states are implemented.
- [ ] Mobile/tablet/desktop layouts work.
- [ ] No horizontal overflow.
- [ ] Motion is smooth and GPU-composited.
- [ ] Expressive surfaces are dimensional.
- [ ] The hero has a memorable focal moment.
- [ ] Real browser screenshots exist.
