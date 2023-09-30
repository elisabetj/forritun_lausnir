from os import getcwd
from importlib import import_module
from pathlib import Path
import sys


def main():
    # Arrange.
    function_name = "change_indentation"
    change_indentation = get_function(function_name)
    expected_return_type = str
    indent = int(input())
    text = sys.stdin.read()

    # Act.
    actual = change_indentation(text, indent)
    actual_return_type = type(actual)

    # Assert.
    print(actual, end="")
    message = f"\n\nInput to function '{function_name}':"
    message += f"\n text ({type(text)}):\n{text}\n"
    message += f"\n spaces ({type(indent)}): {indent}"
    message += f"\nExpected type of output: {expected_return_type}"
    message += f"\nActual type of output: {actual_return_type}"
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
