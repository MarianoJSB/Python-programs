import random

#Characters
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',',','""','@','[]','!','?']

#Password length
amount = int(input("Please, enter the number of characters for the password: "))

#Password generator loop
for c in range(amount):
    character = random.choices(chars)
    passwordChar = "".join(character)
    print(passwordChar , end="")