import requests
from flask import Flask, render_template, request
# import psycopg2

app = Flask(__name__)
@app.route("/login")
def main():
    return render_template("index.html")
@app.route("/login", methods=["POST"])
def login():
    print(str(request.form["username"]))
    print(str(request.form["password"]))
    return render_template("index.html")
