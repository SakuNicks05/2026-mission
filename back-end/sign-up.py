import numpy as np
import pandas as pd
import json
import os
import re
import sqlite3
from datetime import datetime

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

cursor.execute("""
    CREATE TABLE IF NOT EXISTS survey_data (
        devo_freq INTEGER,
        dev_time TIME,
        prayer_freq INTEGER,
        prayer_time TIME,
        season TEXT,
        swc_freq INTEGER,
        swc_time TIME,
        lg_freq INTEGER,
        lg_time TIME,
        spirit_color TEXT
    ) 
""")

# checking if username is taken
# checking if email is valid
# requirements for password
# password strength recommend
# enter again (to test if it was held in json and kept)

def user_data():
    conn = sqlite3.connect("../database/zion.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    table = cursor.fetchall()

    print("USER CREDENTIAL DETAILS:")
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
        user_data()
    elif choice == "S":
        search_user()
        user_data()
    else:
        print("Invalid. Try again.")

def delete_table():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")

    connection.commit()
    connection.close()

    user_data()
    print("Table deleted!")

def show_survey_data():
    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM survey_data")
    survey_table = cursor.fetchall()

    for row in survey_table:
        print(row)

def survey_data():

    # devo data
    devo_freq = int(input("Enter frequency of devotionals: "))
    while True:
        devo_time = input("Enter time for devotional: ")
        try:
            fin_devo_time = datetime.strptime(devo_time, "%H:%M").time().strftime("%H:%M")
            break
        except ValueError:
            print("Invalid time format. Try again.")

    # prayer data
    prayer_freq = int(input("Enter frequency of prayer time: "))
    while True:
        prayer_time = input("Enter time for prayer times: ")
        try:
            fin_prayer_time = datetime.strptime(prayer_time, "%H:%M").time().strftime("%H:%M")
            break
        except ValueError:
            print("Invalid time format. Try again.")

    swc_freq = int(input("Enter frequency of SWC: "))
    while True:
        swc_times = input("Enter time for swc gatherings: ")
        try:
            fin_swc_time = datetime.strptime(swc_times, "%H:%M").time().strftime("%H:%M")
            break
        except ValueError:
            print("Invalid time format. Try again.")

    lg_freq = int(input("Enter frequency of LG: "))
    while True:
        lg_times = input("Enter time for LG gatherings: ")
        try:
            fin_lg_time = datetime.strptime(lg_times, "%H:%M").time().strftime("%H:%M")
            break
        except ValueError:
            print("Invalid time format. Try again.")

    season = input("Enter season of life (student, leader, teacher, working): ")
    color_spirit = input("Enter color of spirit: ")

    connection = sqlite3.connect("../database/zion.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO survey_data (devo_freq, dev_time, prayer_freq, prayer_time, season, swc_freq, swc_time, lg_freq, lg_time, spirit_color)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (devo_freq, fin_devo_time, prayer_freq, fin_prayer_time, season, swc_freq, fin_swc_time, lg_freq, fin_lg_time, color_spirit))

    connection.commit()
    connection.close()

    print("Data added successfully\n")
    print("SURVEY DETAILS:\n")

    show_survey_data()

survey_data()