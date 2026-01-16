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

username = input("Enter your username: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

cursor.execute("""
    INSERT INTO users (username, email, password)
    VALUES (?, ?, ?)
""", (username, email, password))

connection.commit()
connection.close()
print("User added successfully!")

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

show_table()