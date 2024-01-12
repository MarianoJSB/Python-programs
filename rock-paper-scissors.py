#The classic game: rock, paper and scissors. The winner is the first to reach 3 points
import random

#Score
playerScore = 0
botScore = 0
restart = 1

while restart == 1 :
    print("1-Rock")
    print("2-Paper")
    print("1-Scissors")
    
    player = int(input("Choose your attack: "))
    bot = random.randint(1,3)
    
    #Case 1: The player chooses Rock
    if player == 1 and bot == 1:
        print("The bot has chosen Rock. It's a tie")
        print(f"Score : Player {playerScore} - Bot {botScore}")
    elif player == 1 and bot == 2:
        print("The bot has chosen Paper. The bot wins")
        botScore+=1
        print(f"Score : Player {playerScore} - Bot {botScore}")
    elif player == 1 and bot == 3:
        print("The bot has chosen Scissors. You win")
        playerScore+=1
        print(f"Score : Player {playerScore} - Bot {botScore}")

    #Case 2: The player chooses Paper
    if player == 2 and bot == 1:
        print("The bot has chosen Rock. You win")
        playerScore+=1
        print(f"Score : Player {playerScore} - Bot {botScore}")
    elif player == 2 and bot == 2:
        print("The bot has chosen Paper. It's a tie")
        print(f"Score : Player {playerScore} - Bot {botScore}")
    elif player == 2 and bot == 3:
        print("The bot has chosen Scissors. The bot wins")
        botScore+=1
        print(f"Score : Player {playerScore} - Bot {botScore}")

    #Case 3: The player chooses Scissors
    if player == 3 and bot == 1:
        print("The bot has chosen Rock. The bot wins")
        botScore+=1
        print(f"Score : Player {playerScore} - Bot {botScore}")
    elif player == 3 and bot == 2:
        print("The bot has chosen Paper. You win")
        playerScore+=1
        print(f"Score : Player {playerScore} - Bot {botScore}")
    elif player == 3 and bot == 3:
        print("The bot has chosen Scissors. It's a tie")
        print(f"Score : Player {playerScore} - Bot {botScore}")
    
    #The player wins:
    if playerScore >= 3 and botScore < 3:
        playerScore = 0
        botScore = 0
        print("1-Yes")
        print("2-No")
        restart = int(input("Do you want to restart the game: "))
    #The bot wins:
    if playerScore < 3 and botScore >= 3:
        playerScore = 0
        botScore = 0
        print("1-Yes")
        print("2-No")
        restart = int(input("Do you want to restart the game: "))