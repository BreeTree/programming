# Program to write a number to a file
# Author: Breeda Herlihy


filename = "count.txt"
def writeNumber(number):
 with open(filename, "wt") as f:
    f.write(str(number))
    
# test it
writeNumber(3)
print("complete")
