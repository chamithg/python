from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.ninja import Ninja



@app.route("/dojo/<dojo_name>/<int:id>")
def dojo_ninjas(id, dojo_name):
    data={"id":id}
    ninjas = Ninja.get_ninjas(data)
    print(ninjas)
    return render_template("dojo_ninjas.html", ninjas = ninjas, dojo_name = dojo_name)



@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    data ={"first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "age": request.form["age"],
            "dojo_id": request.form["dojo_id"],}
    Ninja.create_ninja(data)
    return redirect("/dojos")
