import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

month = now.month
print(month)

day = now.day
print(day)

day_of_week = now.weekday()
print(day_of_week)

# create a new date object
date = dt.datetime(year=1980, month=2, day=27)

print(date)
