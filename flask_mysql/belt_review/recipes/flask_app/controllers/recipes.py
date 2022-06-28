from flask_app import app
from flask import render_template,request,redirect,session
from flask_app.models.recipe import Recipe
from flask import flash

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/add_recipe", methods = ["POST"])
def add_recipe():
    if 'id' not in session:
        flash("Need to log in to add recipes")
        return redirect('/')
    if not Recipe.validation(request.form):
        return redirect("/create")
    print(request.form["under_thirty"])
    
    if request.form["under_thirty"] =="yes":
        under_thirty= 1
    else:
        under_thirty = 0
    
    data ={
        "name":request.form["name"],
        "date":request.form["date"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under_thirty":under_thirty,
        "user_id":session["id"],
    }
    
    print(request.form["under_thirty"])
    Recipe.add_recipe(data)
    return render_template("create.html")

@app.route("/view/<int:recipe_id>")
def view(recipe_id):
    data ={"recipe_id": recipe_id}
    recipe = Recipe.get_one_recipe(data)
    return render_template("recipe.html", recipe = recipe)

@app.route("/delete/<int:recipe_id>/<int:creator_id>")
def delete(recipe_id, creator_id):
    if creator_id != session["id"]:
        flash("Hey! you cant delete others recipes")
        return redirect('/')
    data ={"recipe_id": recipe_id}
    Recipe.delete_one_recipe(data)
    return redirect("/dashboard")


@app.route("/edit/<int:recipe_id>/<int:creator_id>")
def edit(recipe_id, creator_id):
    if creator_id != session["id"]:
        flash("Hey! you cant edit others recipes")
        return redirect('/')
    data ={"recipe_id": recipe_id}
    recipe = Recipe.get_one_recipe(data)
    return render_template("edit.html", recipe= recipe)


@app.route("/update/<int:recipe_id>/<int:creator_id>", methods = ["POST"])
def update(recipe_id, creator_id):
    if creator_id != session["id"]:
        flash("Hey! you cant edit others recipes")
        return redirect('/')
    if not Recipe.validation(request.form):
        return redirect("/create")
    
    if request.form["under_thirty"] =="yes":
        under_thirty= 1
    else:
        under_thirty = 0
    
    data ={
        "name":request.form["name"],
        "date":request.form["date"],
        "description":request.form["description"],
        "instructions":request.form["instructions"],
        "under_thirty":under_thirty,
        "recipe_id":recipe_id
    }
    
    Recipe.update_recipe(data)
    return redirect("/dashboard")