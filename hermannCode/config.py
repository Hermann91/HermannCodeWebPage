import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'CHAVE-PARA-ENCRIPTAR-INFO-FORMULARIO'

