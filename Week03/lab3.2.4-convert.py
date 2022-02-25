# Program to convert dollars to cents
# Breeda Herlihy

number = float(input("Please enter an amount:"))
convertCents = (number)*100
absoluteValue = abs(convertCents)
print('That amount in cent is {}'.format(int(absoluteValue)))