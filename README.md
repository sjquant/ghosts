# ghosts

Reusable agent skills and reviewers.

Default bias: delete needless layers, reuse what exists, and keep the smallest
safe instruction that preserves the behavior.

## Install

Install all skills globally for your agent:

```sh
npx @solaqua/skul@latest add --global --agent codex sjquant/ghosts --all
```

Replace `codex` with the name of the agent you use, if different.

## Bundles

- `engineering/`: implementation, planning, review, and collaboration skills
  with their reviewers.
- `research/`: bounded, evidence-grounded research and explanation skills.
- `writing/`: writing, rewriting, and change-explanation skills.
- `tools/skills/`: directly maintained tool-integration skills, including
  `vibe-notion`.
- `registry/`: external skill references that are not maintained in this
  repository.

## Upstream sources

| Local component | Upstream | Pinned revision | License |
| --- | --- | --- | --- |
| `writing/skills/humanize-korean/references` | [`epoko77-ai/im-not-ai`](https://github.com/epoko77-ai/im-not-ai), `skills/humanize-korean/references` | [`9747f03`](https://github.com/epoko77-ai/im-not-ai/tree/9747f036cdc28a1a8aea4dc71fef1f7846eb96f7) | MIT |
| `tools/skills/vibe-notion` | [`devxoul/vibe-notion`](https://github.com/devxoul/vibe-notion), `skills/vibe-notion` | [`89c6643`](https://github.com/devxoul/vibe-notion/tree/89c6643cebb4e4c56bbde826b6557da77f9d9d2f) | MIT, declared in the upstream README |

The vendored Vibe Notion skill includes an `UPSTREAM.md` file with its source
path and maintenance notes.

The standalone `humanize-korean` skill selectively syncs applicable rules from
the upstream revision above. Upstream orchestrator, plugin, and agent-runtime
paths are intentionally excluded.
