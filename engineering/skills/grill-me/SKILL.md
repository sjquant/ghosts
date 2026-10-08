---
name: ghosts:grill-me
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking or asks to be grilled.
---

Interview the user relentlessly until you reach a shared understanding. Map
this as a design tree: every decision branches into the decisions that depend
on it.

Work the tree in rounds. The frontier is every decision whose prerequisites
are already settled: questions you can ask now without guessing at answers you
have not heard yet. Ask the whole frontier in one round, number each question,
and give your recommended answer. Then wait for the user's answers.

Format a round like this:

```md
❓ **Q1** - **<Question title>**: <Question, with choices when useful>

➡️ <Recommended answer>

---

❓ **Q2** - **<Question title>**: <Question, with choices when useful>

➡️ <Recommended answer>
```

Each round reshapes the tree. Settled decisions unblock their dependent
questions; recompute the frontier and ask the next round. A question depending
on another question still open in this round belongs to a later round.

Finding facts is your job, never the user's. When a question needs a fact from
the environment, dispatch a subagent to find it. A running exploration is an
unsettled prerequisite: only downstream questions wait; ask the rest of the
frontier now. The decisions are the user's: put each to them and wait.

The session is done when every branch within scope is resolved and nothing
remains silently assumed. An empty frontier while research is pending is not
completion. Do not act until the user confirms the shared understanding.

Present the result using this template in the user's language. Replace
placeholders, repeat decision groups as needed, and omit constraints when none:

```md
## Outcome

<Agreed goal and direction in 1–2 sentences>

## Decisions

### <Related decision group>

- <Agreed choice and its key reason or accepted trade-off>

## Constraints

- <Material scope boundary or constraint>

Does this capture our shared understanding?
```

Keep it readable in one screen without scrolling. Include only what someone
needs to understand the result; omit the interview transcript, question IDs,
and full decision tree. Use a compact table or diagram only when it makes the
decisions easier to understand.
