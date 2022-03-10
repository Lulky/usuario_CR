from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        #[
        #  {"nombre":"luciano", "edad":"29"}
        #  {"nombre":"luciano", "edad":"29"}
        #   {"nombre":"luciano", "edad":"29"}
        #   {"nombre":"luciano", "edad":"29"}
        # ]
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def guardar(cls, data):
        #data = {"first_name":"c" "last_name": "x", "email": "y"}
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        result = connectToMySQL('esquema_usuarios').query_db(query, data)
        return result