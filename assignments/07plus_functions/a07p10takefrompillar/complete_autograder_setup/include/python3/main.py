from os import getcwd
from importlib import import_module
from pathlib import Path


def main():
    # Arrange.
    function_name = "take_from_pillar"
    take_from_pillar = get_function(function_name)
    expected_return_type = tuple
    expected_number_of_return_values = 2
    expected_type = str
    state = input()
    pillar = int(input())

    # Act.
    actual = take_from_pillar(state, pillar)
    actual_return_type = type(actual)

    # Assert.
    print(actual)

    common_message = f"\n\nInput to function '{function_name}':"
    common_message += f"\n state ({type(state)}): {state}"
    common_message += f"\n pillar ({type(pillar)}): {pillar}"

    message = common_message
    message += f"\nExpected type of output: {expected_return_type}"
    message += f"\nActual type of output: {actual_return_type}"
    assert isinstance(actual, expected_return_type), message

    message = common_message
    message += f"\nExpected number of return values: {expected_number_of_return_values}"
    message += f"\nActual number of return values: {len(actual)}"
    assert len(actual) == expected_number_of_return_values, message

    message = common_message
    message += f"\nExpected type of first return value: {expected_type}"
    message += f"\nActual type of first return value: {type(actual[0])}"
    assert isinstance(actual[0], expected_type), message

    message = common_message
    message += f"\nExpected type of second return value: {expected_type}"
    message += f"\nActual type of second return value: {type(actual[1])}"
    assert isinstance(actual[1], expected_type), message


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
