from utils.db import db


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.DECIMAL(4))
    description = db.Column(db.String(200))

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
