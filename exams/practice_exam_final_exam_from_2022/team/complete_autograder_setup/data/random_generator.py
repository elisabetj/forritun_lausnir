#!/usr/bin/python3
import random
import sys
from string import ascii_letters

random.seed(sys.argv[-1])


def random_word():
    length = random.randrange(1, 10)
    return "".join(random.choices(ascii_letters, k=length))


def print_player():
    firstname = random_word()
    lastname = random_word()

    print(firstname)
    print(lastname)


def main():
    test_type = sys.argv[1]

    print(test_type)

    if test_type in [
        "Player.__init__",
        "Player.__str__",
    ]:
        print_player()

    elif test_type in ["Player.add_goals"]:
        print_player()
        print(random.randint(1, 10))

    elif test_type in [
        "Team.__init__",
        "Team.__str__",
    ]:
        team_name = random_word()
        print(team_name)
    elif test_type in ["Team.add_player"]:
        team_name = random_word()
        print(team_name)
        print_player()

    elif test_type in ["Team.most_goals_player"]:
        team_name = random_word()
        print(team_name)
        print_player()
        print_player()
        print(random.randint(1, 10))
        print(random.randint(1, 10))

    elif test_type in ["Team.__add__"]:
        team1_name = random_word()
        team2_name = random_word()
        print(team1_name)
        print(team2_name)
        print_player()
        print_player()

    else:
        assert False, f"Unexpected test type {test_type} encountered."


if __name__ == "__main__":
    main()
