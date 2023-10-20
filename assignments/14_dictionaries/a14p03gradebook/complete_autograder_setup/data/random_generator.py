#!/usr/bin/python3
import random
import sys
from string import ascii_lowercase, digits
from typing import List, Tuple

random.seed(sys.argv[-1])

MIN_STUDENTS = int(sys.argv[1])
MAX_STUDENTS = int(sys.argv[2])
assert 1 <= MIN_STUDENTS <= MAX_STUDENTS
NUM_STUDENTS = random.randint(MIN_STUDENTS, MAX_STUDENTS)

MIN_GRADES_PER_STUDENT = int(sys.argv[3])
MAX_GRADES_PER_STUDENT = int(sys.argv[4])
assert 1 <= MIN_GRADES_PER_STUDENT <= MAX_GRADES_PER_STUDENT

YES = "y"
NO = "n"


def main():
    grade_list = generate_grade_list()
    n = len(grade_list)
    for i, (email, grade) in enumerate(grade_list):
        print(email)
        print(grade)
        if i < n - 1:
            print(YES)
        else:
            assert i == n - 1
            print(NO)


def generate_grade_list() -> List[Tuple[str, int]]:
    students = generate_distinct_emails()
    grades = []
    for student in students:
        grades_for_student = generate_grades()
        student_grade_list = [(student, grade) for grade in grades_for_student]
        grades.extend(student_grade_list)

    return grades


def generate_distinct_emails() -> List[str]:
    emails = [random_email() for _ in range(NUM_STUDENTS)]
    emails = list(set(emails))

    while len(emails) < NUM_STUDENTS:
        email = random_email()
        while email in emails:
            email = random_email()

        emails.append(email)

    assert len(emails) == len(set(emails))
    return emails


def random_email() -> str:
    length = random.randint(1, 10)
    name = "".join(random.choices(ascii_lowercase, k=length))
    year = "".join(random.choices(digits, k=2))
    at_symbol = "@"
    domain = "ru.is"
    return "".join([name, year, at_symbol, domain])


def generate_grades() -> List[int]:
    number_of_grades = random.randint(MIN_GRADES_PER_STUDENT, MAX_GRADES_PER_STUDENT)
    return [random_grade() for _ in range(number_of_grades)]


def random_grade() -> int:
    return random.randint(0, 10)


if __name__ == "__main__":
    main()
