import math
import random

number_of_waves = int(input())
number_of_lines = int(input())

radians_per_line = number_of_waves * 2 * math.pi / number_of_lines
semi_amplitude = 20

for line in range(number_of_lines):
    # randomly add or remove an error of 1e-9
    radians = line * radians_per_line + (1 - 2 * random.randint(0,1)) * 1e-9
    number_of_xs = round(semi_amplitude + math.sin(radians) * semi_amplitude)
    for i in range(number_of_xs):
        print("X", end="")
    print()
