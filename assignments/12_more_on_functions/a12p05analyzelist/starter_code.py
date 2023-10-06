def main():
    input_list = get_correct_data()
    raise NotImplementedError  # TODO: Finish the function.


def get_correct_data() -> list:
    """Asks user repeatedly for input until valid."""

    input_list = get_data()
    raise NotImplementedError  # TODO: Finish this function.


def get_data():
    """Returns a list of positive integers input by the user.

    Returns None if the input contains non-integers or integers < 0.
    """

    raise NotImplementedError  # TODO: Implement this function


# Add as many functions as you think you could use.


def is_prime(n: int) -> bool:
    """Returns True if the given positive number is prime and False otherwise."""

    if n < 2:
        return False

    for i in range(2, n):  # Feel free to improve this function if you like.
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()
