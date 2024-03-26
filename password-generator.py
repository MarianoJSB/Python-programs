import random, string

# #Password length
amount = int(input("Please, enter the number of characters for the password: "))

#Characters
characters = string.ascii_letters
numbers =  string.digits
password = "".join(random.choices(characters + numbers, k=amount))

print(f"Your password is: {password}")
