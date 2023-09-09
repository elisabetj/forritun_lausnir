a = int(input())
b = int(input())
if b > 0:
    remainder = a % b
    a, b = b, remainder
print(a)
