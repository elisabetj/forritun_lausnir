"""A program that calculates final grades of students in this course.

Takes as input a .csv file exported from the gradebook on Mímir.
Extracts information for every student on how many points they scored
in individual quizzes, assignments, projects and exams,
as well as the maximum available points for each.

Since not all of those have been performed already,
it is unknown at this time in which order they will appear in the file.
So this program identifies the columns dynamically
(after the semester is over, it would be possible to simplify this program
by providing this mapping as hard-coded constants).

Next, it standardizes all grades to the scale 0.0 - 1.0,
and then proceeds to calculate the final grades
based on the specifications as given on Canvas (under Home -> Assessment):
https://reykjavik.instructure.com/courses/6232/pages/assessment?titleize=0

Finally, this program prints out the grades of the top 10 students (nicely formatted),
to show an example of what can be done with the results.
"""

import operator


# https://stackoverflow.com/questions/6088581/what-are-python-best-practices-for-dictionary-dict-key-constants
FIRST_NAME = "first name"
LAST_NAME = "last name"
NAME = "name"
EMAIL = "email"
SECTION = "section"

QUIZZES = "quiz"
QUIZZES_IND = "individual quiz"
QUIZZES_GROUP = "group quiz"
ASSIGNMENTS = "assignment"
EXTRA_ASSIGNMENTS = "extra assignment"
PROJECTS = "project"
MIDTERMS = "midterm"
FINAL_EXAM = "final exam"

EXAM = "exam"
FINAL = "final"

SCORE = "_score"
GRADE = " grade"  # Notice any inconsistency that you would like to fix?
SCORES = f"{SCORE}s"
GRADES = f"{GRADE}s"

EXAM_GRADE = f"{EXAM}{GRADE}"
FINAL_GRADE = f"{FINAL}{GRADE}"


def main():
    filename = input("Enter filename: ")
    # Implement your solution
    display_grades([])


# You should use your code from the previous question,
# but here are some functions that you need to implement for the unit tests,
# and they should also prove useful.
def calculate_combined_quiz_grade(
    individual_quiz_grades: list, group_quiz_grades: list
) -> float:
    """Calculates the contribution from the quiz grades toward the final grade.

    Follows the Assessment specification on Canvas:
    - Short quizzes in class: 10%  (75% best count).  Individual quizzes 5%, group quizzes 5%

    Calculates the grades separately for individual quizzes and group quizzes,
    then combines the two.

    Args:
      individual_quiz_grades:
        A list of a particular student's grades from individual quizzes.
        Will not be modified.
      group_quiz_grades:
        A list of a particular student's grades from group quizzes.
        Will not be modified.

    Returns:
        A single combined grade from the quizzes (both individual and group quizzes).
    """

    raise NotImplementedError  # remove this line and provide your implementation.
    # Hint: You can call calculate_quiz_grade() twice,
    # once for the individual quizzes and once for the group quizzes.


def calculate_quiz_grade(quiz_grades: list) -> float:
    """Calculates the contribution from the quiz grades toward the final grade.

    Follows the Assessment specification on Canvas:
    - Short quizzes in class: 10%  (75% best count).  Individual quizzes 5%, group quizzes 5%

    Drops the lowest quarter of grades, and averages the rest.

    Args:
      quiz_grades:
        A list of a particular student's quiz grades (for either individual or group quizzes).
        Will not be modified.

    Returns:
        A single combined grade from the given category of quizzes.
    """

    raise NotImplementedError  # remove this line and provide your implementation.


def calculate_assignment_grade(
    assignment_grades: list, extra_assignment_grades: list
) -> float:
    """Calculates the contribution from the assignment grades toward the final grade.

    Follows the Assessment specification on Canvas:
    - Programming projects in class: 10% (Full points if the students gets 50%, on average, for these projects over the whole term)

    Calculates the average, and scales up by a factor of 2 (limited to full points)

    Args:
      assignment_grades:
        A list of a particular student's assignment grades.
        Will not be modified.
      extra_assignment_grades:
        A list of the same student's extra assignment grades.
        Will not be modified.

    Returns:
        A single combined grade from the assignments and the extra assignments.
    """

    raise NotImplementedError  # remove this line and provide your implementation.


def calculate_project_grade(project_grades: list) -> float:
    """Calculates the contribution from the project grades toward the final grade.

    Follows the Assessment specification on Canvas:
    - Homework/weekly projects (max group size 2): 20% (7 best of 11 count)

    Drops the lowest 4, and averages the remaining 7.

    Args:
      project_grades:
        A list of a particular student's project grades.
        Will not be modified.

    Returns:
        A single combined grade from the projects.
    """

    raise NotImplementedError  # remove this line and provide your implementation.


def calculate_exam_grade(midterm_grades: list, final_exam_grade: float) -> float:
    """Calculates the contribution from the grades from the midterm exams and final exam toward the final grade.

    Follows the Assessment specification on Canvas:
    - Midterm exams: 20%  (Two midterms, no repeat exam)
    - Final exam: 40-60%.  The grade of 5 is needed to pass the course.
    - If a student obtains a higher grade in the final exam compared to the midterm exams,
    - then the weight of the final exam is 60%, otherwise 40%.

    Each midterm grade contributes 10% to the final grade,
    but only those that are higher than the grade from the final exam.
    Those that are lower are ignored, and the final exam counts more instead.

    Args:
      midterm_grades:
        A list of a particular student's midterm grades.
        Will not be modified.
      final_exam_grade:
        The same student's final exam grade.

    Returns:
        A single combined grade from the midterms and the final exam.
    """

    raise NotImplementedError  # remove this line and provide your implementation.


def calculate_final_grade(
    quiz_grade: float, assignment_grade: float, project_grade: float, exam_grade: float
) -> float:
    """Calculates the final grade from the various contributing factors.

    Follows the Assessment specification on Canvas:
    - Short quizzes in class: 10%
    - Programming projects in class: 10%
    - Homework projects (max group size 2): 20%
    - Midterm exams: 20%
    - Final exam: 40-60%.
    - If a student obtains a higher grade in the final exam compared to the midterm exams,
    - then the weight of the final exam is 60%, otherwise 40%.

    Calculates the weighted average of the quizzes, class projects (assignments), homework projects and exams (miderms and final exam),
    with weights:
        10% - quizzes
        10% - assignments
        20% - projects
        60% - exams

    Args:
      quiz_grade:
        A single combined grade from the quizzes.
      assignment_grade:
        A single combined grade from the assignments and the extra assignments.
      project_grade:
        A single combined grade from the projects.
      exam_grade:
        A single combined grade from the midterms and the final exam.

    Returns:
        A single combined grade from the quizzes, assignments, projects and exams.
    """

    raise NotImplementedError  # remove this line and provide your implementation.


# You might find the following function useful.
# It contains the details necessary to get the form of the presentation correct,
# such as whitespace padding and so on.
def display_grades(student_dicts: list) -> None:
    """Prints out the top 10 student grades.

    Args:
      student_dicts:
        A list of dictionaries, one for each student, containing name and final grade,
        along with intermediate grades for each category.
        Will not be modified.
    """

    NAME_WIDTH = 35
    HEADER_WIDTH = 20
    RIGHT_ALIGN = 11
    DECIMAL_PLACES_INTERMEDIATE = 2
    DECIMAL_PLACES_FINAL = 1
    HORIZONTAL_SEPARATOR = "-" * 180

    descending = sorted(
        student_dicts, key=operator.itemgetter(FINAL_GRADE), reverse=True
    )
    top_ten = []
    # If only we had some way of getting a list of the top ten students. Hmm...

    print(f"\n{'Name':{NAME_WIDTH}}", end="")
    for header in [
        "Quizzes (10%)",
        "Assignments (10%)",
        "Projects (20%)",
        "Exam grade (60%)",  # Combined grade from midterms and final exam
        "Final grade (100%)",
    ]:
        print(f"{header:^{HEADER_WIDTH}}", end="")
    print()

    print(HORIZONTAL_SEPARATOR)
    for student in top_ten:
        print(f"{student[NAME]:{NAME_WIDTH}}", end="")
        for category in [QUIZZES, ASSIGNMENTS, PROJECTS, EXAM]:
            grade = student[f"{category}{GRADE}"]
            print(f"{10*grade:^{HEADER_WIDTH}.{DECIMAL_PLACES_INTERMEDIATE}f}", end="")
        print(f"{10*student[FINAL_GRADE]:>{RIGHT_ALIGN}.{DECIMAL_PLACES_FINAL}f}")
    print(HORIZONTAL_SEPARATOR)


if __name__ == "__main__":
    main()
