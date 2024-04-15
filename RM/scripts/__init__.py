from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '985a506435c91cd3638040d6c0026c28'

import routes