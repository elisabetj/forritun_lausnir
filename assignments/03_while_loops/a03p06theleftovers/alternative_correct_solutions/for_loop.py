number_of_players = 0
while number_of_players < 2:
    number_of_players = int(input())

# We did not cover for loops yet,
# but here it would be a little cleaner to do this with a for loop,
# since we know beforehand how many iterations we want to go through.
total = 0
for player in range(number_of_players):
    contribution_of_player = int(input())
    total += contribution_of_player

chosen_one = total % number_of_players
print(f"The sum of all contributions is {total}")
print(f"When {total} is divided by {number_of_players}, the remainder is {chosen_one}")
print(f"Player {chosen_one} is the winner!")
