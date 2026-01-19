import numpy as np
import pandas as pd
import sqlite3

def log_in():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    table = cursor.fetchall()

    for row in table:
        print(row)

    username = input("Enter username: ")
    password = input("Enter password: ")

    match_credentials = """
        SELECT password
        FROM users
        WHERE password = ?
    """

    cursor.execute(match_credentials, (password,))
    pass_matched = cursor.fetchone()

    if password == pass_matched[2]:
        print("Logged in successfully!")
    else:
        print("Password didn't match. Log in failed.")

def testing():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    username = "mary"

    search_query = """
        SELECT id, username, password
        FROM users
        WHERE username = ?
    """

    cursor.execute(search_query, (username,))
    user_match = cursor.fetchone()

    if user_match:
        print(f"Details of {username}:\n")
        print(f"ID: {user_match[0]}\n")
        print(f"NAME: {user_match[1]}\n")
        print(f"PASSWORD: {user_match[2]}\n")

log_in()