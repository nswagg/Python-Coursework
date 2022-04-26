"""
    Homework 7, Exercise 1
    Nick Waggoner
    12-8-2021
    Description: Renaming filenames with American MM-DD-YYYY date format to
    Asian date format: YYYY-MM-DD

"""

import os, shutil, re

# Regex for matching the names of the files with American date format
datePattern = re.compile(r"""^(.*?) #Captures all text before the date
    ((0|1)?\d)-                     #One or two digits for the month
    ((0|2|3)?\d)-                   #One or two digits for the day
    ((19|20)\d\d)                   #Captures the year 19xx-20xx
    (.*?)$                          #All text after
    """, re.VERBOSE)

# Looping over file names in the working directory
for amerFilename in os.listdir('.'):
    check = datePattern.search(amerFilename)
    if check is None:
        continue
    # get parts of filename
    before = check.group(1)
    month = check.group(2)
    day = check.group(4)
    year = check.group(6)
    after = check.group(8)

# Forming the new file nam
asiaFilename = before + year + '-' + month + '-' + day + after

# absolute file paths:
absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
asiaFilename = os.path.join(absWorkingDir, asiaFilename)

# Renaming files
print(f'Renaming "{amerFilename}" to "{asiaFilename}"...') # Console printout
shutil.move(amerFilename, asiaFilename)