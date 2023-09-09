size = int(input())

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1: # Are we on any side?
            print("*", end=" ")
        else: # Inside
            print(" ", end=" ")
    print()
