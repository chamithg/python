from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.email import Email

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods =["POST"])
def index1():
    if not Email.validate_email(request.form):
        return redirect('/')
    
    data = {
        "email_address": request.form["email_address"]
    }
    print(request.form["email_address"])
    Email.save(data)
    return redirect("/output")

@app.route("/output")
def output():
    emails = Email.get_all()
    print (emails)
    return render_template("result.html", emails = emails)

@app.route("/go_back")
def go_back():
    return redirect("/")