from dataclasses import dataclass
from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.dojo import Dojo

@app.route("/")
def Landing():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", dojos = dojos)

@app.route("/dojos")
def index():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", dojos = dojos)

@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    data ={"name": request.form["name"]}
    dojos = Dojo.create_dojo(data)
    print(dojos)
    return redirect("/dojos")

@app.route("/add_ninja")
def add_ninjas():
    dojos = Dojo.get_all()
    return render_template("add_ninja.html", dojos = dojos)
