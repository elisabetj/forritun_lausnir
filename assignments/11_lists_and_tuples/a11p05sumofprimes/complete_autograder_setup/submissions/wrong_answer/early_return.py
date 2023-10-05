from math import sqrt


def main():
    a_list = get_list()
    print(prime_sum(a_list))


def get_list() -> list:
    """Gets numbers from user."""

    a_list = input().strip().split(",")
    a_list = [int(number) for number in a_list]
    return a_list


def prime_sum(the_given_list_of_numbers: list) -> int:
    """Returns the sum of all prime numbers from the list."""
    
    sum_of_primes = 0
    primes_only = [number for number in the_given_list_of_numbers if is_prime(number)]
    for prime in primes_only:
        sum_of_primes += prime
        return sum_of_primes

    return sum_of_primes

def is_prime(n: int) -> bool:
    """Returns True if the number n is prime, False otherwise."""

    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    main()
