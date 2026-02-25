import numpy as np
import pandas as pd
import sqlite3

def log_in():
    pass

def testing():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    print("LOG IN: \n")
    username = input("Enter username: ")
    password = input("Enter username: ")

    user_pass = """
        SELECT password
        FROM users
        WHERE password = ?
    """

    user_id = """
        SELECT id
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

    print("Database: \n")
    cursor.execute("SELECT * FROM users")
    table = cursor.fetchall()
    
    for row in table:
        print(row)

testing()