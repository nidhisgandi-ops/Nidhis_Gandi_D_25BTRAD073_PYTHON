attendance_tracker = {}


def add_student(name):
    """Adds a new student to the tracker if they don't already exist."""
    name = name.strip()
    if name:
        if name not in attendance_tracker:
            attendance_tracker[name] = []
            print(f"Student '{name}' added successfully.")
        else:
            print(f"Student '{name}' already exists in the system.")
    else:
        print("Student name cannot be empty.")


def mark_attendance(name, status):
    """Marks attendance ('Present' or 'Absent') for a student."""
    name = name.strip()
    status = status.strip().capitalize()
    if status not in ["Present", "Absent"]:
        print("Invalid status. Please enter 'Present' or 'Absent'.")
        return
    if name in attendance_tracker:
        attendance_tracker[name].append(status)
        print(
            f"Marked '{status}' for {name}. Total classes recorded:"
            f" {len(attendance_tracker[name])}"
        )
    else:
        print(
            f"Student '{name}' not found. Please add the student first using option"
            " 1."
        )


def update_attendance_record(name, index, new_status):
    """Updates an existing attendance record for a student by session index (0-based)."""
    name = name.strip()
    new_status = new_status.strip().capitalize()
    if new_status not in ["Present", "Absent"]:
        print("Invalid status. Please enter 'Present' or 'Absent'.")
        return

    if name in attendance_tracker:
        records = attendance_tracker[name]
        if 0 <= index < len(records):
            old_status = records[index]
            records[index] = new_status
            print(
                f"Updated {name}'s session {index + 1} from '{old_status}' to"
                f" '{new_status}'."
            )
        else:
            if len(records) == 0:
                print(f"{name} has no attendance records to update.")
            else:
                print(
                    f"Invalid session index. {name} has {len(records)} record(s)"
                    f" (indices 0 to {len(records) - 1})."
                )
    else:
        print(f"Student '{name}' not found.")


def display_attendance():
    """Displays attendance records for all students in an organized format."""
    if not attendance_tracker:
        print("\nNo attendance records found.")
        return

    print("\n" + "=" * 50)
    print(f"{'Student Name':<20} | {'Attendance History':<25}")
    print("-" * 50)
    for name, records in attendance_tracker.items():
        history_str = ", ".join(records) if records else "No records yet"
        print(f"{name:<20} | {history_str}")
    print("=" * 50 + "\n")


def calculate_percentages():
    """Calculates and displays the attendance percentage for each student."""
    if not attendance_tracker:
        print("\nNo attendance records found.")
        return

    print("\n" + "=" * 60)
    print(f"{'Student Name':<20} | {'Attended/Total':<15} | {'Percentage'}")
    print("-" * 60)
    for name, records in attendance_tracker.items():
        total_classes = len(records)
        if total_classes == 0:
            pct = 0.0
            attended = 0
        else:
            attended = records.count("Present")
            pct = (attended / total_classes) * 100
        print(f"{name:<20} | {attended}/{total_classes:<13} | {pct:.2f}%")
    print("=" * 60 + "\n")


def identify_below_threshold(threshold):
    """Identifies and displays students whose attendance percentage is below the threshold."""
    if not attendance_tracker:
        print("\nNo attendance records found.")
        return

    print(
        "\n" + f"--- Students with attendance below {threshold}% ---".upper()
    )
    found = False
    for name, records in attendance_tracker.items():
        total_classes = len(records)
        if total_classes == 0:
            pct = 0.0
        else:
            pct = (records.count("Present") / total_classes) * 100

        if pct < threshold:
            print(
                f" - {name}: {pct:.2f}% (Attended {records.count('Present')}"
                f" out of {total_classes} classes)"
            )
            found = True

    if not found:
        print(f"Great! All students are at or above {threshold}%.")
    print("-" * 50 + "\n")


def main():
    while True:
        print("\n--- Class Attendance Tracker Menu ---")
        print("1. Add a new student")
        print("2. Mark student attendance ('Present' or 'Absent')")
        print("3. Update a past attendance record")
        print("4. Display all attendance records")
        print("5. Calculate attendance percentages")
        print("6. Check students below an attendance threshold")
        print("7. Exit")

        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            status = input("Enter attendance status (Present/Absent): ")
            mark_attendance(name, status)

        elif choice == "3":
            name = input("Enter student name: ")
            try:
                idx = int(
                    input("Enter session index to update (0 for first session): ")
                )
                new_status = input("Enter new status (Present/Absent): ")
                update_attendance_record(name, idx, new_status)
            except ValueError:
                print("Please enter a valid integer for the session index.")

        elif choice == "4":
            display_attendance()

        elif choice == "5":
            calculate_percentages()

        elif choice == "6":
            try:
                thresh = float(
                    input("Enter attendance percentage threshold (e.g., 75): ")
                )
                identify_below_threshold(thresh)
            except ValueError:
                print("Please enter a valid number for the threshold.")

        elif choice == "7":
            print("Exiting Attendance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")


if __name__ == "__main__":
    main()
