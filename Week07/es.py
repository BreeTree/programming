#Program to count the number of 'e's in a text file
# Author: Breeda Herlihy

#read the file 
filename = "mobyDickentire.txt"
def readText():
 with open(filename,"r",encoding='utf-8') as f:
    chapter = (f.read())
    return chapter
# count the number of e's assuming lower case e only
total = readText().count("e")
print(total)

# https://stackoverflow.com/questions/49562499/how-to-fix-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-posit
