# This is a simple Password Generator and Saver.

import secrets
import hashlib
import os
from getpass import getpass

MASTER_FILE = "MasterHash.txt" # placeholder file name

if not os.path.exists(MASTER_FILE):
    while True:
        print("(Note: Typing is hidden for security)")
        pw = getpass("Set a new master password: ")
        confirm = getpass("Confirm master password: ")

        if pw == confirm:
            hashed = hashlib.sha256(pw.encode()).hexdigest()
            with open(MASTER_FILE, "w") as f:
                f.write(hashed)
            print("Master password created and saved securely.")
            break
        else:
            print("Passwords do not match. Please try again.\n")
else:
    with open(MASTER_FILE, "r") as f:
        Master_Hash = f.read().strip()

Lists = [] # Creates a list for the password saver
logged_in = False # ensures that user is authorized

try:
    with open("Password.txt", "r") as file: # Upon program opening, it'll attempt to find the placeholder file
        Lists = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    Lists = [] # Creates a list for the password saver, if the file isn't found.

while True:
    try:
        if not logged_in:
            user_input = getpass("Enter Master Password or quit: ")
            user_hash = hashlib.sha256(user_input.encode()).hexdigest()

            if user_hash == Master_Hash:
                logged_in = True
                print("Access granted.")
                
            elif user_input == "quit":
                break

            else:
                print("Invalid Master Password.")
                continue

        while True:

            action = input("Logged in. Welcome to Main Menu: Password Generate, Password Saver, or Quit?").strip().lower()

            if action == "password generate": # generates a 12-letter, number, and symbol password, with user assigning a title
                while True:
                    GAction = input("Generation Menu: Generate or go back?").strip().lower()
                    if GAction == "generate":
                        PassGen = "".join(secrets.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*", k=12))
                        Title = input("Please title this passsword: ")
                        Lists.append(f"{Title} = {PassGen}")
                        with open("Password.txt", "a") as file:
                            file.write(f"{Title} = {PassGen}\n")
                        print(f"{Title} = {PassGen}")
                    
                    elif GAction in ("go back", "back", "b"):
                        break

            elif action == "password saver": # shows saved passwords, along with their titles
                while True:    
                    SAction = input("Save Menu: View or Delete?").strip().lower()
                    if SAction == "view":
                        if not Lists:
                            print("No entries yet.")
                        else:
                            for index, item in enumerate(Lists):
                                print(index, item)
                            
                    elif SAction == "delete":
                        try:
                            delete = int(input("Type number to delete: "))
                            
                            if 0 <= delete < len(Lists):
                                Lists.pop(delete)
                                print("Password Deleted.")
                            else:
                                print("Invalid index. No password deleted.")

                            with open("Password.txt", "w") as file:
                                for item in Lists:
                                    file.write(item + "\n")
                        except IndexError, ValueError:
                            print("No Entries or Invalid Input. Please try again.")
                    elif SAction in ("go back", "back", "b"):
                            break
                    
                    else:
                        print("Invalid Choice, Try again.")

            elif action == "quit":
                print("Thanks for using my simple Password Generator/Saver! Logging Out. . .")
                break
            else:
                print("Invalid Selection. Try again.")
                continue

    except ValueError: # catch all ValueError to keep from crashing out
        print("Invalid Input. Try again.")