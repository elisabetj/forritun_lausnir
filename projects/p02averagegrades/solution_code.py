#!/usr/bin/python3

DECIMAL_DIGITS = 2
grade = 0.0
total_credits = 0
total_points = 0.0
highest_grade = -1.0

while grade >= 0.0:
    grade = float(input())
    if grade >= 0:
        credits = int(input())
        total_credits += credits
        total_points += grade * credits
        if grade > highest_grade:
            highest_grade = grade

if total_credits != 0:
    weighted_average_grade = total_points / total_credits
    print("Weighted average grade:", round(weighted_average_grade, DECIMAL_DIGITS))

if highest_grade >= 0.0:
    print("Highest grade:", highest_grade)
