---
title: "Protect a distinct behavior with each test"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-dbfc753fd64e620c485082f2"]
---

# Protect a distinct behavior with each test

When adding or revising coverage, identify the behavior that would lose protection without this test. Construction wiring, incidental HTML and duplicated lower-layer assertions can add maintenance without independent confidence.

A service test does not establish that the HTTP response matches its schema. Conversely, a view test may legitimately assert that it calls its service correctly. Judge the boundary protected, rather than banning mocks or requiring every layer to repeat the same scenarios.

## Template changes

Exact headings, CSS classes and element order make a delivery test fail when presentation changes even if delivery behavior remains correct. Check the behavior the test owns, and inspect presentation through a populated render.

## Refactoring

Ask what existing coverage already checks before adding tests for implementation-only changes. A test that recreates a constructor's wiring does not independently show that the service works.
