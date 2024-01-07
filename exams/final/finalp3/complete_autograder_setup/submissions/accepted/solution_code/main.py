#!/usr/bin/python3

import sys

from height import Height

sys.dont_write_bytecode = True


def main():
    module_name = input()
    if module_name == "height":
        test_height()
    else:
        assert False, "Unknown test type"


def test_height():
    callables = {
        "__init__": create_height_instance,
        "__str__": print_height_instance,
        "__add__": demonstrate_adding,
        "__gt__": demonstrate_comparison,
        "cm": demonstrate_cm_conversion,
    }

    callable_name = input()
    callables[callable_name]()


def create_height_instance():
    feet = int(input())
    inches = int(input())
    instance = Height(feet, inches)
    return instance


def print_height_instance():
    instance = create_height_instance()
    print(instance)
    return instance


def demonstrate_adding():
    instance1 = create_height_instance()
    instance2 = create_height_instance()
    instance3 = instance1 + instance2
    print(instance3)
    return instance3


def demonstrate_comparison():
    instance1 = create_height_instance()
    instance2 = create_height_instance()
    return_value = instance1 > instance2
    print(return_value)
    return return_value


def demonstrate_cm_conversion():
    instance = create_height_instance()
    cm = instance.cm()
    print(cm)
    return instance


if __name__ == "__main__":
    main()
