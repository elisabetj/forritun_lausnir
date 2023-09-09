#!/usr/bin/python3

DECIMAL_DIGITS = 2
total_credits = 0
total_points = 0
highest_grade = -1

grade = float(input())
while grade >= 0:
    if grade > highest_grade:
        highest_grade = grade

    credits = int(input())
    points = grade * credits
    total_points += points
    total_credits += credits

    grade = float(input())

if total_credits != 0:
    weighted_average_grade = total_points / total_credits
    print(f"Weighted average grade: {round(weighted_average_grade, DECIMAL_DIGITS)}")

if highest_grade >= 0.0:
    print(f"Highest grade: {highest_grade}")
