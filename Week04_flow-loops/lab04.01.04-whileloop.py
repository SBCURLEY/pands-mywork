# lab04.01.04-whileloop.py
# While loop
# Author: Sharon Curley

i = int(input("Enter an Integer "))

while i == -1:                                          # Ref :https://www.w3schools.com/python/python_while_loops.asp
    print(i)
    print ("Goodbye")
    break
    i += -1

else:
    print(f"Thank you for entering {i}, please enter -1 to end the program")