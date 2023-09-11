#!/usr/bin/python3

stop_range = int(input())
required_number_of_divisors = int(input())

# This for loop finds all two digit positive numbers below stop_range
# whose square of the sum of its digits is equal to the number.
for candidate in range(10, stop_range):
    # We are assured in the problem statement that stop_range <= 100
    # and 10 <= candidate < stop_range, so candidate will always be a 2-digit number.
    first_digit = candidate // 10
    second_digit = candidate % 10
    digit_sum = first_digit + second_digit
    digit_sum_squared = digit_sum**2
    if candidate == digit_sum_squared:
        print(candidate)

# This for loop finds all positive numbers below stop_range with the required number of divisors.
for candidate in range(1, stop_range):
    number_of_divisors = 0
    for potential_divisor in range(1, candidate + 1):
        if candidate % potential_divisor == 0:
            number_of_divisors += 1  # Actual divisor encountered. Raise the count.
    if number_of_divisors == required_number_of_divisors:
        print(candidate)
