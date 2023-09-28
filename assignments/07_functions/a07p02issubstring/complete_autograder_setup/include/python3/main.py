from importlib import import_module
from pathlib import Path


def main():
    function_name = "is_substring_of"
    is_substring_of = get_function(function_name)

    substring = input()
    regstring = input()
    return_val = is_substring_of(substring, regstring)
    print(return_val)

    expected_type = bool
    actual_type = type(return_val)
    message = f"[Function {function_name} returned type {actual_type}, but expected type {expected_type}.]"
    assert isinstance(return_val, expected_type), message


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
