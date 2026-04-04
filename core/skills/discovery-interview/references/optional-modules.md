# Optional Modules

Load this file only when the user wants to go beyond the default requirements-discovery flow.

## Product Deep Dive

Use only after the default requirements checklist is mostly complete, or when the domain clearly requires more depth.

Cover:
- data and state requirements
- roles and permissions
- policy or compliance constraints
- non-functional requirements stated in product terms
- operational workflows that affect the product experience

Keep the questions product-facing.

Examples:
- Good: "What information needs to persist between sessions?"
- Good: "Who can approve, edit, or delete this?"
- Bad: "Postgres or Mongo?"
- Bad: "Should we use RBAC middleware?"

## Research

Use when the user:
- is unsure how something should work
- asks for examples or references
- would benefit from competitor or pattern research

Possible topics:
- reference products
- workflow patterns
- domain norms or terminology
- regulations that affect product behavior

If research touches technical options, keep it descriptive unless the user explicitly opted into technical architecture.

Suggested prompt:

```text
You seem unsure about how this should work. Do you want me to research reference products or patterns before we continue?
```

After research:
1. summarize findings in plain language
2. connect them back to the user's goals
3. ask a narrower follow-up question

## Technical Architecture

Only enter this module with explicit user permission.

Trigger examples:
- "What stack should I use?"
- "Let's decide the architecture"
- "Compare Firebase vs Supabase"
- "How should this be deployed?"

When transitioning, say so clearly:

```text
We can stop here with a requirements-only spec, or continue into technical architecture and stack decisions. Which do you want?
```

If the user opts in, it is valid to cover:
- architecture options
- stack comparisons
- data model details
- infrastructure and deployment choices
- integration design

If the user does not opt in:
- do not recommend frameworks
- do not propose databases unless directly required
- do not turn scale questions into infrastructure advice
- do not add a `Technical Architecture` section to the spec

## Implementation Planning

Only enter this module after a requirements spec exists and the user asks for build planning.

Cover:
- milestone breakdown
- task sequencing
- acceptance checks
- implementation risks

Do not automatically move from requirements discovery into implementation planning.
