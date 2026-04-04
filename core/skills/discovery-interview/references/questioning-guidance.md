# Questioning Guidance

Load this file when you need help phrasing questions, handling ambiguity, or deciding how deep to go.

## Question Phrasing

- Bad: "What database do you want?"
- Good: "What information needs to be saved, and for how long?"

- Bad: "Should this use React Native or Flutter?"
- Good: "Does this need to be a native app, or is mobile web acceptable?"

- Bad: "How should we deploy this?"
- Good: "Does this need to run inside an existing environment or organization?"

## Option Design

Include at least one option that acknowledges uncertainty.

```text
options: [
  {label: "Option A", description: "Clear choice with implications"},
  {label: "Option B", description: "Alternative with different tradeoffs"},
  {label: "I'm not sure", description: "Let's explore this more"},
  {label: "Research this", description: "I'll investigate and come back"}
]
```

## Multi-select Usage

Use multi-select when clarifying:
- features
- exclusions
- stakeholder groups
- policy constraints

## Knowledge Gap Signals

| Signal | What to do |
|--------|------------|
| "I think..." or "Maybe..." | Probe deeper or offer research |
| "That sounds good" | Verify they understand the tradeoff |
| "Just simple/basic X" | Ask what simple means in practice |
| User describes a solution before the problem | Re-anchor on pain point and outcome |
| Conflicting requirements | Surface the conflict explicitly |
| "Whatever is standard" | Explain there is no universal standard |
| User asks for stack advice | Ask whether they want to enter the technical module |

## Conflict Resolution Pattern

Use this when requirements conflict:

```text
I see a conflict: you want [X] and [Y], but those usually push in opposite directions because [reason]. Which matters more?
```

Useful options:
- prioritize X
- prioritize Y
- refine the requirement
- research examples

Common requirement conflicts:
- simple onboarding and rich configuration
- fast first use and detailed setup
- broad flexibility and strict consistency
- low friction and heavy moderation
- collaborative editing and strict review gates

## Iteration Rules

1. Do not write the spec after only a few shallow questions.
2. Get through all relevant default requirement categories first.
3. Prefer clarifying the experience and scope before deepening edge cases.
4. Use research when it reduces ambiguity.
5. Do the default completeness check before writing.
6. Do not drag the user into technical architecture unless they opted in.

## Handling Different User Types

### Technical User
- still default to product requirements first
- gather constraints without forcing architecture decisions
- ask whether they want technical design before going there

### Non-Technical User
- keep questions concrete and user-facing
- use examples instead of jargon
- avoid stack talk unless they request it

### User in a Hurry
- prioritize problem, users, core journey, must-haves, and out-of-scope
- note what remains unresolved
- produce a lean requirements spec rather than an overbuilt design doc
