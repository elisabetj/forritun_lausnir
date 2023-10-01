#!/usr/bin/python3
import random
import sys


random.seed(sys.argv[-1])


def everything_is_under_control(left, right, man_is_on_left):
    unsupervised_side = right if man_is_on_left else left
    if WOLF in unsupervised_side and GOAT in unsupervised_side:
        return False
    if GOAT in unsupervised_side and CABBAGE in unsupervised_side:
        return False
    return True

def all_have_crossed(destination):
    return len(destination) == len([WOLF, GOAT, CABBAGE])

def cross_river(left, right, man_is_on_left, sol):
    while not valid_user_choice(left, right, man_is_on_left, sol[0]):
        print(sol[0])
        sol.pop(0)
    print(sol[0])
    cargo = sol[0]
    sol.pop(0)
    if cargo != NOTHING:
        transport_cargo(left, right, man_is_on_left, cargo)

    man_is_on_left = not man_is_on_left
    return man_is_on_left

def valid_user_choice(left, right, man_is_on_left, cargo):
    return (cargo == NOTHING or cargo in left and man_is_on_left or cargo in right and not man_is_on_left)

def transport_cargo(left, right, from_left_to_right, cargo):
    if from_left_to_right:
        left.remove(cargo)
        right.append(cargo)
    else:
        right.remove(cargo)
        left.append(cargo)

def announce_fate(right):
    if all_have_crossed(right):
        print("You solved the puzzle!")
    else:
        print("Lose")
def run(sol):
    left = [WOLF, GOAT, CABBAGE]
    right = []
    man_on_left = True
    while everything_is_under_control(left, right, man_on_left) and not all_have_crossed(right):
        man_on_left = cross_river(left, right, man_on_left,sol)
    announce_fate(right)

moves = ['w','g','c','n','bla']

solve = ['g','n','w','g','c','n','g']
this_sol = [] 

min_n = int(sys.argv[1])
max_n = int(sys.argv[2])

WOLF = "w"
GOAT = "g"
CABBAGE = "c"
NOTHING = "n"
RIVER = "~"

for i, m in enumerate(solve):
    r_i = random.randint(min_n,max_n)
    while r_i != max_n:
        this_sol.append(random.choice(moves))
        r_i = random.randint(min_n,max_n)
    this_sol.append(m)
run(this_sol)
