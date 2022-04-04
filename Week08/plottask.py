# Program to display the plot of functions
# Author: Breeda Herlihy

import numpy as np
import matplotlib.pyplot as plt

#Return evenly spaced numbers over a specified interval.
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
x = np.linspace(start = 0, stop = 4)
                   
plt.title("Functions of x", fontsize = 30)
# plot f(x) = x
plt.plot(x, x, label="f(x)=x")
# plot and calculate x squared 
    # https://www.geeksforgeeks.org/numpy-square-python/
# use unicode for superscript on the labels 
    # https://www.geeksforgeeks.org/how-to-print-superscript-and-subscript-in-python/
plt.plot(x, np.square(x), ls = '--', label="g(x)=x\u00b2")
# plot and calculate x cubed 
    # https://numpy.org/doc/stable/reference/generated/numpy.power.html
plt.plot(x, np.power(x,3), ls = ':', label="h(x)=x\u00b3")
# set axis limits 
    # https://stackoverflow.com/questions/3777861/setting-y-axis-limit-in-matplotlib
plt.ylim(0,4)
plt.xlim(0,4)
plt.legend()

plt.show()