# A program to print out Summer months of the Gregorian calendar from a tuple
# Author: Breeda Herlihy

#Create a tuple to list months
monthGregorian = ("January", "February", "March", "April", "May", "June", "July",
 "August", "September", "October", "November", "December")

#Create a subset of the tuple to list summer months 
summerMonths = (monthGregorian[4:7])

#Print summer months individually
print(summerMonths[0])
print(summerMonths[1])
print(summerMonths[2])

#Or from solution in lab manual
for month in summerMonths: print(month)