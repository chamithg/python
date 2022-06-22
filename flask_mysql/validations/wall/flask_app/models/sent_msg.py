from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class Sent_msg:
    def __init__(self,data):
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.email= data['email']
            
    @classmethod
    def new_msg_sent(cls,data):
        print("Msg sent")
        query = "INSERT INTO sent_msgs(sent_msg, user_id, sender_name) VALUES (%(sent_msg)s,%(receiver_id)s,%(sender)s);"
        results = connectToMySQL('wall_schema').query_db(query,data)
        return results
    
    @classmethod
    def all_sent_msgs_count(cls,data):
        query = "SELECT COUNT(sent_msg) FROM sent_msgs LEFT JOIN users ON users.id = sent_msgs.user_id WHERE sender_name = %(logged_user_name)s;"
        results = connectToMySQL('wall_schema').query_db(query,data)
        
        return results[0]["COUNT(sent_msg)"]
    
    @staticmethod
    def validation(data):
        is_valid = True
        
        if len(data["sent_msg"]) < 1:
            flash("Message content is empty.")
            is_valid = False
        
        return is_valid
        
    
    
    
    
    # SELECT * FROM sent_msgs LEFT JOIN users ON users.id = sent_msgs.users_id;