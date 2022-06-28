from flask_app import app
from flask import render_template,request,redirect,session
from flask import flash

@app.route("/")
def index1():
    return render_template("login.html")
