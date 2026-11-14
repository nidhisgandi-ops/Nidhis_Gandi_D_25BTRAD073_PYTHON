def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci_recursive(i), end=" ")
