from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


database = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:xhS45M2DgEZmTi8Zyg3g@containers-us-west-192.railway.app:7724/railway"
database.init_app(app)
import db_escritorio.Models

with app.app_context():
    database.drop_all()
    database.create_all()

from db_escritorio import Routes
