'''
    Homework 1
    Name: Nick Waggoner
    Date: 9-3-2021
    Description: The following is a basic security program implementing
    python basics and flow control methods. When the user answers all
    questions correctly, there is a hidden message revealed.

    Tags: random, flow control
'''
#imports for randint, sys.exit, and time.sleep()
import random, sys, time

print("""Welcome to the vault.\n
Please answer the following questions.
If you do not answer correctly, the program will terminate.
""")

#Checks user input for correct name
while True:
    name = input("What is your name?\n")
    if len(name) != 4: #Not 4 characters. Move to exit program
        print("Impostor\nInitiating Shutdown")
    elif name == "Nick": #The Correct answer
        print("Welcome back " + name + ".\n")
        break
    else: #Give the user another try
        print("That seems close, but not quite right.\nAre you an impostor?")
        continue

    #Pauses the program for 3 seconds before exiting
    #Better luck next time
    time.sleep(3)
    sys.exit()

# Set up to ask the user three math questions with progressively
# bigger number answers
for i in range(0,3):
    mathTime = ((i + 2) * 2) ** 2
    print("What is ((" + str(i) + " + 2) * 2) ** 2)?")
    user = int(input())
    if user == mathTime:
        print("Good job")
        continue
    print("Better work on your math skills....")
    time.sleep(3)
    sys.exit()

#50/50 chance coinFlip
coinFlip = random.randint(0,1)
#Uses Truthy/Falsey from coinFlip to automatically respond
print("No time for a break!\nThink you are pretty slick?")
if coinFlip:
    print("Woah, slow down there skater.")
else:
    print("Looks like you forgot the bean dip. Not cool.")

while True:
    #Converts input to float
    user = float(input("Password:"))
    if (user // 4) == 5.0:
        break;

#List of outro comments if all other stages were passed
print("Are you...")
time.sleep(2)
print("ready...")
time.sleep(2)
print("for a secret?")
time.sleep(2)

print("Vault Opened: secret.txt extracted")
time.sleep(2)
print("Reading:")
time.sleep(2)
print("I think black licorice is very tasty.")
print("\n\nTO-DO: Upgrade security")
