import datetime, time, calendar
#import time
#import calendar

print(datetime.datetime.today())
print(datetime.datetime.today().year)
print(datetime.datetime.today().month)
print(datetime.datetime.today().isoweekday())
print(datetime.datetime.today().weekday())

diff = datetime.timedelta(days=5)
print(datetime.datetime.today()-diff)
print(datetime.datetime.today()+diff)
