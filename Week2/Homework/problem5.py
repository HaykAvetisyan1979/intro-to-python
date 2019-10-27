import calendar
import datetime
import time

birth_date = datetime.date(1979, 12, 20)
print("Birthdate:", birth_date)
print("Birthdate year:", birth_date.year)
print("Birthdate month:",birth_date.month)
print("Birthdate day:",birth_date.day)
print("Birthdate weekday:",birth_date.weekday())
print("Birthdate weekday iso:",birth_date.isoweekday())

tday = datetime.date.today()

# Calculating days remaining to upcoming birthday
# depending on the birthday has already passed this year or not
#*****************************************************************************************
if (datetime.date(tday.year, birth_date.month, birth_date.day)) >= tday:   # the upcoming birth day is this year
    upcoming_bday = datetime.date(tday.year, birth_date.month, birth_date.day)
else:    # the upcoming birthday is next year
    upcoming_bday = datetime.date(tday.year+1, birth_date.month, birth_date.day)

print("Days left to upcoming birthday: ", (upcoming_bday-datetime.date.today()).days)
#*****************************************************************************************

cal = calendar.month(2017, 5)
print(cal)

delta = datetime.timedelta(days=1)
ystday = datetime.datetime.today()-delta
print("Yesterday's date and time: ", ystday)
delta = datetime.timedelta(days=2)
print("Yesterday+2days: ", ystday+delta)
delta = datetime.timedelta(days=3)
print("Yesterday-3days: ", ystday-delta)
