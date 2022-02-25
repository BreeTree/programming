#Calculate BMI from weight and height
#Author: Breeda Herlihy

weight = int(input("Enter your weight(kg): "))
height = int(input("Enter your height(cm): "))
#convert height from centimetres to metres
heightMetres = height/100
#calculate BMI
answer = weight/(heightMetres*heightMetres)
txt = "The BMI is {:.2f}(kg/m²)"
print(txt.format(answer))