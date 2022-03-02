# Program that reads an integer and performs a calculation
# known as the Collatz Conjecture
# Author: Breeda Herlihy

# Have the program end if the current value is one.
# Please enter a positive integer: 10
# 10 5 16 8 4 2 1

# solution adapted from # https://www.w3resource.com/python-exercises/challenges/1/python-challenges-1-exercise-23.php
# solution not giving desired output

values = []

value = int(input("Please enter a positive integer: "))
while value > 1: 
    if value % 2 == 0:
        value = value / 2
    else:
        value = 3 * value + 1
    values.append(int(value))

print(value,(values))