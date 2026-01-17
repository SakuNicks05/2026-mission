import pandas as pd
import numpy as np
import string

def make_acc():
    password = input("Enter password: ")

    length = len(password)

    if length < 8:
        print("Password is too short. Must be 8-12 characters.")
    elif length > 12:
        print("Password is too long. Must be 8-12 characters.")
    else:
        print("Password length requirements met.")

    # checks for upper case
    # for char in password:
    #     if char.isupper():
    #         print("There is an upper case.")
    #         break
    #     else:
    #         print("Missing upper case.")
    #         break
    
    # # checks for lower case
    # for char in password:
    #     if char.islower():
    #         print("There is a lower case.")
    #         break
    #     else:
    #         print("Missing lower case.")
    #         break

    miss_lower = any(not char.islower() for char in password)
    miss_upper = any(not char.isupper() for char in password)
    has_space = any(char.isspace() for char in password)
    miss_digit = any(not char.isdigit() for char in password)
    miss_special = any(char.isalnum() for char in password)

    if miss_lower:
        print("Missing lower case letter")
    
    if miss_upper:
        print("Missing upper case letter")

    if has_space:
        print("Make sure not to add spaces")

    if miss_digit:
        print("Missing a number")

    if miss_special:
        print("Missing a special character")

    print("All requirements are satisfied.")


make_acc()