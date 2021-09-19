'''
    Homework 2: Exercise 4 Part 3
    Name: Nick Waggoner
    Date: 9-22-2021
    Description: This program creates a guessing game using a random number generator where
        the user attempts to guess the number within a certain number of guesses. The
        program relays whether the guess was too high or too low.
        This version includes an additional layer where the boundaries for the player to
        guess between are randomized within a maximum upper limit.
        This version implements a computer user to automatically guess the number (not
        hardcoded) using a binary search function implementation based on whether the
        guess is too high or too low (this feedback is stored in hiLo)

    Tags: input validation, rng, automated player, binary search
'''

import random

def computer(last, bounds, hiLo):
    # The computer player is implemented like a binary search. It won't repeat itself,
    # it is not perfect, but it is fairly accurate
    playerMove = int()
    if (last == None):
        playerMove = ((bounds[0] + bounds[1]) // 2) #Finds the mid-way point between the bounds
        print(playerMove)
        return playerMove
    elif (hiLo[-1] == 1): #Guess was too high
        bounds[1] = last - 1    # Modifies upper boundary
        playerMove = ((bounds[0] + bounds[1]) // 2) #Finds the mid-way point between the bounds
        print(playerMove)
        return playerMove
    else:#(hiLo[-1] == 0): #Guess was too low
        bounds[0] = last + 1    # Modifies lower boundary
        playerMove = ((bounds[0] + bounds[1]) // 2) #Finds the mid-way point between the bounds
        print(playerMove)
        return playerMove

#Creates the boundaries for our RNG
max = 10000  # The absolute max number for the RNG
lower = random.randint(0,max)
upper = random.randint(lower,max)

bounds = [lower, upper] # For storing bounds for computer to guess
last = None             # Stores previous guess
hiLo = []               # Was the last guess too high or too low?

guess = random.randint(lower, upper)    # Holds the random number
playerGuesses = 10                      # How many attempts the player gets to guess the number
playerMove = None                       # Non-value variable; declares playerMove but does not fill it
count = 0                               # counter for keeping track of attempts
print('Welcome to the guessing game.\nI am thinking of a number between %s and %s. You have %s tries to guess.' %(lower, upper, playerGuesses))

#Counts the number of guesses.
while (count < playerGuesses):
    playerMove = computer(last, bounds, hiLo)
    last = playerMove
    #Response: Is player hot or cold?
    if playerMove > guess:
        print('Your guess is too high.')
        hiLo.append(1)
    elif playerMove < guess:
        print('Your guess is too low.')
        hiLo.append(0)
    else: #must be that playerMove == guess
        print('Good job! You guessed my number in %s guesses!' %(count + 1))
        break   #exits the loop and stops counting.
    count += 1
#If player does not guess in time
if (count == playerGuesses):
    print('You have run out of guesses.\nWe were looking for %s.\nBetter luck next time.' %(guess))
