#!/usr/bin/python3

from rectangle import Rectangle
from square import Square


def main() -> None:
    request = input()
    available_methods = {
        "Rectangle.__init__": create_rectangle,
        "Rectangle.__str__": print_rectangle,
        "Rectangle.get_perimeter": rectangle_perimeter,
        "Rectangle.get_area": rectangle_area,
        "Square.__init__": create_square,
        "Square.__str__": print_square,
        "Square.get_perimeter": square_perimeter,
        "Square.get_area": square_area,
    }
    assert request in available_methods, f"Unexpected method {request} requested."

    method_to_run = available_methods[request]
    method_to_run()


def create_rectangle():
    width, height = map(int, input().split(","))
    print(f"Initializing Rectangle with {width=} and {height=}.")
    rectangle = Rectangle(width, height)
    print(f"Rectangle created without errors.")
    return rectangle


def print_rectangle():
    rect = create_rectangle()
    print("String representation:")
    print(rect)


def rectangle_perimeter():
    rect = create_rectangle()
    print(f"Perimeter: {rect.get_perimeter()}")


def rectangle_area():
    rect = create_rectangle()
    print(f"Area: {rect.get_area()}")


def create_square():
    sidelength = int(input())
    print(f"Initializing Rectangle with side length {sidelength}.")
    sqare = Square(sidelength)
    print(f"Square created without errors.")
    return sqare


def print_square():
    square = create_square()
    print("String representation:")
    print(square)


def square_perimeter():
    square = create_square()
    print(f"Perimeter: {square.get_perimeter()}")


def square_area():
    square = create_square()
    print(f"Area: {square.get_area()}")


if __name__ == "__main__":
    main()
