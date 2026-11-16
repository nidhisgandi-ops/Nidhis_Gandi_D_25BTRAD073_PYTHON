def get_grade(percentage):
    if percentage >= 90:
        return "A+", 10
    elif percentage >= 80:
        return "A", 9
    elif percentage >= 70:
        return "B", 8
    elif percentage >= 60:
        return "C", 7
    elif percentage >= 50:
        return "D", 6
    elif percentage >= 40:
        return "E", 5
    else:
        return "F", 0


def main():
    students = []
    n = int(input("Number of students: "))
    if n <= 0:
        print("No students entered.")
        return

    num_subjects = int(input("Number of subjects: "))
    max_marks = float(input("Maximum marks per subject: "))

    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        name = input("Name: ")
        marks = []
        for s in range(num_subjects):
            marks.append(float(input(f"  Marks in subject {s + 1}: ")))

        total = sum(marks)
        percentage = (total / (num_subjects * max_marks)) * 100
        grade, points = get_grade(percentage)
        # Fail if any subject is below 40% of max marks
        result = "Fail" if any(m < 0.4 * max_marks for m in marks) else "Pass"

        students.append({
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade,
            "result": result,
        })

    # Rank by percentage (highest first)
    students.sort(key=lambda s: s["percentage"], reverse=True)

    print("\n" + "=" * 60)
    print(f"{'Rank':<6}{'Name':<15}{'Total':<10}{'%':<10}{'Grade':<8}{'Result'}")
    print("=" * 60)
    for rank, s in enumerate(students, start=1):
        print(
            f"{rank:<6}{s['name']:<15}{s['total']:<10.1f}"
            f"{s['percentage']:<10.2f}{s['grade']:<8}{s['result']}"
        )

    avg = sum(s["percentage"] for s in students) / len(students)
    print("=" * 60)
    print(f"Class average: {avg:.2f}%")
    print(f"Topper: {students[0]['name']} ({students[0]['percentage']:.2f}%)")


if __name__ == "__main__":
    main()
