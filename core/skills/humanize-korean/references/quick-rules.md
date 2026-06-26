# Quick Rules - Korean Humanizing Fast Path

Use these rules to detect and locally rewrite Korean AI-tell patterns. Every
edit must be span-grounded and meaning-preserving.

## Do-NOT

Never detect or rewrite:

- proper nouns, product names, model names, institution names;
- numbers, dates, units, math, chemistry, statistics, and legal clauses;
- direct quotations inside Korean or English quotation marks;
- standard technical abbreviations such as LLM, GPU, API, MCP, SQL, HTTP.

## Over-Polish Guard

- Change rate above 30%: warn and re-check for over-editing.
- Change rate above 50%: stop, rollback, and report.

## A. Translationese

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| A-1 | `~에 대해(서)` | S1 | Use a direct object: `X에 대해 논의` -> `X를 논의`. |
| A-2 | overused `~를 통해/통하여` | S1 | Vary with `~로`, `~해서`, `~함으로써`. |
| A-3 | `~에 있어(서)` | S1 | Use `~에서`, `~을 볼 때`, or direct phrasing. |
| A-4 | repeated `~라는 점에서` | S2 | Use `~서`, `~라는 이유로`, or delete. |
| A-5 | `~와 관련하여/관련된` | S2 | Use `~에`, `~의`, or a direct object. |
| A-6 | overused `~에 기반하여/바탕으로` | S2 | Use `~로`, `~을 보고`, `~를 근거로`. |
| A-7 | light-verb literalism: `가지고 있다`, `회의를 가지다` | S1 | Restore the verb or adjective: `회의를 했다`, `경쟁력이 강하다`. |
| A-8 | double passive `~되어진다` | S1 | Use active or single passive: `판단된다`, `판단한다`. |
| A-9 | passive `~에 의해` | S2 | Put the actor in subject position: `AI가 만든`. |
| A-10 | overused `~할 수 있다` | S2 | State directly when the claim is definite. |
| A-11 | overused purpose clause `~을 위해` | S2 | Use `~려고`, `~위한`, or a direct clause. |
| A-15 | abstract subject plus general-purpose verb or causative/cognitive verb | S2 | Restore a concrete subject or split as `~에 따르면 ~이다`, `~때문에`. |
| A-16 | translated pronouns `그/그녀/그것/그들` repeated in a paragraph | S1 | Delete 50%+ where Korean allows zero pronoun; otherwise use a noun or title. |
| A-18 | long left-branching modifier before a noun | S2 | Split the sentence or use a follow-up clause. |
| A-19 | double particles `~에서의/~에로의/~으로의/~에의/~으로부터의` | S2 | Expand into a clause. Do not flag simple `~의`. |

## B. Excess English

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| B-1 | Korean term plus English in parentheses every time | S2 | Keep English only on first occurrence unless the term is technical. |
| B-2 | English word left as-is despite a natural Korean equivalent | S2 | Translate when it does not damage domain meaning; preserve standard terms. |

## C. Structural AI Patterns

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| C-5 | excessive emoji | S1 | Delete in columns, reports, and formal writing. |
| C-7 | formulaic `먼저/반면/결국` three-part flow | S2 | Reduce connectors or absorb them into prose. |
| C-8 | repeated `A인가, B인가` parallel questions | S2 | Keep one if useful; turn the rest into statements. |
| C-9 | numeric parenthetical indexing `(1)`, `(2)`, `(3)` | S2 | Convert to prose or simple line breaks. |
| C-10 | repeated colon subtitles `X: Y` | S1 | Shorten headings or convert to plain headings. |
| C-11 | comma right after connective endings such as `-고,`, `-며,`, `-지만,` | S1 | Remove the comma unless syntax demands it. |

## D. Signature Phrases

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| D-1 | conclusion pivots: `결론적으로`, `따라서`, `이를 통해`, `그러므로`, `요약하면`, `정리하면` | S1 | If repeated more than three times, delete most and vary one or two. |
| D-2 | `시사하는 바가 크다`, `주목할 만하다` | S1 | Delete or replace with the concrete conclusion already in the text. |
| D-3 | `본질적으로`, `핵심적으로` | S1 | Delete unless needed for contrast. |
| D-4 | hype words repeated: `파격적`, `압도적`, `강력한`, `획기적`, `치명적` | S1 | Delete or replace with concrete facts already present. |
| D-5 | personified abstraction: `기술이 묻는다`, `시대가 부른다` | S1 | Restore a person, institution, or plain subject. |
| D-6 | formulaic ending: `~할 때다`, `~해야 한다`, `지금이야말로` | S1 | Close with a plain statement when possible. |
| D-7 | repeated conversion formula `X에서 Y로` | S2 | Keep one, rewrite the rest as ordinary description. |

## E. Rhythm And Endings

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| E-1 | sentence lengths too uniform | S2 | Add one short sentence or allow one longer sentence per affected paragraph. |
| E-2 | four or more consecutive `~다` endings; automatic `~고 있다` mapping | S2 | Vary tense and endings; simplify `~고 있다` to simple tense when valid. |
| E-7 | inconsistent speech level in dialogue or spoken text | S2 | Keep one speech level within the paragraph or speaker turn. |

## F. Excess Modifiers And Nominalization

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| F-4 | accumulated Sino-Korean or English nominalization: `-성`, `-적`, `-화`, `-tion`, `-ment`, `-ness`, `-ity` | S2 | Restore verbs or adjectives where the meaning stays intact. |
| F-5 | abstract `~적 N` chains | S2 | Use noun+noun or expand into a concrete clause. |

## G. Hedging

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| G-1 | overused `~것이다/~할 것이다` | S2 | Use present or definite form when the sentence permits. |
| G-2 | overused `~로 보인다/~인 듯하다` | S2 | State directly where evidence is already given. |
| G-3 | safety-balance lexicon: `양쪽 모두`, `두 가지 모두`, `장점도 있지만`, `신중하게`, `균형` | S2 | If repeated more than four times, replace one or two with the writer's actual stance. |

## H. Connectors

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| H-1 | sentence-initial connectors `또한`, `따라서`, `즉`, `나아가`, `아울러`, `게다가`, `더욱이` five or more times | S1 | Delete most; let sentence order carry flow. |
| H-3 | meta-entry phrases: `이는`, `이 점에서`, `이 관점에서`, `이 말은` | S1 | Absorb into the sentence or delete. |
| H-4 | overused `즉` | S2 | Keep at most one unless the text is technical explanation. |

## I. Bound Nouns And Formal Nouns

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| I-1 | ending `~인 것이다/~한 것이다` | S1 | Use plain ending. |
| I-2 | `X은 ~라는 점에 있다` | S2 | Write `X는 ~다`. |
| I-3 | ending `~다는 뜻이다/~다는 의미다` | S2 | Fold the meaning into the sentence. |
| I-4 | repeated recommendation ending `~해야 한다/~합니다` | S2 | Vary with plain statements when genre permits. |

## J. Visual Decoration

| ID | Pattern | Severity | Fix |
|---|---|---:|---|
| J-1 | excessive Markdown bold emphasis | S2 | Remove from body text in columns and reports. |
| J-2 | emphasis quotes five or more times | S1 | Keep only real quotes or one essential special usage. |
| J-3 | bullet lists in columns or reports | S2 | Integrate into prose unless list structure is necessary. |

## Self-Check

After rewriting, check:

1. Proper nouns, numbers, dates, direct quotes, and technical abbreviations are
   unchanged.
2. Change rate is <= 30%; never > 50%.
3. Genre did not drift.
4. Register did not drift.
5. Remaining S1 patterns are zero.
6. No new metaphor, flourish, claim, citation, or example was added.

If any check fails, rollback that local edit and retry once. If it still fails,
leave the text unchanged and report the failed check.
