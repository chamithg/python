from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.full_name = data['first_name'] + " "+  data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"        
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results: 
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def get_ninjas(cls,data):
        query = "SELECT * FROM dojos_and_ninjas_schema.dojos JOIN ninjas ON dojo_id = dojos.id Where dojo_id = %(id)s;"        
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        ninjas = []
        for ninja in results: 
            ninjas.append( cls(ninja) )
        return ninjas
    
    @classmethod
    def create_ninja(cls,data):
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"        
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return results
    
    
    
    