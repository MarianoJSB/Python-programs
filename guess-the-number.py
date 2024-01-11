import random

print("---Welcome to guess the number between 1-100---")

numero = random.randint(1,100)#Number to guess
intentos = 0#Attempts

while True:
    jugador = int(input("What do you think the number is? "))#Player number
    if jugador == numero:#When the user guesses the number
        print(f"Congratulations you guessed it, the number is {numero}")
        break
    elif jugador > numero:#When the player number is higher
        intentos+=1
        print(f"{jugador} is higher than the number to guess")
    elif jugador < numero:#When the player number is less
        intentos+=1
        print(f'{jugador} is less than the number to guess')
print(f"Attempts: {intentos}")#Attempts printed
print("Game over")