---
title: "Describe occurrences without prescribing handlers"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-65cfcc9f1e91d2c2fed44737"]
---

# Describe occurrences without prescribing handlers

When an event can lead different consumers to different actions, describe what happened or was requested. Naming it after one handler's command constrains reuse and becomes misleading when another handler does something else.

These event-name fragments illustrate the choice; they do not assume an event library.

### Before

```text
reset-game → a listener refreshes account data rather than resetting the game
```

### After

```text
game-reset-requested → listeners choose the work needed for that request
```

A request occurrence is different from successful completion: `requested` does not claim that the action succeeded. A completed event should correspond to the completed action.

A command event can replace bidirectional mutation of shared arguments when a component needs to request a clear action without modifying its caller's state in both directions.
