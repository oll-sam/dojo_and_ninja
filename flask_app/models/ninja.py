from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self,data):
        self.idNinjas = data["idNinjas"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojos1_iddojo = data["dojos1_iddojo"]

    @classmethod
    def insert_ninja(cls, data):
        query = "INSERT INTO ninjas1 (first_name, last_name, age, dojos1_iddojo) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos1_iddojo)s)"
        return connectToMySQL ("mydb").query_db(query,data)