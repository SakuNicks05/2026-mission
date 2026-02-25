import numpy as np
import pandas as pd
import sqlite3

def test_log():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    table = cursor.fetchall()

    for row in table:
        print(row)

    match_credentials = """
        SELECT password
        FROM users
        WHERE username = ?
    """

    username = input("Enter username: ")

    cursor.execute(match_credentials, (username,))
    pass_matched = cursor.fetchone()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user_found = cursor.fetchone()

    if not user_found:
        print("No user found.")
    else:
        password = input("Enter password: ")

    if password == pass_matched[0]: # checks if password matches
        print("Logged in successfully!")
    else:
        print("Password didn't match. Log in failed.")

def testing():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    # prints database
    print("Database: \n")
    cursor.execute("SELECT * FROM users")
    table = cursor.fetchall()
    for row in table:
        print(row)

    print("\nLOG IN: \n")
    username = input("Enter username: ")
    # checks if username exists in database
        # if not, warns that user doesn't exist

    user_details = """
        SELECT id, username, password
        FROM users
        WHERE username = ?
    """

    cursor.execute(user_details, (username,))
    user_match = cursor.fetchone()

    user_id = user_match[0]
    user_name = user_match[1]
    user_pass = user_match[2]

    password = input("Enter password: ")

    if password == user_pass:
        print("Credentials match. Logging in.")
    else:
        print("Wrong credentials. Try again.")

    # if user_match:
    #     print(f"Details of {username}:\n")
    #     print(f"ID: {user_match[0]}\n")
    #     print(f"NAME: {user_match[1]}\n")
    #     print(f"PASSWORD: {user_match[2]}\n")


def log_in():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    user_data = cursor.fetchall()

    for row in user_data:
        print(row)

    while True: # check if username exists
        username = input("Enter username: ")

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user_found = cursor.fetchone()

        if user_found:
            break
        print("User not found. Try again:")

    while True: # check if password matches
        password = input("Enter password: ")
        match_credentials = """
            SELECT password
            FROM users
            WHERE username = ?
        """

        cursor.execute(match_credentials, (username,))
        pass_matched = cursor.fetchone()

        if password == pass_matched[0]: # checks if password matches
            break
        print("Incorrect password. Try again.")

    print("Logged in successfully!")

testing()