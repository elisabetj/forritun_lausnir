"""
I/O tests:

Test case 1:

Input:
3511
3151

Output:
The numbers 3511 and 3151 are permutations of each other.


Test case 2:

Input:
3511
6329

Output:
The numbers 3511 and 6329 are not permutations of each other.


Unit tests:
"""

import unittest

from solution_code import are_permutation_of_same_digits


class PermutationsUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Test case 3:
    def test_3511_and_3135(self):
        # Arrange
        test_input_m = "3511"
        test_input_n = "3135"
        expected = False

        # Act
        actual = are_permutation_of_same_digits(test_input_m, test_input_n)

        # Assert
        message = f"\n\nInput m ({type(test_input_m)}):\n{test_input_m}"
        message += f"\n\nInput n ({type(test_input_n)}):\n{test_input_n}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    # Test case 4:
    def test_equal(self):
        # Arrange
        test_input_m = "315"
        test_input_n = "315"
        expected = True

        # Act
        actual = are_permutation_of_same_digits(test_input_m, test_input_n)

        # Assert
        message = f"\n\nInput m ({type(test_input_m)}):\n{test_input_m}"
        message += f"\n\nInput n ({type(test_input_n)}):\n{test_input_n}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    # Test case 5:
    def test_single_digit(self):
        # Arrange
        test_input_m = "7"
        test_input_n = "9"
        expected = False

        # Act
        actual = are_permutation_of_same_digits(test_input_m, test_input_n)

        # Assert
        message = f"\n\nInput m ({type(test_input_m)}):\n{test_input_m}"
        message += f"\n\nInput n ({type(test_input_n)}):\n{test_input_n}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()
