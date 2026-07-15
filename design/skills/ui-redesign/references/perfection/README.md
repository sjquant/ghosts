# Perfection Ruleset

Use for any frontend code implementation, performance, SEO, accessibility, Core Web Vitals, or quality audit.

## Principle

Performance and visual quality are both required. Do not weaken UX or flatten the surface to buy points.

## Required checks

- real browser render
- responsive screenshots
- console errors
- layout shift
- keyboard focus
- hover/active states
- loading/empty/error states when applicable
- accessibility
- performance budget when applicable

## Performance rules

Do:

- optimize images
- use responsive assets
- lazy-load non-critical visuals
- keep animations GPU-composited
- reduce layout shift
- keep semantic HTML
- preserve material depth

Do not:

- remove animations just to improve score
- hide content
- flatten visual material
- replace UI with static screenshots
- remove interaction states
- ship inaccessible colors

## Completion

If browser execution is impossible, state why and list what would be checked.
