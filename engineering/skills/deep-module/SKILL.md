---
name: deep-module
description: Assess whether a module hides implementation details behind a simple interface for its callers.
disable-model-invocation: true
---

Review the module from the intended caller's perspective. Does it concentrate complexity behind a simple, stable interface? Identify any implementation details, state, lifecycle, ordering, error/retry, or concurrency obligations that callers must know or coordinate themselves, and any internal collaboration methods exposed as public API. Cite the relevant APIs and call sites, explain the material impact, and distinguish genuine abstraction leaks from legitimate domain requirements. If there is no material issue, say so.
