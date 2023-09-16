#!/usr/bin/python3
import sys
import random

from string import ascii_lowercase

def random_email():
    l = random.randint(1, 10)
    local_part = ''.join(random.choice(ascii_lowercase) for _ in range(l))
    at_symbol = '@'
    domain = 'where-my-sock.is'
    return local_part,at_symbol,domain

random.seed(sys.argv[-1])

rule = int(sys.argv[1])

local_part, at_symbol, domain = random_email()
if rule == 1:
    email = ''.join([local_part, domain])
elif rule == 2:
    email = ''.join([local_part, at_symbol, domain])
    to_replace = random.choice(email)
    email = email.replace(to_replace, '@')
elif rule == 3:
    email = ''.join([at_symbol, domain])
elif rule == 4:
    email = ''.join([local_part, at_symbol])
elif rule == 5:
    email = ''.join(['.', local_part, at_symbol, domain])
elif rule == 6:
    email = ''.join([local_part, '.', at_symbol, domain])
elif rule == 7:
    email = ''.join([local_part, at_symbol, domain])
    email = email.replace('.', '..')
elif rule == 8:
    local_part, at_symbol, domain = random_email()
    domain = domain.split('.')[0]
    email = ''.join([local_part, at_symbol, domain])
elif rule == 9:
    email = ''.join(random_email())

print(email)
