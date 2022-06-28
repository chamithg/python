from crypt import methods
from flask_app import app
from flask_app.models.item import Item
from flask_app.models.dept import Dept
from flask_app.models.category import Category
from flask_app.models.whole_store import Whole_store
from flask import render_template,request,redirect,session
from flask import flash


# @app.route("/inventory")
# def display_whole_store():
#     items = Whole_store.get_totals()
#     return render_template("inventory.html", items = items) 

@app.route("/dashbord")
def whole_store_get_totals():
    totals = Whole_store.get_totals()
    return render_template("dashboard.html", totals = totals) 
