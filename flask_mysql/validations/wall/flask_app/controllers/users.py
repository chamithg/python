from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.sent_msg import Sent_msg
from flask_app.models.user import User
from flask_app.models.rec_msg import Rec_msg
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
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "email": request.form["email"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "pw_hash": pw_hash,
    }
    
    User.register(data)
    session['first_name'] = request.form['first_name']
    session['email'] = request.form['email']
    session['pw_hash'] = pw_hash

    return redirect("/output")

@app.route("/login", methods =["POST"])
def login():
    if not User.validate_login(request.form):
        return redirect('/')
    data ={ "logged_user":request.form["email"]}
    user = User.get_one(data)
    if bcrypt.check_password_hash(user.pw_hash, request.form["password"]):
        session['first_name'] = user.first_name
        session['email'] = user.email
        session['pw_hash'] = user.pw_hash
        session['id']= user.id
    else:
        flash("Wrong Password.")
        return redirect("/")
    
    return redirect("/output")


@app.route("/output")
def output():
    data ={ "logged_user":session["email"],"logged_user_name":session["first_name"]}
    logged_user = User.get_one(data)
    msgs_to_display = Rec_msg.all_rec_msgs(data)
    sent_msg_count = Sent_msg.all_sent_msgs_count(data)
    rec_msg_count = len(msgs_to_display)
    users = User.get_all()
    return render_template("wall.html", logged_user = logged_user,
                        users = users,
                        sent_msg_count= sent_msg_count,
                        msgs_to_display = msgs_to_display,
                        rec_msg_count=rec_msg_count)

@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/")