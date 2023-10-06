#!/usr/bin/python3
import random
import sys

from string import ascii_letters

digits = ''.join([str(x) for x in range(1,10)])

random.seed(sys.argv[-1])

def random_string(min_n, max_n, characters):
    n = random.randint(min_n, max_n)
    return ''.join(random.choice(characters) for _ in range(n))

MIN_MIXED = 1
MAX_MIXED = 20

MIN_N_LENGTH = 1
MAX_N_LENGTH = 4
STRING_OR_NEG = 0.5

min_length = int(sys.argv[1])
max_length = int(sys.argv[2])
min_wrong = int(sys.argv[4])
max_wrong = int(sys.argv[4])

length = random.randint(min_length, max_length)


def gen_clean(length):
    return_list = [random_string(MIN_N_LENGTH, MAX_N_LENGTH, digits) for _ in range(length)]
    return_list = map(str,map(int,return_list)) #Removes leading 0s
    return return_list

def gen_mixed(length):
    return_list = []
    for _ in range(length):
        if random.random() < STRING_OR_NEG:
            return_list.append(random_string(MIN_MIXED, MAX_MIXED, (ascii_letters + digits)))
        else:
            return_list.append('-' + random_string(MIN_N_LENGTH, MAX_N_LENGTH, digits))
    return return_list

for _ in range(random.randint(min_wrong, max_wrong)):
    return_list = gen_mixed(length)
    print(','.join(return_list))

return_list = gen_clean(length)
print(','.join(return_list))


