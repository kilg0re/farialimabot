import os
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        filename = os.path.split(db_file)[1]
        print(f"Database created as '{filename}'")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    
if __name__ == '__main__':
    if not os.path.exists('../db/'):
        os.mkdir('../db/')
    create_connection('../db/flbot.db')
