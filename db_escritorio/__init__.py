from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:hjBzejYiRbqD2RH9gWlm@containers-us-west-76.railway.app:8020/railway"
database.init_app(app)

from db_escritorio import Routes