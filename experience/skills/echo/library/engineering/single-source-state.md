---
title: "Derive repeated state from its source"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-5c5181b13641e16905d6f4fe"]
---

# Derive repeated state from its source

When a new variable or metadata declaration represents an existing fact, prefer deriving it from the original. Independently updating both copies creates missed updates and divergence that is hard to trace.

Executable Python reduction of a derived UI label; the same choice applies to computed reactive state.

### Before

```python
from dataclasses import dataclass

@dataclass
class Selection:
    category: str
    title: str

selection = Selection(category="books", title="Books")
selection.category = "music"
# The title still says Books.
```

### After

```python
from dataclasses import dataclass

@dataclass
class Selection:
    category: str

    @property
    def title(self) -> str:
        return self.category.title()

selection = Selection(category="books")
selection.category = "music"
assert selection.title == "Music"
```

The same omission risk appears when dependency objects already declare relationships but developers must also maintain an equivalent string-metadata list.

## When storage is intentional

Keep a stored field when DB filtering requires it. A stored view count can avoid loading very many rows when small divergence is acceptable. Inspect dependency direction before replacing storage with a property: deriving a price from a value that already depends on that price would reverse the dependency.
