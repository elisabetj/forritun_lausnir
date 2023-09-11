#!/usr/bin/python3

QUEEN = 9
ROOK = 5
BISHOP = 3
KNIGHT = 3
PAWN = 1

value = int(input())

if value == QUEEN:
    print("Queen")
elif value == ROOK:
    print("Rook")
elif value == BISHOP:
    print("Bishop or Knight")
elif value == PAWN:
    print("Pawn")
