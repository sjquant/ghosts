# Design Reference Index

Use when there is no concrete visual reference and routing is unclear.

## Layer A - Style

| File | Use when | Notes |
|---|---|---|
| `taste-default.md` | neutral, operational, internal tools, dashboards | Safe but must not be used for expressive briefs. |
| `taste-premium.md` | premium, glossy, beautiful, startup-grade, brand-grade | Requires dimensional material and high-craft Layer B. |
| `taste-minimal.md` | minimal, editorial, quiet, Linear-like, Notion-like | Restraint, spacing, typography, hierarchy. |
| `taste-experimental.md` | cinematic, Awwwards, wow, scroll-driven, high-variance | Use carefully; requires browser QA. |

## Layer B - Brand / design systems

| File | Category | Aesthetic |
|---|---|---|
| `brand-linear.md` | productivity | precise, restrained, gradient accents, dense but calm |
| `brand-stripe.md` | SaaS / fintech | polished, dimensional, colorful, high trust |
| `brand-supabase.md` | developer tools | dark, emerald, code-first, terminal-adjacent |
| `brand-vercel.md` | developer platform | monochrome, sharp typography, disciplined spacing |

## Shortcuts

| User says | Load |
|---|---|
| "make it usable" | `taste-default.md` + existing system or `brand-vercel.md` |
| "premium SaaS" | `taste-premium.md` + `brand-stripe.md` |
| "startup-grade" | `taste-premium.md` + `brand-stripe.md` or `brand-vercel.md` |
| "Linear-like" | `taste-minimal.md` + `brand-linear.md` |
| "developer tool" | `taste-premium.md` + `brand-supabase.md` or `brand-vercel.md` |
| "Awwwards" | `taste-experimental.md` + `brand-stripe.md` |
| "dark product UI" | `taste-premium.md` + `brand-supabase.md` |

## Shortlist rule

For greenfield work:

1. Pick 2-3 plausible Layer B references.
2. In 1-2 sentences each, explain why it fits.
3. Pick one.
4. Pick one Layer A that matches the ambition lane.
5. Extract, do not average. Averaging references produces the generic default.
