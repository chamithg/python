from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route("/")
def index():
    return render_template("login.html")

