from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Book
# model the class after the friend table from our database
class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.full_name = data['first_name'] + " "+  data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []
        self.un_favorite_books = []

    @classmethod
    def all_authors(cls):
        query = "SELECT * FROM authors;"        
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for author in results: 
            authors.append( cls(author) )
        return authors
    
    @classmethod
    def add_author(cls,data):
        query = "INSERT INTO authors (first_name,last_name) VALUES (%(first_name)s,%(last_name)s)"        
        results = connectToMySQL('books_schema').query_db(query,data)
        return results
    
    @classmethod
    def show_author(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s"        
        results = connectToMySQL('books_schema').query_db(query,data)
        all_books = Book.get_all()
        author = cls(results[0])
        for row in results:
            if row['books.id'] == None:
                break
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(Book(data))
        favourite_id_list = []
        for book in author.favorite_books:
            favourite_id_list.append(book.id)
            
        for book in all_books:
            if book.id not in favourite_id_list:
                author.un_favorite_books.append(book)
    
        # print(book.title for book in author.favorite_books)
        
        
        return author
    
    
    @classmethod
    def add_book2author(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s)"        
        results = connectToMySQL('books_schema').query_db(query,data)
        return results
    
    
    