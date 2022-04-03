#Program to count how many times a program has been run
#Author: Breeda Herlihy

#read the number from the file 
filename = "count.txt"
def readNumber():
 with open(filename) as f:
    number = int(f.read())
    return number

num = readNumber()


def writeNumber(number):
 with open(filename, "wt") as f:
    f.write(str(number))
    

writeNumber(number=num+1)
print ("we have run this program {} times".format(num))
#writeNumber(num) #Not sure what the purpose of this line is? 