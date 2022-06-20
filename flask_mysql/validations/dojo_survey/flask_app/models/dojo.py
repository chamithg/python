from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self,data):
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment'] 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results: 
            dojos.append( cls(dojo) )
            
        dojo = dojos[len(dojos)-1]
        return dojo
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s)"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results
    
    @staticmethod
    def validate_dojo(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if data["location"] == "":
            flash("A location has to be selected.")
            is_valid = False
        if data["language"] == "":
            flash("A language has to be selected.")
            is_valid = False
        if len(data['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid