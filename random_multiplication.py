import random

list = [2,3,4]
list_2 = [3,6,7]
random.shuffle(list)
random.shuffle(list_2)

for i,j in zip(list,list_2):
    mul = i * j
    n = input(f"{i} X {j} = ")
    if int(n) == mul:
        print("Correct")
    else:
        print("Incorrect")
