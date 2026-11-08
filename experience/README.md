# Harvest / Curate / Recall

Three agent skills for extracting, curating, and recalling engineering experience,
supported by a Python 3.10+ standard-library helper for mechanical collection and validation.
The calling agent performs extraction, evidence checks, and curation; the helper
never calls an LLM or decides whether a lesson is true.

## Setup

1. Copy `assets/config.example.json` to a personal location (e.g. `~/.config/experience.json`).
2. Fill in `vault` (path to Obsidian vault) and `library` (path to Git knowledge repository).
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

- **Codex**: `$harvest`, `$curate`, `$recall`
- **Claude Code & Antigravity**: `/harvest`, `/curate`, `/recall`

## Usage

### 1. Harvest (Extract Experience)
Ask the agent to harvest recent sessions (e.g. "harvest last 7 days" or "harvest last 30 days").
Under the hood, the helper collects local session packets and writes candidate notes to Obsidian:
```sh
python3 experience/skills/harvest/scripts/experience.py collect --days 7 > /tmp/packet.json
python3 experience/skills/harvest/scripts/experience.py save --packet /tmp/packet.json --decisions /tmp/decisions.json
```
Use `--dry-run` to inspect without modifying files.

### 2. Curate (Refine into Knowledge)
Ask the agent to curate pending candidates:
- Reads candidate notes from Obsidian inbox.
- Rejects generic truisms and tutorial rules.
- Translates verified project lessons into Markdown documents and updates `INDEX.md`.
- Generates a local Git diff or branch for PR review.

Validate the inbox and library structure at any time:
```sh
python3 experience/skills/harvest/scripts/experience.py validate /path/to/vault/inbox /path/to/library
```

### 3. Recall (Consult Prior Experience)
Read-only skill. When explicitly requested or when checking team conventions:
- Progressively opens `INDEX.md` → topic index → relevant document.
- Injects only relevant constraints into context without loading the entire library.

## Testing

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s experience/skills/harvest/tests -v
```
