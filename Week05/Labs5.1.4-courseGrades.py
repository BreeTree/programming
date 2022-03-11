#Program to generate list of course grades
#Author: Breeda Herlihy

#Write a program that stores a student name and a list of her courses and
#grades in a dict, the program should then print out her data.
#The number of course she has could change.
#Student: Mary
# Programming : 45
# History : 99
courses = {"studentName":'Mary', "programming": 45, "history": 99}

x = courses["studentName"]
y = courses["programming"]
z = courses["history"]
print("Student name: ",x)
print("Programming: ",y)
print("History: ",(z))

#x = courses.get("model")
#print(x)

