# Program to get a user to guess a number 
# from a randomly generated number between 0-100
# incorporates hints for the user
# Author: Breeda Herlihy

# Use Python random Module
import random
# use randint method to generate random numbers 
# https://www.geeksforgeeks.org/python-randint-function/?ref=lbp
correctNumber = (random.randint(0, 100))

guessNumber = int(input("Guess a number:"))
while guessNumber != correctNumber:
    if guessNumber < correctNumber:
        print("Wrong answer, too low")
    else:
       print("Wrong answer, too high")
    guessNumber = int(input("Please guess again:"))

print("Well done, correct answer! The number was:", correctNumber)