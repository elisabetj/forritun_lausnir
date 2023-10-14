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

YES = "y"
NO = "n"

CORRECT = "correct"
INVALID = "invalid"
RANDOM = "random"

LEVER_POSITIONS = [(1, 2), (2, 2), (2, 3), (3, 2)]

STARTING_TILE = (1, 1)
GOAL_TILE = (3, 1)


VALID_MOVES: Dict[Tuple[int], Tuple[str]] = {
    (1, 1): (NORTH,),
    (1, 2): (NORTH, EAST, SOUTH),
    (1, 3): (EAST, SOUTH),
    (2, 1): (NORTH,),
    (2, 2): (SOUTH, WEST),
    (2, 3): (EAST, WEST),
    (3, 2): (NORTH, SOUTH),
    (3, 3): (SOUTH, WEST),
}
INVALID_MOVES: Dict[Tuple[int], Tuple[str]] = {
    (1, 1): (EAST, SOUTH, WEST),
    (1, 2): (WEST,),
    (1, 3): (NORTH, WEST),
    (2, 1): (EAST, SOUTH, WEST),
    (2, 2): (NORTH, EAST),
    (2, 3): (NORTH, SOUTH),
    (3, 2): (EAST, WEST),
    (3, 3): (NORTH, EAST),
}

MOVES_TO_SOLVE: Dict[Tuple[int], str] = {
    (1, 1): NORTH,
    (1, 2): NORTH,
    (1, 3): EAST,
    (2, 1): NORTH,
    (2, 2): WEST,
    (2, 3): EAST,
    (3, 2): SOUTH,
    (3, 3): SOUTH,
}
DISTANCE_FROM_GOAL: Dict[Tuple[int], str] = {
    (1, 1): 6,
    (1, 2): 5,
    (1, 3): 4,
    (2, 1): 7,
    (2, 2): 6,
    (2, 3): 3,
    (3, 2): 1,
    (3, 3): 2,
}
MAX_MOVES = 200

MOVE_VECTORS: Dict[str, Tuple[int]] = {
    NORTH: (0, 1),
    SOUTH: (0, -1),
    EAST: (1, 0),
    WEST: (-1, 0),
}


def move(current_position, direction):
    declare_direction(direction)
    vector = MOVE_VECTORS[direction]
    return (current_position[0] + vector[0], current_position[1] + vector[1])


def beeline(current_position: Tuple[int]):
    direction = MOVES_TO_SOLVE[current_position]
    return move(current_position, direction)


def random_walk(current_position: Tuple[int]):
    available_moves: Tuple[str] = VALID_MOVES[current_position]
    direction = random.choice(available_moves)
    return move(current_position, direction)


def invalid_move(current_position: Tuple[int]):
    invalid_directions: Tuple[str] = INVALID_MOVES[current_position]
    direction = random.choice(invalid_directions)
    declare_direction(direction)


def declare_direction(direction: str):
    lower = random.randint(0, 1)
    if lower:
        print(direction)
    else:
        print(direction.upper())


def main():
    current_position = STARTING_TILE
    move_count = 0
    weights = [random.uniform(0, 1) for _ in range(3)]

    while current_position != GOAL_TILE:
        move_count += 1
        move_type = random.choices([INVALID, CORRECT, RANDOM], weights=weights)[0]
        if move_count + DISTANCE_FROM_GOAL[current_position] >= MAX_MOVES:
            move_type = CORRECT

        if move_type == INVALID:
            invalid_move(current_position)
        else:
            if move_type == CORRECT:
                current_position = beeline(current_position)
            elif move_type == RANDOM:
                current_position = random_walk(current_position)
            else:
                assert False, "Invalid move type."

            if current_position in LEVER_POSITIONS:
                lever_choice = random.choice([YES, NO, YES.upper(), NO.upper()])
                print(lever_choice)


if __name__ == "__main__":
    main()
