# React Development Tooling Gate

Use this for React, Next.js, Remix, Vite, or component-heavy frontend tasks.

## Required checks

Before completion, verify the changed UI in the project's actual runtime whenever possible:

- dev server boots
- route renders
- console has no relevant errors
- hydration succeeds
- interaction states work
- keyboard focus works
- no obvious layout shift
- no horizontal overflow

## Recommended tools

Use existing project tools. Do not add dependencies for ceremony.

Helpful tools:

- Playwright for browser automation
- Storybook or local component showcase for primitive states
- React DevTools / profiler when performance or rerender behavior matters
- accessibility checkers where available

## Component-first workflow

For new UI systems:

1. Build primitives.
2. Render states in showcase.
3. QA states.
4. Compose product screens.
5. QA screens.

Do not build product screens from one-off classes and retrofit components later.
