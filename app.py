from flask import Flask, render_template, request, jsonify
import sqlite3
import csv
import db
from db import *

app = Flask(__name__)

conn, cur = openDB()
cur.execute("CREATE TABLE IF NOT EXISTS allitems (id INTEGER PRIMARY KEY AUTOINCREMENT, food_name TEXT NOT NULL, food_type TEXT NOT NULL, meal TEXT NOT NULL, dining_location TEXT NOT NULL )")
# with open('diningScraper.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)  # Skip the header row if it exists

#     for row in csv_reader:
#         cur.execute('INSERT INTO allitems (food_name, food_type, meal, dining_location) VALUES (?,?,?, ?)', (row[0], row[1], row[2], row[3]))
# conn.commit()
close(conn, cur)

atriumItems = getLocationItems("Atrium")
buschItems = getLocationItems("Busch")
liviItems = getLocationItems("Livingston")
neilsonItems = getLocationItems("Neilson")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/busch.html")
def busch():
    print(filterByMealAndLocation("Lunch", "Busch"))
    return render_template("busch.html")

@app.route("/livingston.html")
def livingston():
    return render_template("livingston.html")

@app.route("/neilson.html")
def neilson():
    return render_template("neilson.html")

@app.route("/atrium.html")
def atrium():
    return render_template("atrium.html", location = "Atrium",items = atriumItems)

@app.route('/filterfor<location>', methods=['GET','POST'])
def itemsForMealAtLocation(location):
    option = request.form.get('meal')
    print(option)
    print(location)

    # Process the option as needed
    print('Received option:', option)
    items = filterByMealAndLocation(option, location)
    return render_template(location+".html", location = location, items = items)

if __name__ == '__main__':
    app.run(debug=True)