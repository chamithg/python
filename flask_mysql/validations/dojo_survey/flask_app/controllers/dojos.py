from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods =["POST"])
def index1():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    
    data = {
        "name": request.form["name"],
        "location" : request.form["location"],
        "language" : request.form["language"],
        "comment" : request.form["comment"]
    }
    Dojo.save(data)
    return redirect("/output")

@app.route("/output")
def output():
    dojo = Dojo.get_all()
    return render_template("result.html", dojo = dojo)

@app.route("/go_back")
def go_back():
    return redirect("/")