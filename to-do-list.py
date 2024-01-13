#To-do list app

#List
list = []
#Task
task = ""
#Index
index = 0

#Menu
def menu():
    print("\n1-Add task")
    print("2-Delete task")
    print("3-Clear list")
    print("4-Show list")
    print("5-Exit")

#Function to add a task to the list
def addTask(task, list):
    task = input("Enter the task: ")
    list.append(task)


#Function to delete a task to the list
def deleteTask(index, list):
    index = int(input("Enter the index of the task to delete: "))
    index-=1
    list.pop(index)

#Function to clear list
def clearList(list):
    list.clear()

#Function to show the list
def showList(list):
    print("\nTO-DO-LIST:")
    if len(list) == 0:
        print("Empty list\n")
    for index,task in enumerate(list):
        print(f"{index+1} - {task}")

#Main loop
while True:
    menu()
    option = int(input("Choose an option: "))
    if option == 1:
        addTask(task, list)
        showList(list)
    elif option == 2:
        showList(list)
        deleteTask(index, list)
    elif option == 3:
        clearList(list)
        showList(list)
    elif option == 4:
        showList(list)
    elif option == 5:
        break
print("Program finished")