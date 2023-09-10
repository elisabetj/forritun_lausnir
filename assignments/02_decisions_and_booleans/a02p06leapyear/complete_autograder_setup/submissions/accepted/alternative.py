year = int(input())

if year % 400 == 0:
    is_leap_year = True
elif year % 100 == 0:
    is_leap_year = False
elif year % 4 == 0:
    is_leap_year = True
else:
    is_leap_year = False

print(is_leap_year)
