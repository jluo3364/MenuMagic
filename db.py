import sqlite3

def openDB():
    conn = sqlite3.connect('static/menus.db')
    return (conn, conn.cursor())