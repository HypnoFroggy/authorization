import requests
from flask import Flask, render_template, request
# import psycopg2

app = Flask(__name__)
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if auth(request.form["username"], request.form["password"]):
            return render_template("me.html")
        else:
            return render_template("index.html")
    elif request.method == "GET":
        return render_template("index.html")



def auth(login, password):
    if True:
        return True
    else:
        return false
