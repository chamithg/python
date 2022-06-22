from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.user import User
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app) 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods =["POST"])
def register():
    if not User.validate_input(request.form):
        return redirect('/')
    pwhash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "email": request.form["email"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "pwhash": pwhash,
    }
    
    User.register(data)
    session['first_name'] = request.form['first_name']
    session['email'] = request.form['email']
    session['pwhash'] = pwhash

    return redirect("/output")

@app.route("/login", methods =["POST"])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    data ={ "logged_user":request.form["email"]}
    user = User.get_one(data)
    if bcrypt.check_password_hash(user.pwhash, request.form["password"]):
        session['first_name'] = user.first_name
        session['email'] = user.email
        session['pwhash'] = user.pwhash
    else:
        flash("Wrong Password.")
    
    return redirect("/output")


@app.route("/output")
def output():
    data ={ "logged_user":session["email"]}
    user = User.get_one(data)
    return render_template("result.html", user = user)

@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/")