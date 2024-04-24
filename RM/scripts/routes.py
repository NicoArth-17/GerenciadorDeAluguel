from __init__ import app, database
from flask import render_template, url_for, redirect
from forms import FormCadastroCliente, FormAdcProduto
from models import Clientes, Produtos
from werkzeug.utils import secure_filename
import os

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/AdcProduto')
def adcproduto():

    form_AdcProduto = FormAdcProduto()

    # Verificando envio do formulário de produto
    if form_AdcProduto.validate_on_submit():

        # Criando um nome seguro para o arquivo
        arquivo = form_AdcProduto.imagem.data
        nome_arquivo_seguro = secure_filename(arquivo.filename)

        # Direcionando local de salvamento
        caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            app.config['UPLOAD_FOLDER'],
                            nome_arquivo_seguro)
        
        # Salvando arquivo
        arquivo.save(caminho)

        # Registrando nome do arquivo no banco de dados
        img = Produtos(imagem=nome_arquivo_seguro, id_cliente=Clientes.id)
        database.session.add(img)
        database.session.commit()

    return render_template('adcproduto.html', form=form_AdcProduto)

@app.route('/produtos/masculino', methods=['GET', 'POST'])
def masculino():
    return render_template('masculino.html')

@app.route('/CadastrarClientes')
def CadastrarClientes():

    form_CadCliente = FormCadastroCliente()

    return render_template('cadastrarclientes.html', form=form_CadCliente)

app.route('/calendario')
def calendario():
    return render_template('calendario.html')

app.route('/caixa')
def caixa():
    return render_template('caixa.html')