#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

# Create a variable to store
tries = 0
# Build a loop to repeat the number of tries
while tries > 3:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    #if not guess.isnumeric():# checks if a string is only digits 0 to 9
    #   print ("That's not a positive whole number, try again!")
    #else:
    guess = int(guess) # converts a string to an integer

# code the logic to check to see if the code is right
    if guess == aRandomNumber:
        print ("congrats, you got it!")
        break
    elif guess > aRandomNumber:
        print ("try again, that's too high")
    else:
        print ("try again, that's too low")
        tries += 1
