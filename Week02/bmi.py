#Calculate BMI from weight and height
#Author: Breeda Herlihy

weight = int(input("Enter your weight(kg): "))
height = int(input("Enter your height(cm): "))
heightmetres = height/100
answer = weight/(heightmetres*heightmetres)
txt = "The BMI is {:.2f}(kg/m²)"
print(txt.format(answer))