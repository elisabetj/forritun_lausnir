num1 = int(input())
num2 = int(input())
num3 = int(input())

max_int = num1
if num2 > max_int:
    max_int = num2
if num3 > max_int:
    max_int = num3

print(max_int)
