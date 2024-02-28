# isEven.py
# This program will ask the user to enter a number 
# and tell the user if it is an odd number or an even number

number = int(input("Enter an Integer "))

if(number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

