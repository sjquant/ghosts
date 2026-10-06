---
name: write-adr
description: Create or revise Architecture Decision Records (ADRs) that explain a decision, its context, and its rationale. Use when the user asks to document a decision about architecture, technology, infrastructure, security, engineering practices, or domain design.
disable-model-invocation: true
---

# Write ADR

Record a decision so a future reader can understand what was chosen and why.
ADRs can cover system structure, technology, deployment, security, engineering
practices, or domain boundaries. A glossary or domain-modeling session is not
a prerequisite.

## Gather context

Read the relevant discussion, existing ADRs, and supporting documentation or
code. Identify the decision, the constraints that shaped it, the reason for
the choice, and any material trade-off.

Separate a proposal from an agreed decision, and an agreed decision from its
implementation. Code can show what exists; it does not establish the original
rationale. Do not invent alternatives, evidence, or agreement. Ask only when
a missing choice or reason prevents an accurate record; otherwise state
material uncertainty explicitly.

## Write

Save a new record to the path the user supplies; otherwise use
`/tmp/write-adr-<safe-decision-slug>.md`, appending a timestamp when needed to
avoid a collision. This default applies even when the repository already has
an ADR directory. Create a repository directory only when the user specifies
it as the destination.

When the user asks to revise a specific record, edit that file. When saving a
new record to a user-specified ADR directory, follow its filename conventions;
if it uses sequential numbers, take the highest existing number plus one.
Do not renumber records or overwrite an unrelated file.

Follow an established document format when one exists. Otherwise use
[templates/adr.md](templates/adr.md). Write in the user's language. A title
and one short paragraph are sufficient when they explain:

- the situation or constraint that required a choice;
- the chosen approach and its scope;
- the reason for choosing it, including the key accepted trade-off.

Add only what helps a future reader assess the decision:

- **Status:** distinguish a proposal, an accepted decision, or a retired or
  replaced record when that distinction matters. Use `proposed` for an
  unsettled choice; do not mark it accepted without evidence of agreement.
- **Considered options:** explain alternatives actually considered when their
  rejection is worth preserving.
- **Consequences:** state material costs, limits, or downstream effects that
  the short paragraph cannot explain clearly.

Keep one decision per record. Edit an existing record for corrections or
clarifications when requested. When a new decision replaces an accepted one,
write a new ADR and link to the earlier record to make the replacement clear.
Update the earlier record only when requested. Documenting a decision does
not implement it or establish that implementation is complete.

## Verify and deliver

Reread the record without the preceding conversation. Check that the choice,
scope, rationale, and decision state are understandable, claims match the
available evidence, and referenced files or records exist.

Report the file path, the recorded decision, and any open questions or
proposal status.
