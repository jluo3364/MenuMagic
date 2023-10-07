from flask import Flask, render_template

app = Flask(__name__, static_url_path='/vendor/')

@app.route("/index.html")
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