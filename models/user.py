from utils.db import db
from werkzeug.security import check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.DECIMAL(20))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))

    def __init__(self, name, lastname, email, phone, username, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    def check_password(self, password):
        return check_password_hash(self.password, password)
