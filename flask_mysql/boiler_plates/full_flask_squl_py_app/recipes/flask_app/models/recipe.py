from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Recipe:
    def __init__(self,data):
        self.first_name= data['first_name']
        self.sender= data['sender']
        self.rec_msg= data['rec_msg']
        self.id = data['id']   
        
        
    @classmethod
    def new_msg_rec(cls,data):
        query = "INSERT INTO rec_msgs(rec_msg, user_id, sender) VALUES (%(sent_msg)s,%(receiver_id)s,%(sender)s);"
        results = connectToMySQL('wall_schema').query_db(query,data)
        return results