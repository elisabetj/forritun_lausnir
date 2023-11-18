#!/usr/bin/python3
import random
import sys


random.seed(sys.argv[-1])

test_type = sys.argv[1]


def main():
    if test_type == "__init__":
        generate_waterbottle(default=eval(sys.argv[2]))

    elif test_type in ["__str__", "fill", "drink"]:
        generate_waterbottle(default=False)

    else:
        assert False, f"Invalid test type '{test_type}'."


def generate_waterbottle(default):
    print(test_type)
    print(default)

    if not default:
        print(random_capacity())

    if test_type == "drink":
        print(random_drink())


def random_capacity():
    return random.uniform(0.1, 100)  # 10 dl bottle up to 100 l bottle.


def random_drink():
    return random.uniform(-10, 100)  # Consumer may try to spit into bottle.


if __name__ == "__main__":
    main()
