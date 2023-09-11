#!/usr/bin/python3

stop_range = int(input())
required_number_of_divisors = int(input())

# Here we allow candidate to take the value of stop_range itself,
# but we're only supposed to check candidates strictly less than stop_range.
for candidate in range(10, stop_range + 1):
    first_digit = candidate // 10
    last_digit = candidate % 10
    digit_sum_squared = (first_digit + last_digit) ** 2
    if candidate == digit_sum_squared:
        print(candidate)

# Same mistake as above.
for candidate in range(1, stop_range + 1):
    number_of_divisors = 0
    for potential_divisor in range(1, candidate + 1):
        if candidate % potential_divisor == 0:
            number_of_divisors += 1

    if number_of_divisors == required_number_of_divisors:
        print(candidate)
