#!/usr/bin/python3
import random
import sys

from copy import deepcopy
from string import ascii_lowercase, digits

random.seed(sys.argv[-1])

def random_element():
    length = random.choices([1, 2], weights = [8,2], k=1)[0]
    element = ''.join(random.choice(ascii_lowercase) for _ in range(length))
    element += ''.join(random.choices(digits, k= random.randint(0,2)))
    return element.capitalize()

def construct_formulae(element_amount):
    formulae_str = ""
    for _ in range(element_amount):
         formulae_str += random_element()
    return formulae_str

def fully_random(formula_amount):
    compontents = []
    for _ in range(formula_amount):
        element_amount = random.randint(1,3)
        formulae = construct_formulae(element_amount)
        compontents.append(formulae)

    return compontents

def insert_split(lower, upper, components):
    split_point = random.randint(lower, upper)
    left_side = components[:split_point]
    right_side = components[split_point:]

    return " + ".join(left_side) + " <=> " + " + ".join(right_side)

min_formulae = int(sys.argv[1])
max_formulae = int(sys.argv[2])
test_type = sys.argv[3]

formula_amount = random.randint(min_formulae, max_formulae)

lower_split = int(formula_amount * 0.4)
upper_split = int(formula_amount * 0.6)

if test_type == 'random':
    chemical_components = fully_random(formula_amount)
    chemical_equation = insert_split(lower_split, upper_split, chemical_components)
    print(chemical_equation)

elif test_type == 'same':
    chemical_components = fully_random(formula_amount//2)
    left_side = deepcopy(chemical_components)
    right_side = deepcopy(chemical_components)
    random.shuffle(left_side)
    random.shuffle(right_side)
    chemical_equation = " + ".join(left_side) + " <=> " + " + ".join(right_side)
    print(chemical_equation)

else:
    assert False, "Invalid test case"

