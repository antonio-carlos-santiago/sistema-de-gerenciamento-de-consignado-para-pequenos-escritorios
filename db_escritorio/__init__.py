from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clientes.db"
database.init_app(app)

from db_escritorio import Routes