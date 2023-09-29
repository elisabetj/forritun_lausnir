from os import getcwd
from importlib import import_module
from pathlib import Path


def main():
    # Arrange.
    function_name = "move_many"
    move_many = get_function(function_name)
    expected_return_type = str
    number_of_discs = int(input())
    from_pillar = int(input())
    to_pillar = int(input())
    state = input()

    # Act.
    actual = move_many(number_of_discs, from_pillar, to_pillar, state)
    actual_return_type = type(actual)

    # Assert.
    message = f"\n\nInput to function '{function_name}':"
    message += f"\n number_of_discs ({type(number_of_discs)}): {number_of_discs}"
    message += f"\n from_pillar ({type(from_pillar)}): {from_pillar}"
    message += f"\n to_pillar ({type(to_pillar)}): {to_pillar}"
    message += f"\n state ({type(state)}): {state}"
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
