from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, TelField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class FormCadastroCliente(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    telefone = TelField('Telefone', validators=[DataRequired(), Length(11,11)])
    endereco = StringField('Endereço', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])
    uf = SelectField('UF', choices=['MG', 'RJ', 'ES', 'SP'], validators=[DataRequired()])
    cep = IntegerField('CEP', validators=[DataRequired(), Length(5,5)])
    nascimento = DateField('Data de nascimento', validators=[DataRequired(), Length(10,10)])
    cpf = IntegerField('CPF', validators=[DataRequired(), Length(11,11)])
    concluir = SubmitField('Concluir')