from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Recipe:
    def __init__(self,data):
        self.id = data['id']   
        self.name= data['name']
        self.description= data['description']
        self.instructions= data['instructions']
        self.date= data['date']
        self.under_thirty= data['under_thirty']
        self.user_id= data['user_id']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']
            
    @classmethod
    def add_recipe(cls,data):
        query = "INSERT INTO recipes(name, user_id, description, instructions, date, under_thirty) VALUES (%(name)s,%(user_id)s,%(description)s,%(instructions)s,%(date)s,%(under_thirty)s );"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        return results
    
    @classmethod
    def update_recipe(cls,data):
        query = "UPDATE recipes SET name =%(name)s , description = %(description)s, instructions=%(instructions)s, date=%(date)s, under_thirty=%(under_thirty)s  WHERE id = %(recipe_id)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        return results
    
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes =[]
        if results:
            for recipe in results:
                recipes.append(cls(recipe))
                
        return recipes
    
    @classmethod
    def get_one_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(recipe_id)s;"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        recipes =[]
        if results:
            for recipe in results:
                recipes.append(cls(recipe))
                return recipes[0]
    
    @classmethod
    def delete_one_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(recipe_id)s;"
        return connectToMySQL('recipes_schema').query_db(query,data)   
        
    
    
    @staticmethod
    def validation(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("name must be at least 3 characters.")
            is_valid = False
        if len(data['description']) < 3:
            flash("description must be at least 3 characters.")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("instructions must be at least 3 characters.")
            is_valid = False
        if (data['date']==""):
            flash("Date cant be empty.")
            is_valid = False
        print(data['date'])
        return is_valid
    
    