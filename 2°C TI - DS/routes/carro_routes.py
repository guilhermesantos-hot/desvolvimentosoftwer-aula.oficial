from flask import Blueprint, request                  # DE flask IMPORTAR Blueprint e request:
                                                      # - Blueprint: usado para organizar as rotas do Flask em módulos separados
                                                      # - request: objeto que contém os dados enviados na requisição HTTP

from controllers.carro_controllers import create_carro # DE controllers.carro_controllers IMPORTAR create_carro:
                                                      # função que cria um novo carro no banco (controller)

carro_routes = Blueprint('carro_routes', __name__)    # Cria um Blueprint chamado "carro_routes" (identificador),
                                                      # associado ao módulo atual (__name__), para registrar rotas do carro

@carro_routes.route('/Carro', methods=['POST'])       # Define a rota "/Carro" que aceita apenas requisições HTTP POST
def carros_post():                                    # Função que será executada quando houver POST em "/Carro"
    carro_data = request.json                         # Lê o corpo da requisição no formato JSON e armazena em carro_data
    return create_carro(request.json)                 # Chama a função create_carro (controller) passando os dados recebidos
