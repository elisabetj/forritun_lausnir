#!/usr/bin/python3

from importlib import import_module
from pathlib import Path


def main() -> None:
    requested_method = input()
    class_name, method_name = requested_method.split(".")
    if class_name == "Rectangle":
        test_rectangle(method_name)
    elif class_name == "Square":
        test_square(method_name)
    else:
        assert False, f"Unknown class {class_name} requested."


def test_rectangle(requested_method):
    Rectangle = get_class("Rectangle")
    available_methods = {
        "__init__": test_rectangle_init,
        "__str__": test_rectangle_str,
        "get_perimeter": test_rectangle_perimeter,
        "get_area": test_rectangle_area,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run(Rectangle)


def test_rectangle_init(Rectangle):
    assert hasattr(
        Rectangle, "__init__"
    ), f"Could not find member function '__init__' of class 'Rectangle'."

    parameters = Rectangle.__init__.__code__.co_varnames
    expected_number_of_parameters = 3  # Including self, length, height.
    assert len(parameters) == expected_number_of_parameters, (
        f"Unexpected number of parameters, {len(parameters)}.",
    )

    # Arrange
    width, height = map(int, input().split(","))
    print(f"Initializing Rectangle with {width=} and {height=}.")

    # Act
    try:
        instance = Rectangle(width, height)
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    # Assert
    print(f"Rectangle created without errors.")

    return instance


def test_rectangle_str(Rectangle):
    assert hasattr(
        Rectangle, "__str__"
    ), f"Could not find member function '__str__' of class 'Rectangle'."

    # Arrange
    instance = test_rectangle_init(Rectangle)

    # Act
    try:
        representation = str(instance)
    except Exception as e:
        print(f"Error getting string representation item: {e}")
        raise

    # Assert
    print("String representation:")
    print(representation)

    assert (
        representation is not None
    ), f"'__str__' method returned 'None', but should return a string."
    assert isinstance(
        representation, str
    ), f"'__str__' method returned '{type(representation)}', but should return 'str'."
    first_time = representation
    second_time = str(instance)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the '__str__' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_rectangle_perimeter(Rectangle):
    assert hasattr(
        Rectangle, "get_perimeter"
    ), f"Could not find member function 'get_perimeter' of class 'Rectangle'."

    # Arrange
    instance = test_rectangle_init(Rectangle)

    # Act
    try:
        perimeter = instance.get_perimeter()
    except Exception as e:
        print(f"Error getting perimeter: {e}")
        raise

    # Assert
    print(f"Perimeter: {perimeter}")

    assert (
        perimeter is not None
    ), f"'get_perimeter' method returned 'None', but should return a number."
    assert isinstance(perimeter, int) or isinstance(
        perimeter, float
    ), f"'get_perimeter' method returned '{type(perimeter)}', but should return a number."
    first_time = perimeter
    second_time = instance.get_perimeter()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 'get_perimeter' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_rectangle_area(Rectangle):
    assert hasattr(
        Rectangle, "get_area"
    ), f"Could not find member function 'get_area' of class 'Rectangle'."

    # Arrange
    instance = test_rectangle_init(Rectangle)

    # Act
    try:
        area = instance.get_area()
    except Exception as e:
        print(f"Error getting area: {e}")
        raise

    # Assert
    print(f"Area: {area}")

    assert (
        area is not None
    ), f"'get_area' method returned 'None', but should return a number."
    assert isinstance(area, int) or isinstance(
        area, float
    ), f"'get_area' method returned '{type(area)}', but should return a number."
    first_time = area
    second_time = instance.get_area()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 'get_area' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_square(requested_method):
    Square = get_class("Square")
    available_methods = {
        "__init__": test_square_init,
        "__str__": test_square_str,
        "get_perimeter": test_square_perimeter,
        "get_area": test_square_area,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run(Square)


def test_square_init(Square):
    assert hasattr(
        Square, "__init__"
    ), f"Could not find member function '__init__' of class 'Square'"

    parameters = Square.__init__.__code__.co_varnames
    expected_number_of_parameters = 2  # Including self and side.
    assert len(parameters) == expected_number_of_parameters, (
        f"Unexpected number of parameters, {len(parameters)}.",
    )

    # Arrange
    side = int(input())
    print(f"Initializing Rectangle with side length {side}.")

    # Act
    try:
        instance = Square(side)
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    # Assert
    print(f"Square created without errors.")

    return instance


def test_square_str(Square):
    assert hasattr(
        Square, "__str__"
    ), f"Could not find member function '__str__' of class 'Square'."

    # Arrange
    instance = test_square_init(Square)

    # Act
    try:
        representation = str(instance)
    except Exception as e:
        print(f"Error getting string representation item: {e}")
        raise

    # Assert
    print("String representation:")
    print(representation)

    assert (
        representation is not None
    ), f"'__str__' method returned 'None', but should return a string."
    assert isinstance(
        representation, str
    ), f"'__str__' method returned '{type(representation)}', but should return 'str'."
    first_time = representation
    second_time = str(instance)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the '__str__' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_square_perimeter(Square):
    assert hasattr(
        Square, "get_perimeter"
    ), f"Could not find member function 'get_perimeter' of class 'Square'."

    # Arrange
    instance = test_square_init(Square)

    # Act
    try:
        perimeter = instance.get_perimeter()
    except Exception as e:
        print(f"Error getting perimeter: {e}")
        raise

    # Assert
    print(f"Perimeter: {perimeter}")

    assert (
        perimeter is not None
    ), f"'get_perimeter' method returned 'None', but should return a number."
    assert isinstance(perimeter, int) or isinstance(
        perimeter, float
    ), f"'get_perimeter' method returned '{type(perimeter)}', but should return a number."
    first_time = perimeter
    second_time = instance.get_perimeter()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 'get_perimeter' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_square_area(Square):
    assert hasattr(
        Square, "get_area"
    ), f"Could not find member function 'get_area' of class 'Square'."

    # Arrange
    instance = test_square_init(Square)

    # Act
    try:
        area = instance.get_area()
    except Exception as e:
        print(f"Error getting area: {e}")
        raise

    # Assert
    print(f"Area: {area}")

    assert (
        area is not None
    ), f"'get_area' method returned 'None', but should return a number."
    assert isinstance(area, int) or isinstance(
        area, float
    ), f"'get_area' method returned '{type(area)}', but should return a number."
    first_time = area
    second_time = instance.get_area()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 'get_area' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def get_class(name):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Could not find class '{name}'.")


def load_modules():
    modules = []
    this_file = Path(__file__)
    for submission_file in this_file.parent.iterdir():
        if submission_file == this_file:
            continue

        if submission_file.suffix == ".py":
            modules.append(import_module(submission_file.stem))

    return modules


if __name__ == "__main__":
    main()
