---
name: ghosts:explain-diff
description: Explain a PR, diff, branch, or code change read-only through public-interface behavior, before/after usage examples, and compatibility impact, in the style of release notes; optionally create a visual HTML lesson.
disable-model-invocation: true
---

Explain the change like release notes for someone who uses the affected interfaces. Keep the target read-only: do not modify repository files, execute target code, or publish release notes, PR edits, or comments. Write in the user's language; default to Markdown, with a visual HTML lesson or quiz when requested.

## Scope

Use the supplied PR, diff, branch, or code target; otherwise use the current branch's diff against its base, including uncommitted changes. Ask only if the target or base cannot be established. Inspect the complete final diff and enough before/after definitions, callers, tests, and documentation to establish the observable contract. Treat PR descriptions and commit messages as context, not proof of behavior.

## Explanation

- Lead with what changes for callers or users through the public interface: API, CLI, UI, configuration, file format, or protocol. Group by capability or contract rather than changed files or commit history. Include relevant defaults, errors, side effects, and compatibility changes.
- Show a minimal before/after usage example for each materially changed public interface, including concrete inputs or actions and observable results. For additions or removals, show the supported usage and explain what became available or is no longer supported.
- Put code and text-based requests and responses in fenced code blocks, not inline fragments. For UI changes, show the interaction and resulting state.
- Use real interface names and supported syntax from the relevant revision. Label illustrative data, pseudocode, and unexecuted examples; do not invent prior capabilities or imply examples were run.
- Explain who is affected, why the change matters, and any required caller changes. Include implementation details only to explain an observable guarantee, limitation, or tradeoff. For internal-only changes, state their purpose and whether observable behavior changes; do not invent user benefits or deployment status.
- Use a table or compact diagram only when clearer than prose or a usage example. Keep it understandable through public interfaces without knowledge of internal collaboration.
- Link substantive claims and snippets to code or test evidence with file/line references; use commit-pinned permalinks for GitHub targets. Separate established behavior from inference and unknowns; state material limits of the supplied diff or available evidence.

Cover every material contract change, including removals and breaking changes. Keep the explanation proportional to the change; omit empty sections and file inventories. This is an explanation, not a code review or a release announcement.

## Visual lesson

After the Markdown explanation, ask whether the user wants a visual HTML version, unless visualization was already requested or declined.

When requested, create a self-contained, snippet-led HTML lesson at an ELI5 level: assume no knowledge of the domain, use everyday language and few words, and explain unfamiliar terms on first use. Lead with one sentence about what changes for the reader.

- For each material change, show a short plain-language takeaway, a minimal before/after usage snippet, and the observable result with the same concrete input or action. Put the snippets at the center of the page, with a brief caption explaining what to notice. For additions or removals, show the available usage and state what became possible or stopped working; do not invent a before/after example.
- Prefer short, focused snippets, usually 3–8 lines each. Include only the context needed to understand or use the changed interface; split longer examples into small steps. For UI changes, use concrete actions and resulting states. Keep real interface names and supported syntax, label illustrative or unexecuted examples, and retain source links.
- Keep the main reading path understandable from the takeaways, snippets, and results alone. State required caller changes, breaking changes, and important limitations plainly beside the relevant example. Put optional implementation details and deeper explanations in `details`.
- Use a large, simple diagram only when it makes an example easier to understand. Avoid architecture tours, file inventories, dense prose, and decorative diagrams. Include a table of contents only when it helps navigate a longer lesson.
- If a quiz is requested, include five beginner-level interactive multiple-choice questions about the shown examples, with short feedback in everyday language. Avoid unexplained terminology and implementation trivia.

- Write one responsive HTML file outside the repository as `/tmp/YYYY-MM-DD-explanation-<slug>.html`; return its absolute path. Use semantic headings, inline CSS/JavaScript, and no network assets.
- Make visuals readable without zooming, with accessible text, sufficient contrast, keyboard controls, visible focus, and feedback beyond color. Preserve code whitespace in `<pre><code>` blocks.
- Verify links, code blocks, material-change coverage, accessibility, any quiz interactions, and artifact existence before delivery. Check that each main example makes sense to a beginner without opening technical details.
