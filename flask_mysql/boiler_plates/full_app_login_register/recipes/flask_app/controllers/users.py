from crypt import methods
from dataclasses import dataclass
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

#!register method
@app.route("/register", methods =["POST"])
def register():
    if not User.validation(request.form):
        return redirect("/")
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "email": request.form["email"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "pw_hash": pw_hash,
    }    
    User.register_user(data)
    logged_user = User.get_one_user(data)
    session['last_name'] = logged_user.last_name
    session['first_name'] = logged_user.first_name
    session['email'] = logged_user.email
    session['pw_hash'] = logged_user.pw_hash
    session['id'] = logged_user.id
    
    return redirect("/dashboard")


#!login method
@app.route("/login", methods =["POST"])
def login():
    data ={"email" :request.form['email']}
    logged_user = User.get_one_user(data)
    if not logged_user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if bcrypt.check_password_hash(logged_user.pw_hash, request.form["password"]):
        session['last_name'] = logged_user.last_name
        session['first_name'] = logged_user.first_name
        session['email'] = logged_user.email
        session['pw_hash'] = logged_user.pw_hash
        session['id'] = logged_user.id
    else:
        flash("Wrong Password.")
        return redirect("/")
    return redirect("/dashboard")

#!dashboard display method   
@app.route("/dashboard")
def dashboard():
    if 'id' not in session:
        flash("No any logged in users")
        return redirect('/')
    return render_template("dashboard.html")

#!logout method
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

