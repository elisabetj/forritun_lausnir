def is_float(string_to_test: str) -> bool:
    """Returns True if the given string is a float, otherwise False."""

    # TODO: Add your implementation here.


if __name__ == "__main__":
    # See provided main.py file,
    # but you can also just run this here if you prefer,
    # when testing locally.

    print(is_float("3.45"))
    print(is_float("3e4"))
    print(is_float(".5"))
    print(is_float("abc"))
    print(is_float("4.x"))

    # a = input()
    # print(is_float(a))
