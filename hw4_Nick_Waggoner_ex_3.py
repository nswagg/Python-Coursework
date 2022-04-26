"""
    Homework 4: Exercise 3
    Name: Nick Waggoner
    Date: 10-24-2021
    Description: Finds phone numbers and email addresses on the clipboard.
"""
import pyperclip
import re


phone = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code
    (\s|-|\.)?                      #separator
    (\d{3})                         #First 3 nums
    (\s|-|\.)?                      #separator
    (\d{4})                         #next 4 nums
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension number if available
)''', re.VERBOSE)

email = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                       #the @ symbol
    [a-zA-z0-9.-]+          #domain name
    (\.[a-zA-z]{2,4})       #dot-something. Tells us the type of website between 2 and 4 chars
)''', re.VERBOSE)

clipboard = str(pyperclip.paste())
matches = []

# finds all matches for emails and phone numbers from the clipboard
for groups in phone.findall(clipboard):
    phoneFormat = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneFormat += ' x' + groups[8]
    matches.append(phoneFormat)  # This will put our code into a standardized format
for groups in email.findall(clipboard):
    matches.append(groups[0])

# Now to copy the matches to the clipboard and print to the terminal
if len(matches) > 0:  # ie, the list is not empty
    pyperclip.copy('\n'.join(matches))  # the copy method can only grab one instance at a time, so we need to join them
    # printing to terminal
    print("Successfully copied:")
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses in selection found.")
