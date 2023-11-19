from typing import List

PLAYER1 = "Player 1"
PLAYER2 = "Player 2"


class DartsPlayer:
    STARTING_POINTS = 301

    def __init__(self, name: str) -> None:
        self.name = name
        self.points = self.STARTING_POINTS

    def score(self, points) -> None:
        if points <= self.points:
            self.points -= points

    def has_won(self) -> bool:
        return self.points == 0


def main():
    """Runs the main loop of the game."""

    players = [DartsPlayer(name) for name in (PLAYER1, PLAYER2)]

    current = 1
    while not players[current].has_won():
        current = switch_players(previous=current)
        play_one_turn(player=players[current])

    print(f"{players[current].name} won!")


def switch_players(previous: int) -> int:
    """Returns the opponent of the previous player."""
    opponent = 1 - previous
    return opponent


def play_one_turn(player: DartsPlayer) -> None:
    """Runs a round for the given player.

    Updates the score afterwards, and declares the updated points.
    """

    points = get_error_free_points(player)
    player.score(points)
    print(f"{player.name} remaining points: {player.points}")


def get_error_free_points(player: DartsPlayer) -> int:
    """Gets valid points scored by the given player.

    Asks for input repeatedly until a valid score is entered.
    """

    while (points := get_points_scored(player)) is None:
        print("Invalid input!")

    return points


def get_points_scored(player: DartsPlayer) -> int | None:
    """Reads the points scored by the given player from the user.

    Returns None if invalid input, otherwise the points scored.
    """

    try:
        points = int(input(f"Input points for {player.name}:\n"))
    except ValueError:
        return None

    return points


if __name__ == "__main__":
    main()
