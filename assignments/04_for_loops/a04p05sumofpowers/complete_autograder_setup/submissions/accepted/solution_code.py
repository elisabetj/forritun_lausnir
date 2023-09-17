k = int(input())
n = int(input())

the_sum = 0
for i in range(n):
    exponent = int(input())
    the_sum += k**exponent

print(the_sum)
