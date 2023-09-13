import requests
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database="servise_db",
    user="postgres",
    password="dfgrtgrt",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# моё
@app.route("/login", methods=["POST", "GET"])
def login():
    errors = {}
    if request.method == "POST":
        if request.form.get("login"):
            errors = {}
            login = request.form["username"]
            password = request.form["password"]
            if login == "" or password == "":
                errors["empty_field"] = True
                return render_template("index.html", errors=errors)
            records = auth(login, password)
            if len(records) != 0:
                return render_template("me.html", data=records[0])
            else:
                errors["wrong_data"] = True
                return render_template("index.html", errors=errors)
        elif request.form.get("registration"):
            return redirect("/registration")
    elif request.method == "GET":
        return render_template("index.html", errors=errors)

@app.route("/registration", methods=["GET", "POST"])
def registration():
    errors = {}
    if request.method == "GET":
        return render_template("registration.html")
    if request.method == "POST":
        name = request.form["name"]
        login = request.form["login"]
        password = request.form["password"]
        if login == "" or name == "" or password == "":
            errors["empty_field"] = True
            return render_template("registration.html", errors=errors)
        if checkLogin(login):
            errors["busy_login"] = True
            return render_template("registration.html", errors=errors)
        if len(password) < 8:
            errors["short_password"] = True
            return render_template("registration.html", errors=errors)
        registr(name, login, password)
        return redirect("/login")

def registr(name, login, password):
    cursor.execute("INSERT INTO servise.users (full_name, login, password) VALUES (%s, %s, %s)",
                    (str(name), str(login), str(password)))
    conn.commit()

def auth(login, password):
    cursor.execute("SELECT * FROM servise.users WHERE login=%s AND password=%s", (str(login), str(password)))
    records = list(cursor.fetchall())
    return records

def checkLogin(login):
    cursor.execute("SELECT * FROM servise.users WHERE login='%s'" % (str(login)))
    records = list(cursor.fetchall())
    if records:
        loginInDB = True
    else:
        loginInDB = False
    return loginInDB

