def main():
    dictionary = {}

    add_word(dictionary)
    while more():
        add_word(dictionary)

    display_result(dictionary)


def add_word(dictionary: dict) -> None:
    """Asks the user for a word and definition and stores it in the dictionary."""

    raise NotImplementedError  # TODO: remove this line and implement the function.


def more() -> bool:
    """Checks if the user wants to add more words."""

    raise NotImplementedError  # TODO: remove this line and implement the function.


def display_result(dictionary: dict) -> None:
    """Prints the words in alphabetical order, along with the definitions."""

    raise NotImplementedError  # TODO: remove this line and implement the function.


if __name__ == "__main__":
    main()
