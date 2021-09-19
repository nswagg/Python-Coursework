'''
    Homework 2: Exercise 4 Part 2
    Name: Nick Waggoner
    Date: 9-22-2021
    Description: This program creates a guessing game using a random number generator where
        the user attempts to guess the number within a certain number of guesses. The
        program relays whether the guess was too high or too low.
        This version includes an additional layer where the boundaries for the player to
        guess between are randomized within a maximum upper limit.

        Tags: input validation, rng, user input
'''

import random

#Creates the boundaries for our RNG
max = 4000 # The absolute max number for the RNG
lower = random.randint(0,max)
upper = random.randint(lower,max)

guess = random.randint(lower, upper)    # Holds the random number
playerGuesses = 10                      # How many attempts the player gets to guess the number
playerMove = None                       # Non-value variable; declares playerMove but does not fill it
count = 0                               # counter for keeping track of attempts
print('Welcome to the guessing game.\nI am thinking of a number between %s and %s. You have %s tries to guess.' %(lower, upper, playerGuesses))

#Counts the number of guesses.
while (count < playerGuesses):
    #Input Validation
    while True:
        playerMove = input('Take a guess: ')
        try:
            playerMove = int(playerMove)

            if playerMove < lower or playerMove > upper:
                print('Please enter an integer in bounds.')
                continue
            break
        except ValueError:
            print('ERROR: Enter a valid integer please.')
    #Response: Is player hot or cold?
    if playerMove > guess:
        print('Your guess is too high.')
    elif playerMove < guess:
        print('Your guess is too low.')
    else: #must be that playerMove == guess
        print('Good job! You guessed my number in %s guesses!' %(count + 1))
        break   #exits the loop and stops counting.
    count += 1
#If player does not guess in time
if (count == playerGuesses):
    print('Oops, it looks like you have run out of guesses. Better luck next time.')

