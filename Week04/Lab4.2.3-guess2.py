# Program to get a user to guess a number 
# incorporates hints for the user
# Author: Breeda Herlihy

correctNumber = 17

guessNumber = int(input("Guess a number:"))
while guessNumber != correctNumber:
    if guessNumber < correctNumber:
        print("Wrong answer, too low")
    else:
        print("Wrong answer, too high")
    guessNumber = int(input("Please guess again:"))

print("Well done, correct answer! The number was:", correctNumber)