---
name: ghosts:self-comments
description: Add concise author self-comments explaining what changed and why on non-trivial lines of a GitHub PR diff as draft pending review comments.
disable-model-invocation: true
---

Add draft pending inline review comments on a GitHub pull request to explain non-trivial changes and their rationale for the author and reviewers. Use `gh` for GitHub operations.

## Scope and selection

Use the requested PR; otherwise resolve the current branch's open PR. Ask if the target remains ambiguous. Inspect the complete diff, relevant surrounding code, and existing pending or published PR comments before choosing targets.

Comment only on non-trivial changes where the diff alone does not make the intent obvious—such as control-flow ordering, concurrency or race guards, state invariants, external library constraints, or non-obvious tradeoffs. Skip renames, formatting, boilerplate, and self-explanatory edits. Avoid duplicating existing comments on the same change.

## Comment format

Write in the user's language (using `변경점` and `이유` in Korean). Keep each comment focused without sacrificing necessary context:

- **Heading**: `### <concise purpose> (\`<symbol>\`)` — omit the symbol if there is no single symbol.
- **`변경점` (What changed)**: Explain the surrounding flow before the mechanism—state what data or action this code handles and where it applies so a reader can follow without reading surrounding files—then summarize the change at the level of intent rather than narrating the diff line by line. Put a single point inline; use nested bullets only for multiple distinct points.
- **`이유` (Why)**: State both the problem, constraint, or tradeoff the change addresses and the higher-level design reason behind the approach.

```markdown
### 리셋 도중 게임 전환 방어 (`resetDrawingTools`)
- **변경점**: 초기화 헬퍼를 `resetDrawingTools`로 합치고, `await` 전후로 `gameId` 일치 여부를 검사합니다.
- **이유**: 초기화 API 대기 중 게임이 바뀌면 새 게임의 드로잉 툴과 저장 큐가 빈 목록으로 덮어써지는 문제를 막기 위해서입니다.
```

## Publishing and safety

Add comments as **draft pending review comments** anchored to the relevant diff lines. Do not submit the pending review unless explicitly asked, and do not modify code, commit, push, edit the PR body or title, or resolve existing threads.

When re-running on an updated PR, sync your existing **pending** comments—keep valid ones, update or replace outdated ones, delete obsolete ones, and add only for newly uncovered changes—without modifying **published** or other reviewers' comments (report outdated published self-comments instead).

Report the PR link, synced pending comments with their file and symbol locations, any outdated published comments, and major skipped areas.
