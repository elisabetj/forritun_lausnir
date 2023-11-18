from importlib import import_module
from pathlib import Path

CLASS_NAME = "ComplexNumber"
MAX_PASSED = 2


def main():
    test_complex_number()


def test_complex_number():
    ComplexNumber = get_class()
    callables = {
        "__init__": test_init,
        "__str__": test_str,
        "__repr__": test_repr,
        "re": test_re,
        "im": test_im,
        "__eq__": test_eq,
        "conjugate": test_conjugate,
        "__neg__": test_neg,
        "__add__": test_add,
        "__sub__": test_sub,
        "__mul__": test_mul,
        "inverse": test_inverse,
        "__truediv__": test_truediv,
    }

    callable_name = input()
    callables[callable_name](ComplexNumber)


def test_init(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__init__"
    ), f"Could not find member function '__init__' of class 'ComplexNumber'"

    parameters = ComplexNumber.__init__.__code__.co_varnames
    expected_number_of_parameters = 1 + MAX_PASSED  # Also self.
    assert len(parameters) == expected_number_of_parameters, (
        f"Unexpected number of parameters, {len(parameters)}.",
    )

    # Arrange
    number_of_specified = int(input())
    assert 0 <= number_of_specified <= MAX_PASSED
    specified_parts = [int(input()) for _ in range(number_of_specified)]
    print(
        f"Initializing ComplexNumber with {number_of_specified} specified parts,",
        f"and using default values for the remaining {MAX_PASSED - number_of_specified} parts.",
        sep="\n",
    )
    for name, value in zip(["re", "im"], specified_parts):
        print(f" {name} = {value}")

    # Act
    try:
        instance = ComplexNumber(*specified_parts)
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    # Assert
    print(f"Complex number created without errors.")
    return instance


def test_str(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__str__"
    ), f"Could not find member function '__str__' of class 'ComplexNumber'"

    # Arrange
    instance = test_init(ComplexNumber)

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


def test_repr(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__repr__"
    ), f"Could not find member function '__repr__' of class 'ComplexNumber'"

    # Arrange
    instance = test_init(ComplexNumber)

    # Act
    try:
        representation = repr(instance)
    except Exception as e:
        print(f"Error getting ComplexNumber representation: {e}")
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


def test_re(ComplexNumber):
    assert hasattr(
        ComplexNumber, "re"
    ), f"Could not find member function 're' of class 'ComplexNumber'"

    # Arrange
    instance = test_init(ComplexNumber)
    before = str(instance)
    print(f"Real part of {instance} is:")

    # Act
    try:
        real_part = instance.re()
    except Exception as e:
        print(f"Error getting real part of ComplexNumber: {e}")
        raise

    # Assert
    print(real_part)

    assert (
        real_part is not None
    ), f"'re' method returned 'None', but should return a number."
    assert isinstance(real_part, int) or isinstance(
        real_part, float
    ), f"'re' method returned '{type(real_part)}', but should return a number."
    after = str(instance)
    assert before == after, "\n".join(
        [
            f"The operation appears to have changed the number.",
            f"Before: '{before}'.",
            f"After:  '{after}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = real_part
    second_time = instance.re()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 're' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_im(ComplexNumber):
    assert hasattr(
        ComplexNumber, "im"
    ), f"Could not find member function 'im' of class 'ComplexNumber'"

    # Arrange
    instance = test_init(ComplexNumber)
    before = str(instance)
    print(f"Imaginary part of {instance} is:")

    # Act
    try:
        real_part = instance.im()
    except Exception as e:
        print(f"Error getting imaginary part of ComplexNumber: {e}")
        raise

    # Assert
    print(real_part)

    assert (
        real_part is not None
    ), f"'im' method returned 'None', but should return a number."
    assert isinstance(real_part, int) or isinstance(
        real_part, float
    ), f"'im' method returned '{type(real_part)}', but should return a number."
    after = str(instance)
    assert before == after, "\n".join(
        [
            f"The operation appears to have changed the number.",
            f"Before: '{before}'.",
            f"After:  '{after}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = real_part
    second_time = instance.im()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 'im' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_eq(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__eq__"
    ), f"Could not find member function '__eq__' of class 'ComplexNumber'"

    # Arrange
    instance1 = test_init(ComplexNumber)
    instance2 = test_init(ComplexNumber)
    before_left = str(instance1)
    before_right = str(instance2)
    print(f"Result of comparing {instance1} and {instance2} for equality:")

    # Act
    try:
        result = instance1 == instance2
    except Exception as e:
        print(f"Error equating Vectors: {e}")
        raise

    # Assert
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
            f"The comparison appears to have changed the left number.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The comparison appears to have changed the right number.",
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


def test_conjugate(ComplexNumber):
    assert hasattr(
        ComplexNumber, "conjugate"
    ), f"Could not find member function 'conjugate' of class 'ComplexNumber'"

    # Arrange
    instance = test_init(ComplexNumber)
    before = str(instance)
    print(f"The conjucate of {instance} is:")

    # Act
    try:
        conjugate = instance.conjugate()
    except Exception as e:
        print(f"Error getting conjugate of ComplexNumber: {e}")
        raise

    # Assert
    print(conjugate)

    assert (
        conjugate is not None
    ), f"'conjugate' method returned 'None', but should return a 'ComplexNumber'."
    assert isinstance(
        conjugate, ComplexNumber
    ), f"'conjugate' method returned '{type(conjugate)}', but should return a 'ComplexNumber'."
    after = str(instance)
    assert before == after, "\n".join(
        [
            f"The operation appears to have changed the number.",
            f"Before: '{before}'.",
            f"After:  '{after}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = conjugate
    second_time = instance.conjugate()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 'conjugate' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_neg(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__neg__"
    ), f"Could not find member function '__neg__' of class 'ComplexNumber'"

    # Arrange
    instance = test_init(ComplexNumber)
    before = str(instance)
    print(f"The negation of {instance} is:")

    # Act
    try:
        negative = -instance
    except Exception as e:
        print(f"Error getting negation of ComplexNumber: {e}")
        raise

    # Assert
    print(negative)

    assert (
        negative is not None
    ), f"'__neg__' method returned 'None', but should return a 'ComplexNumber'."
    assert isinstance(
        negative, ComplexNumber
    ), f"'__neg__' method returned '{type(negative)}', but should return a 'ComplexNumber'."
    after = str(instance)
    assert before == after, "\n".join(
        [
            f"The operation appears to have changed the number.",
            f"Before: '{before}'.",
            f"After:  '{after}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = negative
    second_time = -instance
    assert first_time == second_time, "\n".join(
        [
            "It appears that the '__neg__' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_add(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__add__"
    ), f"Could not find member function '__add__' of class 'ComplexNumber'"

    # Arrange
    instance1 = test_init(ComplexNumber)
    instance2 = test_init(ComplexNumber)
    before_left = str(instance1)
    before_right = str(instance2)
    print(f"Result of adding {instance1} and {instance2} together:")

    # Act
    try:
        result = instance1 + instance2
    except Exception as e:
        print(f"Error adding ComplexNumbers: {e}")
        raise

    # Assert
    print(result)

    assert isinstance(result, ComplexNumber), "\n".join(
        [
            f"Method '__add__' did not return a ComplexNumber, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The addition appears to have changed the left number.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The addition appears to have changed the right number.",
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


def test_sub(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__sub__"
    ), f"Could not find member function '__sub__' of class 'ComplexNumber'"

    # Arrange
    instance1 = test_init(ComplexNumber)
    instance2 = test_init(ComplexNumber)
    before_left = str(instance1)
    before_right = str(instance2)
    print(f"Result of subtracting {instance2} from {instance1}:")

    # Act
    try:
        result = instance1 - instance2
    except Exception as e:
        print(f"Error subtracting ComplexNumbers: {e}")
        raise

    # Assert
    print(result)

    assert isinstance(result, ComplexNumber), "\n".join(
        [
            f"Method '__sub__' did not return a ComplexNumber, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The subtraction appears to have changed the left number.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The subtraction appears to have changed the right number.",
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


def test_mul(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__mul__"
    ), f"Could not find member function '__mul__' of class 'ComplexNumber'"

    # Arrange
    instance1 = test_init(ComplexNumber)
    instance2 = test_init(ComplexNumber)
    before_left = str(instance1)
    before_right = str(instance2)
    print(f"Result of multiplying {instance1} and {instance2}:")

    # Act
    try:
        result = instance1 * instance2
    except Exception as e:
        print(f"Error multiplying ComplexNumbers: {e}")
        raise

    # Assert
    print(result)

    assert isinstance(result, ComplexNumber), "\n".join(
        [
            f"Method '__mul__' did not return a ComplexNumber, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The multiplication appears to have changed the left number.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The multiplication appears to have changed the right number.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1 * instance2
    assert first_time == second_time, "\n".join(
        [
            "It appears that the multiplication has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_inverse(ComplexNumber):
    assert hasattr(
        ComplexNumber, "inverse"
    ), f"Could not find member function 'inverse' of class 'ComplexNumber'"

    # Arrange
    instance = test_init(ComplexNumber)
    before = str(instance)
    print(f"The inverse of {instance} is:")

    # Act
    try:
        inverse = instance.inverse()
    except Exception as e:
        print(f"Error getting inverse of ComplexNumber: {e}")
        raise

    # Assert
    print(str(inverse).replace("i", " i"))  # For tokenizer.

    assert (
        inverse is not None
    ), f"'inverse' method returned 'None', but should return a 'ComplexNumber'."
    assert isinstance(
        inverse, ComplexNumber
    ), f"'inverse' method returned '{type(inverse)}', but should return a 'ComplexNumber'."
    after = str(instance)
    assert before == after, "\n".join(
        [
            f"The operation appears to have changed the number.",
            f"Before: '{before}'.",
            f"After:  '{after}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = inverse
    second_time = instance.inverse()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 'inverse' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )


def test_truediv(ComplexNumber):
    assert hasattr(
        ComplexNumber, "__truediv__"
    ), f"Could not find member function '__truediv__' of class 'ComplexNumber'"

    # Arrange
    instance1 = test_init(ComplexNumber)
    instance2 = test_init(ComplexNumber)
    before_left = str(instance1)
    before_right = str(instance2)
    print(f"Result of dividing {instance1} by {instance2}:")

    # Act
    try:
        result = instance1 / instance2
    except Exception as e:
        print(f"Error dividing ComplexNumbers: {e}")
        raise

    # Assert
    print(str(result).replace("i", " i"))  # For tokenizer.

    assert isinstance(result, ComplexNumber), "\n".join(
        [
            f"Method '__truediv__' did not return a ComplexNumber, as expected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            f"The division appears to have changed the left number.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            f"The division appears to have changed the right number.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = result
    second_time = instance1 / instance2
    assert first_time == second_time, "\n".join(
        [
            "It appears that the division has some unwanted side effects.",
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
