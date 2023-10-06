from importlib import import_module
from pathlib import Path


def main():
    int_list = [int(string) for string in input().split()]
    print(f"Original list before calling functions: {int_list}")
    test_without_outliers(int_list)
    print(
        "Original list after extracting middle",
        f"and before removing outliers: {int_list}",
    )
    test_remove_min_and_max(int_list)


def test_without_outliers(test_input):
    # Arrange.
    original_input = test_input[:]

    function_name = "without_outliers"
    without_outliers = get_function(function_name)
    expected_return_type = list
    expected_value_afterwards = original_input

    # Act.
    actual = without_outliers(test_input)
    actual_return_type = type(actual)

    # Assert.
    print(f"Resulting list after extracting middle: {actual}")
    message = "\n".join(
        [
            f"\n\nInput to function '{function_name}':",
            f" a_list ({type(original_input)}):\n{original_input}\n",
            f"Expected type of output: {expected_return_type}",
            f"Actual type of output: {actual_return_type}",
        ]
    )
    assert isinstance(actual, expected_return_type), message

    actual = test_input
    message = "\n".join(
        [
            f"\n\nInput to function '{function_name}':",
            f" a_list ({type(original_input)}):\n{original_input}\n",
            f"Expected to remain unchanged.",
            f"Value afterwards ({type(actual)}):\n{actual}\n",
        ]
    )
    assert actual == expected_value_afterwards, message


def test_remove_min_and_max(test_input):
    # Arrange.
    function_name = "remove_min_and_max"
    remove_min_and_max = get_function(function_name)
    expected_return_value = None

    # Act.
    actual_return_value = remove_min_and_max(test_input)
    actual = test_input

    # Assert.
    print(f"Original list after removing outliers: {actual}")
    message = "\n".join(
        [
            f"\n\nInput to function '{function_name}':",
            f" a_list ({type(test_input)}):\n{test_input}\n",
            f"Expected output: {expected_return_value}",
            f"Actual output: {actual_return_value}",
        ]
    )
    assert actual_return_value == expected_return_value, message


def get_function(name):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Name '{name}' is not defined.")


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
