from utils.db import db


class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_ganado = db.Column(db.DECIMAL(10))
    created_at = db.Column(db.date)

    def __init__(self, id, total_ganado, created_at):
        self.id = id
        self.total_ganado = total_ganado
        self.created_at = created_at
