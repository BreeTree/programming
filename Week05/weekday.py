#Program that outputs whether or not today is a weekday.
#Author: Breeda Herlihy

#Write a program that outputs whether or not today is a weekday.
#(You will need to search the web to find how you work out what day it is)
# https://www.delftstack.com/howto/python/python-datetime-day-of-week/
#An example of running this program on a Thursday is given below.
#python weekday.py
#Yes, unfortunately today is a weekday.
#An example of running it on a Saturday is as follows:
#python weekday.py
#It is the weekend, yay!


from datetime import date
import calendar
curr_date = date.today()
print(calendar.day_name[curr_date.weekday()])

from datetime import datetime
print(datetime.today().weekday())

