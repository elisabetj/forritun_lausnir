def main():
    with get_file() as file_obj:
        numbers = get_numbers_from_file(file_obj)
        display_numbers(numbers)


def get_file():
    """Gets file name from user and returns the open file handle.

    Asks the user repeatedly for file name
    until an existing file name is given.
    """

    raise NotImplementedError  # TODO: Delete this line,
    # and implement this function.
    # You can call the following function in your implementation.


def open_file(filename: str):
    try:
        return open(filename)
    except FileNotFoundError:
        return None


def get_numbers_from_file(file) -> list:
    """Returns a list of all numbers in the given file.

    Assumes all numbers appear on their own,
    separated from other text by whitespace.
    """

    raise NotImplementedError  # TODO: Implement this function.


def display_numbers(numbers):
    """Prints out the list, after sorting it."""

    raise NotImplementedError  # TODO: Implement this function.


if __name__ == "__main__":
    main()
