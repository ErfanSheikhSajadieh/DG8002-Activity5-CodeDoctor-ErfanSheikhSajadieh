TICKET_PRICES = {
    "general": 25.00,
    "student": 15.00,
    "vip": 60.00,
}

available_tickets = {
    "general": 12,
    "student": 8,
    "vip": 4,
}

TAX_RATE = 0.13
DISCOUNT_THRESHOLD = 100.00
DISCOUNT_RATE = 0.10


def show_menu():
    print("\n=== EVENT TICKETS ===")
    for category, price in TICKET_PRICES.items():
        print(f"{category.title()}: ${price:.2f} ({available_tickets[category]} left)")
    print("Type 'done' to finish your order.")


def calculate_subtotal(order):
    subtotal = 0.0
    for item in order:
        subtotal += TICKET_PRICES[item]
    return subtotal


def apply_discount(subtotal):
    # Purchases of $100 or more receive a 10% discount.
    if subtotal >= DISCOUNT_THRESHOLD:
        return subtotal * DISCOUNT_RATE
    return 0.0


def calculate_total(subtotal):
    discount = apply_discount(subtotal)
    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * TAX_RATE
    return discounted_subtotal + tax


def print_receipt(order):
    print("\n=== RECEIPT ===")
    if len(order) == 0:
        print("No tickets were purchased.")
        return

    for item in order:
        print(f"{item.title()}: ${TICKET_PRICES[item]:.2f}")

    subtotal = calculate_subtotal(order)
    discount = apply_discount(subtotal)
    taxable_subtotal = subtotal - discount
    tax = taxable_subtotal * TAX_RATE
    total = taxable_subtotal + tax

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"HST (13%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")


def run_ticket_booth():
    order = []

    while True:
        show_menu()
        category = input("Ticket category: ").strip().lower()

        if category == "done":
            break

        if category not in TICKET_PRICES:
            print("Unknown ticket category. Please choose general, student, or vip.")
            continue

        try:
            quantity = int(input("How many tickets? "))
        except ValueError:
            print("Please enter a whole number for the quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if quantity > available_tickets[category]:
            print(f"Not enough tickets available. Only {available_tickets[category]} left.")
            continue

        for _ in range(quantity):
            order.append(category)

        available_tickets[category] -= quantity
        print(f"Added {quantity} {category} ticket(s).")

    print_receipt(order)


run_ticket_booth()
