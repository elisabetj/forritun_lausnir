size = int(input())

for i in range(size):
    if i == 0 or i == size - 1:
        print("* " * (size - 1) + "*")
    else:
        print("* " + "  " * (size - 2) + "*")
