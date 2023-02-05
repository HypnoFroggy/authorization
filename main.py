import requests
from flask import Flask, render_template, request
# import psycopg2

app = Flask(__name__)
@app.route("/login")
def main():
    return render_template("index.html")
@app.route("/login", methods=["POST"])
def login():
    if auth(request.form["username"], request.form["password"]):
        return render_template("index.html")
    else:
        return render_template("me.html")

def auth(login, password):
    if True:
        return True
    else:
        return false
