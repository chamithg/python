from dataclasses import dataclass
from flask_app import app
from flask_app.models.author import Author
from flask import render_template,request,redirect
from flask_app.models.book import Book

@app.route("/")
def Landing():
    books = Book.get_all()
    return render_template("add_book.html", books= books)

@app.route("/books")
def all_books():
    books = Book.get_all()
    return render_template("add_book.html", books= books)

@app.route("/add_book", methods=["POST"])
def add_book():
    data ={"title": request.form["title"],"num_of_pages": request.form["num_of_pages"]}
    books = Book.add_book(data)
    return redirect("/books")

@app.route("/book/<int:id>")
def show_book(id):
    data ={"id":id}
    book = Book.show_book(data) 
    print(book)  
    return render_template("books_favo_authors.html", book=book)

@app.route("/book/<int:id>/join_authors" , methods=["POST"])
def add_author2book(id):
    data ={"book_id":id,"author_id": request.form["author_id"]}
    Author.add_book2author(data) 
    return redirect("/book/"+str(id))


