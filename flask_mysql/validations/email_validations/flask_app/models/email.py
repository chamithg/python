from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Email:
    def __init__(self,data):
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('email_schema').query_db(query)
        # Create an empty list to append our instances of friends
        emails = []
        
        # Iterate over the db results and create instances of friends with cls.
        for email in results: 
            emails.append( cls(email) )
        return emails
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email_address) VALUES (%(email_address)s);"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('email_schema').query_db(query, data)
        return results
    
    @staticmethod
    def validate_email(data):
        is_valid = True
        if not EMAIL_REGEX.match(data['email_address']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid