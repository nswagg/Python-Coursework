"""
    Homework 4: Exercise 1
    Name: Nick Waggoner
    Date: 10-24-2021
    Description: Password Locker
        This Program uses a class object "Password Locker" which stores a dictionary of passwords
        The user may input the name of the account. If the account exists in the dictionary, the
        password is copied to the user's clipboard.
        Note, this is not a safe or secure password locker. Do not use this as a means of securing
        important data. All given accounts are made up.
"""
import pyperclip as pc


# PasswordLocker object class
class PasswordLocker:
    passwords = {}

    def __init__(self, dictionary):
        self.passwords.update(dictionary)

    def pass2Clipboard(self, account):
        if account.lower() in self.passwords.keys():
            # df=pd.DataFrame([passwords[account]])
            # df.to_clipboard(index=False,header=False)
            pc.copy(self.passwords[account.lower()])
            print("Your password has been copied to the clipboard.")
        else:
            print("Your request could not be completed.")

    def printOut(self):
        print(self.passwords)


placeholder = {"instagram": "he3ho0", "facebook": "GEAspam", "website": "K0s25V7kbCnPnnTg!yD0JO"}
socialMediaPasswords = PasswordLocker(placeholder)  # This creates the new object and stores the data inside
socialMediaPasswords.printOut()
funcCall = input("Which account would you like to access:")
socialMediaPasswords.pass2Clipboard(funcCall)
