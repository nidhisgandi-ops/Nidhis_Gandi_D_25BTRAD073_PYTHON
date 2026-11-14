import random


def play():
    secret = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    print("=== Number Guessing Game ===")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} tries.")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return

    print(f"Out of attempts. The number was {secret}.")


if __name__ == "__main__":
    while True:
        play()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break
