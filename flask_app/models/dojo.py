from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:

    def __init__(self,data):
        self.iddojos = data["iddojos"]
        self.location = data["location"]
        self.created_at = data["created_at"]
        self.updates_at = data["updates_at"]
        self.ninjas = []

    @classmethod
    def insert_dojo(cls,data):
        query = "INSERT INTO dojos1 (location, created_at, updates_at) VALUES (%(location)s, NOW(), NOW())"
        return connectToMySQL ("mydb").query_db(query,data)
    
    @classmethod
    def select_all(cls):
        query ="SELECT * FROM dojos1 ORDER BY iddojos DESC"
        mydb = connectToMySQL ("mydb").query_db(query)
        dojos = []

        for d in mydb:
            dojos.append(cls(d))
        
        return dojos

    @classmethod
    def get_dojos_ninjas(cls, data):
        query = "SELECT * FROM dojos1 LEFT JOIN ninjas1 ON dojos1.iddojos = ninjas1.dojos1_iddojo WHERE iddojos = %(iddojos)s"
        dojo_ninja = connectToMySQL ("mydb").query_db(query,data)

        dojo = Dojo(dojo_ninja[0])

        for ninj in dojo_ninja:

            ninja_data = {
                "idNinjas" : ninj["idNinjas"],
                "first_name" : ninj["first_name"],
                "last_name" : ninj["last_name"],
                "age" : ninj["age"],
                "created_at" : ninj["created_at"],
                "updated_at" : ninj["updates_at"],
                "dojos1_iddojo" : ninj["dojos1_iddojo"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))

        return dojo
