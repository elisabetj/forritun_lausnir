#!/usr/bin/python3

import sys
from importlib import import_module
from pathlib import Path

sys.dont_write_bytecode = True

CLASS_NAME = "Height"


def main():
    module_name = input()
    if module_name == "height":
        test_height()
    else:
        assert False, "Unknown test type"


def test_height():
    Height = get_class()
    callables = {
        "__init__": test_height_init,
        "__str__": test_height_str,
        "__add__": test_height_add,
        "__gt__": test_height_greater_than,
        "cm": test_height_cm,
    }

    callable_name = input()
    callables[callable_name](Height)


def test_height_init(Height):
    assert hasattr(Height, "__init__"), " ".join(
        [
            "Could not find member function '__init__'",
            "of class 'Height'.",
        ]
    )

    actual_number_of_parameters = Height.__init__.__code__.co_argcount
    expected_number_of_parameters = 2 + 1  # Feet, inches and self.
    assert actual_number_of_parameters == expected_number_of_parameters, (
        f"Unexpected number of parameters, {actual_number_of_parameters}.",
    )

    # Arrange.
    feet = int(input())
    inches = int(input())

    # Act.
    try:
        instance = Height(feet, inches)
    except Exception as e:
        print(f"Error calling Height constructor: {e}")
        raise

    # Assert.
    return instance


def test_height_str(Height):
    assert hasattr(Height, "__str__"), " ".join(
        [
            "Could not find member function '__str__'",
            "of class 'Height'.",
        ]
    )

    # Arrange.
    instance = test_height_init(Height)

    # Act.
    try:
        representation = str(instance)
    except Exception as e:
        print(f"Error getting string of Height instance: {e}")
        raise

    # Assert.
    print(representation)
    assert isinstance(representation, str), " ".join(
        [
            f"'__str__' method returned '{type(representation)}',",
            "but should return 'str'.",
        ]
    )
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
    return instance


def test_height_add(Height):
    assert hasattr(Height, "__add__"), " ".join(
        [
            "Could not find member function '__add__'",
            "of class 'Height'.",
        ]
    )

    # Arrange.
    instance1 = test_height_init(Height)
    instance2 = test_height_init(Height)
    before_left = str(instance1)
    before_right = str(instance2)

    # Act.
    try:
        instance3 = instance1 + instance2
    except Exception as e:
        print(f"Error adding two instances of height: {e}")
        raise

    # Assert.
    print(instance3)
    assert isinstance(instance3, Height), "\n".join(
        [
            "Method '__add__' did not return a Height instance, as expected.",
            f"Actual return type: {type(instance3)}",
            f"Actual return value: {instance3}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            "The addition appears to have changed the left operand.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            "The addition appears to have changed the right operand.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = str(instance3)
    second_time = str(instance1 + instance2)
    assert first_time == second_time, "\n".join(
        [
            "It appears that the addition has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )

    return instance3


def test_height_greater_than(Height):
    assert hasattr(Height, "__gt__"), " ".join(
        [
            "Could not find member function '__gt__'",
            "of class 'Height'.",
        ]
    )

    # Arrange.
    instance1 = test_height_init(Height)
    instance2 = test_height_init(Height)
    before_left = str(instance1)
    before_right = str(instance2)

    # Act.
    try:
        return_value = instance1 > instance2
    except Exception as e:
        print(f"Error calling > for height: {e}")
        raise

    # Assert.
    print(return_value)
    assert isinstance(return_value, bool), "\n".join(
        [
            "Method '__gt__' did not return a bool, as expected.",
            f"Actual return type: {type(return_value)}",
            f"Actual return value: {return_value}",
        ]
    )
    after_left = str(instance1)
    after_right = str(instance2)
    assert before_left == after_left, "\n".join(
        [
            "The comparison appears to have changed the left operand.",
            f"Before: '{before_left}'.",
            f"After:  '{after_left}'.",
            "It should remain unchanged.",
        ]
    )
    assert before_right == after_right, "\n".join(
        [
            "The comparison appears to have changed the right operand.",
            f"Before: '{before_right}'.",
            f"After:  '{after_right}'.",
            "It should remain unchanged.",
        ]
    )
    first_time = return_value
    second_time = instance1 > instance2
    assert first_time == second_time, "\n".join(
        [
            "It appears that the comparison has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )

    return return_value


def test_height_cm(Height):
    assert hasattr(Height, "cm"), " ".join(
        [
            "Could not find member function 'cm'",
            "of class 'Height'.",
        ]
    )

    # Arrange.
    instance = test_height_init(Height)

    # Act.
    try:
        cm = instance.cm()
    except Exception as e:
        print(f"Error getting cms: {e}")
        raise

    # Assert.
    print(cm)
    assert isinstance(cm, int), " ".join(
        [
            f"'cm' method returned '{type(cm)}',",
            "but should return an integer.",
        ]
    )
    first_time = cm
    second_time = instance.cm()
    assert first_time == second_time, "\n".join(
        [
            "It appears that the 'cm' method has some unwanted side effects.",
            "It does not return the same value when it is called twice in a row.",
            f"Here's what it returned the first time it was called: '{first_time}'.",
            f"And here's what it returned the second time: '{second_time}'.",
        ]
    )
    return instance


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
