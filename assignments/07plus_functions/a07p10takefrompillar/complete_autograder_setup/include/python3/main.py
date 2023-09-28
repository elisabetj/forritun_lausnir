from os import getcwd
from importlib import import_module
from pathlib import Path


def main():
    take_from_pillar = get_function("take_from_pillar")

    state = input()
    pillar = int(input())
    return_val = take_from_pillar(state, pillar)
    assert isinstance(return_val[0], str)
    assert isinstance(return_val[1], str)
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
