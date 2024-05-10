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



@app.route('/AdcProduto', methods=['GET', 'POST'])
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
        # img = Produtos(imagem=nome_arquivo_seguro)
        produto = Produtos(imagem=nome_arquivo_seguro,
                            tipo=form_AdcProduto.tipo.data,
                            tamanho=form_AdcProduto.tamanho.data,
                            nome=form_AdcProduto.nome.data,
                            valor=form_AdcProduto.valor.data,
                            descricao=form_AdcProduto.descricao.data)

        database.session.add(produto)
        database.session.commit()

        return redirect(url_for('home'))

    return render_template('adcproduto.html', form=form_AdcProduto)



@app.route('/produtos/todos', methods=['GET', 'POST'])
def p_todos():
    
    produto = Produtos.query.with_entities(Produtos.imagem, Produtos.nome, Produtos.id).all()

    return render_template('produtos-todos.html', produto=produto)



@app.route('/produtos/produtos/info', methods=['GET', 'POST'])
def info_produto():

    return render_template('produtos-info.html')



@app.route('/AdcClientes', methods=['GET', 'POST'])
def CadastrarClientes():

    form_CadCliente = FormCadastroCliente()

    if form_CadCliente.validate_on_submit():

        cliente = Clientes(nome=form_CadCliente.nome.data, 
                           telefone=form_CadCliente.telefone.data, 
                           endereco=form_CadCliente.endereco.data, 
                           cidade=form_CadCliente.cidade.data, 
                           uf=form_CadCliente.uf.data, 
                           cep=form_CadCliente.cep.data, 
                           cpf=form_CadCliente.cpf.data)

        database.session.add(cliente)
        database.session.commit()

        return redirect(url_for('home'))

    return render_template('cadastrarclientes.html', form=form_CadCliente)



app.route('/calendario')
def calendario():
    return render_template('calendario.html')



app.route('/caixa')
def caixa():
    return render_template('caixa.html')