# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.full_name = data['first_name'] + " "+  data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_db').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results: 
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls,data):
        print(data)
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s,%(lname)s,%(email)s)"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_db').query_db(query, data)
        return results
        
    @classmethod
    def get_one(cls,data):
        print(data)
        query = "SELECT * FROM users WHERE id = %(id)s;"
        
        results = connectToMySQL('users_db').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def select_update(cls,data):
        print(data)
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_db').query_db(query,data)
        return cls(results[0])
        
    @classmethod
    def update(cls,data):
        print(data)    
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email =%(email)s WHERE id = %(id)s;"
        results = connectToMySQL('users_db').query_db(query,data)
        
    @classmethod
    def delete(cls,data):
        print(data)    
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_db').query_db(query,data)