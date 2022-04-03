# Program to generate random numbers using numpy
# Author: Breeda Herlihy

import numpy as np

# set absolute values into variables
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

salaries = np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.
salaries= np.random.randint(minSalary, maxSalary, numberOfEntries)
print(salaries)

salariesBonus= salaries + 5000 # this is to increase each salary by 5000 
print(salariesBonus)

salariesIncrease = salaries * 1.05 # this is to increase each salary by 5%
print(salariesIncrease)

# salariesRound = salariesIncrease.astype('i')
# https://www.w3schools.com/python/numpy/numpy_data_types.asp
salariesRound = salariesIncrease.astype(int)
print(salariesRound)

