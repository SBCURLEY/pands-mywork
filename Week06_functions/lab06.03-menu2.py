# lab06.03-menu2.py
# Create a program that keeps displaying the menu until the user picks q.
# if the user chooses a then call a function called doAdd() 
# if the user chooses v then call a function called doView()

# Author: Sharon Curley (lab)

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add a new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice=input("Type one letter (a/v/q): ").strip()    # The strip() method removes any leading, and trailing whitespaces.
    return choice

def doAdd():
    # we will fill in later
    print ("in adding")
def doView():
    # we will fill in later
    print ("in viewing")


# main program
choice=displayMenu()
while (choice!="q"):
    # we could do this with Lambda functions - but keeping it basic
    if choice == "a":
        doAdd()
    elif choice =="v":
        doView()
    elif choice !="q":
        print("\n\nPlease select a, v or q")
    choice =displayMenu()
        
    