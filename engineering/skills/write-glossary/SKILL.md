---
name: write-glossary
description: Create or update a project's GLOSSARY.md with precise definitions and canonical terminology. Use when the user asks to write a glossary, document project vocabulary, or revise existing definitions.
disable-model-invocation: true
---

# Write Glossary

Write a glossary that gives the project a shared vocabulary. Capture the
meaning of terms; keep implementation choices and decision rationale in
their own documents.

## Gather context

Read the relevant discussion, documentation, and existing glossary. Inspect
code when it helps establish how a term is currently used. Distinguish current
usage from an intended definition; surface material contradictions instead of
silently treating either as authoritative.

Choose a canonical term for each concept. If a word names several concepts,
separate their definitions and make their scope clear. Ask only when the
available context cannot resolve a distinction that changes the meaning.
Do not invent agreement or turn unresolved terminology into a settled entry.

## Write

Save a new glossary to the path the user supplies; otherwise use
`/tmp/write-glossary-<safe-project-slug>.md`, appending a timestamp when needed
to avoid a collision. This default applies even when the repository already
has a glossary. When the user asks to revise a specific glossary, edit that
file. Create a repository directory only when the user specifies it as the
destination. Write once there is a resolved term to record. A single glossary
can group terms by area and qualify names whose meaning varies by area.

Follow an established document format when one exists. Otherwise use
[templates/glossary.md](templates/glossary.md). Write in the user's language
and preserve canonical names used by the project.

- Keep each definition to one or two sentences explaining the concept and
  the boundary that distinguishes it from nearby concepts.
- Include vocabulary with a specific meaning in this project. Omit generic
  programming definitions unless the project gives them a distinct meaning.
- List competing names under `_Avoid_` when they refer to the same concept or
  would mislead readers. Omit the line when there are none.
- Group entries only when it helps readers find or distinguish terms.
- Keep schemas, algorithms, storage choices, and decision histories out of
  glossary entries. Include conceptual relationships only when they clarify
  the definition.

Update the relevant entries without rewriting unrelated content. This skill
produces the glossary; it does not rename code or create decision records.

## Verify and deliver

Reread the definitions without the preceding conversation. Check that each
term has a clear meaning within its stated scope, nearby concepts remain
distinct, and no entry presents an unresolved assumption as fact.

Report the file path, the vocabulary added or changed, and any unresolved
definitions left out.
