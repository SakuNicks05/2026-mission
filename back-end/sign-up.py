import numpy as np
import pandas as pd
import json
import os
import re
import mysql.connector
import sqlite3

connection = sqlite3.connect("zion.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT,
        password TEXT
    )
""")

connection.commit()
print("Database and table made successfully!")

# create sign up page, add list/array/object IF doesn't have an account yet

# print("Welcome to Zion. \nCreate an account.\n")
# username = input("Enter a username: ")
# email = input("Enter your email: ") # figure out how to double check actual gmail
# password = input("Enter password: ")
# users_data = "users.json"
# # stores user details in json file

# def add_user():
#     if os.path.exists(users_data):
#         with open(users_data, "r") as file:
#             data = json.load(file)
#     else:
#         data = {"users": {}}

#     data["users"][username] = {
#         "email": email,
#         "password": password
#     }

# checking if username is taken
# checking if email is valid
# requirements for password
# password strength recommend
# enter again (to test if it was held in json and kept)