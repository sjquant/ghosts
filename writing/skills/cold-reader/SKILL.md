---
name: cold-reader
description: Draft or revise PR descriptions, ADRs, design documents, implementation plans, review responses, and other engineering artifacts for readers who did not participate in the preceding conversation. Do not use for casual conversation, ordinary code comments, or documents explicitly intended to rely on linked prior context.
---

# Cold-Reader Writing

Create engineering writing that its intended readers can understand without access to the private conversation that produced it.

“Context-free” means independent of preceding conversation context. It does not mean explaining every repository convention, avoiding technical language, or writing for a complete beginner.

## Conversation context

Treat the preceding conversation as private working context, not as context automatically available to the reader.

Notice claims, decisions, exclusions, and shorthand whose meaning depends on that conversation. Restore only the premises materially necessary for the intended reader to understand the artifact.

Do not expose the conversation itself, reproduce every considered alternative, or add background that does not serve the artifact’s purpose.

## Intended reader

Infer the artifact’s intended readers and calibrate the explanation to their likely domain and repository knowledge. Follow any audience the user explicitly identifies.

Do not assume readers participated in the design discussion. Also do not treat experienced project reviewers as beginners or explain familiar concepts without a reason.

When the audience is unclear, write for a technically capable teammate who knows the repository but is unfamiliar with the specific domain or decision.

## Technical language

Preserve technical precision and use domain terminology when it helps the intended reader.

Do not use terminology as a substitute for the concrete meaning it compresses. When a term hides an important premise, failure mode, or scope boundary, make that meaning understandable in the surrounding text.

Do not mechanically remove jargon, add glossaries, expand every acronym, or make the artifact longer merely to appear accessible.

## Cold-reader review

Before delivering or publishing the artifact, reread it as if the preceding conversation were unavailable. Perform this review internally unless the user asks to see it.

Revise anything that materially depends on missing conversation context, including:

- conclusions whose premises exist only in the conversation;
- exclusions justified only as unnecessary, too complex, or not worth the cost;
- references such as “as discussed,” “the current approach,” or “this risk” without a clear referent;
- technical terms standing in for an unexplained situation;
- assumptions about environment, usage, constraints, or reader knowledge that affect the conclusion.

Preserve the user’s chosen structure, tone, and level of detail when they are specified. Otherwise choose the structure, length, and style that best fit the artifact. Do not add sections, follow a fixed template, or rewrite an existing artifact wholesale merely to demonstrate compliance with this skill.
