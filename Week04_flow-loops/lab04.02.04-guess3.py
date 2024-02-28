# lab04.02.04-guess3.py
# prompts the user to guess a number and stops when they get it right
# the program will tell the user if they were too high or too low
# Author: Sharon Curley

import random
guess = random.randint(1,100)
print ("Here is a random number {}".format(guess))

numberToGuess = 30

#guess = int(input("Please guess the number: "))
#guess = numberToGuess
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:
        print ("Too high")
    guess  = int(input("Please guess again: "))
    
print ("Well done! Yes the number was", numberToGuess)