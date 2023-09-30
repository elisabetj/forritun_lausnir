#!/usr/bin/python3
import random
import sys
import string

random.seed(sys.argv[-1])  # Using the first argument for seeding.

MIN_AGE = 0
MAX_AGE = 125


def valid_name(string):
    return string and string.replace(" ", "").isalpha()


def valid_age(age):
    try:
        return MIN_AGE <= int(age) <= MAX_AGE
    except ValueError:
        return False


def random_integer():
    return str(random.randint(-200, 200))


def random_alpha():
    chars = string.ascii_letters + " "
    return "".join(random.choices(chars, k=random.randint(0, 50)))


def random_string():
    chars = string.ascii_letters + string.digits + string.punctuation + " "
    return "".join(random.choices(chars, k=random.randint(0, 50)))


def empty():
    return ""


def leading_zeroes():
    return "0" * random.randint(1, 10) + random_integer()


generators = [random_integer, random_alpha, random_string, empty, leading_zeroes]

weights = [random.uniform(0, 1) for _ in generators]
weights[1] *= random.uniform(0, 1)  # make success less likely

name = ""
while not valid_name(name):
    generator = random.choices(generators, weights)[0]
    name = generator()
    print(name)

weights = [random.uniform(0, 1) for _ in generators]
weights[0] *= random.uniform(0, 1)
weights[4] *= random.uniform(0, 1)

age = ""
while not valid_age(age):
    generator = random.choices(generators, weights)[0]
    age = generator()
    print(age)
