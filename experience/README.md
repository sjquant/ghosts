# Harvest / Curate / Recall

Three independent agent skills for extracting, curating, and recalling experience,
supported by a Python 3.10+ standard-library helper for mechanical collection and validation.
An automated agent run performs extraction, evidence checks, and curation; the helper
never calls an LLM or decides whether a lesson is true. Routine operation is unattended.

## Setup

1. Copy `skills/harvest/assets/config.example.json` to a personal location (e.g. `~/.config/experience.json`).
2. Fill in `vault` (path to Obsidian vault) and `library` (absolute path to the knowledge directory).
   - Recall includes its own [library](skills/recall/library/INDEX.md). For curate, set `library` to the absolute path of the copy you want to update, such as an installed recall skill's `library/` directory.
   - If using GitHub reviews, set `github_login` and add repositories or organizations to the allowlist.
   - Run `gh auth login` for GitHub access (no tokens in config).
3. Set the environment variable:
   ```sh
   export EXPERIENCE_CONFIG=~/.config/experience.json
   ```

### Installation

Install via `skul` (recommended):
```sh
npx @solaqua/skul@latest add --global sjquant/ghosts --include experience/skills/harvest experience/skills/curate experience/skills/recall
```

Or link directly to your agent's skills directory:
```sh
ln -s "$(pwd)/experience/skills/harvest" ~/.agents/skills/
ln -s "$(pwd)/experience/skills/curate" ~/.agents/skills/
ln -s "$(pwd)/experience/skills/recall" ~/.agents/skills/
```

## Automated operation

An external scheduler or event-driven runner invokes the installed skills through
the chosen agent. Set the config path, source interval and credentials in that
runner's environment. Configure the schedule separately; installing a skill does
not register a job. Run harvest, then curate after a successful or partially
successful harvest. The runner must invoke an agent: the Python helper alone
does not extract or curate knowledge. Serialize jobs that share a Vault or Git
working tree. Missing configuration, access failures and deferred candidates go
in the run report; jobs never wait for interactive answers.

### 1. Harvest (Extract Experience)
The job supplies a 7-day, 30-day or explicit interval. The agent reads collected
records, compares independent user corrections across tasks, and saves recurring
decision criteria as candidates. A copied review or repeated instruction is not
an independent occurrence; isolated fixes are not extracted. Helper calls inside the job:
```sh
python3 experience/skills/harvest/scripts/experience.py collect --days 7 > /tmp/packet.json
python3 experience/skills/harvest/scripts/experience.py save --packet /tmp/packet.json --decisions /tmp/decisions.json
```
Use `--dry-run` for automated previews without writes or checkpoints.

### 2. Curate (Refine into Knowledge)
The job processes pending candidates:
- Reads candidate notes from Obsidian inbox.
- Rejects isolated fixes, generic truisms and tutorial rules.
- Verifies repeated user choices in independent contexts and preserves contrary evidence.
- Translates verified project lessons into Markdown documents and updates `INDEX.md`.
- Generates a local Git diff, or creates a PR when `create_pr` is enabled. Never auto-merges.
- Defers unsupported or conflicting rules as `review`, reports the missing decision, and continues other candidates.

Recall's bundled library contains generalized judgments, not private project records.
Candidate IDs refer back to the private Obsidian Vault for original evidence.
Local proposals remain `proposed` until accepted-branch verification; recall must
distinguish those proposals from accepted knowledge.

The job validates the inbox and library before recording its outcome:
```sh
python3 experience/skills/harvest/scripts/experience.py validate /path/to/vault/inbox /path/to/library
```

### 3. Recall (Consult Prior Experience)
Read-only skill intended to trigger before substantive implementation, refactoring,
test writing, code review, or document drafting and revision, even when the
approach seems straightforward, and when the user refers to previous feedback:

- Checks the relevant index without requiring an unresolved decision. Skips mechanical edits and reuses guidance already checked in the current task.
- Opens its bundled `library/INDEX.md` → work-domain index → relevant document. A presentation task does not read engineering topics; domains without curated guidance return no match.
- Injects only relevant constraints into context without loading the entire library.
- Proceeds without recall when the library is unavailable or no topic matches.

The library travels with the recall skill. It does not depend on a ghosts checkout
or other installed skills. Curate creates a domain folder and index when relevant
knowledge is ready; empty writing/presentation folders are not required.

## Testing

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s experience/skills/harvest/tests -v
```
