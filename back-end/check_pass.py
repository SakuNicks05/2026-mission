import pandas as pd
import numpy as np

def make_acc():
    password = input("Enter password: ")

    length = len(password)

    if length < 8:
        print("Password is too short. Must be 8-12 characters.")
    elif length > 12:
        print("Password is too long. Must be 8-12 characters.")
    else:
        print("Password length requirements met.")

    for char in password:
        print(char)


make_acc()
