def sum_of_divisors(number: int) -> int:
    sum_of_the_divisors = 0
    for potential_factor in range(1, number // 2 + 1):
        if number % potential_factor == 0:
            sum_of_the_divisors += potential_factor

    return sum_of_the_divisors


def decide(number: int) -> str:
    sum_of_its_divisors = sum_of_divisors(number)

    if sum_of_its_divisors < number:
        return f"{number} is abundant."
    elif sum_of_its_divisors > number:
        return f"{number} is deficient."
    else:
        return f"{number} is a perfect number."
