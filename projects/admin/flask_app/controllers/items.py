from crypt import methods
from flask_app import app
from flask_app.models.item import Item
from flask_app.models.dept import Dept
from flask_app.models.all_dept import All_dept
from flask_app.models.category import Category
from flask_app.models.all_cat import All_cat
from flask import render_template,request,redirect,session
from flask import flash

@app.route("/")
def index1():
    return render_template("login.html")


@app.route("/inventory")
def inventory():
    items = Item.get_all_items()
    depts = All_dept.all_depts()
    return render_template("inventory.html", items = items, depts=depts) 

@app.route("/inventory/dept/<int:id>")
def inventory_dept(id):
    items = Item.get_all_items_dept({"dept_id":id})
    depts = All_dept.one_dept({"dept_id":id})
    cats = All_cat.all_cats({"dept_id":id})
    return render_template("inventory.html", items = items, depts=depts,cats = cats, dept_id = id)

@app.route("/inventory/dept/<int:dept_id>/<int:id>")
def inventory_cat(dept_id,id):
    items = Item.get_all_items_cat({"cat_id":id})
    depts = All_dept.one_dept({"dept_id":dept_id})
    cats = All_cat.one_cat({"cat_id":id})
    return render_template("inventory.html", items = items, depts=depts,cats = cats, cat_id = id, dept_id = dept_id ) 

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

@app.route("/mark_item/<int:id>")
def mark_item(id):
    data={"id":id, "flag_code": session["flag_code"]}
    Item.mark_item(data)
    return redirect(request.referrer)
    
    
@app.route("/unmark_item/<int:id>")
def unmark_item(id):
    data={"id":id }
    Item.unmark_item(data)
    return redirect(request.referrer)
    
    