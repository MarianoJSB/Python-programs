array = []
option = "y"

#Order menu
def menu():
    print("1-ASC")
    print("2-DESC")

#Items loop
while option.lower() == "y":
    item = int(input("What's the number that you want to add in the array? "))
    array.append(item)
    option = input("Do you continue to add items in the array Y/N? ")

menu()
sort = int(input("How do you want to order a array? "))

#Order and iter an array
if sort == 1:
    array.sort()
    for i, v in enumerate(array):
        print(f"{i+1}° - {v}")
elif sort == 2:
    array.sort(reverse=True)
    for i, v in enumerate(array):
        print(f"{i+1}° - {v}")