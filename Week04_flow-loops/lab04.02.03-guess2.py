# lab04.02.03-guess2.py
# prompts the user to guess a number and stops when they get it right
# the program will tell the user if they were too high or too low
# Author: Sharon Curley

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:
        print ("Too high")
    guess  = int(input("Please guess again: "))
    
print ("Well done! Yes the number was", numberToGuess)