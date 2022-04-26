"""
    Homework 4: Exercise 4
    Name: Nick Waggoner
    Date: 10-24-2021
    Description: This programs checks the strength of a password by passing it through several regex tests.
"""
import re

testLen = re.compile(r'.{8,}')      # Checks that the length is at least 8 chars that are not a newline
testCharUp = re.compile(r'[A-Z]+')  # Checks for at least one uppercase letter
testCharLo = re.compile(r'[a-z]+')  # Checks for at least one lowercase letter
testDig = re.compile(r'\d+')        # Checks for at least one digit


def driver(case):
    # REGEX ignores special characters.
    # Checks to see if at least one instance of each regex appears in the given string. Otherwise, password is weak.
    if (re.search(testLen, case) is not None and re.search(testCharUp, case) is not None and
            re.search(testCharLo, case) is not None and re.search(testDig, case) is not None):
        print("Password is strong.")
    else:
        print("Password is weak.")
        print("\nPassword must contain at least\n8 characters,\nan upper and lowercase letter,\nand at least one digit.")


# Test cases - we could easily enable this for a user input or a list of passphrases.
driver("Marmad7ke") #Strong
driver("kevin")     #Weak

