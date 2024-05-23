from __init__ import database, app
from models import Produtos, Clientes, Alugueis

# Criar banco de dados
with app.app_context():
    database.create_all()