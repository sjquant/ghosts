---
title: "Keep test scenarios visible in the test body"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-181c8ce22f7c8a5659cffeeb"]
---

# Keep test scenarios visible in the test body

Make the conditions and expected results clear without requiring readers to trace branches or hidden setup.

## Example

Setup excerpts from asynchronous coupon-reservation tests.

### Before

The prepared payment state depends on the meaning of `linked`.

```python
usage = await create_coupon_usage(
    session,
    subscription=subscription,
    coupon=coupon,
    payment_id=None if linked else subscription.last_payment_id,
    link_subscription=linked,
    applied_amount=coupon.discount_amount,
    usage_pending=True,
)
```

### After

Each block belongs to a separate test scenario.

```python
# Given: a subscription-linked reservation not yet applied to a payment
usage = await create_coupon_usage(
    session,
    subscription=subscription,
    coupon=coupon,
    payment_id=None,
    link_subscription=True,
    applied_amount=coupon.discount_amount,
    usage_pending=True,
)
```

```python
# Given: a legacy trial-payment reservation without a subscription link
usage = await create_coupon_usage(
    session,
    subscription=subscription,
    coupon=coupon,
    payment_id=subscription.last_payment_id,
    link_subscription=False,
    applied_amount=coupon.discount_amount,
    usage_pending=True,
)
```

Explicit call-site values can still leave branching inside the helper. To remove that branch too, change the helper to accept an explicit `subscription_id` instead of `link_subscription`.

Do not select inputs or expectations through conditionals in test setup, actions or assertions.
