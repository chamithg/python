from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import models

# model the class after the friend table from our database
class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_authors = []
        self.un_favorite_authors = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"        
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for book in results: 
            books.append( cls(book) )
        return books

    @classmethod
    def add_book(cls,data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s)"
        results = connectToMySQL('books_schema').query_db(query, data)
        return results
        
    @classmethod
    def show_book(cls,data):
        query = "SELECT * FROM books_schema.books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s"        
        results = connectToMySQL('books_schema').query_db(query,data)
        print(results)
        all_authors = models.author.Author.all_authors()
        book = cls(results[0])
        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "full_name":str(row['first_name'])+ str(row['last_name']),
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.favorite_authors.append(models.author.Author(data))
        favourite_id_list = []
        for author in book.favorite_authors:
            favourite_id_list.append(author.id)
            
        for author in all_authors:
            if author.id not in favourite_id_list:
                book.un_favorite_authors.append(author)
        
        return book
        #  query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"