from importlib import import_module
from pathlib import Path

CLASS_NAME = "Vector"


def main():
    test_vector()


def test_vector():
    Vector = get_class()
    callables = {
        "__init__": test_vector_init,
        "__str__": test_vector_str,
        "__abs__": test_vector_abs,
        "__add__": test_vector_add,
        "__sub__": test_vector_sub,
        "__eq__": test_vector_eq,
        "__mul__": test_vector_mul,
        "__rmul__": test_vector_rmul,
        "__repr__": test_vector_repr,
        "__gt__": test_vector_gt,
        "__ge__": test_vector_ge,
        "__lt__": test_vector_lt,
        "__le__": test_vector_le,
        "dot": test_vector_dot,
        "cross": test_vector_cross,
    }

    callable_name = input()
    callables[callable_name](Vector)


def test_vector_init(Vector):
    assert hasattr(
        Vector, "__init__"
    ), f"Could not find member function '__init__' of class 'Vector'"

    parameters = Vector.__init__.__code__.co_varnames
    assert len(parameters) >= 3, (f"Too few parameters, {len(parameters)}.",)

    # Arrange
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

    # Act
    try:
        instance = Vector(*specified_coordinates)
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    # Assert
    print(f"Vector created without errors.")

    return instance


def test_vector_str(Vector):
    assert hasattr(
        Vector, "__str__"
    ), f"Could not find member function '__str__' of class 'Vector'"

    # Arrange
    instance = test_vector_init(Vector)

    # Act
    try:
        representation = str(instance)
    except Exception as e:
        print(f"Error getting string representation item: {e}")
        raise

    # Assert
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


def test_vector_abs(Vector):
    assert hasattr(
        Vector, "__abs__"
    ), f"Could not find member function '__abs__' of class 'Vector'"

    # Arrange
    instance = test_vector_init(Vector)
    print("Vector:")
    print(instance)

    # Act
    try:
        result = abs(instance)
    except Exception as e:
        print(f"Error finding length of Vector: {e}")
        raise

    # Assert
    print(f"Length of {instance}:")
    print(result)

    assert isinstance(result, float), "\n".join(
        [
            f"Method '__abs__' did not return a float, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    first_time = result
    second_time = abs(instance)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the '__abs__' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_add(Vector):
    assert hasattr(
        Vector, "__add__"
    ), f"Could not find member function '__add__' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1 + instance2
    except Exception as e:
        print(f"Error adding Vectors: {e}")
        raise

    # Assert
    print(f"Result of adding {instance1} and {instance2} together:")
    print(result)

    assert isinstance(result, Vector), "\n".join(
        [
            f"Method '__add__' did not return a Vector, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The addition appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The addition appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = str(result)
    second_time = str(instance1 + instance2)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the addition has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_sub(Vector):
    assert hasattr(
        Vector, "__sub__"
    ), f"Could not find member function '__sub__' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1 - instance2
    except Exception as e:
        print(f"Error subtracting Vectors: {e}")
        raise

    # Assert
    print(f"Result of subtracting {instance2} from {instance1}:")
    print(result)

    assert isinstance(result, Vector), "\n".join(
        [
            f"Method '__sub__' did not return a Vector, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The subtraction appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The subtraction appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = str(result)
    second_time = str(instance1 - instance2)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the subtraction has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_eq(Vector):
    assert hasattr(
        Vector, "__eq__"
    ), f"Could not find member function '__eq__' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1 == instance2
    except Exception as e:
        print(f"Error equating Vectors: {e}")
        raise

    # Assert
    print(f"Result of comparing {instance1} and {instance2} for equality:")
    print(result)

    assert isinstance(result, bool), "\n".join(
        [
            f"Method '__eq__' did not return a bool, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The comparison appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The comparison appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1 == instance2
    assert first_time == second_time, "\n".join(
        [
            "It appears that the comparison has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_mul(Vector):
    assert hasattr(
        Vector, "__mul__"
    ), f"Could not find member function '__mul__' of class 'Vector'"

    # Arrange
    instance = test_vector_init(Vector)
    before = str(instance)
    scalar = int(input())
    print("Vector:")
    print(instance)

    # Act
    try:
        result = instance * scalar
    except Exception as e:
        print(f"Error multiplying Vector and scalar: {e}")
        raise

    # Assert
    print(f"Result of multiplying {instance} and {scalar}:")
    print(result)

    assert isinstance(result, Vector), "\n".join(
        [
            f"Method '__mul__' did not return a Vector, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after = str(instance)
    assert before == after, "\n".join(
        [
            f"The scaling operation appears to have changed the vector.",
            f"Before: '{before}'.",
            f"After:  '{after}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance * scalar
    assert first_time == second_time, "\n".join(
        [
            "It appears that the scaling operation has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_rmul(Vector):
    assert hasattr(
        Vector, "__rmul__"
    ), f"Could not find member function '__mul__' of class 'Vector'"

    # Arrange
    instance = test_vector_init(Vector)
    before = str(instance)
    scalar = int(input())
    print("Vector:")
    print(instance)

    # Act
    try:
        result = scalar * instance
    except Exception as e:
        print(f"Error multiplying scalar and Vector: {e}")
        raise

    # Assert
    print(f"Result of multiplying {scalar} and {instance}:")
    print(result)

    assert isinstance(result, Vector), "\n".join(
        [
            f"Method '__rmul__' did not return a Vector, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after = str(instance)
    assert before == after, "\n".join(
        [
            f"The scaling operation appears to have changed the vector.",
            f"Before: '{before}'.",
            f"After:  '{after}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = scalar * instance
    assert first_time == second_time, "\n".join(
        [
            "It appears that the scaling operation has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_repr(Vector):
    assert hasattr(
        Vector, "__repr__"
    ), f"Could not find member function '__repr__' of class 'Vector'"

    # Arrange
    instance = test_vector_init(Vector)

    # Act
    try:
        representation = repr(instance)
    except Exception as e:
        print(f"Error getting Vector representation item: {e}")
        raise

    # Assert
    print(representation)

    assert (
        representation is not None
    ), f"'__repr__' method returned 'None', but should return a string."
    assert isinstance(
        representation, str
    ), f"'__repr__' method returned '{type(representation)}', but should return 'str'."
    first_time = representation
    second_time = repr(instance)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the '__repr__' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_gt(Vector):
    assert hasattr(
        Vector, "__gt__"
    ), f"Could not find member function '__gt__' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1 > instance2
    except Exception as e:
        print(f"Error comparing whether Vector1 is greater than Vector2: {e}")
        raise

    # Assert
    print(f"{instance1} greater than {instance2}:")
    print(result)

    assert isinstance(result, bool), "\n".join(
        [
            f"Method '__gt__' did not return a bool, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The comparison appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The comparison appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1 > instance2
    assert first_time == second_time, "\n".join(
        [
            "It appears that the comparison has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_ge(Vector):
    assert hasattr(
        Vector, "__ge__"
    ), f"Could not find member function '__ge__' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1 >= instance2
    except Exception as e:
        print(f"Error comparing whether Vector1 is greater than or equal Vector2: {e}")
        raise

    # Assert
    print(f"{instance1} greater than or equal {instance2}:")
    print(result)

    assert isinstance(result, bool), "\n".join(
        [
            f"Method '__ge__' did not return a bool, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The comparison appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The comparison appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1 >= instance2
    assert first_time == second_time, "\n".join(
        [
            "It appears that the comparison has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_lt(Vector):
    assert hasattr(
        Vector, "__lt__"
    ), f"Could not find member function '__lt__' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1 < instance2
    except Exception as e:
        print(f"Error comparing whether Vector1 is less than Vector2: {e}")
        raise

    # Assert
    print(f"{instance1} less than {instance2}:")
    print(result)

    assert isinstance(result, bool), "\n".join(
        [
            f"Method '__lt__' did not return a bool, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The comparison appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The comparison appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1 < instance2
    assert first_time == second_time, "\n".join(
        [
            "It appears that the comparison has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_le(Vector):
    assert hasattr(
        Vector, "__le__"
    ), f"Could not find member function '__le__' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1 <= instance2
    except Exception as e:
        print(f"Error comparing whether Vector1 is less than or equal Vector2: {e}")
        raise

    # Assert
    print(f"{instance1} less than or equal {instance2}:")
    print(result)

    assert isinstance(result, bool), "\n".join(
        [
            f"Method '__le__' did not return a bool, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The comparison appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The comparison appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1 <= instance2
    assert first_time == second_time, "\n".join(
        [
            "It appears that the comparison has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_dot(Vector):
    assert hasattr(
        Vector, "dot"
    ), f"Could not find member function 'dot' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1.dot(instance2)
    except Exception as e:
        print(f"Error getting dot product of Vectors: {e}")
        raise

    # Assert
    print(f"Dot product of {instance1} and {instance2}:")
    print(result)

    assert isinstance(result, int) or isinstance(result, float), "\n".join(
        [
            f"Method 'dot' did not return a number, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The operation appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The operation appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1.dot(instance2)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the operation has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_vector_cross(Vector):
    assert hasattr(
        Vector, "cross"
    ), f"Could not find member function 'cross' of class 'Vector'"

    # Arrange
    instance1 = test_vector_init(Vector)
    instance2 = test_vector_init(Vector)
    before_left = str(instance1)
    before_right = str(instance2)
    print("Vector 1:")
    print(instance1)
    print("Vector 2:")
    print(instance2)

    # Act
    try:
        result = instance1.cross(instance2)
    except Exception as e:
        print(f"Error getting cross product of Vectors: {e}")
        raise

    # Assert
    print(f"Cross product of {instance1} and {instance2}:")
    print(result)

    assert isinstance(result, Vector), "\n".join(
        [
            f"Method 'cross' did not return a Vector, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The operation appears to have changed the left vector.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The operation appears to have changed the right vector.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1.cross(instance2)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the operation has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def get_class(name=CLASS_NAME):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Could not find class {name}")


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
