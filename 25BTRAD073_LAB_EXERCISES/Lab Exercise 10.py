sentence = "Python is easy and Python is fun"

words = sentence.lower().split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("--- Word Frequency ---")
for word, count in word_counts.items():
    print(f"{word}: {count}")

print("Verification passed:", sum(word_counts.values()) == len(words))

survey_responses = [
    "Good", "Excellent", "Good", "Average",
    "Excellent", "Good", "Poor", "Good"
]

feedback_counts = {}
for response in survey_responses:
    feedback_counts[response] = feedback_counts.get(response, 0) + 1

print("\n--- Classroom Survey Results ---")
for rating, count in feedback_counts.items():
    print(f"{rating}: {count}")

most_common = max(feedback_counts, key=feedback_counts.get)
print(
    f"\nInterpretation: Most students rated the class as '{most_common}' "
    f"({feedback_counts[most_common]} out of {len(survey_responses)} responses)."
)
