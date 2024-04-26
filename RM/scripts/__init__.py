from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '985a506435c91cd3638040d6c0026c28'

# Banco de dados
    # Se estiver Online (deploy pelo render)
if os.getenv("DEBUG") == 0:
    link_sql = os.getenv("DATABASE_URL")

    # Se estiver Local (para modificações)
else:
    link_sql = 'sqlite:///RM.db'

    # Setando link do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = link_sql

    # Base de dados
database = SQLAlchemy(app)

# Upload de produtos
app.config['UPLOAD_FOLDER'] = 'static/upload_img'

# # Login
# login_gerenciador = LoginManager(app)
# login_gerenciador.login_view = 'home'

import routes