import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False

    return True


try:
    num = int(input("Enter an integer: "))
    if is_prime(num):
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")
except ValueError:
    print("Invalid input. Please enter a valid whole number.")
