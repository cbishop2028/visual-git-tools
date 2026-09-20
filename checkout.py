def calculate_total(items, tax_rate=0.05):
    """Calculates the total price of items with tax."""
    subtotal = sum(items)
    total = subtotal + (subtotal * tax_rate)
    return total

if __name__ == "__main__":
    prices = [10.00, 25.50, 4.25]
    print(f"Total: ${calculate_total(prices):.2f}")