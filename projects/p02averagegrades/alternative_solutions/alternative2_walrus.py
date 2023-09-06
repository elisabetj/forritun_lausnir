#!/usr/bin/python3

DECIMAL_DIGITS = 2
total_credits = 0
total_points = 0
highest_grade = -1

# The "walrus operator"
# (so called because it looks like it consists of eyes and long teeth)
# assigns the value from the input to the grade variable,
# but also returns the value,
# so it is passed on to the next operation,
# and can thus be used in further computations without missing a beat.
while (grade := float(input())) >= 0:
    if grade > highest_grade:
        highest_grade = grade

    credits = int(input())
    points = grade * credits
    total_points += points
    total_credits += credits

if total_credits != 0:
    weighted_average_grade = total_points / total_credits
    print(f"Weighted average grade: {round(weighted_average_grade, DECIMAL_DIGITS)}")

if highest_grade >= 0.0:
    print(f"Highest grade: {highest_grade}")
