#!/usr/bin/python3
import re
import sys

ITEM = "item"
CATALOG = "catalog"


def main():
    module_name = sys.stdin.readline()
    assert re.match("(item|catalog)\n$", module_name), "Unknown module"

    module_name = module_name.strip()
    if module_name == ITEM:
        check_item()
    elif module_name == CATALOG:
        check_catalog()

    assert not sys.stdin.read()
    sys.exit(42)


def check_item():
    method = sys.stdin.readline()
    assert re.match(
        "(__init__|__str__|set_name|set_category)\n$", method
    ), "Unknown method"
    method = method.strip()
    check_input_string()
    check_input_string()

    if method == "set_name":
        check_input_string()
    elif method == "set_category":
        check_input_string()


def check_catalog():
    method = sys.stdin.readline()
    assert re.match(
        "(__init__|__str__|set_name|add|remove|clear)\n$", method
    ), "Unknown method"
    method = method.strip()
    check_input_string()

    if method == "set_name":
        check_input_string()
    elif method == "add":
        check_item_sequence()
    elif method == "remove":
        how_many = check_item_sequence()
        num_to_remove_str = sys.stdin.readline()
        assert re.match("[1-5]\n$", num_to_remove_str)
        num_to_remove = int(num_to_remove_str)
        assert num_to_remove <= how_many, "Illegal item to remove"
    elif method == "clear":
        check_item_sequence()


def check_item_sequence():
    how_many_str = sys.stdin.readline()
    assert re.match("[1-5]\n$", how_many_str)
    how_many = int(how_many_str)
    for i in range(how_many):
        check_input_string()
        check_input_string()
    return how_many


def check_input_string():
    a_str = sys.stdin.readline()
    assert re.match(".*\n$", a_str), "Illegal string"


if __name__ == "__main__":
    main()
