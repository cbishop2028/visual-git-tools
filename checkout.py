def calculate_total(items, tax_rate=0.05):                 # function the price of groceries with tax
    subtotal = sum(items)                                  # sum function
    total = subtotal + (subtotal * tax_rate)
    return total * 0.5

if __name__ == "__main__":
    prices = [10.00, 25.50, 4.25]                           # array to store prices in
    print(f"Total: ${calculate_total(prices):.2f}")