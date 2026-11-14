import math


def area_calculator():
    print("=== Area Calculator ===")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")
    choice = input("Choose a shape (1-4): ").strip()

    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
    elif choice == "2":
        side = float(input("Enter side: "))
        area = side ** 2
    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
    elif choice == "4":
        radius = float(input("Enter radius: "))
        area = math.pi * radius ** 2
    else:
        print("Invalid choice.")
        return

    print(f"Area = {area:.2f}")


if __name__ == "__main__":
    area_calculator()
