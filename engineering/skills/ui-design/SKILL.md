---
name: ghosts:ui-design
description: Establish a new UI or redesign's visual direction through references and mockups, record it in DESIGN.md, and optionally implement it. Skip routine UI fixes with a settled design.
---

Explore visual directions with the user, refine their choice, and record it in `DESIGN.md`. Implement when requested.

Read the request and existing interface, design documentation, tokens, and components. Identify the primary user flow, target screens, and constraints. Ask only for missing decisions that would change the design.

Find and inspect references matching the product and mood. Use supplied references first; otherwise search Pinterest, Lapa Ninja, Behance, or relevant live products, preferring freely viewable examples. Gather many varied, relevant candidates; the four-mockup default does not limit reference collection. Favor breadth without padding the selection with duplicates. Use accessible alternatives when blocked; reference assets are not automatically licensed for reuse.

Download reference images, using the available browser skill to visit pages and retrieve them when needed. Build and open a local HTML gallery with the images grouped by theme, numbered candidates, source links, and brief notes on qualities to adapt. Verify that the images display; use accessible previews or screenshots when downloads are unavailable. Ask the user to choose a theme or combine qualities from several references before generating mockups. Wait for their choice unless they already supplied a settled theme or delegated the decision.

Use Codex's built-in `imagegen` skill to create four directions based on the selected theme by default; increase or decrease the count only when the user requests it. Generate each separately using the same screen, realistic content, and viewport. If the tool is unavailable, continue with the selected reference images without extra approval or a CLI/API fallback; label them as references and explain their application to the target screen.

Judge each direction before presenting it:

- Does it support the primary task and preserve required content and behavior?
- Does it offer a meaningful choice in layout, typography, or density, rather than just a palette swap?
- Can its responsive behavior, interaction states, and accessibility work beyond the image?

Show numbered images, explain each direction's tradeoff, recommend one, and ask what to keep or change. Wait for the user's choice, then refine until they confirm the direction. Preserve accepted elements; without image generation, refine the references and proposed adaptations. Honor requests to choose autonomously or build directly.

Record the agreed design in `DESIGN.md`. When creating it, use [the template](references/design-template.md); when updating it, preserve the existing structure. Fold confirmed feedback into the relevant rules as work continues, keeping the document current rather than appending a feedback log. Distinguish unresolved decisions. Save project-referenced generated images in the workspace under the `imagegen` save policy.

After writing `DESIGN.md`, ask whether to build the interface with its tokens and components. Wait unless implementation was already requested. Tokens and components support the working interface; they are not a separate default deliverable.

Implement from `DESIGN.md`, reusing existing conventions and foundations. Prefer suitable headless components for interactive behavior, styled to the chosen direction; retain suitable existing components and native controls. Build only what the requested screens need. Check the rendered result, responsive behavior, keyboard access, and relevant states. Report delivered paths and checks actually performed; visual approval is not usability validation.
