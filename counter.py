#Menu
def menu():
    print("1-Increase")
    print("2-Decrease")
    print("3-Restart")
    print("4-Exit")

#Counter
counter = 0

#Main loop
while True:
    menu()
    option = int(input("Choose an option: "))
    if option == 1:
        counter+=1
        print(f"Counter : {counter}")
    elif option == 2:
        counter-=1
        print(f"Counter : {counter}")
    elif option == 3:
        counter = 0
        print(f"Counter : {counter}")
    elif option == 4:
        break
print("Program finished")