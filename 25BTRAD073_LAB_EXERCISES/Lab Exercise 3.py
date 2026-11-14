name = input("Enter your name: ").strip() or "World"

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values only.")
    exit()

# --- Arithmetic operators ---
add = a + b
sub = a - b
mul = a * b
div = a / b if b != 0 else "undefined (division by zero)"
floor_div = a // b if b != 0 else "undefined"
mod = a % b if b != 0 else "undefined"

try:
    power = a ** b
except OverflowError:
    power = "undefined (number too large)"

# --- Comparison and logical operators ---
is_equal = a == b
is_greater = a > b
both_positive = a > 0 and b > 0

# --- Output ---
print(f"\nHello, {name}!")
print("\n--- Arithmetic ---")
print(f"{a} + {b} = {add}")
print(f"{a} - {b} = {sub}")
print(f"{a} * {b} = {mul}")
print(f"{a} / {b} = {div}")
print(f"{a} // {b} = {floor_div}")
print(f"{a} % {b} = {mod}")
print(f"{a} ** {b} = {power}")

print("\n--- Comparison / Logical ---")
print("a == b:", is_equal)
print("a > b:", is_greater)
print("both positive:", both_positive)

# --- Assignment operators ---
total = 10
total += 5  # 15
total *= 2  # 30
print("\nAfter += 5 and *= 2, total =", total)
