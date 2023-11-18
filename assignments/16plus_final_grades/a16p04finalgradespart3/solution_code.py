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

import csv
import operator
import math


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

UNIQUE_CATEGORIES = [FIRST_NAME, LAST_NAME, EMAIL, SECTION, FINAL_EXAM]
LIST_CATEGORIES = [
    QUIZZES_IND,
    QUIZZES_GROUP,
    ASSIGNMENTS,
    EXTRA_ASSIGNMENTS,
    PROJECTS,
    MIDTERMS,
]

HEADER_PREFIXES = {
    FIRST_NAME: "First Name",
    LAST_NAME: "Last Name",
    EMAIL: "Email",
    SECTION: "Section",
    QUIZZES: "Quiz",
    ASSIGNMENTS: "Assignment",
    PROJECTS: "Project",
    MIDTERMS: "Midterm",
    FINAL_EXAM: "Final",
}

EXAM = "exam"
FINAL = "final"

SCORE = " score"
GRADE = " grade"
SCORES = f"{SCORE}s"
GRADES = f"{GRADE}s"

EXAM_GRADE = f"{EXAM}{GRADE}"
FINAL_GRADE = f"{FINAL}{GRADE}"


def main():
    filename = input("Enter filename: ")
    grades = read_grades_from_file(filename)

    if grades is None:
        print(f"File '{filename}' not found")
        return

    index_record: dict = identify_columns(headers_line=grades[0])
    max_points: dict = get_points_possible(
        subheaders_line=grades[1], columns=index_record
    )
    student_dicts: list = extract_student_data(
        student_lines=grades[2:], columns=index_record
    )

    calculate_raw_grades(student_dicts, max_points)
    calculate_final_grades(student_dicts)
    display_grades(student_dicts)


def read_grades_from_file(filename: str) -> list:
    """Parses the file into a list of lists, one for each line of the file."""

    try:
        with open(filename, encoding="utf-8") as grade_file:
            return list(csv.reader(grade_file))

    except FileNotFoundError:
        return None


def identify_columns(headers_line: list) -> dict:
    """Figures out what the indices of various headers are.

    Args:
      headers_line:
        The first line of the gradebook, which contains the column headers.
        Will not be modified.

    Returns:
        A dictionary with the indices of all relevant headers.
        For example:

        {
            FIRST_NAME: 0,
            LAST_NAME: 1,
            EMAIL: 2,
            SECTION: 3,
            QUIZZES_IND: [4, 8, 16, 24],
            QUIZZES_GROUP: [6, 12, 20, 28],
            ASSIGNMENTS: [5, 9, 14, 17, 19, 26, 29, 32, 34],
            EXTRA_ASSIGNMENTS: [7, 10, 13, 18, 21, 25, 30],
            PROJECTS: [11, 15, 22, 27, 33],
            MIDTERMS: [23, 31],
            FINAL_EXAM: 35,
        }

        The intended use of this dictionary is demonstrated by the following examples:
        >>> columns = identify_columns(gradebook[0])
        Given a line from the gradebook for a particular student:

        1. The name of the student is found as:
        >>> name = f"{line[columns[FIRST_NAME]]} {line[columns[LAST_NAME]]}"

        2. Index of grade from final exam (which is unique):
        >>> final_exam_score = line[columns[FINAL_EXAM]]

        3. Index of grades from other categories, such as projects:
        >>> project_scores = [line[column] for column in columns[PROJECTS]]
    """

    columns = {}
    for category in LIST_CATEGORIES:
        columns[category] = []

    for index, header in enumerate(headers_line):
        category = determine_category(header)
        if category in LIST_CATEGORIES:
            columns[category].append(index)
        elif category in UNIQUE_CATEGORIES:
            columns[category] = index

    return columns


def determine_category(header: str) -> str:
    """Determines which category the given header belongs to."""

    # Special care must be taken to distinguish between the normal assignments and the extra assignments.
    # The header for assignment 1 begins with "Assignment 1:".
    # The header for assignment 1+ begins with "Assignment 1+:"
    # They share the prefix "Assignment 1"
    # so checking the header for the prefix "Assignment" is not enough to distinguish between these two categories.

    # Special care must also be taken to distinguish between
    # the individual quizzes and the group quizzes,
    # since they share a common prefix.
    # The header for the quizzes from lecture 1 begin with
    # "Quiz 1 (Individual):" and "Quiz 1 (Group):", for example.
    # So checking the header for the prefix "Quiz" is not enough to distinguish between them.

    for category in HEADER_PREFIXES:
        if header.startswith(HEADER_PREFIXES[category]):
            if category == ASSIGNMENTS and "+:" in header:
                return EXTRA_ASSIGNMENTS
            if category == QUIZZES:
                if "(Individual)" in header:
                    return QUIZZES_IND
                else:
                    assert "(Group)" in header
                    return QUIZZES_GROUP
            return category

    return "Unknown"


def get_points_possible(subheaders_line: list, columns: dict) -> dict:
    """Reads maximum available points for each grade from the file.

    Args:
      subheaders_line:
        The second line of the gradebook,
        which contains the maximum available points for each coursework.
        Will not be modified.
      columns:
        A dictionary with the indices of all relevant headers.
        Will not be modified.

    Returns:
        A dictionary with the maximum points that can be scored for each coursework.
        Intended to be used for comparison with grades of an individual student,
        as demonstrated by the following:

        >>> points_possible = get_points_possible(gradebook[1], columns)
        >>> max_points = points_possible[category]
        >>> points = [float(student_line[column]) for column in columns[category]]
        >>> assert len(points) == len(max_points)
        >>> assert all([0 <= score <= maximum > 0 for score, maximum in zip(points, max_points))
        >>> grades = [score / maximum for score, maximum in zip(points, max_points)]
    """

    assert subheaders_line[0] == "Points Possible"
    points_possible = {}
    for category in LIST_CATEGORIES:
        points_possible[category] = [
            float(subheaders_line[column]) for column in columns[category]
        ]
    points_possible[FINAL_EXAM] = (
        float(subheaders_line[columns[FINAL_EXAM]]) if FINAL_EXAM in columns else 1
    )
    return points_possible


def extract_student_data(student_lines: list, columns: dict) -> list:
    """Extracts the student data from the file and organizes it into dictionaries.

    Args:
      student_lines:
        A list of lines from the gradebook (aside from the first two lines).
        Will not be modified.
      columns:
        A dictionary with the indices of all relevant headers.
        Will not be modified.

    Returns:
        A list of dictionaries, one for each student,
        containing the points scored by the student in each coursework,
        along with some basic information about the student.
    """

    student_dicts = []
    for student_line in student_lines:
        student_dict = get_basic_information(student_line, columns)
        for category in LIST_CATEGORIES:
            student_dict[f"{category}{SCORES}"] = [
                float(student_line[column]) for column in columns[category]
            ]
        student_dict[f"{FINAL_EXAM}{SCORE}"] = (
            float(student_line[columns[FINAL_EXAM]]) if FINAL_EXAM in columns else 0
        )
        student_dicts.append(student_dict)

    return student_dicts


def get_basic_information(student_line: list, columns: dict) -> dict:
    """Extracts the basic information about the given student from the file.

    Args:
      student_lines:
        A list of lines from the gradebook (aside from the first two lines).
        Will not be modified.
      columns:
        A dictionary with the indices of all relevant headers.
        Will not be modified.

    Returns:
        A dictionary with the name and email of the given student,
        as well as the section the student is assigned to
        (i.e. which lectures the student is supposed to show up for).
    """

    return {
        NAME: f"{student_line[columns[FIRST_NAME]]} {student_line[columns[LAST_NAME]]}",
        EMAIL: student_line[columns[EMAIL]],
        SECTION: student_line[columns[SECTION]],
    }


def calculate_raw_grades(student_dicts: list, points_possible: dict) -> None:
    """Fills in the individual grades based on scored points and the corresponding maximum points.

    Stores the results into the student dictionaries in the student_dicts list

    Args:
      student_dicts:
        A list of dictionaries, one for each student,
        containing the points scored by the student in each coursework,
        along with some basic information about the student.
        *** WILL BE MODIFIED ***
      points_possible:
        A dictionary with the maximum points that can be scored for each coursework.
        Will not be modified.
    """

    for student_dict in student_dicts:
        for category in LIST_CATEGORIES:
            fill_in_category_grades(
                category,
                student_dict,
                points_possible_for_category=points_possible[category],
            )
        fill_in_final_exam_grade(student_dict, points_possible)


def fill_in_category_grades(
    category: str, student: dict, points_possible_for_category: list
) -> None:
    """Calculates the grades for the given category, based on the scored points and the maximum points.

    Stores the results as a list into the student dictionary.
    For example, if the category is "quiz",
    then the scores will be read from student["quiz scores"]
    and the grades list written to student["quiz grades"]

    Args:
      category:
        The name of the category to fill in.
      student:
        A dictionary containing the points scored by the student in each coursework,
        along with some basic information about the student.
        *** WILL BE MODIFIED ***
      points_possible_for_category:
        A list of the maximum points that can be scored for the given category.
        Will not be modified.
    """

    scores = student[f"{category}{SCORES}"]
    assert len(scores) == len(points_possible_for_category)

    grades = []
    for points, max_points in zip(
        scores, points_possible_for_category
    ):  # iterate through pairs of corresponding elements from these lists
        assert max_points > 0

        points = max(0, min(points, max_points))
        assert 0 <= points <= max_points

        grade = points / max_points
        assert 0 <= grade <= 1

        grades.append(grade)

    student[f"{category}{GRADES}"] = grades


def fill_in_final_exam_grade(student: dict, points_possible: dict) -> None:
    """Calculates the grade from the final exam, based on the scored points and the maximum points.

    Stores the results into the student dictionary.
    Reads the score from student["final exam score"] and
    writes the grade to student["final exam grade"]

    Args:
      student:
        A dictionary containing the points scored by the student in each coursework,
        among other things, such as some basic information about the student.
        *** WILL BE MODIFIED ***
      points_possible:
        A dictionary with the maximum points that can be scored for each coursework.
        Will not be modified.
    """

    points = student[f"{FINAL_EXAM}{SCORE}"]
    max_points = points_possible[FINAL_EXAM]
    assert 0 < max_points

    points = max(0, min(points, max_points))
    assert 0 <= points <= max_points

    grade = points / max_points
    assert 0 <= grade <= 1

    student[f"{FINAL_EXAM}{GRADE}"] = grade


def calculate_final_grades(student_dicts: list) -> None:
    """Calculates the final grades of all students.

    Calculates the grades for each category and, from these, the final grade.
    Stores these results in the student dictionary, for each student.

    Args:
      student_dicts:
        A list of dictionaries, one for each student,
        containing their grades in each coursework,
        among other things, such as some basic information about the student.
        *** WILL BE MODIFIED ***
    """

    for student_dict in student_dicts:
        quiz_grade = calculate_combined_quiz_grade(
            individual_quiz_grades=student_dict[f"{QUIZZES_IND}{GRADES}"],
            group_quiz_grades=student_dict[f"{QUIZZES_GROUP}{GRADES}"],
        )
        assignment_grade = calculate_assignment_grade(
            assignment_grades=student_dict[f"{ASSIGNMENTS}{GRADES}"],
            extra_assignment_grades=student_dict[f"{EXTRA_ASSIGNMENTS}{GRADES}"],
        )
        project_grade = calculate_project_grade(
            project_grades=student_dict[f"{PROJECTS}{GRADES}"]
        )
        exam_grade = calculate_exam_grade(
            midterm_grades=student_dict[f"{MIDTERMS}{GRADES}"],
            final_exam_grade=student_dict[f"{FINAL_EXAM}{GRADE}"],
        )
        final_grade = calculate_final_grade(
            quiz_grade, assignment_grade, project_grade, exam_grade
        )

        student_dict.update(
            {
                f"{QUIZZES}{GRADE}": quiz_grade,
                f"{ASSIGNMENTS}{GRADE}": assignment_grade,
                f"{PROJECTS}{GRADE}": project_grade,
                EXAM_GRADE: exam_grade,
                FINAL_GRADE: final_grade,
            }
        )


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

    ind_quiz_grade = calculate_quiz_grade(quiz_grades=individual_quiz_grades)
    group_quiz_grade = calculate_quiz_grade(quiz_grades=group_quiz_grades)
    quiz_grade = average([ind_quiz_grade, group_quiz_grade])
    assert 0 <= quiz_grade <= 1

    return quiz_grade


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

    quiz_grades = quiz_grades[1:]  # Quiz 0 did not count

    number_to_drop = math.ceil(len(quiz_grades) / 4)
    for _ in range(number_to_drop):
        quiz_grades.remove(min(quiz_grades))

    grade = average(quiz_grades)
    assert 0 <= grade <= 1

    return grade


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

    grade = average(assignment_grades)
    assert 0 <= grade <= 1

    grade = 2 * grade  # scale so that 0.5 becomes 1
    assert 0 <= grade <= 2

    # Extra assignments were provided for students as further practice on more involved problems.
    # In the unlikely case that a student does not get full score for the basic assignments, while doing well on the extra assignments,
    # the extra assignments can give some bonus points.
    # The exact implementation is as follows:

    # First, the grade from each extra assignment is compared to the established grade from the basic assignments,
    # and only those where the student scored higher than the basic grade are taken into account.
    # Of those, the average grade is calculated,
    # and then the total grade for this part is calculated as the weighted average of
    # the grade for the basic assignments and the grade for the extra assignments,
    # where the weight for the basic assignments is half the number of basic assignments,
    # and the weight for the extra assignments is the number of extra assignments being taken into account,
    # but of course scaled so that the weights sum up to 1.

    extras = [
        extra_grade for extra_grade in extra_assignment_grades if extra_grade > grade
    ]
    augmented_grade = weighted_average(
        grades=[grade, average(extras)],
        weights=[len(assignment_grades) / 2, len(extras)],
    )
    assert augmented_grade >= grade
    grade = augmented_grade

    grade = min(1, grade)  # limit to full points
    assert 0 <= grade <= 1

    return grade


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

    project_grades = project_grades[:]

    while len(project_grades) > 7:
        project_grades.remove(min(project_grades))

    grade = average(project_grades)
    assert 0 <= grade <= 1

    return grade


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

    assert len(midterm_grades) <= 2
    exam_grades = [grade for grade in midterm_grades if grade > final_exam_grade]
    weights = [10] * len(exam_grades)

    final_exam_weight = 60 - sum(weights)
    assert 40 <= final_exam_weight <= 60

    weights.append(final_exam_weight)
    assert sum(weights) == 60

    exam_grades.append(final_exam_grade)
    assert len(exam_grades) == len(weights)

    exam_grade = weighted_average(exam_grades, weights)
    assert 0 <= exam_grade <= 1

    return exam_grade


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

    grade = weighted_average(
        [quiz_grade, assignment_grade, project_grade, exam_grade],
        weights=[10, 10, 20, 60],
    )
    assert 0 <= grade <= 1

    return grade


def average(grades: list) -> float:
    """Returns the average of the numbers in the grades list if not empty, otherwise 0."""

    return sum(grades) / len(grades) if grades else 0


def weighted_average(grades: list, weights: list) -> float:
    """Calculates the weighted average of the grades list with respect to the given weights.

    Expects non-negative weights.
    Both lists must be of the same length.

    Args:
      grades:
        A list of numbers.
        Will not be modified.
      weights:
        A list of weights.
        Will not be modified.

    Returns:
        The weighted average if any positive weights found, 0 otherwise.
    """

    assert len(grades) == len(weights)
    for weight in weights:
        assert weight >= 0

    total_weight = sum(weights)
    if total_weight > 0:
        weights = [
            weight / total_weight for weight in weights
        ]  # Does not modify the original.
        assert sum(weights) == 1

    return sum([grade * weight for grade, weight in zip(grades, weights)])


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
    top_ten = descending[:10]

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
