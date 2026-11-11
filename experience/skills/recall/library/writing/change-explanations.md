---
title: "Give reviewers the reason and concrete result"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-53a3933960e792259de992ea", "candidate-6ab63dccb2f8f9d6bd09877b", "candidate-7c93707f12050e47539d15d6"]
---

# Give reviewers the reason and concrete result

When describing a change, give a reader who missed the conversation enough information to understand why it is needed and assess its result. Listing operations or showing a Before/After table alone may leave the reason unanswered.

Generalized PR text illustrates the distinction.

### Before

```text
Split the scheduler into input and render phases.
```

### After

```text
Drawing before queued input can paint the previous drag position. Process
input before drawing so the render uses the updated position.
```

Report only checks actually run. Mark manual checks as manual and state their conditions and observable result; implementation details are not test cases. This lets reviewers identify missing coverage.

Choose a concrete artifact that answers the reader's question: sample input/output and types for a schema, code blocks for an interface, or a populated render for an email or UI. These choices do not require screenshots for every change.

Keep explanation focused on the decision. Capture-environment narration and incidental investigation details can be omitted when they do not help assess the change.
