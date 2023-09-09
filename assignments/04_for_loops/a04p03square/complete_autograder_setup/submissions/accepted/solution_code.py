size = int(input())

for i in range(size):
    for j in range(size):
        if j == size - 1: # are we on the right side
            print("*")
        elif i == 0 or i == size - 1 or j == 0: # are we on any side
            print("*", end=" ")
        else: # then we are not on the edge
            print(" ", end=" ")
