#High card game: you play vs a bot, The winner is the one who gets highest card
import random

#Card
value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
stick = ['♦️', '♥️', '♣️', '♠️']

#Player card
player_value = random.choice(value)
player_stick = random.choice(stick)

#Bot card
bot_value = random.choice(value)
bot_stick = random.choice(stick)

#Player result
print(f"Player card: {player_value} of {player_stick}")

#Bot result
print(f"Bot card: {bot_value} of {bot_stick}")

if player_value > bot_value:
    print("¡CONGRATS! You win")
else:
    print("The bot wins :(")