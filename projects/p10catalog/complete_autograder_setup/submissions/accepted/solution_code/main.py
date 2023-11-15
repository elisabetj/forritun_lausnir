#!/usr/bin/python3

import sys
import importlib
from typing import Iterable

from item import Item
from catalog import Catalog

sys.dont_write_bytecode = True


def main():
    module_name = input()
    if module_name == "item":
        test_item()
    elif module_name == "catalog":
        test_catalog()
    else:
        assert False, "Unknown test type"


def test_item():
    callables = {
        "__init__": create_item,
        "__str__": print_item,
        "set_name": set_item_name,
        "set_category": set_item_category,
    }

    callable_name = input()
    callables[callable_name]()


def test_catalog():
    callables = {
        "__init__": create_catalog,
        "__str__": print_catalog,
        "set_name": set_catalog_name,
        "add": add_to_catalog,
        "remove": remove_from_catalog,
        "clear": clear_catalog,
    }

    callable_name = input()
    callables[callable_name]()


def create_item():
    name = input()
    category = input()
    instance = Item(name, category)
    return instance


def print_item():
    instance = create_item()
    print(instance)
    return instance


def set_item_name():
    instance = create_item()
    new_name = input()
    instance.set_name(new_name)
    print(instance)
    return instance


def set_item_category():
    instance = create_item()
    new_category = input()
    instance.set_category(new_category)
    print(instance)
    return instance


def create_catalog():
    name = input()
    instance = Catalog(name)
    return instance


def print_catalog():
    instance = create_catalog()
    print(instance)
    return instance


def set_catalog_name():
    instance = create_catalog()
    new_name = input()
    instance.set_name(new_name)
    print(instance)
    return instance


def add_items_to_catalog(catalog):
    items = []
    num_items = int(input())
    for i in range(num_items):
        item = create_item()
        items.append(item)
        catalog.add(item)
    return items


def add_to_catalog():
    catalog = create_catalog()
    add_items_to_catalog(catalog)
    print(catalog)
    return catalog


def remove_from_catalog():
    catalog = create_catalog()
    items = add_items_to_catalog(catalog)

    item_num_to_remove = int(input())
    item_to_remove = items[item_num_to_remove - 1]
    catalog.remove(item_to_remove)

    print(catalog)
    return catalog


def clear_catalog():
    catalog = create_catalog()
    add_items_to_catalog(catalog)

    print(catalog)
    catalog.clear()
    print(catalog)

    return catalog


if __name__ == "__main__":
    main()
