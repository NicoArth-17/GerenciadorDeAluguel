from __init__ import app, database
from flask import render_template, url_for, redirect
from forms import FormCadastroCliente, FormAdcProduto, FormAlugar
from models import Clientes, Produtos, Alugueis
from werkzeug.utils import secure_filename
import os

def formatarReais(n):
    n = f'R${n:.2f}'
    n = n.replace('.',',')
    return n


def formatar_cpf(num):
    f_cpf = num

    if f_cpf[0] == 0:
        f_cpf = f'0{f_cpf[:3]}.{f_cpf[3:6]}.{f_cpf[6:9]}-{f_cpf[9:]}'
    else:
        f_cpf = f'{f_cpf[:3]}.{f_cpf[3:6]}.{f_cpf[6:9]}-{f_cpf[9:]}'

    return f_cpf


def formatar_tell(num):
    f_tell = str(num)
    f_tell = f'({f_tell[:2]}) {f_tell[2:7]}-{f_tell[7:]}'
    return f_tell


def formatar_cep(num):
    f_cep = str(num)
    f_cep = f'{f_cep[:5]}-{f_cep[5:]}'
    return f_cep



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
        produto = Produtos(imagem=nome_arquivo_seguro,
                            tipo=form_AdcProduto.tipo.data,
                            tamanho=form_AdcProduto.tamanho.data,
                            nome=form_AdcProduto.nome.data,
                            valor=formatarReais(form_AdcProduto.valor.data),
                            descricao=form_AdcProduto.descricao.data)

        database.session.add(produto)
        database.session.commit()

        return redirect(url_for('home'))

    return render_template('adcproduto.html', form=form_AdcProduto)



@app.route('/produtos/todos', methods=['GET', 'POST'])
def p_todos():
    
    produto = Produtos.query.with_entities(Produtos.imagem, Produtos.nome, Produtos.id).all()

    return render_template('produtos-todos.html', produto=produto)



@app.route('/produtos/produto<id_produto>/info', methods=['GET', 'POST'])
def info_produto(id_produto):

    # Formulário de locação
    form_Alugar = FormAlugar()

    # Inserindo coluna dos nomes de clientes cadastrados no banco de dados no campo de seleção do formulário de locação
    form_Alugar.cliente.choices = [(f'{client.id} - {client.nome}') for client in Clientes.query.all()]

    # Selecionando o produto no banco de dados referênte ao clicado na página anterior para exibir suas informações
    produto = Produtos.query.filter_by(id=id_produto).first()

    # Método para formatar data inserida no formulario de alugar como dia/mes/ano
    def formatarData(data):
        data_f = data.strftime('%d/%m/%Y')
        return data_f

    # Se o botão de conclusão do formulário for clicado
    if form_Alugar.validate_on_submit():

        # Preenchendo a tabela de aluguel com as informações do formulário
        aluguel = Alugueis(locacao=formatarData(form_Alugar.locacao.data),
                           devolucao=formatarData(form_Alugar.devolucao.data),
                           id_cliente=form_Alugar.cliente.data,
                           id_produto=id_produto)

        # Adicionando no banco de dados
        database.session.add(aluguel)
        database.session.commit()

        # aluguel1 = Alugueis.query.filter_by(id=id_produto).all()

        # # Após formulário submetido, retornar a mesma página inserindo os dados enviados na tabela abaixo do formulário
        # return render_template('produtos-info.html', produto=produto, aluguel=aluguel1, form=form_Alugar)

    alugueis_produto = Alugueis.query.filter_by(id=id_produto).all()

    # Retornar página com as informações do produto selecionado na página anterior
    return render_template('produtos-info.html', produto=produto, alugueis_produto=alugueis_produto, form=form_Alugar)



@app.route('/AdcClientes', methods=['GET', 'POST'])
def CadastrarClientes():

    form_CadCliente = FormCadastroCliente()

    if form_CadCliente.validate_on_submit():

        cliente = Clientes(nome=form_CadCliente.nome.data, 
                           telefone=formatar_tell(form_CadCliente.telefone.data), 
                           endereco=form_CadCliente.endereco.data, 
                           cidade=form_CadCliente.cidade.data, 
                           uf=form_CadCliente.uf.data, 
                           cep=formatar_cep(form_CadCliente.cep.data), 
                           cpf=formatar_cpf(form_CadCliente.cpf.data))

        database.session.add(cliente)
        database.session.commit()

        return redirect(url_for('home'))

    return render_template('cadastrarclientes.html', form=form_CadCliente)



@app.route('/clientes', methods=['GET', 'POST'])
def clientes():

    cliente = Clientes.query.with_entities(Clientes.id, Clientes.nome, Clientes.cpf, Clientes.telefone, Clientes.endereco, Clientes.cidade, Clientes.uf, Clientes.cep).all()

    return render_template('clientes.html', cliente=cliente)



@app.route('/calendario')
def calendario():
    return render_template('calendario.html')



app.route('/caixa')
def caixa():
    return render_template('caixa.html')