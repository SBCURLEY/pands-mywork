    # lab07.05-menuitem.py
    # Create a new menu item called save
    # When the user selects the doSave() function should be called
    # Author: Sharon Curley
    # 

students=[]

def displayMenu():
        print("What would you like to do?")
        print("\t(a) Add a new student")
        print("\t(v) View students")
        print("\t(s) Save students")
        print("\t(q) Quit")
        choice=input("Type one letter (a/v/s/q): ").strip()    # The strip() method removes any leading, and trailing whitespaces.
        return choice

def doAdd(students):
        # you have code here to view
        print ("in adding")
def doView(students):
        # you have code here to view
        print ("in viewing")
def doSave (students):
        # you will put the call to save dict here
        print ("in save")
        


    # main program
choice = displayMenu()
while (choice!="q"):
        # we could do this with Lambda functions - but keeping it basic
        if choice == "a":
            doAdd (students)
        elif choice =="v":
            doView (students)
        elif choice =="s":
            doSave (students)      
        elif choice !="q":
            print("\n\nPlease select a, v or q")
        choice =displayMenu()