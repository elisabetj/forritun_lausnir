from solution_code import (
    calculate_quiz_grade,
    calculate_combined_quiz_grade,
    calculate_assignment_grade,
    calculate_project_grade,
    calculate_exam_grade,
    calculate_final_grade,
)

"""
I/O tests:

Test case 1 (0. File not found):

Input:
Number 12 Grimmauld Place.txt

Output:
Enter filename: File 'Number 12 Grimmauld Place.txt' not found


Unit tests:

Test case 2 (1.1. Quiz grades):
"""

import unittest

from main import calculate_quiz_grade


EPSILON = 0.00000001  # allowed rounding error


class CodingRoomsUnitTests(unittest.TestCase):
    def test_calculate_quiz_grade_6(self):
        # Arrange
        test_input = [1.0, 0.4, 0.6]
        expected = 0.6

        # Act
        actual = calculate_quiz_grade(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_quiz_grade_7(self):
        # Arrange
        test_input = [1.0, 0.5, 0.7, 0.2, 0.9]
        expected = 0.7

        # Act
        actual = calculate_quiz_grade(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_quiz_grade_9(self):
        # Arrange
        test_input = [0.9, 0.8, 0.9, 0.7, 1.0, 0.6, 0.8, 0.9, 1.0]
        expected = 0.9

        # Act
        actual = calculate_quiz_grade(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)


if __name__ == "__main__":
    unittest.main()


"""
Test case 3 (1.2. Combined quiz grades):
"""

import unittest

from main import calculate_combined_quiz_grade


EPSILON = 0.00000001  # allowed rounding error


class CodingRoomsUnitTests(unittest.TestCase):
    def test_calculate_combined_quiz_grade_75(self):
        # Arrange
        ind_grades = [1.0, 0.4, 0.6]
        group_grades = [1.0, 0.6, 0.9]
        expected = 0.75

        # Act
        actual = calculate_combined_quiz_grade(ind_grades, group_grades)

        # Assert
        message = "\n\nInput:"
        message += f"\n ind_grades ({type(ind_grades)}):\n{ind_grades}"
        message += f"\n group_grades ({type(group_grades)}):\n{group_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_combined_quiz_grade_8(self):
        # Arrange
        ind_grades = [1.0, 0.5, 0.7, 0.2, 0.9]
        group_grades = [1.0, 0.8, 0.9, 0.6, 1.0]
        expected = 0.8

        # Act
        actual = calculate_combined_quiz_grade(ind_grades, group_grades)

        # Assert
        message = "\n\nInput:"
        message += f"\n ind_grades ({type(ind_grades)}):\n{ind_grades}"
        message += f"\n group_grades ({type(group_grades)}):\n{group_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_combined_quiz_grade_925(self):
        # Arrange
        ind_grades = [0.9, 0.8, 0.9, 0.7, 1.0, 0.6, 0.7, 0.9, 1.0]
        group_grades = [0.9, 0.9, 1.0, 0.9, 1.0, 0.8, 0.8, 1.0, 1.0]
        expected = 0.925

        # Act
        actual = calculate_combined_quiz_grade(ind_grades, group_grades)

        # Assert
        message = "\n\nInput:"
        message += f"\n ind_grades ({type(ind_grades)}):\n{ind_grades}"
        message += f"\n group_grades ({type(group_grades)}):\n{group_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)


if __name__ == "__main__":
    unittest.main()


"""
Test case 4 (2.1. Assignment grades):
"""

import unittest

from main import calculate_assignment_grade


EPSILON = 0.00000001  # allowed rounding error


class CodingRoomsUnitTests(unittest.TestCase):
    def test_calculate_assignment_grade_1_basic_no_extra(self):
        # Arrange
        assignment_grades = [1.0]
        extra_assignment_grades = []
        expected = 1.0

        # Act
        actual = calculate_assignment_grade(assignment_grades, extra_assignment_grades)

        # Assert
        message = "\n\nInput:"
        message += (
            f"\n assignment_grades ({type(assignment_grades)}):\n{assignment_grades}"
        )
        message += f"\n extra_assignment_grades ({type(extra_assignment_grades)}):\n{extra_assignment_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_assignment_grade_2_basic_no_extra(self):
        # Arrange
        assignment_grades = [1.0, 0.0]
        extra_assignment_grades = []
        expected = 1.0

        # Act
        actual = calculate_assignment_grade(assignment_grades, extra_assignment_grades)

        # Assert
        message = "\n\nInput:"
        message += (
            f"\n assignment_grades ({type(assignment_grades)}):\n{assignment_grades}"
        )
        message += f"\n extra_assignment_grades ({type(extra_assignment_grades)}):\n{extra_assignment_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_assignment_grade_2_basic_2_extra_on_boundary(self):
        # Arrange
        assignment_grades = [0.5, 0.5]
        extra_assignment_grades = [0.0, 0.0]
        expected = 1.0

        # Act
        actual = calculate_assignment_grade(assignment_grades, extra_assignment_grades)

        # Assert
        message = "\n\nInput:"
        message += (
            f"\n assignment_grades ({type(assignment_grades)}):\n{assignment_grades}"
        )
        message += f"\n extra_assignment_grades ({type(extra_assignment_grades)}):\n{extra_assignment_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_assignment_grade_2_basic_2_extra(self):
        # Arrange
        assignment_grades = [0.7, 0.4]
        extra_assignment_grades = [0.0, 0.0]
        expected = 1.0

        # Act
        actual = calculate_assignment_grade(assignment_grades, extra_assignment_grades)

        # Assert
        message = "\n\nInput:"
        message += (
            f"\n assignment_grades ({type(assignment_grades)}):\n{assignment_grades}"
        )
        message += f"\n extra_assignment_grades ({type(extra_assignment_grades)}):\n{extra_assignment_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_assignment_grade_2_basic_2_extra_below_10(self):
        # Arrange
        assignment_grades = [0.2, 0.4]
        extra_assignment_grades = [0.0, 0.0]
        expected = 0.6

        # Act
        actual = calculate_assignment_grade(assignment_grades, extra_assignment_grades)

        # Assert
        message = "\n\nInput:"
        message += (
            f"\n assignment_grades ({type(assignment_grades)}):\n{assignment_grades}"
        )
        message += f"\n extra_assignment_grades ({type(extra_assignment_grades)}):\n{extra_assignment_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_assignment_grade_20_basic_20_extra(self):
        # Arrange
        assignment_grades = [
            1.0,
            0.9,
            1.0,
            0.7,
            0.5,
            0.3,
            0.2,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]
        extra_assignment_grades = [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]
        expected = 0.46

        # Act
        actual = calculate_assignment_grade(assignment_grades, extra_assignment_grades)

        # Assert
        message = "\n\nInput:"
        message += (
            f"\n assignment_grades ({type(assignment_grades)}):\n{assignment_grades}"
        )
        message += f"\n extra_assignment_grades ({type(extra_assignment_grades)}):\n{extra_assignment_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)


if __name__ == "__main__":
    unittest.main()


"""
Test case 5 (2.2. Extra assignment grades):
"""

import unittest

from main import calculate_assignment_grade


EPSILON = 0.00000001  # allowed rounding error


class CodingRoomsUnitTests(unittest.TestCase):
    def test_calculate_assignment_grade_20_basic_20_extra_affect(self):
        # Arrange
        assignment_grades = [
            1.0,
            0.9,
            1.0,
            0.7,
            0.5,
            0.3,
            0.2,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]
        extra_assignment_grades = [
            1.0,
            0.7,
            0.1,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]
        expected = 0.525

        # Act
        actual = calculate_assignment_grade(assignment_grades, extra_assignment_grades)

        # Assert
        message = "\n\nInput:"
        message += (
            f"\n assignment_grades ({type(assignment_grades)}):\n{assignment_grades}"
        )
        message += f"\n extra_assignment_grades ({type(extra_assignment_grades)}):\n{extra_assignment_grades}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)


if __name__ == "__main__":
    unittest.main()


"""
Test case 6 (3. Project grades):
"""

import unittest

from main import calculate_project_grade


EPSILON = 0.00000001  # allowed rounding error


class CodingRoomsUnitTests(unittest.TestCase):
    def test_calculate_project_grade_1_project(self):
        # Arrange
        test_input = [1.0]
        expected = 1

        # Act
        actual = calculate_project_grade(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_project_grade_4_projects(self):
        # Arrange
        test_input = [0.9, 0.8, 0.6, 0.7]
        expected = 0.75

        # Act
        actual = calculate_project_grade(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_project_grade_7_projects(self):
        # Arrange
        test_input = [0.9, 0.8, 0.6, 0.7, 0.8, 0.7, 0.4]
        expected = 0.7

        # Act
        actual = calculate_project_grade(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_project_grade_8_projects(self):
        # Arrange
        test_input = [0.9, 0.8, 0.6, 0.7, 0.8, 0.7, 0.2, 0.4]
        expected = 0.7

        # Act
        actual = calculate_project_grade(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_project_grade_11_projects(self):
        # Arrange
        test_input = [0.9, 0.8, 0.6, 0.7, 0.3, 0.5, 0.8, 0.9, 0.4, 0.9, 0.1]
        expected = 0.8

        # Act
        actual = calculate_project_grade(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)


if __name__ == "__main__":
    unittest.main()


"""
Test case 7 (4. Exam grades):
"""

import unittest

from main import calculate_exam_grade


EPSILON = 0.00000001  # allowed rounding error


class CodingRoomsUnitTests(unittest.TestCase):
    def test_calculate_exam_grade_1_lower_1_higher(self):
        # Arrange
        midterm_grades = [1.0, 0.6]
        final_grade = 0.7
        expected = 0.75

        # Act
        actual = calculate_exam_grade(midterm_grades, final_grade)

        # Assert
        message = f"\n\nInput:"
        message += f"\n midterm_grades ({type(midterm_grades)}):\n{midterm_grades}"
        message += f"\n final_grade ({type(final_grade)}):\n{final_grade}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_exam_grade_2_lower(self):
        # Arrange
        midterm_grades = [0.5, 0.6]
        final_grade = 0.7
        expected = 0.7

        # Act
        actual = calculate_exam_grade(midterm_grades, final_grade)

        # Assert
        message = f"\n\nInput:"
        message += f"\n midterm_grades ({type(midterm_grades)}):\n{midterm_grades}"
        message += f"\n final_grade ({type(final_grade)}):\n{final_grade}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_exam_grade_2_higher(self):
        # Arrange
        midterm_grades = [0.9, 0.8]
        final_grade = 0.64
        expected = 0.71

        # Act
        actual = calculate_exam_grade(midterm_grades, final_grade)

        # Assert
        message = f"\n\nInput:"
        message += f"\n midterm_grades ({type(midterm_grades)}):\n{midterm_grades}"
        message += f"\n final_grade ({type(final_grade)}):\n{final_grade}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_exam_grade_perfect_final(self):
        # Arrange
        midterm_grades = [0.6, 0.1]
        final_grade = 1.0
        expected = 1.0

        # Act
        actual = calculate_exam_grade(midterm_grades, final_grade)

        # Assert
        message = f"\n\nInput:"
        message += f"\n midterm_grades ({type(midterm_grades)}):\n{midterm_grades}"
        message += f"\n final_grade ({type(final_grade)}):\n{final_grade}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_exam_grade_perfect(self):
        # Arrange
        midterm_grades = [1.0, 1.0]
        final_grade = 1.0
        expected = 1.0

        # Act
        actual = calculate_exam_grade(midterm_grades, final_grade)

        # Assert
        message = f"\n\nInput:"
        message += f"\n midterm_grades ({type(midterm_grades)}):\n{midterm_grades}"
        message += f"\n final_grade ({type(final_grade)}):\n{final_grade}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_exam_grade_perfect_midterms(self):
        # Arrange
        midterm_grades = [1.0, 1.0]
        final_grade = 0.7
        expected = 0.8

        # Act
        actual = calculate_exam_grade(midterm_grades, final_grade)

        # Assert
        message = f"\n\nInput:"
        message += f"\n midterm_grades ({type(midterm_grades)}):\n{midterm_grades}"
        message += f"\n final_grade ({type(final_grade)}):\n{final_grade}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)


if __name__ == "__main__":
    unittest.main()


"""
Test case 8 (5. Final grades):
"""

import unittest

from main import calculate_final_grade


EPSILON = 0.00000001  # allowed rounding error


class CodingRoomsUnitTests(unittest.TestCase):
    def test_calculate_final_grade_86(self):
        # Arrange
        quiz_grade = 1.0
        assignment_grade = 1.0
        project_grade = 0.9
        exam_grade = 0.8
        expected = 0.86

        # Act
        actual = calculate_final_grade(
            quiz_grade, assignment_grade, project_grade, exam_grade
        )

        # Assert
        message = f"\n\nInput:"
        message += f"\n quiz_grade: {quiz_grade} ({type(quiz_grade)})"
        message += f"\n assignment_grade: {assignment_grade} ({type(assignment_grade)})"
        message += f"\n project_grade: {project_grade} ({type(project_grade)})"
        message += f"\n exam_grade: {exam_grade} ({type(exam_grade)})"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_final_grade_59(self):
        # Arrange
        quiz_grade = 0.6
        assignment_grade = 0.9
        project_grade = 0.7
        exam_grade = 0.5
        expected = 0.59

        # Act
        actual = calculate_final_grade(
            quiz_grade, assignment_grade, project_grade, exam_grade
        )

        # Assert
        message = f"\n\nInput:"
        message += f"\n quiz_grade: {quiz_grade} ({type(quiz_grade)})"
        message += f"\n assignment_grade: {assignment_grade} ({type(assignment_grade)})"
        message += f"\n project_grade: {project_grade} ({type(project_grade)})"
        message += f"\n exam_grade: {exam_grade} ({type(exam_grade)})"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_final_grade_6(self):
        # Arrange
        quiz_grade = 0.0
        assignment_grade = 0.0
        project_grade = 0.0
        exam_grade = 1.0
        expected = 0.6

        # Act
        actual = calculate_final_grade(
            quiz_grade, assignment_grade, project_grade, exam_grade
        )

        # Assert
        message = f"\n\nInput:"
        message += f"\n quiz_grade: {quiz_grade} ({type(quiz_grade)})"
        message += f"\n assignment_grade: {assignment_grade} ({type(assignment_grade)})"
        message += f"\n project_grade: {project_grade} ({type(project_grade)})"
        message += f"\n exam_grade: {exam_grade} ({type(exam_grade)})"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)

    def test_calculate_final_grade_5(self):
        # Arrange
        quiz_grade = 0.5
        assignment_grade = 0.5
        project_grade = 0.5
        exam_grade = 0.5
        expected = 0.5

        # Act
        actual = calculate_final_grade(
            quiz_grade, assignment_grade, project_grade, exam_grade
        )

        # Assert
        message = f"\n\nInput:"
        message += f"\n quiz_grade: {quiz_grade} ({type(quiz_grade)})"
        message += f"\n assignment_grade: {assignment_grade} ({type(assignment_grade)})"
        message += f"\n project_grade: {project_grade} ({type(project_grade)})"
        message += f"\n exam_grade: {exam_grade} ({type(exam_grade)})"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPSILON, message)


if __name__ == "__main__":
    unittest.main()


"""
I/O tests (Use strict whitespace):

Test case 9 (6.1. Complete output before final exam):
Description: Final exam not included in file

Input:
Muggle Studies 2021-3 (T-111-MUST) standard grades.csv

Output:
Enter filename: 
Name                                  Quizzes (10%)     Assignments (10%)     Projects (20%)     Exam grade (60%)   Final grade (100%) 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Hermione Granger                          10.00               10.00               10.00                3.27                6.0
Angelina Johnson                           9.72               10.00               10.00                3.29                5.9
Harry Potter                               9.85               10.00                9.86                3.31                5.9
Adrian Pucey                               9.74               10.00                9.93                3.25                5.9
Millicent Bulstrode                        9.60               10.00                9.86                3.29                5.9
Kevin Entwhistle                           9.85               10.00                9.64                3.29                5.9
Ronald Weasley                             9.34               10.00                9.71                3.33                5.9
Dean Thomas                                8.45               10.00               10.00                3.31                5.8
Justin Finch-Fletchley                     9.25               10.00                9.93                3.19                5.8
Morag McDougal                             9.15               10.00                9.79                3.12                5.7
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Test case 10 (6.2. Complete output after final exam):
Description: Final exam included in file

Input:
Muggle Studies 2021-3 (T-111-MUST) standard grades - with final exam included.csv

Output:
Enter filename: 
Name                                  Quizzes (10%)     Assignments (10%)     Projects (20%)     Exam grade (60%)   Final grade (100%) 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Hermione Granger                          10.00               10.00               10.00               10.00               10.0
Angelina Johnson                           9.72               10.00               10.00               10.00               10.0
Morag McDougal                             9.15               10.00                9.79               10.00                9.9
Dean Thomas                                8.45               10.00               10.00               10.00                9.8
Katie Bell                                 8.31               10.00                9.93                9.90                9.8
Anthony Goldstein                          8.70               10.00                8.43               10.00                9.6
Ronald Weasley                             9.34               10.00                9.71                9.40                9.5
Kevin Entwhistle                           9.85               10.00                9.64                9.22                9.4
Percy Ignatius Weasley                     8.51               10.00                8.29                9.90                9.4
Justin Finch-Fletchley                     9.25               10.00                9.93                9.12                9.4
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
