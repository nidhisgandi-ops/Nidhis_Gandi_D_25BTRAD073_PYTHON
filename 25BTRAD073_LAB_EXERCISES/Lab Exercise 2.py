def main():
    name = input("What's your name? ").strip() or "World"
    print(f"Hello, {name}!")
    
    numbers = [1, 2, 3, 4, 5]
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))
    print("Squares:", [n ** 2 for n in numbers])
    
    for i in range(1, 4):
        print(f"Count: {i}")


if __name__ == "__main__":
    main()
