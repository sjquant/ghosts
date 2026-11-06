# Evaluation record

Evaluated during implementation on 2026-11-06. The unit suite exercises the
deterministic helper, not an automatic semantic extractor. The calling agent
also followed the three skill bodies in a temporary Vault and Git repository.
There was no previous version to compare and no independent model evaluation.

## Automated checks

`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s engineering/skills/harvest/tests -v`

14 tests passed. Coverage includes all three log readers, exact message intervals,
subagent attribution, changed revisions, repeat execution, empty extraction,
dry-run, partial failures, human edit conflicts, unsupported formats, redaction,
symlink escape, GitHub reviewer identity/own-PR exclusion, pagination/rate limits,
relative links, unreachable documents, oversized indexes and shared installation.
GitHub API responses are fixtures; pagination tests verify the `gh` invocation
and returned pages, not live GitHub access.

## Agent walkthrough

Input: a synthetic Codex session containing an explicit user correction that an
API replacement must preserve atomic writes, followed by a model's report that
a test passed. The existing library already had one API contract document.

1. Harvest: read the normalized record, extract one medium-confidence candidate
   and save it through the helper. The note distinguishes the explicit correction
   from the unverified model test report. No test-output verification was invented.
2. Curate: read the candidate, root INDEX and existing API contract document.
   Choose `update`, retain one knowledge document, add the partial-visibility
   example and source qualification, and improve the existing INDEX description.
   The candidate becomes `proposed`, with a target path. It is not promoted merely
   because a local diff exists.
3. Recall: for an API replacement task, read root INDEX and that one linked
   document. Return the caller-guarantee check, with its atomicity limitation.
   No evidence file or unrelated topic was needed.

Observed result: one saved candidate, two changed Git files, one knowledge
document, clean `git diff --check`, and zero note/link/line validation errors.
Additional curator input: a low-confidence candidate proposing a global lock,
with an explicit rejection due to deadlocks and no implementing patch. Compared
it with the existing caller-specific guidance, set `review` and recorded the
missing evidence. The library diff remained byte-for-byte unchanged.

Additional recall task: adjust CSS spacing. Read the root INDEX containing only
API contract guidance; found no relevant topic and opened no knowledge document.
These are implementation-agent smoke checks, not independent or cross-model
behavior guarantees. Extraction quality still needs evaluation on real usage.

## Local source probes and limits

One real local file per adapter was read successfully: Codex 17 messages,
Claude Code 3 messages, and AGY 678 messages. AGY used a May 2026 transcript;
this does not establish that recent AGY records exist. Source contents were
not copied into this repository. Opaque AGY conversations remain unsupported.

`gh auth status` returned nonzero; live review collection was not run. No personal
Vault/library destination or GitHub allowlist was supplied. Native skill discovery
in all three agent applications, real remote PR creation and an unattended runner
remain unverified. No personal skills were installed or scheduler enabled.
