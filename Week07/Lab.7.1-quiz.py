#Program to answer quiz questions
#Author: Breeda Herlihy

# the with statement will automatically close the file
# when it is finished with it
#with open("test-a.txt") as f:
# data = f.read()
# print (data)
# Q1.a. Answer: File not found

# the with statement will automatically close the file
# when it is finished with it
#with open("test-b.txt", "w") as f:
 #   data = f.write("test b\n") # returns the number of chars written
  #  print (data)
#with open("test-b.txt", "w") as f2: # open file again
 #   data = f2.write("another line\n")
  #  print (data)
#Q1.b. Answer: Number of characters 7 and 13
#Q1.c. Answer: another line

# The with statement will automatically close the file
# when it is finished with it
with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns the number of chars written
    print (data)
with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line\n")
    print (data)
#Q1.d. Answer: test d and another line