"""
I/O tests:

Test case 1:

Input:
100000

Output:


Test case 2:

Input:
1000000

Output:
142857


Unit tests:
"""

import unittest

from solution_code import is_permutative


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Test case 3:
    def test_single_digit(self):
        # Arrange
        test_input = 6
        expected = True

        # Act
        actual = is_permutative(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    # Test case 4:
    def test_1035(self):
        # Arrange
        test_input = 1035
        expected = False

        # Act
        actual = is_permutative(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    # Test case 5:
    def test_142857(self):
        # Arrange
        test_input = 142857
        expected = True

        # Act
        actual = is_permutative(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    # Test case 6:
    def test_153846(self):
        # Arrange
        test_input = 153846
        expected = False

        # Act
        actual = is_permutative(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    # Test case 7:
    def test_285714(self):
        # Arrange
        test_input = 285714
        expected = False

        # Act
        actual = is_permutative(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    # Test case 8:
    def test_2178(self):
        # Arrange
        test_input = 2178
        expected = False

        # Act
        actual = is_permutative(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()
