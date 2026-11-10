# Validation

## Deterministic helper

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s experience/skills/harvest/tests -v
```

The suite covers source readers and time intervals, fork/subagent identities,
GitHub authorship and pagination, changed revisions, repeat execution, dry-run,
partial failures, edit conflicts, redaction, path safety and Markdown navigation.
GitHub responses are fixtures. These tests verify collection and persistence,
not the agent's extraction quality. Single-correction fixtures exercise storage;
they do not justify extracting a recurring judgment from one situation.

## Semantic checks

A targeted pass over real sessions and GitHub feedback produced four patterns:
return-value meaning, responsibility boundaries, test readability and test-file
placement. Original passages and independent contexts are retained in private
Obsidian candidates. One pattern includes a contrary choice limiting its scope.

The first search missed file-placement corrections because it started with a few
anticipated themes. Discovery now inventories direct corrections before grouping.
This addresses the known omission; it does not establish exhaustive coverage or
independent model evaluation.

Check these cases when evaluating future extraction runs:

- One isolated fix produces no recurring-pattern candidate.
- A correction copied to several agents still counts as one situation.
- Independent choices sharing a trade-off retain their original passages.
- Contrary choices qualify or defer an interpretation.
- Naming and placement corrections are compared before being dismissed as cosmetic.

For recall, a matching question should open only the relevant document; a near
miss should open none. Keep the original evidence in candidates and the reusable
criterion, conditions and examples in the library.

## Limits

Local sessions and selected live GitHub comments were read, but source access
alone does not prove complete collection. Opaque AGY conversations remain
unsupported; see [source limits](../references/sources.md).
Native skill discovery across all agents, remote PR creation and an unattended
scheduler run remain unverified. No scheduler was enabled by these checks.
