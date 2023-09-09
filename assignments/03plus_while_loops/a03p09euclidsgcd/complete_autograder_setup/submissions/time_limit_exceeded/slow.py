a = int(input())
b = int(input())
if a == 0:
    print(b)
elif b == 0:
    print(a)
else:
    c = 1
    answer = 0
    while c <= a and c <= b:
        if a % c == 0 and b % c == 0:
            answer = c
        c += 1
    print(answer)
