import random


def simulate_dice_rolls(num_dice=1, num_rolls=100):
    min_sum = num_dice
    max_sum = num_dice * 6
    frequencies = {total: 0 for total in range(min_sum, max_sum + 1)}

    print(f"--- Rolling {num_dice} Dice for {num_rolls} Trials ---")

    for roll_num in range(1, num_rolls + 1):
        rolls = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(rolls)
        frequencies[total] += 1

        if roll_num <= 5:
            print(f"Roll {roll_num}: {rolls} -> Total = {total}")

    if num_rolls > 5:
        print(f"... ({num_rolls - 5} more rolls simulated) ...")

    print(f"\n--- Outcome Frequency Analysis ({num_rolls} Rolls) ---")
    print(f"{'Outcome':<10} {'Count':<10} {'Observed %':<12} {'Visual Chart'}")
    print("-" * 55)

    for outcome, count in frequencies.items():
        percentage = (count / num_rolls) * 100
        bar = "*" * int(percentage // 2)
        print(f"{outcome:<10} {count:<10} {percentage:>6.1f}%      {bar}")

    assert sum(frequencies.values()) == num_rolls, "Count mismatch!"

    most_frequent = max(frequencies, key=frequencies.get)
    print(
        f"\nInterpretation: Outcome '{most_frequent}' appeared most often "
        f"({frequencies[most_frequent]} times)."
    )


simulate_dice_rolls(num_dice=1, num_rolls=600)
print("\n" + "=" * 60 + "\n")
simulate_dice_rolls(num_dice=2, num_rolls=1000)
