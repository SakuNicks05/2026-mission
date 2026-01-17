import numpy as np
import pandas as pd
import json
import os
import re
import mysql.connector
import sqlite3

DB_DIR = "../database"
DB_PATH = os.path.join(DB_DIR, "zion.db")

os.makedirs(DB_DIR, exist_ok=True)

connection = sqlite3.connect("../database/zion.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        email TEXT,
        password TEXT
    )
""")

# checking if username is taken
# checking if email is valid
# requirements for password
# password strength recommend
# enter again (to test if it was held in json and kept)

def show_table():
    conn = sqlite3.connect("../database/zion.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    table = cursor.fetchall()

    for row in table:
        print(row)

def search_user():
    conn = sqlite3.connect("../database/zion.db")
    cur = conn.cursor()

    find_user = input("Enter username to search: ")

    cur.execute(
        "SELECT * FROM users WHERE username = ?",
        (find_user,)
    )

    user = cur.fetchone()

    if user:
        print("User found in database.")
    else:
        print("User not found.")

def check_password(password):
    pass

def add_user():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    choice = input("Search or Add a user (S/A): ")
    
    if choice == "A":
        while True:
            username = input("Enter your username: ")

            cursor.execute(
                "SELECT * FROM users WHERE username = ?",
                (username,)
            )
            found_user = cursor.fetchone()

            if found_user:
                print("Username is already taken. Try another username.")
            elif not found_user:
                break
            else:
                print("Invalid.")

        email = input("Enter your email: ")
        password = input("Enter your password: ")

        check_password(password)

        cursor.execute("""
            INSERT INTO users (username, email, password)
            VALUES (?, ?, ?)
        """, (username, email, password))

        connection.commit()
        connection.close()
        print("User added successfully!")
        show_table()
    elif choice == "S":
        search_user()
        show_table()
    else:
        print("Invalid. Try again.")

def delete_table():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")

    connection.commit()
    connection.close()

    show_table()
    print("Table deleted!")

add_user()