from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(), unique=True)
    telefone = db.Column(db.Integer())
    endereco = db.Column(db.String(255))

    def __init__(self, id, nome, telefone, endereco):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def __repr__(self):
        return '<User %r>' % self.nome
