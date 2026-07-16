---
name: vibe-notion
description: Manage Notion pages, databases, blocks, users, and comments with the Vibe Notion CLI.
version: 1.10.0
allowed-tools: Bash(vibe-notion:*)
metadata:
  openclaw:
    requires:
      bins:
        - vibe-notion
    install:
      - kind: node
        package: vibe-notion
        bins: [vibe-notion]
---

# Vibe Notion

Use the Vibe Notion CLI for every Notion operation. It supports the unofficial
private API as the signed-in user; `vibe-notionbot` uses the official API as an
integration.

## Rules

- Never call Notion's internal API directly or use another Notion client.
- Never write scripts to automate Notion. Use `vibe-notion batch` for bulk work.
- Read before modifying; make the smallest requested change; then verify it.
- Do not expose or save tokens, credentials, or page contents in persistent
  memory.

## Choose the CLI

Use `vibe-notion` when the Notion desktop app is installed and signed in. It
extracts `token_v2`, acts as the user, and supports rows, views, and workspace
listing. Use `vibe-notionbot` only when a `NOTION_TOKEN` integration token is
available and the desktop app is not.

If neither is available, ask the user to set one up. If `vibe-notion` is not
installed, ask which package runner to use (`npx`, `bunx`, or `pnpm dlx`) unless
the user's preference is known.

## Persistent Memory

Use the Obsidian note
[`memory/vibe-notion/MEMORY.md`](obsidian://open?vault=brain&file=memory%2Fvibe-notion%2FMEMORY.md)
in vault `brain` as persistent memory.

Use it as a reusable lookup index, not an activity log.

At the start of each Notion task, run:

```sh
obsidian vault=brain read path="memory/vibe-notion/MEMORY.md"
```

If the note does not exist, proceed without it. Create or update it only for:

- **Stable index:** workspace and database IDs, aliases, schema or hierarchy,
  reusable conventions, and durable user preferences.
- **Recurring context:** a project, hub, parent page, or view explicitly marked
  ongoing or reused in a later independent task. Retain it only when future use
  is likely and rediscovery is expensive or ambiguous.

An explicit request to remember something, use it by default, or treat it as
ongoing qualifies it for storage. Creation or discovery alone does not.

Do not store individual tasks or pages, generated children, search results,
temporary views, block IDs, or anything used only by the current request.

Keep the note in this structure:

```markdown
## Stable Index

### Workspaces
### Databases
### Aliases
### Conventions

## Recurring Context

- `<id>` — `<short label>`
  - Why retained: `<ongoing use>`
  - Last verified: `YYYY-MM-DD`
  - Remove when: `<completion or invalidation condition>`
```

Store IDs and short labels only—never credentials or page content. Update a
recurring entry's verification date when used. Remove it when its removal
condition is met or it becomes stale or inaccessible. Never add task history.

## Workflow

1. Load persistent memory and use a known, verified ID when available.
2. Resolve missing context with the narrowest read command: `workspace list`,
   `workspace resolve`, `search`, `page get`, `database get`, `database query`,
   `block get`, or `block children`.
3. For mutations, use the matching CLI command. Prefer `page properties` when
   content blocks are unnecessary, and use `--backlinks` for reverse relation
   lookups.
4. Verify the resulting page, properties, blocks, rows, or view configuration.
5. Update the Obsidian memory note only when the result meets the retention
   criteria above. Prune a relevant entry when the task proves it stale or its
   removal condition has been met.

Pass `--workspace-id` when listing, searching, creating at the workspace root,
or when the target cannot resolve its workspace. Targeted operations usually
auto-resolve it. Use `--pretty` for human-readable inspection; commands emit
JSON by default.

## Mutations and Bulk Work

Use the command family that owns the resource:

- `page`: list, get, properties, create, update, archive
- `database`: get, query, create, update, add-row, update-row, views
- `table`: create, add-row, update-cell, delete-row
- `block`: get, children, append, update, delete, upload, move
- `comment`: list, create, get

For more than one independent mutation, use `batch`. For dependent operations,
use multiple batches: create resources first, then reference their returned IDs.
Stop and report the failure when a batch fails; do not retry blindly.

Use `--after` or `--before` when insertion position matters. Use a temporary
markdown file only through a CLI `--markdown-file` option, not through a custom
automation script.

## Reference Material

- [Block and rich-text JSON](references/block-types.md)
- [Batch operation format and rate-limit strategy](references/batch-operations.md)
- [Common task patterns](references/common-patterns.md)
- [Output shapes and `$hints`](references/output-format.md)

Run `vibe-notion --help` or `<command> --help` for current syntax. If
authentication extraction fails while the desktop app is open, ask the user to
quit Notion completely and retry `vibe-notion auth extract --debug`.
