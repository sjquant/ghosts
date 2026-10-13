---
name: ghosts:make-skill
description: Create or revise an agent skill with the fewest instructions needed to preserve its intended behavior.
disable-model-invocation: true
---

Read the request, target skill, and nearby conventions. Ask only when a missing decision would change behavior. Write `SKILL.md` in the requested location or the repository's skill structure.

Put activation in the frontmatter description and the main action first in the body. Keep every detail that changes the result; remove everything that does not. Preserve required inputs, outputs, constraints, and edge cases. Prefer a direct instruction or an `Any ...?` question over a procedure. Keep examples or references only when they resolve ambiguity. Do not add invented requirements, mandatory logs, checklists, or diagrams.

- Any intended behavior lost or changed?
- Any unnecessary rule, repetition, or explanation?
- Any instruction whose input, action, or result remains unclear?

If yes, make the smallest repair and recheck. Otherwise finish. Return the skill path and a brief description of its purpose.
