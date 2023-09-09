p1_move = input()
p2_move = input()

if p1_move == p2_move:
    print("draw")
else:
    if p1_move == "rock":
        if p2_move == "paper":
            winner = "Player 1"
        else:
            winner = "Player 2"
    elif p1_move == "paper":
        if p2_move == "scissors":
            winner = "Player 1"
        else:
            winner = "Player 2"
    elif p1_move == "scissors":
        if p2_move == "rock":
            winner = "Player 1"
        else:
            winner = "Player 2"
    print(winner)
