#!/usr/bin/python3

from importlib import import_module
from pathlib import Path

def main() -> None:
    requested_method = input()
    classname = requested_method.split('.')[0]
    shapeClass = get_class(classname)
    available_methods = {
        "Rectangle.__str__": print_rectangle,
        "Square.__str__": print_square,
        "Rectangle.get_perimeter": rectangle_perimeter,
        "Square.get_perimeter": square_perimeter,
        "Rectangle.get_area": rectangle_area,
        "Square.get_area": square_area,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run(shapeClass)


def print_rectangle(Rectangle):
	width, height = map(int, input().split(','))
	print(Rectangle(width, height))


def print_square(Square):
    sidelenth = int(input())
    print(Square(sidelenth))


def rectangle_perimeter(Rectangle):
    width, height = map(int, input().split(','))
    rect = Rectangle(width, height)
    print(f"get_perimeter: {rect.get_perimeter()}")


def square_perimeter(Square):
    sidelength = int(input())
    square = Square(sidelength)
    print(f"get_perimeter: {square.get_perimeter()}")


def rectangle_area(Rectangle):
    width, height = map(int, input().split(','))
    rect = Rectangle(width, height)
    print(f"get_area: {rect.get_area()}")


def square_area(Square):
    sidelength = int(input())
    square = Square(sidelength)
    print(f"get_area: {square.get_area()}")

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
