#!/usr/bin/python3

import sys
import importlib
from typing import Iterable

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
    callables = prepare_item()
    if callables is None:
        return

    callable_name = input()
    callables[callable_name]()


def test_catalog():
    item_callables = prepare_item()
    if item_callables is None:
        return

    callables = prepare_catalog()
    if callables is None:
        return

    callable_name = input()
    callables[callable_name]()


def prepare_item():
    module_name = "item"
    class_name = "Item"
    callables = {
        "__init__": test_item_init,
        "__str__": test_item_str,
        "set_name": test_set_item_name,
        "set_category": test_item_set_category,
    }

    if not prepare(module_name, class_name, callables):
        return

    return callables


def prepare_catalog():
    module_name = "catalog"
    class_name = "Catalog"
    callables = {
        "__init__": test_catalog_init,
        "__str__": test_catalog_str,
        "set_name": test_set_catalog_name,
        "add": test_add_catalog,
        "remove": test_remove_catalog,
        "clear": test_clear_catalog,
    }

    if not prepare(module_name, class_name, callables):
        return

    return callables


def prepare(module_name: str, class_name: str, expected_callables: Iterable):
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"Could not import module {module_name}, does {module_name}.py exist?")
        return False

    if not hasattr(module, class_name):
        print(f"Could not find class {class_name} in module {module_name}")
        return False

    cls = getattr(module, class_name)

    for callable_name in expected_callables:
        if not hasattr(cls, callable_name):
            print(f"Could not find member function {callable_name} of class {class_name}")
            return False

    globals()[module_name] = module
    globals()[class_name] = cls
    return True


def test_item_init():
    name = input()
    category = input()
    instance = None
    try:
        instance = Item(name, category)
    except Exception as e:
        print(f"Error calling constructor: {e}")
    return instance


def test_item_str():
    instance = test_item_init()
    if instance is not None:
        try:
            print(instance)
        except Exception as e:
            print(f"Error printing item: {e}")
    return instance


def test_set_item_name():
    instance = test_item_init()
    if instance is None:
        return None
    new_name = input()
    try:
        result = instance.set_name(new_name)
        if result is not None:
            print(f"Function set_name should not return a value but returned `{repr(result)}`")
            return None
    except Exception as e:
        print(f"Error setting name of item: {e}")
    try:
        print(instance)
    except Exception as e:
        print(f"Error printing item: {e}")
    return instance


def test_item_set_category():
    instance = test_item_init()
    if instance is None:
        return None
    new_category = input()
    try:
        result = instance.set_category(new_category)
        if result is not None:
            print(f"Function set_category should not return a value but returned `{repr(result)}`")
            return None
    except Exception as e:
        print(f"Error setting name of item: {e}")
    try:
        print(instance)
    except Exception as e:
        print(f"Error printing item: {e}")
    return instance


def test_catalog_init():
    name = input()
    instance = None
    try:
        instance = Catalog(name)
    except Exception as e:
        print(f"Error calling constructor: {e}")
    return instance


def test_catalog_str():
    instance = test_catalog_init()
    if instance is not None:
        try:
            print(instance)
        except Exception as e:
            print(f"Error printing catalog: {e}")
    return instance


def test_set_catalog_name():
    instance = test_catalog_init()
    if instance is None:
        return None
    new_name = input()
    try:
        result = instance.set_name(new_name)
        if result is not None:
            print(f"Function set_name should not return a value but returned `{repr(result)}`")
            return None
    except Exception as e:
        print(f"Error setting name of catalog: {e}")
    try:
        print(instance)
    except Exception as e:
        print(f"Error printing catalog: {e}")
    return instance


def add_items_to_catalog(catalog):
    items = []
    num_items = int(input())
    for i in range(num_items):
        item = test_item_init()
        items.append(item)
        try:
            result = catalog.add(item)
            if result is not None:
                print(f"Function add should not return a value but returned `{repr(result)}`")
                return None
        except Exception as e:
            print(f"Error adding to catalog: {e}")
    return items


def test_add_catalog():
    catalog = test_catalog_init()
    if catalog is None:
        return None

    add_items_to_catalog(catalog)
    try:
        print(catalog)
    except Exception as e:
        print(f"Error printing catalog: {e}")
    return catalog


def test_remove_catalog():
    catalog = test_catalog_init()
    if catalog is None:
        return None

    items = add_items_to_catalog(catalog)
    item_num_to_remove = int(input())
    item_to_remove = items[item_num_to_remove - 1]
    try:
        catalog.remove(item_to_remove)
    except Exception as e:
        print(f"Error removing from catalog: {e}")

    try:
        print(catalog)
    except Exception as e:
        print(f"Error printing catalog: {e}")
    return catalog


def test_clear_catalog():
    catalog = test_catalog_init()
    if catalog is None:
        return None

    add_items_to_catalog(catalog)
    try:
        print(catalog)
    except Exception as e:
        print(f"Error printing catalog: {e}")
    try:
        catalog.clear()
    except Exception as e:
        print(f"Error clearing catalog: {e}")

    try:
        print(catalog)
    except Exception as e:
        print(f"Error printing catalog: {e}")
    return catalog


if __name__ == "__main__":
    main()
