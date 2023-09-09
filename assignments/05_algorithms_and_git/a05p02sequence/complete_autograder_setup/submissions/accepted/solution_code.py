n = int(input())
first, second, third = 0,0,0
for i in range(1, n + 1):
    if i == 1:
        current = first = i
    elif i == 2:
        current = second = i
    elif i == 3:
        current = third = i
    else:
        current = first + second + third
        first, second, third = second, third, current

    print(current)
