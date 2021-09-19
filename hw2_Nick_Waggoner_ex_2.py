'''
    Homework 2: Exercise 2
    Name: Nick Waggoner
    Date: 9-22-2021
    Description: collatz() as one argument called number.
        If number is even, then collatz() should print number // 2
        and return this value. If number is odd, then collatz()
        should print and return 3 * number + 1. This process is
        recursively called until the returned number equals 1.
        This version includes additional input validation to
        make sure the that value entered by the user is valid.

    Tags: input validation, try catch
'''

import sys, time

def collatz(number):
    #Check if even
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    #else, it is odd
    else:
        result = number * 3 +1
        print(result)
        return result


inputValid = False
while inputValid == False:
    userNumber = input('Enter positive integer: ')
    try:
        userNumber = int(userNumber)

        if userNumber < 0:
            print('Please enter a positive integer')
            continue
        break
    except ValueError:
        print('ERROR: Enter a valid integer please.')
        time.sleep(2.0)

userNumber = collatz(userNumber)
while userNumber != 1:
    userNumber = collatz(userNumber)
