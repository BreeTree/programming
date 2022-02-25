# Program to normalise and transform text
# Author: Breeda Herlihy

string = input("Please enter a string:")
stringNormalise = string.casefold().strip()

lengthOfString = len(string)
lengthofstringNormalise = len(stringNormalise)
print("That string normalised is :{}".format(stringNormalise))
print("We reduced the input string from {} to {} characters".format(lengthOfString,lengthofstringNormalise))