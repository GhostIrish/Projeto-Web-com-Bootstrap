from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes

    - /clientes/ (GET) - Listar clientes OK
    - /clientes/ (POST) - Inserir o cliente no servidor OK
    - /clientes/new (GET) - Renderizar um formulario para criar um cliente OK
    - /clientes/<id> (GET) - Obter um cliente pelo id OK
    - /clientes/<id>/edit (GET) - Renderiza um formulario para editar um cliente OK
    - /clientes/<id>/update (PUT) - Atualizar os dados do cliente OK
    - /clientes/<id>/delete (DELETE) - Deleta o registro do usuário OK
    
"""

@cliente_route.route('/', methods=['GET'])
def lista_clientes():
    '''Lista os clientes, é a pagina principal'''
    return render_template('lista_clientes.html')
@cliente_route.route('/', methods=['POST'])
def insere_cliente():
    '''Método que vai realizar a inserção do cliente na database'''
    pass

@cliente_route.route('/new')
def form_novo_cliente():
    '''formulario para cadastro de cliente'''
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>', methods=['GET']) # obtem o id do cliente dinasmicamente
def obter_clientes(cliente_id):
    '''exibe detalhes do cliente buscando pelo id'''
    pass

@cliente_route.route('/editar/<int:cliente_id>/edit')
def form_editar_cliente(cliente_id):
    '''renderiza o formulario para edição do cliente desejado'''
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    '''Método que vai inserir essa atualização feita no formulário'''
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    '''Deleta o cliente desejado'''
    pass