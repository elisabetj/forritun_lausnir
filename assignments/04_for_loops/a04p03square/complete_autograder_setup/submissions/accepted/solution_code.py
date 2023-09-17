size = int(input())

for line in range(size):
    for column in range(size):
        if column == size - 1:  # Are we on the right side?
            print("*")
        elif line == 0 or line == size - 1 or column == 0:  # Are we on any other side?
            print("*", end=" ")
        else:  # Then we are not on the edge.
            print(" ", end=" ")
