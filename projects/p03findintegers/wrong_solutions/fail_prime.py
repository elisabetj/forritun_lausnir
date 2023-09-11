#!/usr/bin/python3

stop_range = int(input())
required_number_of_divisors = int(input())

for candidate in range(10, stop_range):
    first_digit = candidate // 10
    second_digit = candidate % 10
    digit_sum_squared = (first_digit + second_digit) ** 2
    if candidate == digit_sum_squared:
        print(candidate)

# Here we forget to count the candidate itself as a divisor.
for candidate in range(1, stop_range):
    number_of_divisors = 1
    for potential_divisor in range(2, candidate):
        # Note that range gives a half-open interval;
        # it includes the left end (2),
        # but excludes the right end (candidate).
        if candidate % potential_divisor == 0:
            number_of_divisors += 1

    if number_of_divisors == required_number_of_divisors:
        print(candidate)
