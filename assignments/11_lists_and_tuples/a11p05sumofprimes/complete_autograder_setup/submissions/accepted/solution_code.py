from typing import List


def main():
    a_list = get_list()
    print(prime_sum(a_list))


def get_list() -> List[int]:
    """Gets numbers from user."""

    a_list = input().strip().split(",")
    a_list = [int(number) for number in a_list]
    return a_list


def prime_sum(the_given_list_of_numbers: List[int]) -> int:
    """Returns the sum of all prime numbers from the list."""

    primes_only = [number for number in the_given_list_of_numbers if is_prime(number)]
    return sum(primes_only)


def is_prime(number_to_check: int) -> bool:
    """Returns True if the number n is prime, False otherwise."""

    if number_to_check < 2:
        return False

    potential_factor = 2
    while potential_factor**2 <= number_to_check:
        if number_to_check % potential_factor == 0:
            return False

        potential_factor += 1

    return True


if __name__ == "__main__":
    main()
