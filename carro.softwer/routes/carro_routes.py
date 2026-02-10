from flask import blueprints, request

from controllers.carro_controllers import create_carro

create_carro = blueprints('carro_routes',__name__)

@carro_routes.route('/carro',methods=['POST'])
def carros_post():
    carro_data =request.json
    return create_carro(request.json)