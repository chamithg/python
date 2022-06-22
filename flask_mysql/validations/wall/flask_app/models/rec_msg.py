from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re



class Rec_msg:
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
    
    @classmethod
    def all_rec_msgs(cls,data):
        query = "SELECT * FROM rec_msgs LEFT JOIN users ON users.id = rec_msgs.user_id WHERE email = %(logged_user)s;"
        results = connectToMySQL('wall_schema').query_db(query,data)        
        rec_msgs=[]
        
        if results:
            for msg in results:
                rec_msgs.append(cls(msg))
        
        return rec_msgs
        
    @classmethod
    
    def delete(cls,data):
        query = "DELETE FROM rec_msgs WHERE id = %(msg_id)s;"
        return connectToMySQL('wall_schema').query_db(query,data)
        