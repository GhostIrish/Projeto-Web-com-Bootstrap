from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes

    - /clientes/ (GET) - Listar clientes OK
    - /clientes/ (POST) - Inserir o cliente no servidor OK
    - /clientes/new (GET) - Renderizar um formulario para criar um cliente OK
    - /clientes/<id> (GET) - Obter um cliente pelo id OK
    - /clientes/<id>/edit (GET) - Renderiza um formulario para editar um cliente OK
    - /clientes/<id>/update (PUT) - Atualizar os dados do cliente 
    - /clientes/<id>/delete (DELETE) - Deleta o registro do usuário
    
"""

@cliente_route.route('/', method='GET')
def lista_clientes():
    pass

@cliente_route.route('/', method='POST')
def insere_cliente():
    pass

@cliente_route.route('/novo_cliente', method='GET')
def formulario_novo_cliente():
    pass

@cliente_route.route('/<int:cliente_id>', method='GET') # obtem o id do cliente dinasmicamente
def obter_clientes(cliente_id):
    pass

@cliente_route.route('/editar/<int:cliente_id>')
def formulario_editar_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>', method='PUT')
def atualizar_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>', method='DELETE')
def deletar_cliente(cliente_id):
    pass