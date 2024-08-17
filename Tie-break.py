#Tie break tennis counter
import random

def template(p1,p2):
    return f"Player 1 {p1} - {p2} Player 2"

def tie_break():
    player1_points = 0
    player2_points = 0
    exp = player1_points < 7 and player2_points < 7 and (player1_points - player2_points != 2) and (player2_points - player1_points != 2)
    while exp:
        result = random.randint(1,2)
        point = input("?")
        if result == 1:
            player1_points += 1
            print("Point for player 1")
            print(template(player1_points, player2_points))
        else: 
            player2_points += 1
            print("point for player 2")
            print(template(player1_points, player2_points))
        if player1_points >= 7 and (player1_points - player2_points >= 2):
            return f"Tie-break for player 1\nFinal result: {template(player1_points, player2_points)}"
        elif player2_points >= 7 and (player2_points - player1_points >= 2):
            return f"Tie-break for player 2\nFinal result: {template(player1_points, player2_points)}"
print(tie_break())