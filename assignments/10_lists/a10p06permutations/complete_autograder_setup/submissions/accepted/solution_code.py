#!/usr/bin/env python3


def main():
    a = input()
    b = input()
    if are_permutation_of_same_digits(a, b):
        print(f"The numbers {a} and {b} are permutations of each other.")
    else:
        print(f"The numbers {a} and {b} are not permutations of each other.")


def are_permutation_of_same_digits(m: str, n: str) -> bool:
    """Returns True if the given strings are permutations of each other, False otherwise."""

    return sorted(m) == sorted(n)


if __name__ == "__main__":
    main()
