from importlib import import_module
from pathlib import Path


def main():
    # Arrange.
    function_name = "list_to_bool_tuple"
    list_to_bool_tuple = get_function(function_name)
    expected_return_type = tuple
    test_input = input().strip().split(",")

    # Act.
    actual = list_to_bool_tuple(test_input)
    actual_return_type = type(actual)

    # Assert.
    print(actual)
    message = "\n".join(
        [
            f"\n\nInput to function '{function_name}':",
            f" a_list ({type(test_input)}):\n{test_input}\n",
            f"Expected type of output: {expected_return_type}",
            f"Actual type of output: {actual_return_type}",
        ]
    )
    assert isinstance(actual, expected_return_type), message


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
