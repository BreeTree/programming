#Program that outputs whether or not today is a weekday.
#Author: Breeda Herlihy

# Get the day of the week
# https://www.delftstack.com/howto/python/python-datetime-day-of-week/

from datetime import datetime
x = int(datetime.today().weekday())

#Use a while loop to check if it is a weekday
while x < 5:
    print("Yes, unfortunately today is a weekday.")
#if the condition is not true, then it is a weekend day    
else: 
    print("It is the weekend, yay!")
    