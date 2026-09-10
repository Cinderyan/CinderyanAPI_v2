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

