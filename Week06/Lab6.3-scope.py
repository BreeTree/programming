#more messing with functions
# Author: Breeda Herlihy

from multiprocessing.connection import answer_challenge


def topower(number, power=3): 
    #print number
    return number ** power

num = 7
answer = topower(num)
print ("cube of", num, "is", answer)
