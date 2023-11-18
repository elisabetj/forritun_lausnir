#!/usr/bin/python3

from complex_number import ComplexNumber

MAX_NUMBER_OF_PARAMETERS = 2

# Inputs needed for each method
# "__init__"   : [re, [im]]
# "__str__"    : C
# "__repr__"   : C
# "re"         : C
# "im"         : C
# "__eq__"     : CxC
# "conjugate"  : C
# "__neg__"    : C
# "__add__"    : CxC
# "__sub__"    : CxC
# "__mul__"    : CxC
# "inverse"    : C
# "__truediv__": CxC


def main() -> None:
    requested_method = input()
    available_methods = {
        "__init__": create_complex_number,
        "__str__": print_complex_number,
        "__repr__": repr_complex_number,
        "re": get_real_part,
        "im": get_imaginary_part,
        "__eq__": compare_if_equal,
        "conjugate": conjugate,
        "__neg__": negate,
        "__add__": add,
        "__sub__": subtract,
        "__mul__": multiply,
        "inverse": invert,
        "__truediv__": divide,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run()


def create_complex_number():
    number_of_specified = int(input())
    assert 0 <= number_of_specified <= MAX_NUMBER_OF_PARAMETERS
    specified_parts = [int(input()) for _ in range(number_of_specified)]
    print(
        f"Initializing ComplexNumber with {number_of_specified} specified parts,",
        f"and using default values for the remaining {MAX_NUMBER_OF_PARAMETERS - number_of_specified} parts.",
        sep="\n",
    )
    for name, value in zip(["re", "im"], specified_parts):
        print(f" {name} = {value}")

    instance = ComplexNumber(*specified_parts)
    print(f"Complex number created without errors.")
    return instance


def print_complex_number(number=None):
    if number is None:
        number = create_complex_number()

    print(number)


def repr_complex_number(number=None):
    if number is None:
        number = create_complex_number()

    representation = repr(number)
    print(representation)


def add(number1=None, number2=None):
    if number1 is None:
        number1 = create_complex_number()
    if number2 is None:
        number2 = create_complex_number()

    print(f"Result of adding {number1} and {number2} together:")
    result = number1 + number2
    print(result)


def subtract(number1=None, number2=None):
    if number1 is None:
        number1 = create_complex_number()
    if number2 is None:
        number2 = create_complex_number()

    print(f"Result of subtracting {number2} from {number1}:")
    result = number1 - number2
    print(result)


def get_real_part(number=None):
    if number is None:
        number = create_complex_number()

    print(f"Real part of {number} is:")
    result = number.re()
    print(result)


def get_imaginary_part(number=None):
    if number is None:
        number = create_complex_number()

    print(f"Imaginary part of {number} is:")
    result = number.im()
    print(result)


def compare_if_equal(number1=None, number2=None):
    if number1 is None:
        number1 = create_complex_number()
    if number2 is None:
        number2 = create_complex_number()

    print(f"Result of comparing {number1} and {number2} for equality:")
    result = number1 == number2
    print(result)


def conjugate(number=None):
    if number is None:
        number = create_complex_number()

    print(f"The conjucate of {number} is:")
    result = number.conjugate()
    print(result)


def negate(number=None):
    if number is None:
        number = create_complex_number()

    print(f"The negation of {number} is:")
    result = -number
    print(result)


def multiply(number1=None, number2=None):
    if number1 is None:
        number1 = create_complex_number()
    if number2 is None:
        number2 = create_complex_number()

    print(f"Result of multiplying {number1} and {number2}:")
    result = number1 * number2
    print(result)


def invert(number=None):
    if number is None:
        number = create_complex_number()

    assert number != ComplexNumber()

    print(f"The inverse of {number} is:")
    result = number.inverse()
    print(str(result).replace("i", " i"))  # For tokenizer.


def divide(number1=None, number2=None):
    if number1 is None:
        number1 = create_complex_number()
    if number2 is None:
        number2 = create_complex_number()

    print(f"Result of dividing {number1} by {number2}:")
    result = number1 / number2
    print(str(result).replace("i", " i"))  # For tokenizer.


if __name__ == "__main__":
    main()
