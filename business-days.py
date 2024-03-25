#Program that calculator all business days (Monday-Friday) between two dates
from datetime import datetime, date, timedelta

print("business days calculation")

month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
year = int(input("Enter a year: "))

def businessDays(month, day, year):
    user_date = date(year, month, day)
    today = date.today()
    days = 0
    business = 0
    while today >= user_date:
        print(today.strftime('%Y-%m-%d'))
        print(today.strftime('%A'))
        today -= timedelta(days=1)
        if today.strftime('%A') == 'Saturday' or today.strftime('%A') == 'Sunday':
            days += 1
        business += 1
    business -= days
    print(days)
    return f"Business days from {user_date} are {business}"
bd = businessDays(month, day, year)
print(bd)