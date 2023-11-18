#!/usr/bin/python3

from waterbottle import WaterBottle

TOLERANCE = 0.00001


def main():
    # The sample from the problem statement
    run_problem_statement_example()

    # These are more or less the same as the example given in the problem statement,
    # but split into individual parts:
    # run_samples()


def run_problem_statement_example():
    bottle = WaterBottle(5)
    print(f"Bottle max capacity: {bottle.max_capacity}L.")

    bottle.fill()
    print(f"Currently holding {bottle.current_contents}L of water.")

    sip = bottle.drink(3.7)
    print(f"Received {sip} liters.")

    print(bottle)


def run_samples():
    print("Running sample 1")
    sample1_test_constructor()

    print("Running sample 2")
    sample2_test_fill()

    print("Running sample 3")
    sample3_test_drink()

    print("Running sample 4")
    sample4_test_print()


def sample1_test_constructor():
    """Constructor tests."""
    # Arrange
    test_input = 5
    expected_capacity = 5
    expected_contents = 0

    # Act
    bottle = WaterBottle(max_capacity=test_input)
    actual_capacity = bottle.max_capacity
    actual_contents = bottle.current_contents

    # Assert
    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}): {test_input}",
            f"Expected capacity ({type(expected_capacity)}): {expected_capacity}",
            f"Actual capacity ({type(actual_capacity)}): {actual_capacity}",
        ]
    )
    assert expected_capacity == actual_capacity, message

    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}): {test_input}",
            f"Expected contents ({type(expected_contents)}): {expected_contents}",
            f"Actual contents ({type(actual_contents)}): {actual_contents}",
        ]
    )
    assert expected_contents == actual_contents, message


def sample2_test_fill():
    """Fill function test."""
    # Arrange
    test_input = 10
    bottle = WaterBottle(max_capacity=test_input)
    expected = test_input

    # Act
    bottle.fill()
    actual = bottle.current_contents

    # Assert
    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}): {test_input}",
            f"Expected contents ({type(expected)}): {expected}",
            f"Actual contents ({type(actual)}): {actual}",
        ]
    )
    assert expected == actual, message


def sample3_test_drink():
    # Arrange
    size = 5
    bottle = WaterBottle(max_capacity=size)
    bottle.fill()

    test_input = 3.7
    expected = test_input

    # Act
    actual = bottle.drink(test_input)

    # Assert
    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}): {test_input}",
            f"Expected output ({type(expected)}): {expected}",
            f"Actual output ({type(actual)}): {actual}",
        ]
    )
    assert abs(expected - actual) < TOLERANCE, message


def sample4_test_print():
    # Arrange
    size = 4
    bottle = WaterBottle(max_capacity=size)
    bottle.fill()

    expected = "The bottle currently holds 4.0L of water."

    # Act
    actual = str(bottle)

    # Assert
    message = "\n".join(
        [
            f"\n\nExpected output ({type(expected)}):\n{expected}\n",
            f"Actual output ({type(actual)}):\n{actual}\n",
        ]
    )
    assert expected == actual, message


if __name__ == "__main__":
    main()
