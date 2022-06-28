from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self,data):
        self.id= data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.email= data['email']
        self.pw_hash= data['pw_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #!---> reg user (login/reg)
    @classmethod
    def register_user(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,pw_hash) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(pw_hash)s);"
        return connectToMySQL('recipes_schema').query_db(query,data)
    
    #!---> geting single user (login/reg)
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE email =%(email)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        users =[]
        if results:
            for user in results:
                users.append(cls(user))
                return users[0] 

    #!---> validation
    @staticmethod
    def validation(data):
        
        query = "SELECT email FROM users;"
        results = connectToMySQL('recipes_schema').query_db(query)
        all_emails = []
        if results:
            for email in results:
                all_emails.append(email["email"])
        
        is_valid = True
        
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
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