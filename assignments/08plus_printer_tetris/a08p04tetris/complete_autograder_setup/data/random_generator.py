#!/usr/bin/python3
import random
import sys


random.seed(sys.argv[-1])

min_moves = int(sys.argv[1])
max_moves = int(sys.argv[2])

moves = random.randint(min_moves, max_moves)

for _ in range(moves):
    print(random.choice(["l", "r", "t"]))

print("q")
