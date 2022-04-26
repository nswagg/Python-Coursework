# Python-Coursework
***
The following is a list of the descriptions of each file if the file has one and the basic principles used in the program.
---
## HW4:
- EX1: This Program uses a class object "Password Locker" which stores a dictionary of passwords The user may input the name of the account. If the account exists in the dictionary, the password is copied to the user's clipboard. Note, this is not a safe or secure password locker. Do not use this as a means of securing important data. All given accounts are made up. // Uses class object, pypterclip, dictionary
- EX2: The program uses inheritance for the Square, Circle, and Rectangle classes, which all implement the abstract methods defined in the parent Shape class. Each class is capable of computing the shape's area, perimeter, and diagonal (diameter for the circle). // Inheritance, object classes
- EX3: Finds phone numbers and email addresses on the clipboard. //  Regex, pyperclip lib, clipboard
- EX4: This programs checks the strength of a password by passing it through several regex tests. // Regex (regular expressions) unit testing, functions

## HW5: 
- EX1: This is an iterator class that iterates backwards through a list //Iterator, object class
- EX2: This program uses a generator expression to calculate Pythagorean triples. Using the take() function, our program will run until it creates "n" yields. Thus, as is, the program will create a list of 10 tuples, which contain values for pythagorean triples // Generators, generator expressions
- EX3: This program uses a generator to recreate the range() function for the purpose of reserving memory. // Generator, optimization.

## HW6:
- EX1: a modification of the slowDown function: uses another external decorator to set the amount of time the system sleeps before counting down in the function. Will accept 1 or 0 arguments to the @sleepTimer decorator // Uses Decorators and Wrappers
- EX2:The program uses a decorator to store the results of the fibonacci function call in order to save storage and improve runtime. The countCalls decorator demonstrates how the cache decorator reduces the number of function calls required to run the fibonnaci function. Even to run fibonacci for the first 5 values, the cache reduces the number of calls almost in half. // Uses function decorators.
- EX3.1:The multi-clipboard is updatable using inputs to the command line. See below for format specifications. It creates a file using shelve and, like a dictionary, can get the information from the file when called. The data structure is dynamically updated depending on the needs of the user and how many "clipboards" have been saved. The current implementation does not include a method for deleting previously saved clipboards. // Uses shelves, clipboard/pyperclip library to copy text to clipboard (Ctrl + V)

## HW7:
- EX1: Renaming filenames with American MM-DD-YYYY date format to Asian date format: YYYY-MM-DD // Uses REGEX; Pathing, File I/O
- EX2: Program scans Desktop folder for all files with .pdf file extension and places them into a subfolder on the Desktop // Uses Pathing, directory walking
- EX3: The program creates an arbitrary number of threads defined by the user and executes a function and running DEBUG logging with each thread before    pausing and terminating. // Uses threading, debug logging

### _See the folder titled MORE EXAMPLES for a few extra, small examples. Generators, decorators, and web-scraping_
