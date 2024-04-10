from __init__ import app
from flask import render_template, url_for, redirect

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/AdcProduto')
def adcproduto():
    return render_template('adcproduto.html')

@app.route('/alugueis')
def alugueis():
    return render_template('alugueis.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

app.route('/calendario')
def calendario():
    return render_template('calendario.html')

app.route('/caixa')
def caixa():
    return render_template('caixa.html')