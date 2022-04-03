# Program to create scatter plot of ages versus salaries
# Author: Breeda Herlihy

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1) # this is so that the "random" numbers 
# are the same each time to make it easier to debug.
salaries= np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low = 21, high = 65, size = numberOfEntries) 

plt.scatter(ages, salaries)
plt.show()