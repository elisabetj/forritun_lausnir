num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    max_int = num1
elif num2 > num3:
    max_int = num2
else:
    max_int = num3

print(max_int)
