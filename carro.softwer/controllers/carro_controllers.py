from models.carro_models import Carro
from db import db
import json
from flask import make_response

def create_carro(carro_date):
    novo_carro = Carro(
        modelo=carro_date['modelo'],
        marca=carro_date['marca'],
        ano=carro_date['ano']
    )
    db.session.add(novo_carro)
    db.session.commit()
    response=make_response(
        json.dumps({
            'mensagem':'Carro cadastrado como sucesso',
            'Carro':novo_carro.json()
        }, sart_keys=False)
    )
    response.headers['content-type'] = 'application/json'
    return response