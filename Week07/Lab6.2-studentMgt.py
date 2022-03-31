# A program to mnanage students
# Author: Breeda Herlihy`

import json
# the array we store everything in 
students= []
filename="studentRecords.json"
def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(l) Load records")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/l/q):").strip()
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit):").strip()

    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules

def displayModules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print("\t{} \t{}".format(module["name"], module["grade"]))

def doSave(students):
    with open(filename, "wt") as f: 
        json.dump(students, f) 
    #writeDict(students)
    print("records saved")

def doLoad(): 
    with open(filename, "rt") as f:
        return json.load(f)

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);
 

 
#main program
students = []
choice = displayMenu()
while(choice != 'q'):
 # we could do this with lamda functions
 # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave(students)
    elif choice == 'l':
        students = doLoad()
    elif choice !='q':
        print("\n\nplease select either a, v, s, or q")
    choice=displayMenu() 
