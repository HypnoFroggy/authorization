import requests
from flask import Flask, render_template, request
# import psycopg2

app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")
