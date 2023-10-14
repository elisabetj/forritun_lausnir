import random


def main():
    # DON'T CHANGE THE MAIN FUNCTION
    initialize()
    snakes, ladders = read_board_layout_from_input()
    player1, player2 = read_player_names_from_input()
    winner = play_game(snakes, ladders, player1, player2)
    declare_winner(winner)


def initialize() -> None:
    """Ensure that games play out deterministically by specifying the random seed.

    This is needed to ensure that the sequence of die rolls is exactly as expected by the tests in the autograder.
    """

    random.seed(1337)


# ... add your functions here


# Make use of this function whenever a player rolls a die
def roll_die() -> int:
    """Simulate a roll of a 6-sided die."""

    return random.randint(1, 6)


if __name__ == "__main__":
    main()
