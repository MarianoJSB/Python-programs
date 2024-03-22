#Program to know if any year is leap year or not

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is a leap year"
            else:
                return f"{year} is not a leap year"
        else:
            return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"
yearn = leap_year(int(input("Enter a year: ")))
print(yearn)