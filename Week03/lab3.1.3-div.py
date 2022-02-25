#Program that divides two numbers and gives a remainder
#Author: Breeda Herlihy

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the division and rounds the result down to the nearest whole number
remainder = x%y # % Modulus returns the remainder of a division
print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))