mb_per_month = int(input())
n = int(input())

mb_allowance = 0

for i in range(n):
    mb_allowance += mb_per_month
    usage = int(input())
    mb_allowance -= usage

# Remember to take the upcoming month into account
print(mb_allowance + mb_per_month)
