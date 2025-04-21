from flask_login import UserMixin

# Simulación de base de datos en memoria
users_db = {
    'admin': {'password': '1234'},
    'usuario': {'password': 'abcd'}
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

    def get_id(self):
        return self.id

def get_user(username):
    if username in users_db:
        return User(username)
    return None

def validate_user(username, password):
    user = users_db.get(username)
    return user and user['password'] == password
