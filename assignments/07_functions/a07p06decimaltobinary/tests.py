import unittest

from solution_code import decimal_to_binary


class DecimalToBinaryTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Points: 2
    def test_8(self):
        # Arrange
        expected = "1000"

        # Act
        actual = decimal_to_binary(8)

        # Assert
        message = f"\nExpected: {expected}.\nActual: {actual}."
        self.assertEqual(expected, actual, message)

    # Points: 2
    def test_123(self):
        # Arrange
        expected = "1111011"

        # Act
        actual = decimal_to_binary(123)

        # Assert
        message = f"\nExpected: {expected}.\nActual: {actual}."
        self.assertEqual(expected, actual, message)

    # Points: 1
    def test_0(self):
        # Arrange
        expected = "0"

        # Act
        actual = decimal_to_binary(0)

        # Assert
        message = f"\nExpected: {expected}.\nActual: {actual}."
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()
