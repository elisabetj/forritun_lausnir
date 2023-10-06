from typing import Tuple

from solution_code import extract_evens, remove_odds


def main():
    # You can use this for local testing:
    run_examples()
    # or
    run_samples()

    # Or run this to take input from terminal:
    run_like_autograder()


def run_examples():
    # Example usage
    a_list = [1, 1, 2, 3, 4, 5]
    print(f"a_list initially: {a_list}")
    remove_odds(a_list)
    print(f"a_list after removing odds: {a_list}")

    b_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"b_list initially: {b_list}")
    c_list = extract_evens(b_list)
    print(f"b_list after extracting evens: {b_list}")
    print(f"c_list after extracting evens: {c_list}")


def run_samples():
    run_sample_1()
    run_sample_2()
    # Add the other samples yourself if you wish.


def run_sample_1():
    test_input = "1 1 2 3 4 5"
    int_list = get_int_list(test_input)
    output(int_list)


def run_sample_2():
    test_input = "10 7 7 7 7 1 10 9 9"
    int_list = get_int_list(test_input)
    output(int_list)


def get_int_list(test_input: str):
    return [int(string) for string in test_input.split()]


def output(int_list):
    print(f"Original list before calling functions: {int_list}")
    result = extract_evens(int_list)
    print(f"Resulting list after extracting evens: {result}")
    print(f"Original list after extracting evens and before removing odds: {int_list}")
    remove_odds(int_list)
    print(f"Original list after removing odds: {int_list}")


def run_like_autograder():
    int_list = get_int_list(input())
    test(int_list)


def test(test_input):
    print(f"Original list before calling functions: {test_input}")
    test_extract_evens(test_input)
    print(
        f"Original list after extracting evens and before removing odds: {test_input}"
    )
    test_remove_odds(test_input)


def test_extract_evens(test_input):
    # Arrange.
    original_input = test_input[:]

    expected_return_type = list
    expected_value_afterwards = original_input

    # Act.
    actual = extract_evens(test_input)
    actual_return_type = type(actual)

    # Assert.
    print(f"Resulting list after extracting evens: {actual}")
    message = "\n".join(
        [
            f"\n\nInput to function 'extract_evens':",
            f" int_list ({type(original_input)}):\n{original_input}\n",
            f"Expected type of output: {expected_return_type}",
            f"Actual type of output: {actual_return_type}",
        ]
    )
    assert isinstance(actual, expected_return_type), message

    actual = test_input
    message = "\n".join(
        [
            f"\n\nInput to function 'extract_evens':",
            f" int_list ({type(original_input)}):\n{original_input}\n",
            f"Expected to remain unchanged.",
            f"Value afterwards ({type(actual)}):\n{actual}\n",
        ]
    )
    assert actual == expected_value_afterwards, message


def test_remove_odds(test_input):
    # Arrange.
    expected_return_value = None

    # Act.
    actual_return_value = remove_odds(test_input)
    actual = test_input

    # Assert.
    print(f"Original list after removing odds: {actual}")
    message = "\n".join(
        [
            f"\n\nInput to function 'remove_odds':",
            f" int_list ({type(test_input)}):\n{test_input}\n",
            f"Expected output: {expected_return_value}",
            f"Actual output: {actual_return_value}",
        ]
    )
    assert actual_return_value == expected_return_value, message


if __name__ == "__main__":
    main()
