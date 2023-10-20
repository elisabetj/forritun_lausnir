UI = False


def main():
    gradebook = {}

    add_student_grade(gradebook)
    while more():
        add_student_grade(gradebook)

    display_grades(gradebook)


def add_student_grade(gradebook: dict) -> None:
    student_email, student_grade = get_grade()

    if student_email not in gradebook:
        gradebook[student_email] = []

    gradebook[student_email].append(student_grade)


def get_grade() -> tuple:
    student_email = input("Enter the student email:\n" if UI else "")
    student_grade = float(input("Enter the students grade:\n" if UI else ""))

    return student_email, student_grade


def more() -> bool:
    """Checks if the user wants to add more grades."""

    answer = input("Would you like to add another grade (y/n)?:\n" if UI else "")
    return answer.lower() != "n"


def display_grades(gradebook: dict) -> None:
    for student_email, grades in sorted(gradebook.items()):
        average_grade = sum(grades) / len(grades)
        print(f"{student_email}: {round(average_grade, 2)}")


if __name__ == "__main__":
    main()
