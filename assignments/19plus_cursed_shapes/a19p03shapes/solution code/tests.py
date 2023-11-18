import unittest
from unittest.mock import create_autospec

from shapes import (
    Canvas,
    Shape,
    Rectangle,
    Square,
    Triangle,
    HorizontalLine,
    VerticalLine,
)


class InheritanceUnitTests(unittest.TestCase):
    """
    Test case 1 (Inheritance):
    """

    def test_inheritance(self):
        # Arrange
        rectangle = Rectangle(1, 3, 4, 2)
        square = Square(5, 6, 2)
        triangle = Triangle(8, 0, 3)
        h_line = HorizontalLine(3, 4, 3)
        v_line = VerticalLine(9, 19, 30)

        # Assert
        self.assertTrue(isinstance(rectangle, Shape))
        self.assertTrue(isinstance(square, Rectangle))
        self.assertTrue(isinstance(triangle, Shape))
        self.assertTrue(isinstance(h_line, Shape))
        self.assertTrue(isinstance(v_line, Shape))


class MoveUnitTests(unittest.TestCase):
    """
    Test case 2 (Move):
    """

    def test_move(self):
        # Arrange
        shape = Square(3, 4, 5)

        # Act
        shape.move(0, 0)
        shape.move(3, -2)
        shape.move(-1, 1)

        # Assert
        self.assertEqual(shape.x, 5)
        self.assertEqual(shape.y, 3)


class RectangleUnitTests(unittest.TestCase):
    """
    Test case 3 (Rectangle, w2, h2):
    """

    def test_draw_2_by_2_rectangle(self):
        # Arrange
        mock_canvas = create_autospec(Canvas)
        x = 1
        y = 2
        width = 2
        height = 2

        # Act
        rectangle = Rectangle(x, y, width, height)
        rectangle.draw(mock_canvas)

        # Assert
        mock_canvas.draw_upper_left_corner.assert_called_with(x, y)
        mock_canvas.draw_upper_right_corner.assert_called_with(x + width - 1, y)
        mock_canvas.draw_lower_left_corner.assert_called_with(x, y + height - 1)
        mock_canvas.draw_lower_right_corner.assert_called_with(
            x + width - 1, y + height - 1
        )

        mock_canvas.draw_horizontal_line.assert_not_called()
        mock_canvas.draw_vertical_line.assert_not_called()

    """
    Test case 4 (Rectangle, w3, h4):
    """

    def test_draw_3_by_4_rectangle(self):
        # Arrange
        mock_canvas = create_autospec(Canvas)
        x = 1
        y = 2
        width = 3
        height = 4

        # Act
        rectangle = Rectangle(x, y, width, height)
        rectangle.draw(mock_canvas)

        # Assert
        mock_canvas.draw_upper_left_corner.assert_called_with(x, y)
        mock_canvas.draw_upper_right_corner.assert_called_with(x + width - 1, y)
        mock_canvas.draw_lower_left_corner.assert_called_with(x, y + height - 1)
        mock_canvas.draw_lower_right_corner.assert_called_with(
            x + width - 1, y + height - 1
        )

        mock_canvas.draw_horizontal_line.assert_any_call(x + 1, y, width - 2)
        mock_canvas.draw_horizontal_line.assert_any_call(
            x + 1, y + height - 1, width - 2
        )

        mock_canvas.draw_vertical_line.assert_any_call(x, y + 1, height - 2)
        mock_canvas.draw_vertical_line.assert_any_call(x + width - 1, y + 1, height - 2)


class SquareUnitTests(unittest.TestCase):
    """
    Test case 5 (Square, 5 by 5):
    """

    def test_draw_5_by_5_square(self):
        # Arrange
        mock_canvas = create_autospec(Canvas)
        x = 1
        y = 2
        size = 5
        width = size
        height = size

        # Act
        square = Square(x, y, size)
        square.draw(mock_canvas)

        # Assert
        mock_canvas.draw_upper_left_corner.assert_called_with(x, y)
        mock_canvas.draw_upper_right_corner.assert_called_with(x + width - 1, y)
        mock_canvas.draw_lower_left_corner.assert_called_with(x, y + height - 1)
        mock_canvas.draw_lower_right_corner.assert_called_with(
            x + width - 1, y + height - 1
        )

        mock_canvas.draw_horizontal_line.assert_any_call(x + 1, y, width - 2)
        mock_canvas.draw_horizontal_line.assert_any_call(
            x + 1, y + height - 1, width - 2
        )

        mock_canvas.draw_vertical_line.assert_any_call(x, y + 1, height - 2)
        mock_canvas.draw_vertical_line.assert_any_call(x + width - 1, y + 1, height - 2)


class TriangleUnitTests(unittest.TestCase):
    """
    Test case 6 (Triangle):
    """

    def test_draw_triangle(self):
        # Arrange
        mock_canvas = create_autospec(Canvas)
        x = 1
        y = 2
        size = 5

        # Act
        shape = Triangle(x, y, size)
        shape.draw(mock_canvas)

        # Assert
        mock_canvas.draw_lower_left_corner.assert_called_with(x, y + size - 1)
        mock_canvas.draw_horizontal_line.assert_called_with(
            x + 1, y + size - 1, size - 1
        )
        mock_canvas.draw_vertical_line.assert_called_with(x, y, size - 1)
        for i in range(1, size - 1):
            mock_canvas.draw_backslash.assert_any_call(x + i, y + i)

        self.assertEqual(mock_canvas.draw_backslash.call_count, size - 2)


class HorizontalLineUnitTests(unittest.TestCase):
    """
    Test case 7 (Horizontal Line):
    """

    def test_draw_horizontal_line(self):
        # Arrange
        mock_canvas = create_autospec(Canvas)
        x = 5
        y = 7
        size = 3

        # Act
        shape = HorizontalLine(x, y, size)
        shape.draw(mock_canvas)

        # Assert
        mock_canvas.draw_horizontal_line.assert_called_with(x, y, size)


class VerticalLineUnitTests(unittest.TestCase):
    """
    Test case 8 (Vertical Line):
    """

    def test_draw_vertical_line(self):
        # Arrange
        mock_canvas = create_autospec(Canvas)
        x = 3
        y = 4
        size = 8

        # Act
        shape = VerticalLine(x, y, size)
        shape.draw(mock_canvas)

        # Assert
        mock_canvas.draw_vertical_line.assert_called_with(x, y, size)


if __name__ == "__main__":
    unittest.main()
