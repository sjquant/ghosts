---
name: ghosts:ui-design
description: Establish a new UI or redesign's visual direction through references and mockups, record it in DESIGN.md, and optionally implement it. Skip routine UI fixes with a settled design.
---

Explore visual directions with the user, refine their choice, and record it in `DESIGN.md`. Implement when requested.

Read the request and existing interface, design documentation, tokens, and components. Identify the primary user flow, target screens, and constraints. Ask only for missing decisions that would change the design.

## Choose reference themes

Identify the screen pattern and the decisions references should inform: for a dashboard, this may include chart types, metric hierarchy, filters, and drill-downs. Start with supplied references. Search image-led galleries such as Pinterest, Behance, and Dribbble for visual mood, using the screen type plus varied style terms; include comparable interfaces from other industries. Use the available browser skill to inspect the actual images. Search live products when interaction or information structure needs validation. Prefer freely viewable interface screens with enough detail to judge the target task; discard ads and decorative images that hide the interface. Use separate references for screen structure and visual treatment when one image cannot provide both; do not import a mobile layout into a desktop design. Gather many varied, relevant candidates; the four-mockup default does not limit reference collection. Avoid duplicates and unrelated examples collected only for visual variety. Reference assets are not automatically licensed for reuse.

Download reference images, using the available browser skill to visit pages and retrieve them when needed. Build and open a local HTML gallery with images grouped by theme, numbered candidates, and source links. For each candidate, explain the comparable UI pattern, the visual or interaction choice it illustrates, and the decision or tradeoff it helps the user make. Recommend the strongest candidates for the brief. Verify that the images display; use accessible previews or screenshots when downloads are unavailable. Ask the user which themes or references to explore; they may choose several. Wait for their choice unless they already supplied it or delegated the decision.

## Explore and refine

Use Codex's built-in `imagegen` skill to create four directions by default; increase or decrease the count only when the user requests it. Before generating, give each direction a distinct visual theme and reference anchor from the selected material. Vary the visual language, typography, palette, and composition while keeping the same representative screen, realistic content, and viewport. Do not send the same reference set and visual brief to every call by default. If the selection is too narrow for four distinct directions, ask whether to broaden it. Generate each separately, passing its selected reference images as actual image inputs through the tool's supported mechanism; viewing them beforehand or describing them in text is not sufficient. Identify each image's role and the qualities to draw from it, adapting them to the target content and flow rather than reproducing the source screen. If the tool is unavailable or cannot receive the references, continue with the selected reference images without extra approval or a CLI/API fallback; label them as references and explain their application to the target screen.

Judge each direction before presenting it:

- Does it support the primary task and preserve required content and behavior? Check any numbers, units, and time spans against the task's rules.
- Does it reflect the chosen qualities of the references while fitting the target task? Compare the images directly; correct unexplained drift without requiring an exact match.
- Does it offer a distinct theme through layout, typography, palette, and density, rather than small variations of one design?
- Can its responsive behavior, interaction states, and accessibility work beyond the image?

Show numbered images, explain each direction's tradeoff, recommend one, and ask what to keep or change. Wait for the user's choice, then refine until they confirm the direction. Pass the selected mockup as the edit target when refining it and preserve accepted elements; without image generation, refine the references and proposed adaptations. A theme already settled by the user needs no new selection; otherwise skip theme or mockup selection only when the user explicitly delegates that choice or asks to skip it. A general request to make an app authorizes implementation after selection, not bypassing selection.

## Document and implement

Record the agreed design in `DESIGN.md`. When creating it, use [the template](references/design-template.md); when updating it, preserve the existing structure except source-attribution entries. Keep reference names and website URLs in the HTML gallery; put only the adopted design decisions and selected local preview in `DESIGN.md`. Record any viewport or container breakpoints where layout, navigation, or content changes, including the threshold and change. Fold confirmed feedback into the relevant rules as work continues, keeping the document current rather than appending a feedback log. Distinguish unresolved decisions. Save project-referenced generated images in the workspace under the `imagegen` save policy.

After writing `DESIGN.md`, ask whether to build the interface with its tokens and components. Wait unless implementation was already requested. Tokens and components support the working interface; they are not a separate default deliverable.

Implement from `DESIGN.md`, reusing existing conventions and foundations. Prefer suitable headless components for interactive behavior, styled to the chosen direction; retain suitable existing components and native controls. Build only what the requested screens need. Compute domain values from application data rather than copying labels from generated images. Check the rendered result across target viewports and around any recorded breakpoints, plus keyboard access and relevant states. Report delivered paths and checks actually performed; visual approval is not usability validation.
