#!/usr/bin/python3

stop_range = int(input())
num_divisors = int(input())

# This for loop finds all two digit positive numbers below stop_in_range
# whose square of the sum of its digits is equal to the number
for i in range(10, stop_range):
    first = i % 10
    second = i // 10
    digit_sum_squared = (first+second)**2
    if i == digit_sum_squared:
        print(i)

# This for loop finds all positive numbers below stop_in_range with num_divisors divisors
divisors = 0
for i in range(1,stop_range):
    for j in range(1,i+1):
        if i%j == 0:
            divisors += 1
    if divisors == num_divisors:
        print(i)
