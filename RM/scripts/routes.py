from __init__ import app
from flask import render_template, url_for, redirect
from forms import FormCadastroCliente, FormAdcProduto

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/AdcProduto')
def adcproduto():

    form_AdcProduto = FormAdcProduto()

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