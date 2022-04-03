# Program to create a pie chart
# Author: Breeda Herlihy

import numpy as np
import matplotlib.pyplot as plt

# Make the array of counties
counties = ['Cork', 'Kerry', 'Clare', 'Waterford', 'Limerick', 'Tipperary']
# Generate a random list of 100, p sets the frequency, must add up to 1
countiesRan = np.random.choice(counties, p=[0.6, 0.05, 0.05, 0.1, 0.1, 0.1], size = (100))

# calculate number of occcurences of each county
unique, counts = np.unique(countiesRan, return_counts = True)
plt.pie(counts, labels = unique)

plt.show()