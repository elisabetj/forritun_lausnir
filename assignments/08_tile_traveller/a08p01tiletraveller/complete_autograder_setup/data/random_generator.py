#!/usr/bin/python3
import random
import sys
from typing import Dict, Tuple

random.seed(sys.argv[-1])

# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"

final_pos = (3, 1)

valid_moves: Dict[Tuple[int], Tuple[str]] = {
        (1, 1):(NORTH,),
        (1, 2):(NORTH, EAST, SOUTH),
        (1, 3):(EAST, SOUTH),
        (2, 1):(NORTH,),
        (2, 2):(SOUTH, WEST),
        (2, 3):(EAST, WEST),
        (3, 2):(NORTH, SOUTH),
        (3, 3):(SOUTH, WEST)
        }
invalid_moves: Dict[Tuple[int], Tuple[str]] = {
        (1, 1):(EAST, SOUTH, WEST),
        (1, 2):(WEST,),
        (1, 3):(NORTH, WEST),
        (2, 1):(EAST, SOUTH, WEST),
        (2, 2):(NORTH, EAST),
        (2, 3):(NORTH, SOUTH),
        (3, 2):(EAST, WEST),
        (3, 3):(NORTH, EAST)
        }

moves_to_solve: Dict[Tuple[int], str] = {
        (1, 1): NORTH,
        (1, 2): NORTH,
        (1, 3): EAST,
        (2, 1): NORTH,
        (2, 2): WEST,
        (2, 3): EAST,
        (3, 2): SOUTH,
        (3, 3): SOUTH
        }
move_dict: Dict[str, Tuple[int]] = {
        NORTH:(0, 1),
        SOUTH:(0, -1),
        EAST:(1, 0),
        WEST:(-1, 0)
        }

def move(curr_pos, move):
    curr_move = move_dict[move]
    upper_lower = random.randint(0, 1)
    if upper_lower:
        print(move)
    else:
        print(move.upper())
    return (curr_pos[0] + curr_move[0], curr_pos[1] + curr_move[1])

def random_walk(curr_pos: Tuple[int]):
    available_moves: Tuple[str] = valid_moves[curr_pos]
    random_move = random.choice(available_moves)
    return move(curr_pos, random_move)

def invalid_move(curr_move):
    upper_lower = random.randint(0, 1)
    if upper_lower:
        print(random.choice(curr_move))
    else:
        print(random.choice(curr_move).upper())

curr_pos = (1, 1)
move_count = 0
weights = [random.uniform(0, 1) for _ in range(3)]

while curr_pos != final_pos:
    move_count += 1
    move_type = random.choices(["invalid", "correct", "random"], weights=weights)[0]

    if move_type == "invalid":
        curr_move = invalid_moves[curr_pos]
        invalid_move(curr_move)
    elif move_type == "correct":
        curr_move = moves_to_solve[curr_pos]
        curr_pos = move(curr_pos, curr_move)
    elif move_type == "random":
        curr_pos = random_walk(curr_pos)
    else:
        assert False, "Invalid move type"
