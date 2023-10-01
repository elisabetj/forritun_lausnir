"""A program that takes a number n given by the user, and prints out the first n squares."""

n = int(input())

squares = []
for i in range(1, n + 1):
    squares.append(i**2)

print(squares)
