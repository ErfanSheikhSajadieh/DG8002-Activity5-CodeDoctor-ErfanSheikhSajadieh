# DG8002 Activity 5: Code Doctor

Hi, I'm Erfan. This is my Activity 5 project for DG8002. I repaired a Python ticket booth program and tested the main parts of it.

## What the program does

The program lets a customer choose general, student, or VIP tickets. It tracks how many tickets are left, calculates the subtotal, applies a 10% discount to orders of $100 or more, adds 13% HST, and prints a receipt.

## Fixes I made

- Fixed the subtotal so it adds every ticket price.
- Made the discount apply to orders of exactly $100 as well as higher orders.
- Changed the discount so it is taken off the price.
- Calculated HST after the discount.
- Added checks for unknown ticket types, invalid quantities, and quantities that are zero or less.
- Prevented customers from ordering more tickets than are available.
- Added a clear message when no tickets are purchased.

## How to run

You need Python 3. Open a terminal in this folder and run:

```bash
python Activity5.py
```

Choose a ticket category (`general`, `student`, or `vip`) and enter a quantity. Type `done` when you finish your order.

## Testing

I tested a regular order with more than one ticket type, an order at the $100 discount limit, and invalid entries including an unavailable quantity. The program gave the expected totals and rejected the invalid entries.

See [Activity5_Notes.md](Activity5_Notes.md) for the issues I found and the test results.

## Files

- `Activity5.py` — the repaired ticket booth program
- `Activity5_Notes.md` — my notes about the bugs and tests
