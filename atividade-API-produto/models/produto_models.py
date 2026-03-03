from db import db

class Produto(db.Model):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_Key=True)
    nome = db.Column(db.String(80), nullable=False)
    categoria = db.Column(db.String(80), nullable=False)