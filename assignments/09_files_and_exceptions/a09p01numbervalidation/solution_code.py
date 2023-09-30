def is_float(string_to_test: str) -> bool:
    """Returns True if the given string is a float, otherwise False."""
    try:
        float(string_to_test)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    a = input()
    print(is_float(a))
