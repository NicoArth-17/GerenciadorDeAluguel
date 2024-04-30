from __init__ import database
from flask_login import UserMixin

# Decorator e function obrigatórios para utilizar LoginManager()
# @login_gerenciador.user_loader
# def load_user(id_user):
#     return Usuario.query.get(int(id_user))


# Tabela de clientes cadastrados
class Clientes(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    telefone = database.Column(database.Integer)
    endereco = database.Column(database.Text, nullable=False)
    cidade = database.Column(database.String, nullable=False)
    uf = database.Column(database.String, nullable=False) #multipla escolha
    cep = database.Column(database.Integer)
    cpf = database.Column(database.Integer)

# Tabela de produtos adicionados
class Produtos(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default='default.png')
    tipo = database.Column(database.String, nullable=False) # multipla escolha
    tamanho = database.Column(database.String, nullable=False) #multipla escolha
    nome = database.Column(database.String, nullable=False, unique=True)
    valor = database.Column(database.Float)
    descricao = database.Column(database.Text, nullable=False)
