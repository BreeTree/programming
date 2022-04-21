# Program to create an employee class
# Author: Breeda Herlihy

from timesheetentry import *

class Employee:
    timesheets = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name + " " + self.last_name

    def log_minutes(self, project, minutes):
        now = dt.datetime.now
        timesheetentry = Timesheetentry(project, now, minutes)
        self.timesheets.append(timesheetentry)

    def gettotaltime(self):
        total_minutes = 0
        for ts in self.timesheets:
            total_minutes += ts.duration
            return total_minutes

if __name__ == '__main__': 
    test = Employee('Breeda', 'Herlihy')
    print(test)
    assert ('Breeda Herlihy' == str(test))
test.log_minutes('p1', 30)
test.log_minutes('p1', 60)
mins = test.gettotaltime()
print (mins)
assert(mins == 90)
print ('All good')
#Program giving assertion error - durations not being added up
