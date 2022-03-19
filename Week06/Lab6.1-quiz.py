# Quiz as part of Week 06 lab for programming and scripting
# Author: Breeda Herlihy

# function yo takes one parameter
def yo(a):
 return a * 2
# here we are calling the function yo
# and are passing in an argument, 3
yo(3)
var = yo(3)
print(yo(3))
print(var)

# tutorials from Datacamp
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = str.upper(place)

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count("o"))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
