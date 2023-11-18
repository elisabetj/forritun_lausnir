#!/usr/bin/python3

from vector import Vector


def main() -> None:
    requested_method = input()
    available_methods = {
        "__init__": create_vector,
        "__str__": print_vector,
        "__abs__": abs_vector,
        "__add__": add_vector,
        "__sub__": sub_vector,
        "__eq__": eq_vector,
        "__mul__": mul_vector,
        "__rmul__": rmul_vector,
        "__repr__": repr_vector,
        "__gt__": gt_vector,
        "__ge__": ge_vector,
        "__lt__": lt_vector,
        "__le__": le_vector,
        "dot": dot_product_vector,
        "cross": cross_product_vector,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run()


def create_vector():
    number_of_specified = int(input())
    assert 0 <= number_of_specified <= 3
    specified_coordinates = [int(input()) for _ in range(number_of_specified)]
    print(
        f"Initializing Vector with {number_of_specified} specified coordinates,",
        f"and using default values for the remaining {3 - number_of_specified} coordinates:",
        sep="\n",
    )
    for name, value in zip(["x", "y", "z"], specified_coordinates):
        print(f" {name} = {value}")

    vector_instance = Vector(*specified_coordinates)

    print(f"Vector created without errors.")

    return vector_instance


def print_vector(vector=None):
    if vector is None:
        vector = create_vector()

    print(vector)


def abs_vector(vector=None):
    if vector is None:
        vector = create_vector()

    print("Vector:")
    print(vector)

    result = abs(vector)

    print(f"Length of {vector}:")
    print(result)


def add_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1 + vector2

    print(f"Result of adding {vector1} and {vector2} together:")
    print(result)


def sub_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1 - vector2

    print(f"Result of subtracting {vector2} from {vector1}:")
    print(result)


def eq_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1 == vector2

    print(f"Result of comparing {vector1} and {vector2} for equality:")
    print(result)


def mul_vector(vector=None):
    if vector is None:
        vector = create_vector()

    scalar = int(input())
    print("Vector:")
    print(vector)

    result = vector * scalar

    print(f"Result of multiplying {vector} and {scalar}:")
    print(result)


def rmul_vector(vector=None):
    if vector is None:
        vector = create_vector()

    scalar = int(input())
    print("Vector:")
    print(vector)

    result = scalar * vector

    print(f"Result of multiplying {scalar} and {vector}:")
    print(result)


def repr_vector(vector=None):
    if vector is None:
        vector = create_vector()

    representation = repr(vector)
    print(representation)


def gt_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1 > vector2

    print(f"{vector1} greater than {vector2}:")
    print(result)


def ge_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1 >= vector2

    print(f"{vector1} greater than or equal {vector2}:")
    print(result)


def lt_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1 < vector2

    print(f"{vector1} less than {vector2}:")
    print(result)


def le_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1 <= vector2

    print(f"{vector1} less than or equal {vector2}:")
    print(result)


def dot_product_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1.dot(vector2)

    print(f"Dot product of {vector1} and {vector2}:")
    print(result)


def cross_product_vector(vector1=None, vector2=None):
    if vector1 is None:
        vector1 = create_vector()
    if vector2 is None:
        vector2 = create_vector()

    print("Vector 1:")
    print(vector1)
    print("Vector 2:")
    print(vector2)

    result = vector1.cross(vector2)

    print(f"Cross product of {vector1} and {vector2}:")
    print(result)


if __name__ == "__main__":
    main()
