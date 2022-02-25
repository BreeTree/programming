# Program that takes an inputted string and outputs it in reverse order skipping characters
# Author: Breeda Herlihy

#Please enter a sentence: The quick brown fox jumps over the lazy dog.
#Output as .o zletrv pu o wr cu h

string = input ("Please enter a sentence: ")
txtReverse = string[::-1]
txtDrop = txtReverse[::2]
print(txtDrop)
