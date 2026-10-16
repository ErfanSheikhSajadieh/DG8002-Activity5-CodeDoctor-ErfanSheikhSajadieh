# DG8002 Activity 5: Code Doctor

## What the program does

In this activity, I worked with a ticket booth program. It shows the ticket types, prices, and how many tickets are still available. A customer can choose tickets, and the program updates the available amount and prints a receipt. Orders of $100 or more get a 10% discount, and then 13% HST is added to the discounted amount.

## Problems I found and fixed

1. **The subtotal only counted the last ticket.** The program replaced the subtotal each time it checked a ticket. I changed it so each ticket price is added to the subtotal.
2. **A $100 order did not get a discount.** The original condition only checked for an amount over $100. I changed it to include orders of exactly $100.
3. **The discount made the price higher.** The original calculation added 10% to the price. I changed it so the program takes 10% off.
4. **HST was calculated before the discount.** I changed the total calculation so HST is added to the price after the discount.
5. **Letters in the quantity caused the program to stop.** I added `try/except` so the program gives a message and continues if the customer does not enter a whole number.
6. **Zero and negative quantities were accepted.** I added a check so the quantity must be greater than zero.
7. **Customers could ask for more tickets than were available.** The program now checks the available amount before adding tickets or changing the inventory.
8. **The receipt was unclear when no tickets were purchased.** I added a message for an empty order.

## Tests I ran

### Test 1: Different tickets, no discount

I entered 2 general tickets, 1 student ticket, and then `done`.

The receipt showed a $65.00 subtotal, no discount, $8.45 HST, and a $73.45 total.

### Test 2: The $100 discount limit

I entered 4 general tickets and then `done`.

The receipt showed a $100.00 subtotal, a $10.00 discount, $11.70 HST on the discounted amount, and a $101.70 total.

### Test 3: Invalid entries and ticket limit

I tried an unknown ticket type, a word instead of a quantity, a negative number, zero, and a request for 13 general tickets when only 12 were available. Then I bought 2 general tickets and entered `done`.

The program rejected each invalid entry and did not change the inventory. The valid purchase showed a $50.00 subtotal, no discount, $6.50 HST, and a $56.50 total.

## Concepts I used

I used variables, numbers and text, dictionaries, lists, conditionals, `for` and `while` loops, functions, formatted strings, and `try/except` for checking input.
