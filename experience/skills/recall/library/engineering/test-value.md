---
title: "Protect a distinct behavior with each test"
scope: "global"
status: "proposed"
confidence: "high"
candidate_ids: ["candidate-dbfc753fd64e620c485082f2", "candidate-bd288f79be4f83ca4d3a6d00"]
---

# Protect a distinct behavior with each test

When adding or revising coverage, identify the behavior that would lose protection without this test. Construction wiring, incidental HTML, and duplicated lower-layer assertions add maintenance and runtime cost without independent confidence.

## Choose the lightest boundary that owns the behavior

A service test does not establish that an HTTP response matches its schema, and a view test may legitimately assert that it calls its service with the expected arguments. Judge the boundary protected rather than banning mocks or repeating every scenario across layers:

- When a heavy view, browser, or database harness delegates calculation or status selection to a lower unit, verify the cross-layer wiring once in the heavy harness and test the detailed value or status matrix at the lower boundary.
- Avoid `N × M` cross-product parameterization in integration or view tests when the axes vary independently.

Deidentified view and status-helper test fragments; the host project supplies the HTTP test client, order factory, and `resolve_badge_status`.

### Before

```python
@pytest.mark.parametrize(
    ("paid", "shipped", "expected_badge"),
    [(False, False, "pending"), (True, False, "paid"), (True, True, "shipped")],
)
def test_order_page_badge(client, create_order, paid: bool, shipped: bool, expected_badge: str) -> None:
    order = create_order(paid=paid, shipped=shipped)
    response = client.get(f"/orders/{order.id}")
    assert response.json()["badge"] == expected_badge
```

### After

```python
def test_order_page_includes_badge(client, create_order) -> None:
    order = create_order(paid=True, shipped=False)
    response = client.get(f"/orders/{order.id}")
    assert response.json()["badge"] == "paid"


@pytest.mark.parametrize(
    ("paid", "shipped", "expected_badge"),
    [(False, False, "pending"), (True, False, "paid"), (True, True, "shipped")],
)
def test_resolve_badge_status(paid: bool, shipped: bool, expected_badge: str) -> None:
    assert resolve_badge_status(paid=paid, shipped=shipped) == expected_badge
```

## Keep test scope proportionate to the change

- Do not add tests for untouched comparison paths, defensive type-narrowing branches (such as `typeof value === "string"` guards), or improbable edge cases outside the change's failure modes.
- When a new scenario or parameterized test subsumes an older narrow test case, fold or remove the redundant test instead of keeping both.

## Template changes and refactoring

Exact headings, CSS classes, and element order make a delivery test fail when presentation changes even if delivery behavior remains correct. Check the behavior the test owns, and inspect presentation through a populated render.

Ask what existing coverage already checks before adding tests for implementation-only refactors. A test that recreates a constructor's wiring does not independently show that the service works.
