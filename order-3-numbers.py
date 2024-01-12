#Program that sorts 3 numbers(ASC) entered by user

#Variables
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#Sorting case 1:
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"{num3} - {num2} - {num1}")
    else:
        print(f"{num2} - {num3} - {num1}")

#Sorting case 2:
if num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"{num3} - {num1} - {num2}")
    else:
        print(f"{num1} - {num3} - {num2}")

#Sorting case 3:
if num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f"{num2} - {num1} - {num3}")
    else:
        print(f"{num1} - {num2} - {num3}")