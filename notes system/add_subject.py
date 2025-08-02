import csv

def write_csv(info):
    with open("notes.csv" ,"a", newline="") as file:
        field = ["Subject", "Test 1", "Test 2", "Average"]
        writer = csv.DictWriter(file, fieldnames=field)
        file.seek(0)
        writer.writerows(info)

def add_sub(subject, test_1, test_2, average):
    data = [
        {
            "Subject": subject,
            "Test 1": test_1,
            "Test 2": test_2,
            "Average": average
        }
    ]
    write_csv(data)

def template():
    print("----CBC management system----")
    print("1-Yes")
    print("2-No")

while True:
    template()
    option = int(input("Do you want to add a new subject information? "))
    if option == 1:
        sub = input("Enter a subject name: ")
        t1 = int(input("Enter the first test note: "))
        t2 = int(input("Enter the second test note: "))
        ave = (t1 + t2) / 2
        add_sub(sub, t1, t2, ave)
    elif option == 2:
        print("¡Thank you for use the system!")
        break