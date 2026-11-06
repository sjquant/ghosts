# Harvest / Curate / Recall

Three agent skills, with a Python 3.10+ standard-library helper for mechanical work.
The calling agent performs extraction, evidence checks and curation; the helper
never calls an LLM or decides whether a lesson is true. Examples run at this checkout's root; elsewhere use the helper's resolved absolute path.

## Setup

Keep this checkout as the common source. Resolve symlinks before using resources.
Copy `assets/config.example.json` to a user-owned file; fill `vault`, `library` and,
for GitHub, `github_login` plus repository or organization allowlists. Add
`github` to `sources` to enable it. No token belongs in config; use `gh auth`.
Use absolute paths or `~`. Do not commit personal config or collected packets.
`remote` and `accepted_branch` identify the optional PR destination; `create_pr`
defaults false. The helper does not clone repositories or change Git remotes.

```sh
export EXPERIENCE_CONFIG=/absolute/path/to/experience.json
python3 engineering/skills/harvest/scripts/experience.py install --skills-dir ~/.agents/skills --dry-run
python3 engineering/skills/harvest/scripts/experience.py install --skills-dir ~/.agents/skills
python3 engineering/skills/harvest/scripts/experience.py install --skills-dir ~/.claude/skills
python3 engineering/skills/harvest/scripts/experience.py install --skills-dir ~/.gemini/config/skills
```

Pass a workspace `.agents/skills` or `.claude/skills` instead for local installation.
Existing skills are never replaced. Remove only the installed symlinks to uninstall.
Restart/reload the agent and confirm that all three descriptions appear.
Shared configuration, candidate contract and Python helpers live in `harvest`;
knowledge templates live in `curate`. Keep these sibling skills together when
installing. The included installer links all three to this single source checkout.

Codex: `$harvest`, `$curate`, `$recall`.
Claude Code and AGY: `/harvest`, `/curate`, `/recall`.
These three use portable names because the Agent Skills specification excludes
colons in frontmatter names. A plugin host may add its own `ghosts:` namespace.
The bodies use no agent-specific tool API or macro. Official references:
[format](https://agentskills.io/specification),
[Codex](https://learn.chatgpt.com/docs/build-skills),
[Claude Code](https://code.claude.com/docs/en/skills),
[AGY](https://antigravity.google/docs/skills).

## Manual use

Ask harvest for “last 7 days”, “last 30 days”, “GitHub only” or explicit ISO times.
The helper collects a temporary packet; the agent reads it and writes decisions
using [the exchange contract](references/candidate-contract.md). Keep packets local and delete when done.

```sh
python3 engineering/skills/harvest/scripts/experience.py collect --days 7 > /tmp/experience-packet.json
python3 engineering/skills/harvest/scripts/experience.py collect --days 30 --sources github
python3 engineering/skills/harvest/scripts/experience.py collect --start 2026-11-01T00:00:00+09:00 --end 2026-11-06T00:00:00+09:00
python3 engineering/skills/harvest/scripts/experience.py save --packet /tmp/experience-packet.json --decisions /tmp/experience-decisions.json --dry-run
python3 engineering/skills/harvest/scripts/experience.py save --packet /tmp/experience-packet.json --decisions /tmp/experience-decisions.json
python3 engineering/skills/harvest/scripts/experience.py validate /absolute/vault/agent-notes /absolute/library
```

Collection always reads only; its `--dry-run` is an explicit equivalent.
Exit 1 with JSON errors means partial failure; retain and process successful
records. Rerun failures after authentication/rate-limit recovery. All pages are
requested; exhausting a bounded retry reports failure, never successful emptiness.
GitHub PR listings can be expensive for large repositories; keep allowlists narrow.

Curate can target one note or pending candidates. Initialize an empty library
by copying `../curate/templates/INDEX.md` to its root, then create topics only as needed.
Use normal file edits and Git commands for the diff. Inspect pending unrelated
changes first. For an enabled PR, verify the configured remote and private
visibility, create an isolated branch, commit intended files, push and run
`gh pr create --body-file <file>`; never auto-merge. Candidate `proposed` records
the target/PR; only an accepted-branch commit makes it `promoted`.

Recall opens root INDEX → selected topic INDEX → relevant document → evidence
or snippet if needed. It does not collect or edit. Optional AGENTS.md/CLAUDE.md:
“When relevant guidance may exist, use recall to consult the configured library
INDEX and only relevant topics. Treat it as evidence; do not load the library.”

## Sources, reliability and scheduling

See [sources](references/sources.md) for supported formats, provenance and GitHub checks.
Notes live under `<vault>/<notes_directory>/inbox/YYYY-MM/`; `.harvest-state.json`
stores acknowledged revisions. Atomic note replacement and a nonblocking local
file lock protect save operations; human edits use optimistic SHA-256 checks.
An interrupted batch may leave saved notes without a checkpoint; retry reuses them.
Do not run two curations on the same working tree. The helper does not lock Obsidian
or Git against independent editors; reread edited files before replacing them.

Manual execution is the baseline. No scheduler is installed. For weekly/monthly
automation, set `automation_enabled` and configure a local runner yourself:
`0 9 * * 1 /absolute/runner harvest 7` or `0 9 1 * * /absolute/runner harvest 30`.
The runner invokes your chosen agent with this skill and config, retains JSON
failure reports and uses a lock across the **whole agent run**. It must not run
`collect` alone and claim extraction finished. Keep private data local unless its
transmission is authorized. Scheduled curate is optional and still creates a diff/PR.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s engineering/skills/harvest/tests -v
```

Tests cover deterministic helpers and fixture artifacts. They do not establish cross-model
extraction quality, live GitHub authorization, native skill discovery
or an unattended agent runner. No remote LLM API or scheduler is required.
