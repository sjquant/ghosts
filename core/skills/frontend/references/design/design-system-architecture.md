# Design System Architecture

`DESIGN.md` is the implementation contract. UI code may not introduce visual values outside `DESIGN.md` or the existing design system.

## Required sections

1. Intent
2. References loaded
3. Visual direction
4. Tokens
5. Component primitives
6. Layout grammar
7. Responsive behavior
8. Accessibility
9. Accepted design debt
10. QA matrix

## Token rules

Token or name every:

- color
- typography
- spacing
- radius
- border
- shadow
- material recipe
- motion duration/easing
- z-index/layering
- breakpoint behavior

No orphan hex values or magic pixel values. Add needed values to `DESIGN.md` first.

## Component primitive rules

Build primitives before product screens. A primitive is required when a pattern repeats or represents a system concept.

Each primitive must define:

- purpose
- variants
- default state
- hover state
- active/pressed state
- focus-visible state
- disabled state
- loading state when applicable
- empty state when applicable
- error state when applicable
- accessibility notes
- motion notes
- responsive behavior

## Product screen rules

Product screens compose primitives.

Allowed:

- local composition
- content-specific layout
- screen-specific imagery
- documented one-off when `DESIGN.md` records accepted debt

Not allowed:

- new ad-hoc colors
- new ad-hoc shadows
- new button style without primitive update
- screenshot-as-background
- hardcoded layout that cannot adapt

## Existing project rule

If the project already has tokens/components, prefer them. Update them only when the requested outcome requires a new visual capability.

## Showcase requirement

Before final screens, build a component showcase or state harness for new primitives. Show variants and states at mobile, tablet, and desktop widths.
