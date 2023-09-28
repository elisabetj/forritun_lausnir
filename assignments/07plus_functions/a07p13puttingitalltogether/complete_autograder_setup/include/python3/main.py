from os import getcwd
from importlib import import_module
from pathlib import Path


def main():
    move_many = get_function("move_many")

    number_of_discs = int(input())
    from_pillar = int(input())
    to_pillar = int(input())
    state = input()
    move_many(number_of_discs, from_pillar, to_pillar, state)


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
