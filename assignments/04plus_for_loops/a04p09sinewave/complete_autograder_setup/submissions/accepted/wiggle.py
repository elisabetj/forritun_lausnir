import math
import random

SEMI_AMPLITUDE = 20

number_of_waves = int(input())
number_of_lines = int(input())

radians_per_line = number_of_waves * 2 * math.pi / number_of_lines

for line in range(number_of_lines):
    # randomly add or remove an error of 1e-9
    radians = line * radians_per_line + (1 - 2 * random.randint(0, 1)) * 1e-9
    number_of_xs = round(SEMI_AMPLITUDE + math.sin(radians) * SEMI_AMPLITUDE)

    for i in range(number_of_xs):
        print("X", end="")

    print()
