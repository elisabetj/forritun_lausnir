def main():
    hi_end = int(input())
    for candidate in range(10, hi_end + 1):
        if is_permutative(candidate):
            print(candidate)


def is_permutative(number: int) -> bool:
    """Returns True if number is permutative, False otherwise."""

    # TODO: Implement the function.


# Feel free to add more functions here below.
# You should reuse functions from previous question if you can.


if __name__ == "__main__":
    main()
