num = int(input("Up to what number do you want to make the Fibonacci series?"))

def fibonacci(num):
    list = [0]
    x = 1
    sum = 0
    for y in range(1,num):
        y = x
        x = sum
        sum = y + x
        list.append(sum)
    return list
print(fibonacci(num))