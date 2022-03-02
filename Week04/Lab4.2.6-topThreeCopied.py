#Program to generate 10 random numbers
# in the range 1-100, print these numbers
# and print the top 3 numbers
# Author: Breeda Herlihy

# Use Python random Module
import random

# I programming the general case
howMany    = 10
topHowMany = 3
rangeFrom  = 0
rangeto    = 100

numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeto))
print ("{} random numbers\t {}".format(howMany,numbers))
# I am keeping the original list maybe I don't need to 
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))