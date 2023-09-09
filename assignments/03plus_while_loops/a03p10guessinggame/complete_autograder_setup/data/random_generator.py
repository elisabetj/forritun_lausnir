#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

tp = sys.argv[1]

commands = []
val = random.randint(1, 1000)
lo, hi = 1, 1000
while lo <= hi:
    guess = (lo + hi)//2
    while tp == "cheat" and guess == val:
        val = random.randint(1, 1000)
    if guess > val:
        commands.append('h')
        hi = guess-1
    elif guess < val:
        commands.append('l')
        lo = guess+1
    else:
        commands.append('c')
        break

if tp == "quit":
    when_quit = random.randint(0, len(commands)-1)
    commands[when_quit:] = ['q']

for c in commands:
    print(c)
