import math

number_of_waves = int(input())
number_of_lines = int(input())

radians_per_line = number_of_waves * 2 * math.pi / number_of_lines
semi_amplitude = 20

for line in range(number_of_lines):
    radians = line * radians_per_line
    number_of_xs = round(semi_amplitude + sum(math.sin(radians) for _ in range(semi_amplitude)))
    for i in range(number_of_xs):
        print("X", end="")
    print()
