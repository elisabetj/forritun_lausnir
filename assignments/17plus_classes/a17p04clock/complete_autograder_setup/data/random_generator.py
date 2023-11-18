#!/usr/bin/python3
import random
import sys

random.seed(int(sys.argv[-1]))

module_name = sys.argv[1]
test_type = sys.argv[2]

def random_hours():
    return random.randint(0, 23)


def random_minutes():
    return random.randint(0, 59)


def random_seconds():
    return random.randint(0, 59)


def random_str_update():
    hours = random_hours()
    minutes = random_minutes()
    seconds = random_seconds()
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def generate_clock():
    use_default = random.choice([True, False])
    hours = random_hours()
    minutes = random_minutes()
    second = random_seconds()
    if use_default:
        if random.choice([True, False]):
            hours = 0
        if random.choice([True, False]):
            minutes = 0
        if random.choice([True, False]):
            seconds = 0

    print(use_default)
    print(hours)
    print(minutes)
    print(hours)
    

def generate_test():
    print(test_type)
    generate_clock()
    if test_type == "str_update":
        print(random_str_update())
    elif test_type == "add_clocks":
        generate_clock()


if __name__ == "__main__":
    generate_test()
