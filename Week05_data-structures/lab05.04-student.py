# lab05.04-student.py
# from lab sheet
# 4.	Write a program that stores a student name 
# and a list of her courses and grades in a dict, 
# the program should then print out her data.
# The number of course she has could change.
# in this example the data is hard coded
# Author: Sharon Curley (lab)

student ={
    "name":"Mary",
    "modules":[
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade": 99
        }
    ]
}

print (f"Student: {student['name']}")
#print("Student: {}".format(student["name"]))

for module in student["modules"]:
    print (f"\t {module['courseName']} \t: {module['grade']}")
    #print ("\t {} \t: {}".format(module["courseName"], module["grade"]))
