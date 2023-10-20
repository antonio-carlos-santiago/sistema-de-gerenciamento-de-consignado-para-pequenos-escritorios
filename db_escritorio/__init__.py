import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

load_dotenv()


class Base(DeclarativeBase):
    pass


database = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
database.init_app(app)
import db_escritorio.Models

with app.app_context():
    database.drop_all()
    database.create_all()

from db_escritorio import Routes
