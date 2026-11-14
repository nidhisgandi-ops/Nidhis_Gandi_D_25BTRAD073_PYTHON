def calculate_grade(marks):
    """Calculates the letter grade and status based on numerical marks."""
    if not (0 <= marks <= 100):
        return "Invalid Marks", "Error"
    elif marks >= 90:
        return "A", "Distinction"
    elif marks >= 80:
        return "B", "First Class"
    elif marks >= 70:
        return "C", "Second Class"
    elif marks >= 60:
        return "D", "Pass"
    else:
        return "F", "Fail"


def evaluate_class(student_records):
    """Processes a dictionary of students, prints results, and summarizes performance."""
    print(f"{'Student Name':<18} | {'Marks':<6} | {'Grade':<13} | {'Status'}")
    print("-" * 55)

    total_marks = 0
    valid_students = 0
    passed_count = 0

    for name, marks in student_records.items():
        grade, status = calculate_grade(marks)
        print(f"{name:<18} | {marks:<6} | {grade:<13} | {status}")

        if grade != "Invalid Marks":
            total_marks += marks
            valid_students += 1
            if grade != "F":
                passed_count += 1

    print("-" * 55)
    if valid_students > 0:
        class_avg = total_marks / valid_students
        pass_rate = (passed_count / valid_students) * 100
        print(f"Class Average: {class_avg:.2f}% | Pass Rate: {pass_rate:.1f}%\n")


academic_class = {
    "Aarav Sharma": 94,
    "Priya Patel": 82,
    "Rohan Verma": 75,
    "Ananya Nair": 61,
    "Vikram Singh": 48,
}

print("=== ACADEMIC SCENARIO RESULTS ===")
evaluate_class(academic_class)

test_cases = {
    "Test_Upper_Limit": 100,
    "Test_Boundary_A": 90,
    "Test_Just_Below_A": 89,
    "Test_Boundary_D": 60,
    "Test_Just_Below_D": 59,
    "Test_Lower_Limit": 0,
    "Test_Out_Of_Range": 105,
}

print("=== BOUNDARY TEST CASES ===")
evaluate_class(test_cases)
