#Program to know the factorial of any number

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return f"The factorial of {n} is {fac}"
fact = factorial(int(input("Enter a number: ")))
print(fact)