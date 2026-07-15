"""
AI Governance & Digital Safety Bootcamp - Week 1
Project: Student Grade Management System
"""

# ==========================================
# 1. CUSTOM FUNCTIONS & ERROR HANDLING
# ==========================================

# Requirement: Custom Function #1
def calculate_average(grades: list) -> float:
    # Requirement: Proper Error Handling (try-except)
    try:
        if not grades:
            raise ZeroDivisionError("The grades list cannot be empty.")

        total = sum(grades)
        average = float(total / len(grades))
        return round(average, 2)

    except ZeroDivisionError as e:
        print(f"[Error] {e}")
        return 0.0
    except TypeError:
        print("[Error] Grades list must contain only numbers.")
        return 0.0


# Requirement: Custom Function #2
def determine_letter_grade(average: float) -> str:
    # Requirement: Control Structures (if-elif-else)
    if average >= 90.0:
        return "A"
    elif average >= 80.0:
        return "B"
    elif average >= 70.0:
        return "C"
    elif average >= 60.0:
        return "D"
    else:
        return "F"


# Requirement: Custom Function #3
def create_student_record(student_id: int, name: str, grades: list) -> dict:
    average = calculate_average(grades)
    letter_grade = determine_letter_grade(average)

    is_passing = average >= 60.0

    # Requirement: Demonstrating basic data types (int, string, list, float, boolean, dictionary)
    student_record = {
        "id": student_id,              # int
        "name": name,                  # string
        "grades": grades,              # list
        "average": average,            # float
        "letter_grade": letter_grade,  # string
        "is_passing": is_passing       # boolean
    }

    return student_record


def main():
    student_database = []

    print("=" * 50)
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    print("=" * 50)

    # Requirement: Control Structures (Loops)
    while True:
        print("\n--- MENU ---")
        print("1. Add a Student Record")
        print("2. View All Student Records")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            print("\n--- Create New Record ---")

            while True:
                try:
                    student_id = int(input("Enter Student ID (numeric): "))
                    break
                except ValueError:
                    print("Invalid Input! Please enter a whole number.")

            name = input("Enter Student Name: ").strip()

            while not name:
                print("Name cannot be empty.")
                name = input("Enter Student Name: ").strip()

            grades_list = []

            print("Enter grades one by one. Enter -1 to finish:")

            while True:
                try:
                    grade = float(input("Enter grade (0-100): ").strip())

                    if grade == -1:
                        if not grades_list:
                            print("You must enter at least one grade.")
                            continue
                        break

                    if 0 <= grade <= 100:
                        grades_list.append(grade)
                    else:
                        print("Grade must be between 0 and 100.")

                except ValueError:
                    print("Invalid input. Enter a number.")

            record = create_student_record(
                student_id,
                name,
                grades_list
            )

            student_database.append(record)

            print(f"\nRecord created for {name}.")

        elif choice == "2":
            print("\n--- Student Records ---")

            if not student_database:
                print("No records found.")
                continue

            # Requirement: Control Structures (Looping through a list)
            for index, student in enumerate(student_database, start=1):
                print(f"\n[{index}] {student['name']} (ID: {student['id']})")
                print(f"Grades: {student['grades']}")
                print(f"Average: {student['average']}%")
                print(f"Letter Grade: {student['letter_grade']}")

                if student['is_passing']:
                    print("Status: PASSING")
                else:
                    print("Status: FAILING")

        elif choice == "3":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()