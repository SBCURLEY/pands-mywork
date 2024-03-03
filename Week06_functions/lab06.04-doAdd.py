# lab06.04-doAdd.py
# We can now write the function doAdd(  
# Read in the student’s name
# Read in the module names and grades
# Test this function, it creates a student dict, we can print that out.
# We should add the student dict to list (pass this list in)

students = []
def readModules():
    return[]
    
def doAdd (students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    
    students.append (currentStudent)
    
#test

doAdd (students)

doAdd (students)
print (students)