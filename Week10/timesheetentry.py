# Program to create a timesheet class
# Author: Breeda Herlihy

import datetime as dt

class Timesheetentry: 
    def __init__(self, project, start_time, duration):
        self.project = project
        self.start_time = start_time
        self.duration = duration
    
    def __str__(self):
        return self.project + ":" + str(self.duration)

if __name__ == '__main__': 
    ts = dt.datetime (2022, 4, 20, 21, 33)
    test = Timesheetentry('test', ts, 60)
    print(test)
