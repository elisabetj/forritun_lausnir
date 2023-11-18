from typing import Tuple

from complex_number import ComplexNumber

MAX_NUMBER_OF_PARAMETERS = 2

# Test types:
INITIALIZATION = "init"
STRING = "str"
REPRESENTATION = "repr"
REAL = "real"
IMAGINARY = "imagine"
COMPARISIN = "eq"
CONJUGATION = "conjugate"
ADDITION = "add"
NEGATION = "neg"
SUBTRACTION = "sub"
MULTIPLICATION = "mul"
INVERSE = "inverse"
DIVISION = "div"
# Feel free to use other values for these constants as you see fit.


def main():
    # You can use this for local testing:
    run_your_own_tests()

    # Or use this to run the examples given in the problem statement:
    run_examples()

    # Or this to run the samples:
    run_samples()

    # Or run this to take input from terminal:
    run_like_autograder()


def run_your_own_tests():
    # Add whatever tests you want.
    pass


def run_examples():
    run_str_examples()
    run_repr_examples()
    run_re_examples()
    run_im_examples()
    run_eq_examples()
    run_conjugation_examples()
    run_negation_examples()
    run_addition_examples()
    run_subtraction_examples()
    run_multiplication_examples()


def run_str_examples():
    print("\nString examples.\n")
    z = ComplexNumber(5, 7)
    print(z)
    assert str(z) == "5 + 7i"
    assert str(ComplexNumber(5, -7)) == "5 - 7i"
    assert str(ComplexNumber(5, 0)) == "5"
    assert str(ComplexNumber(5)) == "5"
    assert str(ComplexNumber(-5)) == "-5"
    assert str(ComplexNumber(0, 7)) == "7i"
    assert str(ComplexNumber(0, -7)) == "-7i"
    assert str(ComplexNumber(0, 0)) == "0"
    assert str(ComplexNumber()) == "0"


def run_repr_examples():
    print("\nRepr examples.\n")
    z = ComplexNumber(5, 7)
    print(repr(z))
    assert repr(z) == "ComplexNumber(5, 7)"
    w = eval(repr(z))
    assert type(w) == ComplexNumber
    print(w)


def run_re_examples():
    print("\nRe examples.\n")
    z = ComplexNumber(3, 4)
    print(z.re())
    assert z.re() == 3


def run_im_examples():
    print("\nIm examples.\n")
    z = ComplexNumber(3, 4)
    print(z.im())
    assert z.im() == 4


def run_eq_examples():
    print("\nComparison examples.\n")
    z = ComplexNumber(3, 4)
    w = ComplexNumber(5, 4)
    assert not z == w
    assert z == z
    assert z == ComplexNumber(3, 4)
    assert z == eval(repr(z))


def run_conjugation_examples():
    print("\nConjugation examples.\n")
    z = ComplexNumber(3, 4)
    w = z.conjugate()
    assert type(w) == ComplexNumber
    print(w)
    assert str(w) == "3 - 4i"
    print(w.conjugate())
    assert str(w.conjugate()) == "3 + 4i"
    assert z.conjugate().conjugate() == z


def run_negation_examples():
    print("\nNegation examples.\n")
    z = ComplexNumber(5, -3)
    assert type(-z) == ComplexNumber
    print(-z)
    print(-(-z))
    assert z == -(-z)


def run_addition_examples():
    print("\nAddition examples.\n")
    z = ComplexNumber(300, 800)
    w = ComplexNumber(1, -2)
    assert type(z + w) == ComplexNumber
    print(z + w)
    assert str(z + w) == "301 + 798i"


def run_subtraction_examples():
    print("\nSubtraction examples.\n")
    z = ComplexNumber(300, 800)
    w = ComplexNumber(1, -2)
    assert type(z - w) == ComplexNumber
    print(z - w)
    assert str(z - w) == "299 + 802i"


def run_multiplication_examples():
    print("\nMultiplication examples.\n")
    z = ComplexNumber(300, 800)
    w = ComplexNumber(1, -2)
    assert type(z * w) == ComplexNumber
    print(z * w)
    assert str(z * w) == "1900 + 200i"


def run_inversion_examples():
    print("\nInversion examples.\n")
    z = ComplexNumber(4, 3)
    assert type(z.inverse()) == ComplexNumber
    print(z.inverse())
    assert str(z.inverse()) == "0.16 - 0.12i"


def run_division_examples():
    print("\nDivision examples.\n")
    z = ComplexNumber(4, 3)
    w = ComplexNumber(1) / z
    assert type(w) == ComplexNumber
    print(w)
    assert str(w) == "0.16 - 0.12i"
    print(z.inverse().inverse())
    assert z.inverse().inverse() == "4.0 + 3.0i"
    assert z == z.inverse().inverse()


def run_samples():
    # Add more samples.
    pass


def run_sample_1():
    test_type = STRING
    number_of_specified_parameters = 0
    specified_parameters = []
    number = create_complex_number(specified_parameters)
    print(number)


def run_sample_2():
    test_type = STRING
    number_of_specified_parameters = 1
    specified_parameters = [5]
    number = create_complex_number(specified_parameters)
    print(number)


def run_sample_3():
    test_type = STRING
    number_of_specified_parameters = 2
    specified_parameters = [5, 7]
    number = create_complex_number(specified_parameters)
    print(number)


def run_sample_4():
    test_type = STRING
    number_of_specified_parameters = 2
    specified_parameters = [5, -7]
    number = create_complex_number(specified_parameters)
    print(number)


def run_sample_5():
    test_type = STRING
    number_of_specified_parameters = 2
    specified_parameters = [-5, -7]
    number = create_complex_number(specified_parameters)
    print(number)


def run_sample_6():
    test_type = CONJUGATION
    number_of_specified_parameters = 2
    specified_parameters = [5, 7]
    number = create_complex_number(specified_parameters)
    conjugate_number(number)


def run_sample_7():
    test_type = INVERSE
    number_of_specified_parameters = 2
    specified_parameters = [3, 4]
    number = create_complex_number(specified_parameters)
    invert_number(number)


def run_sample_8():
    test_type = ADDITION
    first_number = create_complex_number([3, 4])
    second_number = create_complex_number([5, 7])
    add(first_number, second_number)


def run_sample_9():
    test_type = SUBTRACTION
    first_number = create_complex_number([5, 7])
    second_number = create_complex_number([3, 4])
    subtract(first_number, second_number)


def run_sample_10():
    test_type = DIVISION
    first_number = create_complex_number([3, 4])
    second_number = create_complex_number([5, 7])
    divide(first_number, second_number)


def run_like_autograder():
    test_type, numbers = get_input()
    available_methods = {
        INITIALIZATION: create_complex_number,
        STRING: print,
        REPRESENTATION: repr_complex_number,
        REAL: get_real_part,
        IMAGINARY: get_imaginary_part,
        COMPARISIN: compare_if_equal,
        CONJUGATION: conjugate_number,
        ADDITION: add,
        NEGATION: negate,
        SUBTRACTION: subtract,
        MULTIPLICATION: multiply,
        INVERSE: invert_number,
        DIVISION: divide,
    }
    assert test_type in available_methods
    method_to_run = available_methods[test_type]
    method_to_run(*numbers)


def get_input() -> Tuple:
    """Gets numbers from user."""

    test_type = input()

    how_many = int(input())
    specified_parameters = [float(input()) for _ in range(how_many)]
    if test_type == INITIALIZATION:
        numbers = [specified_parameters]
        # In case you want to test the initialization specifically.
    else:
        number = create_complex_number(specified_parameters)
        numbers = [number]

    if test_type in [
        COMPARISIN,
        ADDITION,
        SUBTRACTION,
        MULTIPLICATION,
        DIVISION,
    ]:
        second = int(input())
        specified_parameters_for_second = [float(input()) for _ in range(second)]
        second_number = create_complex_number(specified_parameters_for_second)
        numbers.append(second_number)

    return test_type, numbers


def create_complex_number(specified_parts):
    assert 0 <= len(specified_parts) <= MAX_NUMBER_OF_PARAMETERS
    number_of_specified = len(specified_parts)
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


def repr_complex_number(number):
    representation = repr(number)
    print(representation)


def get_real_part(number):
    print(f"Real part of {number} is:")
    result = number.re()
    print(result)


def get_imaginary_part(number):
    print(f"Imaginary part of {number} is:")
    result = number.im()
    print(result)


def compare_if_equal(number1, number2):
    print(f"Result of comparing {number1} and {number2} for equality:")
    result = number1 == number2
    print(result)


def conjugate_number(complex_number):
    print(f"The conjucate of {complex_number} is:")
    result = complex_number.conjugate()
    print(result)


def add(number1, number2):
    print(f"Result of adding {number1} and {number2} together:")
    result = number1 + number2
    print(result)


def negate(number):
    print(f"The negation of {number} is:")
    result = -number
    print(result)


def subtract(number1, number2):
    print(f"Result of subtracting {number2} from {number1}:")
    result = number1 - number2
    print(result)


def multiply(number1, number2):
    print(f"Result of multiplying {number1} and {number2}:")
    result = number1 * number2
    print(result)


def invert_number(complex_number):
    assert complex_number != ComplexNumber()
    print(f"The inverse of {complex_number} is:")
    result = complex_number.inverse()
    print(str(result).replace("i", " i"))  # For tokenizer.


def divide(number1, number2):
    assert number2 != ComplexNumber()
    print(f"Result of dividing {number1} by {number2}:")
    result = number1 / number2
    print(str(result).replace("i", " i"))  # For tokenizer.


if __name__ == "__main__":
    main()
