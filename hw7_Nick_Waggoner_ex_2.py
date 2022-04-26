"""
    Homework 7, Exercise 2
    Nick Waggoner
    12-8-2021
    Description: Program scans Desktop folder for all files with .pdf file extension and places them
    into a subfolder on the Desktop

"""

import os
import shutil

# Finds the user's path to the Desktop folder
desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Creates the new directory and stores the path if it doesn't already exist
newDir = os.path.join(desktopPath, 'Pycharm PDFS')
if not os.path.isdir(newDir):
    os.makedirs(newDir)

for folderName, subfolders, filenames in os.walk(desktopPath):
    #So we don't walk through the folder we just created
    if folderName != newDir:
        # move the things to the new directory
        print("Begin Walk in os.walk() for " + folderName)
        for filename in filenames:
            if filename.endswith(('.pdf', '.Pdf', '.PDF')):  # Capturing Edge cases
                pathSize = os.path.getsize(os.path.join(folderName, filename))
                print(f'Copying {filename} (Size: {str(int(pathSize / 1000))} KB) from {folderName} to {newDir}...')
                shutil.move(os.path.join(folderName, filename), newDir)

print("Walks completed.")
