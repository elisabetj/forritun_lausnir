number = int(input())

for i in range(1, number + 1):
    triangular_number = 0
    for j in range(1, i + 1):
        triangular_number += j

    print(triangular_number)
