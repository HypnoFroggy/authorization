import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database="servise_db",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login = request.form["username"]
        password = request.form["password"]
        if login == "": return render_template("index.html", validator=True, data=[False, False, True])
        if password == "": return render_template("index.html", validator=True, data=[False, False, True])
        records = auth(login, password)
        if len(records) != 0:
            return render_template("me.html", data=records[0])
        else:
            valid = checkLogin(login)
            return render_template("index.html", data=[valid, not valid])
    elif request.method == "GET":
        return render_template("index.html")


def auth(login, password):
    cursor.execute("SELECT * FROM servise.users WHERE login=%s AND password=%s", (str(login), str(password)))
    records = list(cursor.fetchall())
    return records

def checkLogin(login):
    cursor.execute("SELECT * FROM servise.users WHERE login='%s'" % (str(login)))
    records = list(cursor.fetchall())
    if len(records) == 0:
        loginInDB = False
    else:
        loginInDB = True
    return loginInDB

