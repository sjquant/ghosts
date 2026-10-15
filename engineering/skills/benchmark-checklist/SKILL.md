---
name: ghosts:benchmark-checklist
description: Validate performance measurements and before/after claims. Use for benchmarks, speedups, regressions, or performance-based choices.
disable-model-invocation: true
---

Validate the claim against the measurement harness and actual work performed.

- **Work equivalence:** same correct outputs and workload; count errors, retries, and dropped work. Confirm awaited, consumed work falls inside the timed region.
- **Experimental control:** comparable production builds, versions, tuning, data, cache state, and concurrency. Separate profiling from timing; identify host noise and load-generator saturation.
- **Repeatability:** interleave before/after runs; report run count, median, and spread. Treat differences within noise as inconclusive. A requested ballpark may use one run, explicitly labeled.
- **Bottleneck / Amdahl's law:** identify the limiter, sanity-check physical bounds, and relate microbenchmarks to the end-to-end path users wait on.

Return faster, slower, no measurable difference, or inconclusive, with units and supporting artifacts. Qualify claims when tuning, correctness, or measurement validity remains unresolved; do not pick a winner from an invalid comparison.
