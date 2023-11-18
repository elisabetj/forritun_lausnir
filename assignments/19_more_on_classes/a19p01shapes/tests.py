import unittest

from rectangle import Rectangle
from square import Square


class RectangleUnitTests(unittest.TestCase):
    """
    Test case 1 (1. Rectangle):
    """

    def test_area(self):
        # Arrange
        rectangle = Rectangle(2, 3)
        expected = 6

        # Act
        actual = rectangle.get_area()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_perimeter(self):
        # Arrange
        rectangle = Rectangle(2, 3)
        expected = 10

        # Act
        actual = rectangle.get_perimeter()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_string(self):
        # Arrange
        rectangle = Rectangle(2, 3)
        expected = f"Rectangle with area of 6.00 and perimeter of 10.00"

        # Act
        actual = str(rectangle)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


class SquareUnitTests(unittest.TestCase):
    """
    Test case 2 (2. Square):
    """

    def test_area(self):
        # Arrange
        rectangle = Square(3)
        expected = 9

        # Act
        actual = rectangle.get_area()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_perimeter(self):
        # Arrange
        rectangle = Square(3)
        expected = 12

        # Act
        actual = rectangle.get_perimeter()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_string(self):
        # Arrange
        rectangle = Square(3)
        expected = f"Square with area of 9.00 and perimeter of 12.00"

        # Act
        actual = str(rectangle)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
template:


import unittest

from rectangle import Rectangle
from square import Square


class TemplateUnitTests(unittest.TestCase):
    def test_template(self):
        # Arrange
        expected = True

        # Act
        actual = Rectangle()

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()

"""

if __name__ == "__main__":
    unittest.main()
