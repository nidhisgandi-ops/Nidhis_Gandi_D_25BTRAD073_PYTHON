import os

FILE_NAME = "students.txt"


def id_exists(student_id):
    if not os.path.exists(FILE_NAME):
        return False
    with open(FILE_NAME, "r") as file:
        for line in file:
            if line.strip().split(",")[0] == student_id:
                return True
    return False


def add_student():
    student_id = input("Enter Student ID (e.g., S101): ").strip()
    if not student_id or id_exists(student_id):
        print("Error: Invalid or duplicate Student ID.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course (e.g., B.Tech CSE): ").strip()

    try:
        cgpa = float(input("Enter CGPA (0.0 - 10.0): "))
        if not (0.0 <= cgpa <= 10.0):
            raise ValueError
    except ValueError:
        print("Error: CGPA must be a number between 0.0 and 10.0.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{student_id},{name},{course},{cgpa}\n")
    print("Student record saved successfully.")


def display_students():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No student records found.")
        return

    print("\n--- College Student Records ---")
    print(f"{'ID':<10} {'Name':<20} {'Course':<15} {'CGPA':<5}")
    print("-" * 52)
    with open(FILE_NAME, "r") as file:
        for line in file:
            sid, name, course, cgpa = line.strip().split(",")
            print(f"{sid:<10} {name:<20} {course:<15} {cgpa:<5}")


def search_student():
    search_id = input("Enter Student ID to search: ").strip()
    if not os.path.exists(FILE_NAME):
        print("Record file does not exist.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            sid, name, course, cgpa = line.strip().split(",")
            if sid == search_id:
                print(
                    f"\nRecord Found -> ID: {sid} | Name: {name} | "
                    f"Course: {course} | CGPA: {cgpa}"
                )
                return
    print("Student ID not found.")


def update_student():
    target_id = input("Enter Student ID to update CGPA: ").strip()
    if not os.path.exists(FILE_NAME):
        print("Record file does not exist.")
        return

    updated_lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            sid, name, course, cgpa = line.strip().split(",")
            if sid == target_id:
                try:
                    new_cgpa = float(input(f"Enter new CGPA for {name} (Current: {cgpa}): "))
                    if not (0.0 <= new_cgpa <= 10.0):
                        raise ValueError
                    updated_lines.append(f"{sid},{name},{course},{new_cgpa}\n")
                    found = True
                except ValueError:
                    print("Invalid CGPA entered. Update cancelled.")
                    return
            else:
                updated_lines.append(line)

    if found:
        with open(FILE_NAME, "w") as file:
            file.writelines(updated_lines)
        print("Student record updated successfully.")
    else:
        print("Student ID not found.")


while True:
    print("\n=== College Student Data Manager ===")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by ID")
    print("4. Update Student CGPA")
    print("5. Exit")

    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
