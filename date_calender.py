import datetime
import calendar

"""Create a program to display today’s date, time, hour, mins, second, and calendar year in 3 columns."""

e = datetime.datetime.now()
print(e)

c = calendar.calendar(2026)
print(c)