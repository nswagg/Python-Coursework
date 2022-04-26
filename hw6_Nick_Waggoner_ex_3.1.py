"""
Homework 6, Exercise 3
Nick Waggoner
11-23-2021
Description: The multi-clipboard is updatable using inputs to the command
line. See below for format specifications. It creates a file using shelve
and, like a dictionary, can get the information from the file when called.
The data structure is dynamically updated depending on the needs of the
user and how many "clipboards" have been saved. The current implementation
does not include a method for deleting previously saved clipboards.

"""
# py.exe mcb.py save <keyword> - Saves clipboard to keyword.
# py.exe mcb.py <keyword> - Loads keyword to clipboard.
# py.exe mcb.py list - Loads all keywords to clipboard.

import pyperclip
import shelve
import sys

mcbShelf = shelve.open('mcb')  # opens the file for reading and working
# Saving clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower(0) == 'list':
        print(str(list(mcbShelf.keys())))
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()  # make sure to close the file
