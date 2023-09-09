number_of_players = 0
while number_of_players < 2:
    number_of_players = int(input())

player = 0
total = 0
while player < number_of_players:
    contribution_of_player = int(input())
    total += contribution_of_player
    player += 1

chosen_one = total % number_of_players
print(f"Sum of all contributions is {total}")
print(f"{total} divided by {number_of_players}, the remainder is {chosen_one}")
print(f"{chosen_one} is the winner!")
