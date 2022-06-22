from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self,data):
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.email= data['email']
        self.pw_hash= data['pw_hash']
        self.id= data['id']
        
        
 
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE email =%(logged_user)s ;"
        results = connectToMySQL('wall_schema').query_db(query,data)
        users =[]
        for user in results:
            users.append(cls(user))
        return users[0]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('wall_schema').query_db(query)
        users =[]
        for user in results:
            users.append(cls(user))
        return users
    
    
    @classmethod
    def register(cls,data):
        query = "INSERT INTO users (first_name, last_name, email,pw_hash) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(pw_hash)s);"
        results = connectToMySQL('wall_schema').query_db(query, data)
        return results
    
    
    @staticmethod
    def validate_login(data):
        
        query = "SELECT email FROM users;"
        results = connectToMySQL('wall_schema').query_db(query)
        all_emails = []
        for email in results:
            all_emails.append(email["email"])
        is_valid = True
        if data["email"] not in all_emails:
            flash("User did not found")
            is_valid = False 
        return is_valid 
            
    
    
    @staticmethod
    def validate_input(data):
        
        query = "SELECT email FROM users;"
        results = connectToMySQL('wall_schema').query_db(query)
        all_emails = []
        for email in results:
            all_emails.append(email["email"])
        is_valid = True
        
        if len(data['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if data["email"] in all_emails:
            flash("Email already registered!")
            is_valid = False  
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if (data['confirm_password'])!= (data['password']) :
            flash("Passwords do not match.")
            is_valid = False
        
        return is_valid