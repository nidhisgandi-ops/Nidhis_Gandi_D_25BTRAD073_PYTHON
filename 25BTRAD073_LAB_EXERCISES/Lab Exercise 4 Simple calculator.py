def calculator():
    print("=== Simple Calculator ===")
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ").strip()
    b = float(input("Enter second number: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b if b != 0 else "Error: division by zero"
    else:
        result = "Error: invalid operator"

    print(f"Result: {result}")


if __name__ == "__main__":
    calculator()
