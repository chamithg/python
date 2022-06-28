from crypt import methods
from flask_app import app
from flask_app.models.item import Item
from flask import render_template,request,redirect,session
from flask import flash

@app.route("/")
def index1():
    return render_template("login.html")


@app.route("/inventory")
def inventory():
    items = Item.get_all_items()
    return render_template("inventory.html", items = items) 

@app.route("/add_sales/<int:id>")
def add_sales(id):
    data ={"id":id}
    item = Item.get_single_item(data)
    return render_template("add_sales.html", item = item) 

@app.route("/edit_sales", methods =["POST"])
def edit_sales():
    data ={"inv_id":request.form["inv_id"],
        "prev_week_sale":request.form["prev_week_sale"],
        "prev_week_target":request.form["prev_week_target"],
        "prev_week_shrink":request.form["prev_week_shrink"],
        "prev_week_shrink_target":request.form["prev_week_shrink_target"],
        "nxt_week_sale_proj":request.form["nxt_week_sale_proj"],
        "nxt_week_target":request.form["nxt_week_target"],
        "nxt_week_shrink_proj":request.form["nxt_week_shrink_proj"],
        "nxt_week_shrink_target":request.form["nxt_week_shrink_target"],
        
        
    }
    Item.edit_sales(request.form)
    return redirect ("/inventory") 
