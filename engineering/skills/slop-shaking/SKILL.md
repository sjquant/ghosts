---
name: ghosts:slop-shaking
description: Use when the user asks to remove slop, mentions $slop-shaking, or asks whether code, documents, presentations, HTML, or UI contain unnecessary content, structure, or complexity.
---

Review the artifact or change specified by the user; otherwise use the work being discussed. Identify its audience, purpose, and intended behavior or message. For code, inspect callers and tests. For documents and presentations, inspect the surrounding narrative and rendered layout when available. For HTML and UI, inspect the rendered surface and relevant user flows when available; state when visual or interaction checks are unavailable.

Judge each element by whether it helps the user understand, decide, or act. Remove or combine elements that add no useful contribution or duplicate another element. Reduce the user's total reading, reasoning, and interaction burden; fewer elements alone are not the goal. Preserve necessary behavior, information, navigation, accessibility, and meaningful risk coverage. Do not hide necessary information or controls if doing so makes tasks harder.

Give one general subagent the artifact, relevant context, and this prompt. Use only the checks relevant to the artifact:

```text
Review the artifact or change read-only:

AI-generated work can overcomplicate simple problems and overfill documents and interfaces. Look for omissions, combinations, or simpler designs that reduce the intended audience's burden while preserving the artifact's purpose. Do not force every artifact through every checklist or invent findings to justify a cleanup.

For code:
- Any low-value, duplicate, implementation-shaped, or one-off tests—including those that only recheck documented dependency guarantees—that can be removed or combined without losing meaningful behavior, edge-case, or risk coverage? Any tests for hypothetical concurrency or timing risks without a credible execution path or meaningful failure impact?
- Any unnecessary variables or intermediate state that can be omitted, inlined, or reused without obscuring intent?
- Any unnecessary interfaces or abstractions? Would omission, existing code reuse, standard features, or a different design solve the same problem more simply from the caller's perspective? Any internal state, lifecycle, ordering, or retry details that callers must coordinate but the module could hide?

For documents and presentations:
- Any headings, subheadings, sections, introductions, conclusions, summaries, or footers that repeat information or add structure without helping readers navigate or understand?
- Any exhaustive details, boilerplate, or explanations that do not support the audience's purpose? Can they be removed, combined, or moved to a reference or appendix without making the main material harder to use?
- Any slides or visual elements that duplicate a message, compete with the main point, or fragment a coherent explanation? Preserve necessary evidence, citations, and useful context.

For HTML and UI:
- Any cards, containers, borders, badges, labels, helper text, buttons, or repeated instructions that add visual or cognitive burden without helping the user complete a task?
- Any unnecessary options, implementation details, or intermediate states exposed to users? Can sensible defaults, existing controls, or progressive disclosure simplify the flow without adding excessive clicks or hiding important choices?
- Does each proposed removal preserve discoverability, navigation, accessibility, feedback, and recovery from errors? Judge the whole flow, not just how sparse one screen looks.

Report findings with locations, evidence, and the smallest useful cleanup. Say when no useful cleanup is found.
```

After the subagent responds, judge each suggestion: does it reduce the user's burden, or merely remove useful context or shift complexity elsewhere? Apply supported cleanups within the requested scope and run relevant checks. For code, verify affected behavior; for documents and presentations, check meaning and layout; for HTML and UI, check affected flows and rendered states when available. If asked for review only, report without editing. Leave the artifact unchanged when no useful cleanup remains.

Report in the user's language. For a small cleanup, briefly explain what was removed or combined, why, and how it was checked. Mention rejected suggestions only when their tradeoff helps explain the outcome. If there are no findings, say so.

For multiple findings that benefit from comparison, or when the user requests a structured report, use the format below. Use `PROPOSED` for review-only findings, `BLOCKED` for unresolved cleanups, and `SKIP` for rejected suggestions worth explaining. Locations can be file lines, document sections, slide numbers, or UI screens and elements; use commit-pinned permalinks for GitHub targets.

```markdown
## Findings

### <APPLIED|PROPOSED|BLOCKED|SKIP> - <title>

- Location: <file and line, section, slide, or UI element>
- Kind: <test|variable|interface|content|structure|visual|interaction>
- Evidence / rule: <concrete evidence and the cleanup criterion>
- Change / reason: <what changed or is proposed, or why it was blocked or skipped>
```
