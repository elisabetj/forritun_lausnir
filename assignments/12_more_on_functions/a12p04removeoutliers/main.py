from typing import List

from solution_code import without_outliers, remove_min_and_max


def main():
    # You can use this for local testing:
    run_examples()
    # or
    run_samples()

    # Or run this to take input from terminal:
    run_like_autograder()


def run_examples():
    # Example usage
    a_list = [3, 9, 5, 1, 6, 8]
    print(f"Before calling remove_min_and_max: {a_list = }")
    remove_min_and_max(a_list)
    print(f"After calling remove_min_and_max: {a_list = }")

    b_list = [9, 2, 3, 6, 1, 8, 7]
    print(f"Before calling without_outliers: {b_list = }")
    c_list = without_outliers(b_list)
    print(f"After calling without_outliers: {b_list = }")
    print(f"After calling without_outliers: {c_list = }")

    # If the format strings are messing with you, read this:
    # https://docs.python.org/3/whatsnew/3.8.html#f-strings-support-for-self-documenting-expressions-and-debugging


def run_samples():
    run_sample_1()
    run_sample_2()
    # Add the other samples yourself if you wish.


def run_sample_1():
    test_input = "21 1 23 102"
    int_list = get_int_list(test_input)
    output(int_list)


def run_sample_2():
    test_input = "5 4 3 2 1 0"
    int_list = get_int_list(test_input)
    output(int_list)


def get_int_list(test_input: str) -> List[int]:
    return [int(string) for string in test_input.split()]


def output(int_list):
    print(f"Original list before calling functions: {int_list}")
    result = without_outliers(int_list)
    print(f"Resulting list after extracting middle: {result}")
    print(
        f"Original list after extracting middle and before removing outliers: {int_list}"
    )
    remove_min_and_max(int_list)
    print(f"Original list after removing outliers: {int_list}")


def run_like_autograder():
    int_list = get_int_list(input())
    test(int_list)


def test(test_input):
    print(f"Original list before calling functions: {test_input}")
    test_without_outliers(test_input)
    print(
        "Original list after extracting middle",
        f"and before removing outliers: {test_input}",
    )
    test_remove_min_and_max(test_input)


def test_without_outliers(test_input):
    # Arrange.
    original_input = test_input[:]
    expected_value_afterwards = original_input
    expected_return_type = list

    # Act.
    actual = without_outliers(test_input)
    actual_return_type = type(actual)

    # Assert.
    print(f"Resulting list after extracting middle: {actual}")
    message = "\n".join(
        [
            f"\n\nInput to function 'without_outliers':",
            f" a_list ({type(original_input)}):\n{original_input}\n",
            f"Expected type of output: {expected_return_type}",
            f"Actual type of output: {actual_return_type}",
        ]
    )
    assert isinstance(actual, expected_return_type), message

    actual = test_input
    message = "\n".join(
        [
            f"\n\nInput to function 'without_outliers':",
            f" a_list ({type(original_input)}):\n{original_input}\n",
            f"Expected to remain unchanged.",
            f"Value afterwards ({type(actual)}):\n{actual}\n",
        ]
    )
    assert actual == expected_value_afterwards, message


def test_remove_min_and_max(test_input):
    # Arrange.
    expected_return_value = None

    # Act.
    actual_return_value = remove_min_and_max(test_input)
    actual = test_input

    # Assert.
    print(f"Original list after removing outliers: {actual}")
    message = "\n".join(
        [
            f"\n\nInput to function 'remove_min_and_max':",
            f" a_list ({type(test_input)}):\n{test_input}\n",
            f"Expected output: {expected_return_value}",
            f"Actual output: {actual_return_value}",
        ]
    )
    assert actual_return_value == expected_return_value, message


if __name__ == "__main__":
    main()
