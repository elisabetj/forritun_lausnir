#!/usr/bin/python3

def get_function_info(function: callable) -> str:
    divider = "-" * 40
    args = [0] * function.func_code.co_argcount
    function(*args)
    return f"Name: {function.__name__}\n{divider}\n{function.__doc__}"
