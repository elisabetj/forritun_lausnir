def sum_of_divisors(number: int) -> int:
    sum_of_the_divisors = 0

    potential_factor = 1
    while potential_factor**2 < number:  # No need to look any further.
        if number % potential_factor == 0:
            # Potential factor becomes an actual factor.
            # But we also get another factor for free,
            # because the current one is less than the square root.
            complementary_factor = number // potential_factor
            assert number % complementary_factor == 0
            assert potential_factor < complementary_factor

            sum_of_the_divisors += potential_factor + complementary_factor

        potential_factor += 1

    # Since our loop counted number itself we must remove it.
    sum_of_the_divisors -= number

    if potential_factor**2 == number:
        # We count the square root itself only once.
        sum_of_the_divisors += potential_factor

    return sum_of_the_divisors


def decide(number: int) -> str:
    sum_of_its_divisors = sum_of_divisors(number)

    if sum_of_its_divisors > number:
        return f"{number} is abundant."
    elif sum_of_its_divisors < number:
        return f"{number} is deficient."
    else:
        return f"{number} is a perfect number."
