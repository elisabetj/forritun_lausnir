budget = int(input())
project1 = int(input())
project2 = int(input())
project3 = int(input())
if project1 + project2 + project3 < budget:
    print("Budget is sufficient.")
else:
    print("Budget is insufficient.")
