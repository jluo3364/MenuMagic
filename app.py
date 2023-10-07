from flask import Flask, render_template
import sqlite3
import csv
import db
from db import openDB

app = Flask(__name__)

conn, cur = openDB()
cur.execute("CREATE TABLE IF NOT EXISTS allitems (id INTEGER PRIMARY KEY AUTOINCREMENT, food_name TEXT NOT NULL, food_type TEXT NOT NULL, meal TEXT NOT NULL, dining_location TEXT NOT NULL )")
with open('diningScraper.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row if it exists

    for row in csv_reader:
        cur.execute('INSERT INTO allitems (food_name, food_type, meal, dining_location) VALUES (?,?,?, ?)', (row[0], row[1], row[2], row[3]))
conn.commit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/busch.html")
def busch():
    return render_template("busch.html")

@app.route("/livingston.html")
def livingston():
    return render_template("livingston.html")

@app.route("/neilson.html")
def neilson():
    return render_template("neilson.html")