---
name: deep-module
description: Assess whether a module hides implementation details behind a simple interface for its callers.
disable-model-invocation: true
---

Any excessive implementation details that callers must know because the module fails to concentrate complexity behind a simple, stable interface, such as state, lifecycle, ordering, error/retry, or concurrency obligations they must coordinate themselves, or internal collaboration methods exposed as public API? Cite the relevant APIs and call sites, explain the material impact, and distinguish genuine abstraction leaks from legitimate domain requirements. If there is no material issue, say so.
