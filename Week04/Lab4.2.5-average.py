# Program to input numbers until 0 is entered
# list all numbers entered and find an average
# Author: Breeda Herlihy

values = []

value = int(input("enter a number (0 to quit): "))
while value != 0:
    values.append(value)
    value = int(input ("enter another number (0 to quit): "))
    
# use for to print a list    
for eachNumber in values: 
    print (eachNumber)

#find average
average = float(sum(values)) / len(values)
print ("The average is {}".format(average))