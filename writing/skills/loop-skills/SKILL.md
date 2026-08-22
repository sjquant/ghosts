---
name: loop-skills
description: Simple iterative workflow for creating, reviewing, or improving agent skills.
disable-model-invocation: true
---

# Loop Skills

Create or improve an agent skill through a short loop. Keep the result small,
clear, and useful; use judgment instead of forcing a fixed template.

Before starting, create a checklist at
`/tmp/loop-skills-<safe-task-slug>.md` and update it as you work:

```text
- [ ] Understand the goal and inspect nearby skills
- [ ] Sketch the trigger, input, output, and main steps
- [ ] Choose a simple design
- [ ] Write or revise the skill
- [ ] Any material problem with scope, clarity, or usefulness?
- [ ] Fix problems and make a final check
```

## Loop

1. **Understand**

   Decide whether this is a new skill, a revision, or a review. Read relevant
   repository instructions and a few nearby skills. Ask a question only when
   the missing answer would materially change the result; otherwise make a
   reasonable assumption.

2. **Sketch**

   Write down just enough of the contract to guide the draft:

   - when the skill applies, and when it does not;
   - what it needs as input;
   - what it should do;
   - what the user should receive;
   - any important boundary or failure case.

3. **Choose**

   Prefer the smallest design that satisfies the goal. Reuse an existing skill,
   convention, reference, or tool when it already fits. Add supporting files
   only when they make the skill meaningfully clearer or more reliable.

   If the scope or design is materially uncertain, show a short plan and wait
   for approval. If the request is clear, proceed without an unnecessary gate.

4. **Write**

   Create or revise the target `SKILL.md`. Keep its frontmatter valid, its
   description specific, and its instructions direct. State important
   stopping, retry, or side-effect boundaries, but do not turn every preference
   into a hard rule. Use examples and references only when they prevent likely
   mistakes.

5. **Check and repair**

   Read the result once as a user and ask:

   ```text
   Any wrong or overly broad trigger?
   Any unclear instruction or missing input/output detail?
   Any unnecessary complexity or duplicated guidance?
   Any important failure or out-of-scope case left undefined?
   ```

   If any answer is yes, make the smallest useful repair and check again. Stop
   when the skill is clear enough to use and no remaining issue would materially
   change its behavior or usefulness.

## Final response

Lead with the result. Mention the changed path, the skill's purpose, the check
performed, and any meaningful uncertainty. Keep it brief and use the user's
language.
