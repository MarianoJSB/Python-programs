#Age calculator with datetime module
from datetime import datetime, date

month = int(input("Enter your month of birth: "))
day = int(input("Enter your day of birth: "))
year = int(input("Enter your year of birth: "))

today = date.today()
age = date(year, month, day)
counter = today - age
age_calculation = int(counter.days / 365)
month_calculation = int(counter.days / 30)
days_calculation = int(counter.days)

if month_calculation > 12:
    age_calculation += 1
    month_calculation -= 12

if days_calculation > 365:
    days_calculation -= 365
print(f"Your age is {age_calculation} with {month_calculation} months and {days_calculation} days")