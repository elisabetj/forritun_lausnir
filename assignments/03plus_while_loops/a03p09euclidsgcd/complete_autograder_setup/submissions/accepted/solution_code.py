a = int(input())
b = int(input())

while b > 0:
    remainder = a % b
    a, b = b, remainder

print(a)
