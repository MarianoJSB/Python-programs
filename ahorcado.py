import random

list = ["casa", "perro", "computadora", "television", "papa"]
health = 3
play_again = "y"
word = random.choice(list)
word_sep = []
for i in word:
    word_sep.append(i)
print(f"The word has {len(word_sep)} letters")

while health > 0 and play_again.lower() == "y":
    player = input("Letra: ")
    if player in word_sep:
        count = word_sep.count(player)
        for x in range(count):
            word_sep.remove(player)
        print(f"Correct, {player} is in the word")
    else:
        print(f"Incorrect, {player} not in the word\nLifes {health - 1}")
        health -= 1
    if health == 0:
        print(f"¡GAME OVER! The word was {word}")
    if len(word_sep) == 0 and health > 0:
        health = 3
        print(f"Congratulations, the word was {word}")
        word_sep.clear()
        word = random.choice(list)
        word_sep = []
        for i in word:
            word_sep.append(i)
        play_again = input("Do you want to play again? (Y/N): ")
        if play_again.lower() != "y":
            break
        print(word_sep)