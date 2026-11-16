customer_name = input("Enter customer name: ")
phone_number = input("Enter customer phone number: ")

# Lists to store item details
items = []
quantities = []
prices = []

# Loop to collect purchased items
while True:
    item_name = input("\nEnter item name (or type done to finish): ")
    if item_name.lower() == "done":
        break
    qty = int(input(f"Enter quantity of {item_name}: "))
    price = float(input(f"Enter unit price of {item_name}: ₹"))

    # Store inputs in the lists
    items.append(item_name)
    quantities.append(qty)
    prices.append(price)

# --- Print the Bill ---
print("\n" + "=" * 45)
print("SARAVANA STORES")
print("=" * 45)
print(f"Customer Name : {customer_name}")
print(f"Phone Number  : {phone_number}")
print("-" * 45)
print(f"{'Item':<15}{'Qty':<8}{'Rate':<10}{'Total':<10}")
print("-" * 45)

subtotal = 0
for i in range(len(items)):
    item_total = quantities[i] * prices[i]
    subtotal += item_total
    print(
        f"{items[i]:<15}{quantities[i]:<8}{prices[i]:<10.2f}{item_total:<10.2f}"
    )

# Calculate GST (e.g., 5%) and Final Total
tax_rate = 0.05
tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount

print("-" * 45)
print(f"{'Subtotal:':<33}₹{subtotal:.2f}")
print(f"{'GST (5%):':<33}₹{tax_amount:.2f}")
print("=" * 45)
print(f"{'GRAND TOTAL:':<33}₹{grand_total:.2f}")
print("=" * 45)
print("Thank you for shopping with us!")
print("=" * 45)
