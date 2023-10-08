import sqlite3

def openDB():
    conn = sqlite3.connect('static/menus.db')
    return (conn, conn.cursor())

def close(conn, cur):
    cur.close()
    conn.close()

def getLocationItems(location): #locations are Atrium, Busch, Livingston, Neilson, 
    conn, cur = openDB()

    sql = "SELECT * FROM allitems WHERE dining_location = ?"
    cur.execute(sql, (location, ))
    res = cur.fetchall() #get rows
    items = []
    for r in res:
        items.append(r)
    close(conn, cur)
    return items

def filterByMeal(meal):
    conn, cur = openDB()

    sql = "SELECT * FROM allitems WHERE meal = ?"
    cur.execute(sql, (meal, ))
    res = cur.fetchall() #get rows
    items = []
    for r in res:
        items.append(r)
    close(conn, cur)
    return items

def filterByMealAndLocation(meal, location):
    conn, cur = openDB()

    sql = "SELECT * FROM allitems WHERE dining_location = ? AND meal = ?"
    cur.execute(sql, (location, meal))
    res = cur.fetchall() #get rows
    items = []
    for r in res:
        items.append(r)
    close(conn, cur)
    return items