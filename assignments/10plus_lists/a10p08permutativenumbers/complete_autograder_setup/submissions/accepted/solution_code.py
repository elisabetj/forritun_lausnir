def main():
    hi_end = int(input())
    for candidate in range(10, hi_end + 1):
        if is_permutative(candidate):
            print(candidate)


def is_permutative(number: int) -> bool:
    """Returns True if number is permutative, False otherwise."""

    for i in range(2, number_of_digits(number) + 1):
        if not are_permutation_of_same_digits(number, number * i):
            return False
    return True


def number_of_digits(number: int) -> int:
    return len(str(number))


def are_permutation_of_same_digits(num1: int, num2: int) -> bool:
    """Returns True if num1 and num2 are permutations of each other, False otherwise."""

    return sorted_digits(num1) == sorted_digits(num2)


def sorted_digits(number: int) -> list:
    return sorted(str(number))


if __name__ == "__main__":
    main()
