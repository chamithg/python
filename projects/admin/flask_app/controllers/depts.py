from crypt import methods
from flask_app import app
from flask_app.models.item import Item
from flask_app.models.dept import Dept
from flask import render_template,request,redirect,session
from flask import flash


@app.route("/inventory/<int:dept_id>")
def display_depts(dept_id):
    data = {"dept_id": dept_id}
    items = Dept.get_totals(data)
    return render_template("inventory.html", items = items) 

