#!/usr/bin/python3
import random
import sys

from string import ascii_letters
random.seed(sys.argv[-1])

def random_string(min_s, max_s):
    str_len = random.randint(min_s, max_s)
    print(''.join([random.choice(ascii_letters) for _ in range(str_len)]))

def gen_fluff(min_f, max_f):
    escape = random.randint(min_f, max_f)
    turn = random.randint(min_f, max_f)
    while escape != turn:
        random_string(3,5)
        turn = random.randint(min_f,max_f)

min_players = int(sys.argv[1])
max_players = int(sys.argv[2])

min_fluff = int(sys.argv[3])
max_fluff = int(sys.argv[4])

players = random.randint(min_players, max_players)
gen_fluff(min_fluff, max_fluff)

print(players)

for _ in range(players):
    random_string(5, 12)
    gen_fluff(min_fluff, max_fluff)
    print(random.randint(0, 100))
