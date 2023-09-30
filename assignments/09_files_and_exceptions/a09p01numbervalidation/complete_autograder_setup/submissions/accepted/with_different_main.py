def is_float(string_to_test: str) -> bool:
    """Returns True if the given string is a float, otherwise False."""
    try:
        float(string_to_test)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print(is_float("3.45"))
    print(is_float("3e4"))
    print(is_float(".5"))
    print(is_float("abc"))
    print(is_float("4.x"))
