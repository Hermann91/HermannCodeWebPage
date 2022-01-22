from app import app
from flask import render_template
from app.models.form_cadastro import cadastro
from app.models.tables import User
from sqlalchemy.orm import joinedload


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/formulario-fale-conosco", methods=['POST', 'GET'])
def formulario_cadastro():
    formulario = cadastro()

    return render_template('form_fale_conosco.html', formulario=formulario)
