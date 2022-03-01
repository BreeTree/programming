# Program to get a user to guess a number
# Author: Breeda Herlihy

correctNumber = 17

guessNumber = input("Enter a number:")
while guessNumber != correctNumber :
   print("Wrong answer, try again")
   guessNumber = int(input("Please guess again:"))

print ("Well done, correct answer! The number was:", correctNumber)