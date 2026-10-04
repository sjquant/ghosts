# Frontend Testing Guide

Frontend-specific standards. Apply them together with `common.md`.

## 1. Priority Targets

- Core business logic
  Example: payment, authentication
- Complex data transformation logic
- Utility functions with frequent edge cases

## 2. Testing Trophy

We follow Kent C. Dodds' `Testing Trophy` model, with the strongest emphasis on integration tests. A test can exercise components, composables, and state management together while protecting one clearly defined behavior.

1. `Static (Lint/Type)`
   Use TypeScript and ESLint to catch typos, type mismatches, and other basic mistakes.
2. `Unit`
   Verify highly complex calculations or isolated pure functions.
3. `Integration`
   This is our primary tactic. Verify whether multiple components work together to deliver a feature. Prefer sociable tests with minimal mocking.
4. `E2E`
   Verify user scenarios in a real browser environment.
   Example: sign in -> search -> purchase
   This is the safest level, but also the most expensive, so apply it only to critical paths.

## 3. File Structure

- Place specs for simple modules or component-local behavior next to the source file.
- If a feature spans multiple components, place the spec under the feature's `tests/` directory or next to the representative entry component.
- Even when the filename follows a representative component name, the test scope should cover the user-observable behavior delivered with its child components and composables.

```text
src/
├── components/
│   ├── BaseButton.vue
│   ├── BaseButton.spec.ts
│   └── Cart/
│       ├── Cart.vue
│       ├── CartRow.vue
│       ├── useCart.ts
│       └── tests/
│           └── Cart.spec.ts
└── utils/
    ├── price.ts
    ├── date.ts
    └── tests/
        ├── price.spec.ts
        └── date.spec.ts
```

## 4. `describe` Block Structure

Use `describe` to show the shared subject of the tests, not the internal implementation structure. Keep it flat by default instead of nesting it.

```tsx
// Components / classes
describe('Cart', () => {
  it('수량을 증가시키면 총액이 재계산된다', () => {
    // ...
  });

  it('수량은 1 미만으로 감소하지 않는다', () => {
    // ...
  });

  it('삭제 버튼을 누르면 해당 상품이 목록에서 사라진다', () => {
    // ...
  });
});

// Public functions
describe('formatPrice', () => {
  it('정수를 원화 문자열로 변환한다', () => {
    // ...
  });
});

describe('applyDiscount', () => {
  it('할인율만큼 차감된 금액을 반환한다', () => {
    // ...
  });
});
```

- Name each `describe` block after the test target. Example: component name, hook name, public function name
- Write each `it` or `test` block as a sentence that describes the expected outcome in that context.
- Do not nest child `describe` blocks. If you need another context, split it into another top-level `describe` block instead.

## 5. Given / When / Then In Specs

Mark each section with `// Given`, `// When`, and `// Then`. `Then` covers rendered UI, user-visible state, and outgoing requests or events.

```tsx
it('상품 수량을 변경하면 장바구니 총액이 재계산된다', async () => {
  // Given
  const product = { id: 1, name: 'T-Shirt', price: 10000 };

  render(Cart, {
    props: {
      initialItems: [{ ...product, quantity: 1 }],
    },
  });

  // When
  const incrementButton = screen.getByRole('button', { name: /increase quantity/i });
  await userEvent.click(incrementButton);

  // Then
  expect(screen.getByText(/total: 20,000 KRW/i)).toBeInTheDocument();
});
```

Supporting comments can explain the scenario:

```tsx
it('쿠폰을 적용하면 최소 주문 금액 조건을 만족할 때만 할인 금액이 반영된다', async () => {
  // Given: 장바구니 총액은 30,000원이고, 5,000원 할인 쿠폰은 최소 주문 금액 50,000원이 필요하다.
  // 따라서 초기 상태에서는 쿠폰을 선택해도 할인은 적용되면 안 된다.

  // When: 사용자가 수량을 늘려 총액을 50,000원 이상으로 만든 뒤 같은 쿠폰을 적용하면.

  // Then: 할인 금액이 반영되고, 주문 요약 영역에 최종 결제 금액이 다시 계산되어 보여야 한다.
});
```

## 6. Mocking

- Mock API calls at the network boundary with `MSW (Mock Service Worker)` instead of mocking server logic directly.
- Prefer testing the integrated state where parent and child components actually collaborate.
- In black-box component tests, keep real rendering whenever possible. Consider stubs, spies, or mocks only when unrelated side effects make the test unstable or too noisy.

### 6.1 Shared MSW Setup

Do not repeat the same MSW setup in every spec. Build tests on top of a shared test environment, then override only the conditions required for the scenario with `server.use(...)`.

- Do not default to fine-grained `vi.mock()` calls against internal composables or API modules.
- Write overrides so that they reveal only the condition the test is trying to validate.
- Prefer helpers with obvious intent over large and noisy fixture payloads.

### 6.2 Shared Component Test Environment

Query client, store, injectables, and browser storage are usually better provided by the default test environment than recreated in each spec.

## 7. Async UI Waiting

In component tests, the synchronization point should not be "has the request finished?" It should be "has the DOM reached the state the user is supposed to see?"

- Wait for appearance with `findBy*`.
- Wait for disappearance with `waitForElementToBeRemoved`.
- Use `waitFor(() => expect(...))` only when `findBy*` or dedicated removal APIs cannot express the expectation cleanly.
- If `waitFor` is required, keep only one assertion inside the callback.

`findBy*`, `waitFor`, and `waitForElementToBeRemoved` do not wait forever. They fail if the condition is not satisfied within the default timeout. Increase the timeout only when the specific test needs it.

## 8. Non-Deterministic Inputs

Inject time or randomness as a parameter so the test can fix it.

```ts
// Before
const getDeadline = () => {
  const now = new Date();
  return addDays(now, 7);
};

// After
const getDeadline = (baseDate = new Date()) => {
  return addDays(baseDate, 7);
};

it('마감일은 기준일로부터 7일 후다', () => {
  const fixedDate = new Date('2024-01-01');
  expect(getDeadline(fixedDate)).toEqual(new Date('2024-01-08'));
});
```

## 9. UI Verification And Accessibility

We avoid pixel-perfect visual regression tests by default. Screen structure and styles change often, and their maintenance cost is high. Instead, write tests against attributes that users actually perceive and interact with.

### Query Priority

| Priority | Query | When To Use |
| --- | --- | --- |
| 1 | `getByRole` | Most semantic UI elements such as buttons, inputs, links, headings, and dialogs. Use with `name` whenever possible |
| 2 | `getByLabelText` | Form fields connected to labels |
| 3 | `getByDisplayValue` | When the current selected value is the best identifier |
| 4 | `getByText` | When visible text is the most meaningful query |
| 5 | `getByTestId` | Only when the other options are not practical |

### `data-testid` Usage

Use `data-testid` only for elements that cannot be identified well through accessibility roles or similar user-facing semantics. Do not add `aria-label` only to make tests easier to query.

```vue
<button data-testid="submit-button">Submit</button>
```

```ts
screen.getByTestId('submit-button'); // BAD
screen.getByRole('button', { name: /submit/i }); // GOOD
```

```vue
<div data-testid="product-card-skeleton">...</div>
```

```ts
screen.getByTestId('product-card-skeleton');
```

For repeated UI, narrow by user-visible context with `within(...)` before falling back to `data-testid`.

```ts
const row = screen.getByRole('row', { name: /Samsung Electronics/i });
expect(within(row).getByText('72,000')).toBeInTheDocument();
```

### Prefer To Avoid

- CSS class names
- DOM structure itself
- Positional selectors such as `nth-child`
- Auto-generated or meaningless `id` values
- Text that is likely to change often
- Broad snapshot comparisons

## 10. Review Checklist

In addition to the common checklist:

- Does the test wait for the user-visible DOM state instead of request completion?
- Do queries follow the priority order, using `data-testid` only when user-facing semantics are impractical?
- Are API calls replaced at the network boundary with MSW rather than with `vi.mock()` on internal modules?
