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
    telefone = database.Column(database.String, nullable=False)
    endereco = database.Column(database.Text, nullable=False)
    cidade = database.Column(database.String, nullable=False)
    uf = database.Column(database.String, nullable=False) #multipla escolha
    cep = database.Column(database.String, nullable=False)
    cpf = database.Column(database.String, nullable=False)
    c_aluguel = database.relationship('Alugueis', backref='clientes', lazy=True)
    

# Tabela de produtos adicionados
class Produtos(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default='default.png')
    tipo = database.Column(database.String, nullable=False) # multipla escolha
    tamanho = database.Column(database.String, nullable=False) #multipla escolha
    nome = database.Column(database.String, nullable=False, unique=True)
    valor = database.Column(database.String, nullable=False)
    descricao = database.Column(database.Text, nullable=False)
    p_aluguel = database.relationship('Alugueis', backref='produtos', lazy=True)
    

# Tabela de aluguéis
class Alugueis(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    locacao = database.Column(database.String, nullable=False)
    devolucao = database.Column(database.String, nullable=False)
    id_cliente = database.Column(database.Integer, database.ForeignKey('clientes.id'), nullable=False)
    id_produto = database.Column(database.Integer, database.ForeignKey('produtos.id'), nullable=False)
    
    