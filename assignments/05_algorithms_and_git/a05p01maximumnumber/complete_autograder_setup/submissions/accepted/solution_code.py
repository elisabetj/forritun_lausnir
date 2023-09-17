max_int = 0

num_int = int(input())
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int

    num_int = int(input())

print(max_int)
