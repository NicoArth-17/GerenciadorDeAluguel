from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

class FormCadastroCliente(FlaskForm):
    nome = StringField()
    telefone = IntegerFielf()
    endereco = StringField()
    cidade = StringField()
    uf = SelectField()
    cep = IntegerField()
    cpf = IntegerField()
    nascimento = StringField()
    concluir = SubmitField()