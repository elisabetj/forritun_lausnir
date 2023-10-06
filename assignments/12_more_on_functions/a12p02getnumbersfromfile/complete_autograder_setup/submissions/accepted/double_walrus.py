def main():
    with get_file() as file_obj:
        numbers = get_numbers_from_file(file_obj)
        display_numbers(numbers)


def get_file():
    """Gets file name from user and returns the open file handle.

    Asks the user repeatedly for file name
    until an existing file name is given.
    """

    while (file_handle := open_file(file_name := input())) is None:
        print(f"{file_name} not found! Please try again.")

    return file_handle


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

    numbers = []
    for line in file:
        word_list = line.strip().split()
        for word in word_list:
            if word.isdigit():
                numbers.append(int(word))
    return numbers


def display_numbers(numbers):
    """Prints out the sorted list."""

    print(sorted(numbers))


if __name__ == "__main__":
    main()
