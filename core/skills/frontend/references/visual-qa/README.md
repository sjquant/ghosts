# Visual QA

Visual QA checks the rendered surface. It complements code review.

## When to use

Use after the last UI edit for:

- page UI
- component UI
- terminal UI screenshots
- generated mock implementation
- screenshot/Figma/reference matching
- responsive changes
- visual redesign

## Capture matrix

Capture at minimum:

- 375px mobile
- 768px tablet
- 1280px desktop

Also capture applicable states:

- hover
- focus
- active/pressed
- disabled
- loading
- empty
- error
- modal/dropdown/open
- dark mode

## Visual QA asks

1. Does it match `DESIGN.md`?
2. Does it match the reference packet if one exists?
3. Are all states implemented?
4. Does the layout respond correctly?
5. Is there horizontal overflow?
6. Does motion feel intentional?
7. Are fonts actually loaded?
8. Are colors from the declared ramp?
9. Does the surface have depth where required?
10. Is the code reusable?

## Failure types

Both fail QA:

- Defects: clipping, wrong font, missing state, overflow, jank.
- Flatness: generic surface, no material, no focal moment, default drift.
