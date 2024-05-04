from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, TelField, SelectField, FileField, DecimalField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from models import Clientes, Produtos


class FormCadastroCliente(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    telefone = TelField('Telefone', validators=[DataRequired(), Length(min=11,max=11)])
    endereco = StringField('Endereço', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])
    uf = SelectField('UF', choices=['MG', 'RJ', 'ES', 'SP'], validators=[DataRequired()])
    cep = IntegerField('CEP', validators=[DataRequired(), NumberRange(min=10000000,max=99999999)])
    cpf = IntegerField('CPF', validators=[DataRequired(), NumberRange(min=10000000000,max=99999999999)])
    concluir = SubmitField('Concluir')


class FormAdcProduto(FlaskForm):
    imagem = FileField('Imagem', validators=[DataRequired()])
    tipo = SelectField('Tipo do produto', choices=['Acessórios', 'Masculino', 'Vestidos', 'Saias'], validators=[DataRequired()])
    tamanho = SelectField('Tamanho', choices=['Não se aplica', '3 anos', '5 anos', '7 anos', '10 anos', '12 anos', '14 anos', '16 anos', 'P', 'M', 'G'])
    nome = StringField('Nome do produto', validators=[DataRequired()])
    valor = DecimalField('Preço', places=2, validators=[DataRequired()])
    descricao = TextAreaField('Descrição', validators=[Length(0,100)])
    concluir = SubmitField('Concluir')