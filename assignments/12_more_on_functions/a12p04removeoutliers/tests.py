"""
Unit tests:
"""

import unittest
from copy import deepcopy

from solution_code import remove_min_and_max, without_outliers


class OutliersUnitTests(unittest.TestCase):
    # Test case 1:
    def test_1(self):
        # Arrange
        test_input = [21, 1, 23, 102]
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        expected = [21, 23]

        # Act
        remove_min_and_max(test_input)
        actual = test_input

        # Assert
        message += f"\n\nExpected result ({type(expected)}):\n{expected}"
        message += f"\n\nActual result ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    # Test case 2:
    def test_2(self):
        # Arrange
        test_input = [5, 4, 3, 2, 1, 0]
        expected = [4, 3, 2, 1]
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        remove_min_and_max(test_input)
        actual = test_input

        # Assert
        message += f"\n\nExpected result ({type(expected)}):\n{expected}"
        message += f"\n\nActual result ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 3:
    """

    def test_3_input_unaltered(self):
        # Arrange
        test_input = [21, 1, 23, 102]
        original_test_input = deepcopy(test_input)
        expected = original_test_input
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        result = without_outliers(test_input)
        actual = test_input

        # Assert
        message += f"\n\nYour function seems to have altered the given list."
        message += f"\nThe list is supposed to remain unchanged as:"
        message += f"\nExpected ({type(expected)}):\n{expected}"
        message += f"\n\nBut you seem to have changed it to:"
        message += f"\nActual ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_3_output(self):
        # Arrange
        test_input = [21, 1, 23, 102]
        expected = [21, 23]
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        actual = without_outliers(test_input)

        # Assert
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 4:
    """

    def test_4_input_unaltered(self):
        # Arrange
        test_input = [5, 4, 3, 2, 1, 0]
        original_test_input = deepcopy(test_input)
        expected = original_test_input
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        result = without_outliers(test_input)
        actual = test_input

        # Assert
        message += f"\n\nYour function seems to have altered the given list."
        message += f"\nThe list is supposed to remain unchanged as:"
        message += f"\nExpected ({type(expected)}):\n{expected}"
        message += f"\n\nBut you seem to have changed it to:"
        message += f"\nActual ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_4_output(self):
        # Arrange
        test_input = [5, 4, 3, 2, 1, 0]
        expected = [4, 3, 2, 1]
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        actual = without_outliers(test_input)

        # Assert
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()


"""
I/O tests:

Test case 5:

Input:

Output:
Before calling remove_min_and_max: a_list = [3, 9, 5, 1, 6, 8]
After calling remove_min_and_max: a_list = [3, 5, 6, 8]
Before calling without_outliers: b_list = [9, 2, 3, 6, 1, 8, 7]
After calling without_outliers: b_list = [9, 2, 3, 6, 1, 8, 7]
After calling without_outliers: c_list = [2, 3, 6, 8, 7]
"""
