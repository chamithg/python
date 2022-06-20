from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.author import Author




@app.route("/authors")
def all_authors():
    authors = Author.all_authors()
    return render_template("add_author.html", authors = authors)



@app.route("/add_author", methods=["POST"])
def add_author():
    data ={"first_name": request.form["first_name"],
            "last_name": request.form["last_name"]}
    Author.add_author(data)
    return redirect("/authors")

@app.route("/author/<int:id>")
def show_author(id):
    data ={"id":id}
    author = Author.show_author(data)   
    return render_template("authors_favo_books.html", author = author)

@app.route("/author/<int:id>/join_books" , methods=["POST"])
def add_book2author(id):
    data ={"author_id":id,"book_id": request.form["book_id"]}
    Author.add_book2author(data) 
    return redirect("/author/"+str(id))
