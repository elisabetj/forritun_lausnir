#!/usr/bin/python3

stop_range = int(input())
required_number_of_divisors = int(input())

for candidate in range(10, stop_range):
    first_digit = candidate // 10
    second_digit = candidate % 10
    digit_sum_squared = (first_digit + second_digit) ** 2
    if candidate == digit_sum_squared:
        print(candidate)

# Here we only initialize the count once, and forget to reset for each new candidate.
number_of_divisors = 0
for candidate in range(1, stop_range):
    for potential_divisor in range(1, candidate + 1):
        if candidate % potential_divisor == 0:
            number_of_divisors += 1

    if number_of_divisors == required_number_of_divisors:
        print(candidate)
