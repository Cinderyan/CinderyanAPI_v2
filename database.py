#歐睿安版權所有
#CinderyanAPT
#database
#
#
#

import sqlite3

def calendar_connection():
    conn = sqlite3.connect("data/calendar_data.db")
    return conn

def calendar_init():
    conn = calendar_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calendar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def time_tracker_connection():
    conn = sqlite3.connect("data/time_tracker_data.db")
    return conn

def time_tracker_init():
    conn = time_tracker_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS time_tracker(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL UNIQUE,
            working_hours REAL NOT NULL DEFAULT 0,
            study_hours REAL NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def deadline_connection():
    conn = sqlite3.connect("data/deadline_data.db")
    return conn

def deadline_init():
    conn = deadline_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXIST deadline(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            ststus TEXT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()