def main():
    lines = gather_input()
    for line in lines:
        process(line)


def gather_input():
    lines = []

    while (line := readline()) is not None:
        lines.append(line)

    return lines


def readline():
    try:
        return input()
    except EOFError:
        return None


def process(line):
    file_handle = open_file(line)
    if file_handle is None:
        print(f"{line} not found! Please try again.")
        return

    with file_handle:
        numbers = get_numbers_from_file(file_handle)
        display_numbers(numbers)


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
