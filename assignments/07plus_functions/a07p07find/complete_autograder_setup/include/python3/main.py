from os import getcwd
from importlib import import_module
from pathlib import Path


def main():
    find_index_of_kth_occurrence = get_function("find_index_of_kth_occurrence")

    sequence = input()
    element_to_find = input()
    occurrence = int(input())
    return_val = find_index_of_kth_occurrence(sequence, element_to_find, occurrence)
    assert isinstance(return_val, int)
    print(return_val)


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
