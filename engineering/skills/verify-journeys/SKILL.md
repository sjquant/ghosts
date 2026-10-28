---
name: ghosts:verify-journeys
description: Verify real user journeys through an app, CLI, or service and report observable outcomes, evidence, and coverage gaps.
disable-model-invocation: true
---

Verify the user's target through real public interfaces. Ground commands, selectors, and prerequisites in the repository. Ask only for prerequisites the repository cannot establish.

## Scope

Map the requested journeys before execution; default to the primary 3–5 features, or all if fewer. Identify the primary runtime, existing harnesses, entry points, material sub-features, prerequisites, actions, expected outcomes, contractual side effects, isolation constraints, and auth, platform, or harness limitations. Name omitted surfaces; one entry point does not prove others. Keep unrelated product fixes out of scope.

## Scenarios

Use Specification by Example with Gherkin Given/When/Then acceptance scenarios: reuse existing `.feature` files or create them in the repository's verification location. Derive observable expected outcomes from requirements; assign stable, unique scenario tags. Use Scenario Outlines with Examples for equivalent cases and record results per example. Keep commands, selectors, and setup recipes in the harness or execution notes. Cucumber and step definitions are optional; a written scenario is not verification.

```gherkin
Feature: Language settings
  @journey-language-change
  Scenario: Language changes apply without restarting
    Given the service is running with Korean selected
    When the user changes the language to English through the settings API
    Then the next response is in English without restarting the service
```

## Execution

- **Launch:** prefer documented commands; confirm the checkout builds and starts. Perform setup, migrations, seed data, auth, and startup from an empty scratch data directory; confirm usable readiness. Build short-lived CLIs once and drive each in an isolated session. State unsupported fresh-start conditions and precise blockers.
- **Doctor:** a read-only check of instance ownership, build identity, readiness, and auth. Run before driving and after unexpected behavior; reset or relaunch when process health cannot detect a broken UI state.
- **Drive:** outside-in journeys through public interfaces with real stable selectors or commands. Reuse existing harnesses before adding helpers. State isolation requirements for ports, profiles, and data; do not double-drive an instance that cannot be isolated.
- **Evidence:** name the oracle and artifact location. Capture actions and resulting state, including contractual side effects. Internal setters, test-only endpoints, and a final screenshot alone do not prove a journey. Mock only at existing external boundaries. Observe dry-run side effects before relying on it. Keep credentials out of files and artifacts.
- **Cleanup:** remove only owned instances, scratch state, and marked temporary scaffolding, including failed-attempt residue; never kill by process name. Retain evidence outside cleanup targets and confirm it survives cleanup.
- **Helpers:** add only helpers that improve reproducibility; make scripts executable and record their invocation.

Execute each mapped journey end to end. Missing prerequisites block the affected journey without weakening its oracle. Clean up failed attempts, correct verification setup errors, and rerun affected steps; report product failures without fixing unrelated code.

## Results

Keep mapped, exercised, passed, failed, and blocked coverage distinct; report remaining gaps. One passing journey does not prove full coverage. For surrogate environments, record setup differences, target-only prerequisites, and untested behavior; a surrogate pass does not verify the target.

Write a separate YAML report per run outside cleanup targets. Include the environment, commands and actions performed, and one result per scoped scenario or example linked by tag and source file. Use `passed`, `failed`, `blocked`, or `not_run`; include reasons for failures, blockers, and omissions, and evidence locations for executed scenarios. For example:

```yaml
environment: local checkout, isolated scratch data
execution: artifacts/run-001/actions.log
results:
  - scenario: journey-language-change
    source: features/settings.feature
    status: passed
    evidence:
      - artifacts/run-001/language-change.log
```
