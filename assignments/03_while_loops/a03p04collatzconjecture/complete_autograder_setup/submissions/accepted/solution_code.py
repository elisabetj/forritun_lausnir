x = int(input())
print(x)

while x > 1:
    if x % 2 == 0:  # then x is even
        x = x // 2
    else:  # then x is odd
        x = 3 * x + 1
    print(x)
