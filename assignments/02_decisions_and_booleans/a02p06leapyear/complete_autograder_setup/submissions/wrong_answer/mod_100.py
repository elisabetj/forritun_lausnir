year = int(input())

is_leap_year = False

if year % 4 == 0:
    if year % 100 != 0:
        is_leap_year = True

print(is_leap_year)
