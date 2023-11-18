#!/usr/bin/python3

import sys
import importlib
from typing import Iterable

sys.dont_write_bytecode = True

def prepare(module_name: str, class_name: str, required_callables: Iterable):
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"Could not import module {module_name}, does {module_name}.py exist?")
        return False

    if not hasattr(module, class_name):
        print(f"Could not find class {class_name} in module {module_name}")
        return False

    cls = getattr(module, class_name)

    #for callable_name in required_callables:
    #    if not hasattr(cls, callable_name):
    #        print(f"Could not find member function {callable_name} of class {class_name}")
    #        return False
    
    globals()[module_name] = module
    globals()[class_name] = cls
    return True


def test_clock_init():
    use_default = bool(input())
    hours = int(input())
    minutes = int(input())
    seconds = int(input())
    if use_default:
        args = tuple()
        if hours or minutes or seconds:
            args = args + (hours, )
            if minutes or seconds:
                args = args + (minutes, )
                if seconds:
                    args = args + (seconds, )
    else:
        args = (hours, minutes, seconds)
    instance = None
    try:
        instance = Clock(*args)
    except Exception as e:
        print(f"Error calling constructor: {e}")
    return instance


def test_clock_str():
    instance = test_clock_init()
    if instance is not None:
        try:
            print(instance)
        except Exception as e:
            print(f"Error printing clock: {e}")
    return instance


def test_clock_str_update():
    instance = test_clock_str()
    if instance is None:
        return None
    new_value = input()
    try:
        result = instance.str_update(new_value)
        if result is not None:
            print(f"Function str_update should not return a value but returned `{repr(result)}`")
            return None
    except Exception as e:
        print(f"Error calling str_update: {e}")
    try:
        print(instance)
    except Exception as e:
        print(f"Error printing clock: {e}")
    return instance


def test_clock_add():
    instance = test_clock_init()
    if instance is None:
        return None
    other = test_clock_init()
    try:
        result = instance.add_clocks(other)
        if not isinstance(result, Clock):
            print(f"Function add_clocks should not return a value of type Clock but returned `{repr(result)}`")
            return None
    except Exception as e:
        print(f"Error adding clocks: {e}")
    try:
        print(instance)
        print(other)
        print(result)
    except Exception as e:
        print(f"Error printing clock: {e}")
    return instance


def prepare_clock():
    module_name = "clock"
    class_name = "Clock"
    callables = {
        "__init__": test_clock_init,
        "__str__": test_clock_str,
        "str_update": test_clock_str_update,
        "add_clocks": test_clock_add
    }
    
    if not prepare(module_name, class_name, callables):
        return
    
    return callables


def test_clock():
    callables = prepare_clock() 

    callable_name = input()
    callables[callable_name]()


def main():
    prepare_clock()
    test_clock()
    

if __name__ == "__main__":
    main()
