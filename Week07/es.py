#Program to count the number of 'e's in a text file
# Author: Breeda Herlihy

#import sys module to use code from command line
import sys

# read the file specified on the command line
filename = sys.argv[1]
def readText():
 with open(filename,"r",encoding='utf-8') as f:
    # Resolve error with unknown characters in text file by encoding UTF-8 
    # https://stackoverflow.com/questions/49562499/how-to-fix-unicodedecodeerror-charmap-codec-cant-decode-byte-0x9d-in-posit
    chapter = (f.read())
    return chapter

# count the number of e's in text being read in
total_lowercase= readText().count("e")
total_uppercase = readText().count("E")
total = total_lowercase + total_uppercase

# output the count
print("Total count of 'e's in Moby Dick:", total)
