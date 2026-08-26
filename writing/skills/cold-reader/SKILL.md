---
name: cold-reader
description: Draft or revise PR descriptions, ADRs, design documents, implementation plans, review responses, and other engineering artifacts for readers who did not participate in the preceding conversation. Do not use for casual conversation, ordinary code comments, or documents explicitly intended to rely on linked prior context.
---

# Cold-Reader Writing

Draft or revise engineering artifacts so their intended readers can understand them without access to the private conversation behind them.

Use this for PR descriptions, ADRs, design documents, implementation plans, review responses, and similar artifacts. Do not use it for casual conversation, ordinary code comments, or artifacts explicitly intended to rely on linked prior context.

## Context

Treat preceding conversation as private working context. Identify claims, decisions, exclusions, and shorthand that depend on it, then restore only the premises needed by the reader.

Do not expose the conversation, reproduce every considered alternative, or add irrelevant background.

## Audience

Infer the intended readers and calibrate the explanation to their domain and repository knowledge. Follow any audience the user specifies.

Do not assume readers participated in the design discussion or treat experienced reviewers as beginners.

When the audience is unclear, write for a technically capable teammate who knows the repository but not the specific domain or decision.

## Language

Preserve technical precision and use domain terminology when useful. This does not require explaining every repository convention, avoiding technical language, or writing for a complete beginner.

When terminology hides an important premise, failure mode, or scope boundary, make that meaning understandable in the surrounding text.

Do not mechanically remove jargon, add glossaries, expand every acronym, or lengthen the artifact merely to appear accessible.

## Cold-reader review

Before delivering or publishing, reread the artifact as if the preceding conversation were unavailable. Perform this review internally unless the user asks to see it.

Revise anything that materially depends on missing context, including:

- conclusions whose premises exist only in the conversation;
- exclusions justified only as unnecessary, too complex, or not worth the cost;
- references such as “as discussed,” “the current approach,” or “this risk” without a clear referent;
- technical terms standing in for an unexplained situation;
- assumptions about environment, usage, constraints, or reader knowledge that affect the conclusion.

Preserve the user’s chosen structure, tone, and level of detail when specified. Otherwise choose what best fits the artifact. Do not add sections, follow a fixed template, or rewrite an existing artifact wholesale merely to demonstrate compliance.
