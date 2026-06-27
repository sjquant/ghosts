# Performance Audit

## Checklist

- bundle size changed?
- images optimized?
- fonts loaded efficiently?
- animations use transform/opacity/filter?
- no expensive layout animation?
- no unnecessary client-side JS?
- no layout shift?
- loading states exist?
- route renders without console errors?

## Rule

Performance optimizations must preserve the design contract. Do not replace dimensional material with flat fills unless the user accepts that visual change.
