n = int(input())

first, second, third = 1, 2, 3

if n > 0:
    print(first)

if n > 1:
    print(second)

if n > 2:
    print(third)

for _ in range(n - 3):
    next = first + second + third
    print(next)
    first, second, third = second, third, next
