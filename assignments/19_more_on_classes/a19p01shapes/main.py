#!/usr/bin/python3

from rectangle import Rectangle
from square import Square


def main():
    # The sample from the problem statement
    run_problem_statement_examples()


def run_problem_statement_examples():
    run_problem_statement_example1()
    run_problem_statement_example2()

    # These are more or less the same as the example given in the problem statement,
    # but split into individual parts:
    run_explicit_tests()


def run_problem_statement_example1():
    rect = Rectangle(2, 3)
    print(rect.get_area())
    print(rect.get_perimeter())
    print(rect)

    sq = Square(2)
    print(sq.get_area())
    print(sq.get_perimeter())
    print(sq)


def run_problem_statement_example2():
    rect = Rectangle(5, 10)
    print(f"Rectangle area: {rect.get_area()}")
    print(f"Rectangle perimeter: {rect.get_perimeter()}")
    print(rect)

    square = Square(7)
    print(f"Square area: {square.get_area()}")
    print(f"Square perimeter: {square.get_perimeter()}")
    print(square)


def run_explicit_tests():
    print("Testing rectangle perimeter.")
    example2_test_rectange_perimeter()

    print("Testing square area.")
    example2_test_square_area()

    print("Testing square string representation.")
    example2_test_print()

    # Feel free to add the rest, or any further tests you would like.


def example2_test_rectange_perimeter():
    # Arrange
    test_input_width = 5
    test_input_height = 10
    rect = Rectangle(test_input_width, test_input_height)
    expected_perimeter = 30

    # Act
    actual_perimeter = rect.get_perimeter()

    # Assert
    message = "\n".join(
        [
            f"\n\nInput to constructor:",
            f" width ({type(test_input_width)}): {test_input_width}",
            f" height ({type(test_input_height)}): {test_input_height}",
            f"Expected perimeter ({type(expected_perimeter)}): {expected_perimeter}",
            f"Actual perimeter ({type(actual_perimeter)}): {actual_perimeter}",
        ]
    )
    assert expected_perimeter == actual_perimeter, message


def example2_test_square_area():
    # Arrange
    test_input = 7
    square = Square(test_input)
    expected = 49

    # Act
    actual = square.get_area()

    # Assert
    message = "\n".join(
        [
            f"\n\nInput to constructor:",
            f" side ({type(test_input)}): {test_input}",
            f"Expected area ({type(expected)}): {expected}",
            f"Actual area ({type(actual)}): {actual}",
        ]
    )
    assert expected == actual, message


def example2_test_print():
    # Arrange
    test_input = 7
    square = Square(test_input)

    expected = "Square with area of 49.00 and perimeter of 28.00"

    # Act
    actual = str(square)

    # Assert
    message = "\n".join(
        [
            f"\n\nInput to constructor:",
            f" side ({type(test_input)}): {test_input}",
            f"Expected output ({type(expected)}): {expected}",
            f"Actual output ({type(actual)}): {actual}",
        ]
    )
    assert expected == actual, message


if __name__ == "__main__":
    main()
