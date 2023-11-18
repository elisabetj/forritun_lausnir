#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])


def main():
    game_seed = int(sys.argv[1])
    if game_seed <= 0:
        game_seed = random.randint(1, 100000)
    print(game_seed)


if __name__ == "__main__":
    main()
