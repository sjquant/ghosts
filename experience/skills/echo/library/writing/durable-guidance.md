---
title: "Write guidance around the reader’s current decision"
scope: "global"
status: "proposed"
confidence: "high"
candidate_ids: ["candidate-91e3e891e9f6eec5c3e2a791", "candidate-81dda8089bc1dd947703ce07", "candidate-f8f9ce35851fd3a721658a63"]
---

# Write guidance around the reader’s current decision

When writing a policy, operating guide, README, or reusable knowledge document, keep only the rules and usage instructions that future readers need to operate or use the system.

## Keep change-specific notes in the PR description

Do not create or expand repository documentation (`docs/`, `README.md`, or runbooks) for one-off migration queries, rollout steps, external data provenance, or implementation details that only matter during code review or deployment. Put those operational and review notes in the pull request description instead.

When a change updates ongoing product or operational policy, update the canonical policy document in the same change—written as the current rule rather than a changelog entry.

## State current rules, not migration history

Define unfamiliar domain terms and write conditions and cause-and-effect relationships in complete sentences when compressed noun labels hide them.

### Before

```text
Legacy records were backfilled during the migration.
```

### After

```text
The recorded amount can differ from the amount actually billed. Check the
billing report when reconciling a payment.
```

The reusable caveat and next action survive; the completed migration history does not help the reader decide.
