"""
Unit tests:
"""

import unittest
from copy import deepcopy

from solution_code import remove_odds, extract_evens


class RemoveOddsUnitTests(unittest.TestCase):

    """
    Test case 1:
    """

    def test_1(self):
        # Arrange
        test_input = [1, 1, 2, 3, 4, 5]
        expected = [2, 4]
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        remove_odds(test_input)
        actual = test_input

        # Assert
        message += f"\n\nExpected result ({type(expected)}):\n{expected}"
        message += f"\n\nActual result ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 2:
    """

    def test_2(self):
        # Arrange
        test_input = [10, 7, 7, 7, 7, 1, 10, 9, 9]
        expected = [10, 10]
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        remove_odds(test_input)
        actual = test_input

        # Assert
        message += f"\n\nExpected result ({type(expected)}):\n{expected}"
        message += f"\n\nActual result ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


class ExtractEvensUnitTests(unittest.TestCase):

    """
    Test case 3:
    """

    def test_3_input_unaltered(self):
        # Arrange
        test_input = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        original_test_input = deepcopy(test_input)
        expected = original_test_input
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        result = extract_evens(test_input)
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
        test_input = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [2, 4, 6, 8, 10]
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        actual = extract_evens(test_input)

        # Assert
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 4:
    """

    def test_4_input_unaltered(self):
        # Arrange
        test_input = [9, 1, 3, 3, 52, 7]
        original_test_input = deepcopy(test_input)
        expected = original_test_input
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        result = extract_evens(test_input)
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
        test_input = [9, 1, 3, 3, 52, 7]
        expected = [52]
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"

        # Act
        actual = extract_evens(test_input)

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
a_list initially: [1, 1, 2, 3, 4, 5]
a_list after removing odds: [2, 4]
b_list initially: [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_list after extracting evens: [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c_list after extracting evens: [2, 4, 6, 8, 10]
"""
