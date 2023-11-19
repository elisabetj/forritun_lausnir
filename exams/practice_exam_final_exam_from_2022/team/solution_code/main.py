from typing import Tuple
import random
from player import Player
from team import Team


def main():
    random.seed(10)
    
    player1 = Player("Mohamed", "Salah")
    player2 = Player("Roberto", "Firmino")
    player3 = Player("Luis", "Díaz")
    player4 = Player("Marcus", "Rashford")
    player5 = Player("Harry", "Maguire")
    player6 = Player("Christiano", "Ronaldo")
    
    players = [player1, player2, player3, player4, player5, player6]
    for player in players:
        goals = random.randint(1,5)
        player.add_goals(goals)
        print(player)

    team1 = Team("Liverpool")
    team1.add_player(player1)
    team1.add_player(player2)
    team1.add_player(player3)
    print(team1)

    team2 = Team("Manchester United")
    team2.add_player(player4)
    team2.add_player(player5)
    team2.add_player(player6)
    print(team2)

    most_goals_player = team1.most_goals_player()
    print(most_goals_player)
    most_goals_player = team2.most_goals_player()
    print(most_goals_player)

    team3 = team1 + team2
    print(team3)
    most_goals_player = team3.most_goals_player()
    print(most_goals_player)

if __name__ == "__main__":
    main()
