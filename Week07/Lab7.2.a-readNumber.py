# Program to read a number from a file
# Author: Breeda Herlihy


filename = "count.txt"
def readNumber():
 with open(filename) as f:
    number = int(f.read())
    return number
# test it
num = readNumber()
print(num)
