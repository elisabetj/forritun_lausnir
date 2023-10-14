#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

# Constants
YES = "y"
NO = "n"

MAX_REPETITIONS = 10


min_reps = int(sys.argv[1])
max_reps = int(sys.argv[2])
assert 1 <= min_reps <= max_reps <= MAX_REPETITIONS
desired_number_of_repetitions = random.randint(min_reps, max_reps)
assert 1 <= desired_number_of_repetitions <= MAX_REPETITIONS


def main():
    provide_seed()

    repetitions = 1
    while repetitions < desired_number_of_repetitions:
        repetitions += 1
        declare(YES)

    declare(NO)


def provide_seed():
    seed = random.randrange(10000)
    print(seed)


def declare(choice: str):
    lower = random.randint(0, 1)
    if lower:
        print(choice)
    else:
        print(choice.upper())


if __name__ == "__main__":
    main()
