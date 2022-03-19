# Program that calculates square root 
# Author: Breeda Herlihy

# read in the number 14.5
x = float(input("Please enter a positive number: "))

# define a function to calculate square root of a number using Newton's method
# https://stackoverflow.com/questions/3047012/how-to-perform-square-root-without-using-math-module
def sqrt(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001: # example threshold
            return guess
        last_guess= guess

#round the square root to one decimal place
y = round((sqrt(x)), 1)
print('The square root of {} is approx. {}'.format(x, y))