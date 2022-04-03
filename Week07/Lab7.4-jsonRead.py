#Program to read JSON from a file
#Author: Breeda Herlihy

import json
filename="testdict.json"

def readDict():
    with open(filename) as f:
       return json.load(f)

#test the function
someDict = readDict()
print(someDict)