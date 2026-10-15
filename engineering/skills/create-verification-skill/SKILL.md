---
name: ghosts:create-verification-skill
description: Create or repair a project-local skill for verifying real user journeys through an app, CLI, or service.
disable-model-invocation: true
---

Create a project-local verification skill for an agent reading it cold. Follow the repository's skill conventions; otherwise use `.agents/skills/verify-<app>/`. Ground commands, selectors, and prerequisites in the repository; leave no placeholders. Ask only for prerequisites the repository cannot establish.

Identify user-facing surfaces, the primary runtime, existing harnesses, observable outcomes, and isolation constraints. Prefer documented startup commands. Establish that the checkout builds and starts; report blockers precisely rather than inventing a working recipe. Keep unrelated product fixes out of scope. Mark any temporary verification scaffolding and include its removal in cleanup.

Write `SKILL.md` with YAML `name` and an activation `description` naming the app and surface. Include these executable sections:

- **Launch:** exact setup, migrations, seed data, auth, startup, and usable readiness from an empty scratch data directory. Build short-lived CLIs once and drive each in an isolated session; state unsupported fresh-start conditions explicitly.
- **Doctor:** a read-only check of instance ownership, build identity, readiness, and auth. Run before driving and after unexpected behavior; reset or relaunch when process health cannot detect a broken UI state.
- **Drive:** outside-in journeys through public interfaces with real stable selectors or commands. Reuse existing harnesses before adding helpers. State isolation requirements for ports, profiles, and data; do not double-drive an instance that cannot be isolated.
- **Evidence:** name the oracle and artifact location. Capture actions and resulting state, including contractual side effects. Internal setters, test-only endpoints, and a final screenshot alone do not prove a journey. Mock only at existing external boundaries. Observe dry-run side effects before relying on it. Keep credentials out of files and artifacts.
- **Cleanup:** remove only owned instances and scratch state, including failed-attempt residue; never kill by process name. Retain evidence outside cleanup targets.
- **Helpers:** ship only helpers that improve reproducibility; make scripts executable and document their invocation.

Create `features/README.md` as an index and `features/<feature>.md` per mapped user-facing feature. Start with the primary 3–5 features, or all if fewer; name omitted surfaces in the index. Each feature file contains:

- **Entry points:** sub-features, user-visible routes or commands, and prerequisites.
- **Journeys:** exact harness actions for each distinct entry point and material sub-feature.
- **Oracles:** observable outcomes, side effects, and evidence locations per journey.
- **Gotchas:** auth, seed-data, platform, and harness limitations.

Keep mapped, exercised, passed, failed, and blocked coverage distinct. A convenient entry point does not prove the others. Missing prerequisites block the affected journey; record the reason without weakening its oracle.

Dogfood the generated instructions end to end: launch, doctor, one complete mapped journey, evidence capture, cleanup, and confirmation that evidence survives. One journey validates the recipe, not the whole feature map. Clean up each failed attempt, repair recipe defects, and rerun affected steps.

For surrogate environments, record setup differences, target-only prerequisites, and untested behavior; a surrogate pass does not verify the target. Report the skill path, exact coverage and evidence, and remaining gaps. If the end-to-end run is blocked, label the skill a draft. Keep the feature map and harness aligned when routes, commands, or prerequisites change.
