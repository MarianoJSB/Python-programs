#With this program you will know if any number is prime or not
#Input number
num = int(input("Enter a number to find out if it is a prime number: "))

def prime(x):
    if x < 2:
        return f"{x} is not a prime number"
    elif x == 2:
        return f"{x} is a prime number"
    for y in range(2,x):
        if x % y == 0:
            return f"{x} is not a prime number"
    return f"{x} is a prime number"

#Call a function
func = prime(num)
print(func)