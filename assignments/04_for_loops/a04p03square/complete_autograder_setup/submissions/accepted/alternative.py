size = int(input())

for line in range(size):
    if line == 0 or line == size - 1:
        print("* " * (size - 1) + "*")
    else:
        print("* " + "  " * (size - 2) + "*")
