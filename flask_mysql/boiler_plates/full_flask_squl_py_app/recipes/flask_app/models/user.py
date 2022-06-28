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
        
        
 
    # @classmethod
    # def get_one(cls,data):
    #     query = "SELECT * FROM users WHERE email =%(logged_user)s ;"
    #     results = connectToMySQL('wall_schema').query_db(query,data)
    #     users =[]
    #     for user in results:
    #         users.append(cls(user))
    #     return users[0]
    