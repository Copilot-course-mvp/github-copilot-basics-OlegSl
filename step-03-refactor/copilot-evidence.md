# Copilot Evidence — Step 03

## Refactor prompt

Analise checkout_total and invoice_total functions, find duplicated code, extract it to a private function.

## Why behavior is preserved

The extracted helper function `_calculate_total` implements the same subtotal, discount, clamping, and rounding logic that both original functions used. `checkout_total` and `invoice_total` now delegate to that helper without changing any input/output behavior.

## Before vs after summary

Before: `checkout_total` and `invoice_total` contained duplicated subtotal, discount, clamping, and rounding logic.
After: Both functions now delegate to a shared private helper `_calculate_total`, reducing duplication while preserving behavior.

Note: `_calculate_total` was renamed to pass the test.
