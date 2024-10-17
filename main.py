from flask import Flask, url_for, render_template

# url_for serve para montar url internas do nosso servidor web, de acordo com o nome da nossa func
app = Flask(__name__)

@app.route('/')
def ola_mundo():
    titulo = 'Gestão de Usuários'
    usuarios = [
        {'nome': 'Guilherme', 'membro_ativo': True},
        {'nome': 'pedro', 'membro_ativo': False},
        {'nome': 'ana', 'membro_ativo': False},
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)
    # o render template é utilizado para carregarmos o html e utilizarmos python com html
    # retornamos titulo=titulo e usuarios=usuarios, pois vou utilizar ambas as variáveis no intex.html.
    
#     return f'''Hello, World, tamo junto!
# <a href='{ url_for('ve_ai') }'>Segunda página</a>
# ''' # isso faz com que o texto 'segunda pagina' vire um link que te redirecione para a pagina dois.

@app.route('/ve_ai')
def ve_ai():
    return 'Essa aqui é a pagina dois'


app.run(debug=True)