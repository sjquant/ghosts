# Source support and evidence

## Sessions

| Source | Reader | Limit |
| --- | --- | --- |
| Codex | `sessions/**/*.jsonl`, `archived_sessions/**/*.jsonl` | Reads user/assistant messages and tool outputs from `response_item` |
| Claude Code | `projects/**/*.jsonl`, including subagents | Reads user/assistant text and tool results, not hidden reasoning |
| AGY | `brain/*/.system_generated/logs/transcript.jsonl` | User/model content only; opaque `.pb`/`.db` without transcript reported unsupported |

Readers use message timestamps, not file modification times. Intervals are
start-inclusive/end-exclusive and require timezones. Missing roots, malformed
JSONL and unsupported conversation stores are explicit errors. A malformed file
is retried as a whole; other files continue. Agent log formats are undocumented
local formats that may change. An empty log is not proof that all history exists.
Do not infer repository scope from a folder name; inspect the session's actual
work context and use the real `owner/repo` when assigning a candidate's scope.

Each record preserves role, timestamp and line locator; AGY's path supplies its
session ID. Messages outside the interval are omitted, so fetch surrounding
context directly from the local file when necessary. A shifted interval may
re-evaluate overlap; stable candidate keys prevent duplicate notes. Acknowledging
an unchanged revision suppresses repeated processing. A changed revision is
re-evaluated, with prior notes protected from silent overwrite.

Unknown schemas must be reported rather than treated as support. These readers
do not reconstruct deleted, remote-only, compacted or encrypted history. Check
source coverage in the report before claiming completeness.

## GitHub

Use authenticated `gh` with read access only for harvest. Never store tokens.
Configured repositories and organizations bound collection; organization access
does not grant permission to send private source text elsewhere. Private knowledge
repositories are the default; check visibility before any push.

The helper reads paginated inline comments and submitted review bodies. It filters
by configured login and excludes PRs authored by that login. Empty feedback and
simple approval messages are omitted; the agent excludes other low-value text.
Inline source timestamps are `updated_at`; review bodies use the available
`updated_at` or `submitted_at`. Edits to an old review body without an edit
timestamp may fall outside the window. Deleted/undisclosed edits cannot be reconstructed.

Every harvested review starts with `adoption: unverified`. Before promoting:

- Fetch the PR and original comment/review using its URL/ID.
- Read replies with `gh api --paginate repos/OWNER/REPO/pulls/NUMBER/comments`
  and discussion with `gh api --paginate repos/OWNER/REPO/issues/NUMBER/comments`.
- Compare the reviewed commit and subsequent commits at the cited path, using
  `gh api repos/OWNER/REPO/compare/OLD...NEW` or a local checkout. Account for
  renames, changed context and code unrelated to the comment. Large API diffs may
  be truncated; use the checkout rather than claim complete verification.
- Identify the actual fix or explicit confirmation. Record rejection, disagreement
  or uncertainty. A merged PR, resolved thread or “approved” status is insufficient.

Model messages that say “fixed” are also claims, not independent verification.
Read actual tests/output/code or qualify them. Preserve source IDs and minimal
evidence in notes; do not duplicate entire transcripts or diffs into the library.

The helper retries rate-limit/server errors a bounded number of times, then
reports failures. It does not sleep through an arbitrary rate-limit reset.
Successful source records survive other failures and can be acknowledged normally.
