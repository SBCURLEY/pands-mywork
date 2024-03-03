# lab06.06-together1.py
# Putting it all together

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice=input("Type one letter (a/v/q): ").strip()    # The strip() method removes any leading, and trailing whitespaces.
    return choice

def doAdd (students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name: ")
    currentStudent["modules"]= readModules()
    students.append (currentStudent)
    
def readModules ():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()
    
    while moduleName != "":
        module = {}
        module ["name"] = moduleName
        # There is no error handling
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        # Now read the next module
        moduleName = input("\tEnter the next Module name (blank to quit) :").strip()
        
    return modules

def displayModules(modules):
    print("\tName       \tGrade")
    for module in modules:
        print(f"\t{module['name']}      \t{ module['grade']}")

def doView(students):
    for currentStudent in students:
        print (currentStudent["name"])
        displayModules(currentStudent["modules"]);
    
#main program

students=[]
choice=displayMenu()
while (choice!="q"):
    # we could do this with Lambda functions - but keeping it basic
    if choice == "a":
        doAdd(students)
    elif choice =="v":
        doView(students)
    elif choice !="q":
        print("\n\nPlease select a, v or q")
    choice =displayMenu()
    