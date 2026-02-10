from db import db

class carro(db.Model):
    _tablename_ = 'carros'

    id = db.Column(db.integer, primary_key=True)
    modelo = db.Column(db.Sring(80), nullable=False)
    marca = db.Column(db.string(80), nullable=False)
    ano = db.column(db.Integer, nullable=False)
    

    def json(self):
        return{
            'id':self.id,
            'modelo':self.modelo,
            'marca':self.marca,
            'ano':self.ano,
        }