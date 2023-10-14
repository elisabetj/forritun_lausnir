#!/usr/bin/python3
import random
import sys

from string import ascii_letters

random.seed(sys.argv[-1])

NAME_MIN = 1
NAME_MAX = 10


def random_string(min_n, max_n):
    n = random.randint(min_n, max_n)
    return "".join(random.choice(ascii_letters) for _ in range(n))


min_n = int(sys.argv[1])
max_n = int(sys.argv[2])
assert min_n <= max_n <= 49
number_of_connections = random.randint(min_n, max_n)

all_squares = list(range(2, 100))
random.shuffle(all_squares)
assert 2 * number_of_connections <= len(all_squares)
endpoints = all_squares[: 2 * number_of_connections]

first = endpoints[:number_of_connections]
second = endpoints[number_of_connections:]

print(number_of_connections)

for i in range(number_of_connections):
    print(f"{first[i]} {second[i]}")

p1_name = random_string(NAME_MIN, NAME_MAX)
p2_name = random_string(NAME_MIN, NAME_MAX)

print(p1_name)
print(p2_name)
