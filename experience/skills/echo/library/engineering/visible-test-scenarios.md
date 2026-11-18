---
title: "Keep test scenarios visible in the test body"
scope: "global"
status: "proposed"
confidence: "medium"
candidate_ids: ["candidate-181c8ce22f7c8a5659cffeeb"]
---

# Keep test scenarios visible in the test body

Make the conditions and expected results clear without requiring readers to trace branches or hidden setup.

## Explicit setup values

Deidentified setup fragments from asynchronous coupon-reservation tests. The host project supplies the models, async creation helper and database session. Each After block is a separate scenario.

### Before

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

Keep small scenario data beside the test. Move data elsewhere when its size obstructs reading the test itself. Put test cases before supporting fixtures and helpers.

## Parameterized scenarios

Keep parameterization when it makes cases easy to compare. Group related inputs under field names, and give failure cases IDs that describe the failing condition.

The following deidentified fragments illustrate an approval test. The host project supplies the async persistence helpers, organization and document types.

### Before

Positional values need the parameter header to be understood; the setup helper also chooses email and income-earner values from the settlement type.

```python
pytest.param("WITHHOLDING", "SOLE_PROPRIETOR", True, True, document_types)
# In the test body:
await prepare_approval(session, organization, settlement_type, document_types)
```

### After

```python
pytest.param(
    {"business_type": "SOLE_PROPRIETOR", "is_domestic_resident": True,
     "is_representative": True, "tax_invoice_email": None},
    {"settlement_type": "WITHHOLDING", "income_earner_name": "Applicant"},
    document_types,
    id="withholding-sole-proprietor",
)
# The parameter names are application, settlement, document_types.
# In the test body:
organization.update(application)
await add_submission_documents(session, organization.id, document_types)
await add_settlement_profile(session, organization.id, **settlement)
```

The helper persists the supplied settlement values; it does not choose scenario conditions or overwrite application fields. Name failure cases such as `missing-bank` and `blank-account-holder` so test output identifies the condition.

Keep the action, response checks, and resulting state/history assertions visible in the test body. This cleanup does not require a scenario class or builder.
