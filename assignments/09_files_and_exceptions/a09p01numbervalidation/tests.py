import unittest

from solution_code import is_float


class NumberValidationUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_decimal(self):
        # Arrange
        test_input = "3.45"
        expected = True

        # Act
        actual = is_float(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_scientific_notation(self):
        # Arrange
        test_input = "3e4"
        expected = True

        # Act
        actual = is_float(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_decimal_point_first(self):
        # Arrange
        test_input = ".5"
        expected = True

        # Act
        actual = is_float(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_no_digits(self):
        # Arrange
        test_input = "abc"
        expected = False

        # Act
        actual = is_float(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_mixed(self):
        # Arrange
        test_input = "4.x"
        expected = False

        # Act
        actual = is_float(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()
