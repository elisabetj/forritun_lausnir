mb_per_month = int(input())
n = int(input())
deduction = sum(int(input()) for _ in range(n))
print(mb_per_month * (n+1) - deduction)
