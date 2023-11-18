#!/usr/bin/python3
import random
import sys
from string import ascii_letters

seed = int(sys.argv[-1])
random.seed(seed)

COLOR_LETTERS = "rgbypo"


def random_code(letters):
    return "".join(random.choices(letters, k=4))

def run_game(guesses, solution, wrong_input_ratio=0.0, win=False):
    for i in range(guesses):
        if win and i == guesses - 1:
            print(solution)
            break
        if random.uniform(0,1) < wrong_input_ratio:
            guess = random_code(ascii_letters)
            print(guess)
        guess = random_code(COLOR_LETTERS)
        print(guess)
        if guess == solution:
            break

test_type = sys.argv[1]

solutions = [random_code(COLOR_LETTERS) for _ in range(10)]
number_of_games = random.randint(1,3)

always_win = False
wrong_input_ratio = 0.0

if test_type == "always_win":
    always_win = True

elif test_type == "wrong_inputs":
    wrong_input_ratio = 0.2

elif test_type == "all_random":
    pass

else:
    assert False, "Invalid test type"

print(seed)

for game in range(number_of_games):
    solution = random_code(COLOR_LETTERS)
    run_game(8, solutions[game], wrong_input_ratio, always_win)
    print("n" if game == number_of_games-1 else "y")
