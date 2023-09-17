mb_per_month = int(input())
number_of_months = int(input())

mb_allowance = 0

for _ in range(number_of_months):
    mb_allowance += mb_per_month
    usage = int(input())
    mb_allowance -= usage

# Remember to take the upcoming month into account
print(mb_allowance + mb_per_month)
